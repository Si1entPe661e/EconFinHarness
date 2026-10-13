#!/usr/bin/env Rscript
# Run from the repository root. No author programs or output tables are read.
options(warn = 1)
started <- Sys.time()
source("harness/examples/war-discourse/methods.R")
required <- c("sandwich", "jsonlite", "ggplot2", "testthat")
missing <- required[!vapply(required, requireNamespace, quietly=TRUE, FUN.VALUE=logical(1))]
if (length(missing)) stop("Install these R packages first: ", paste(missing, collapse=", "))
spec <- jsonlite::fromJSON("harness/examples/war-discourse/specification.json")
input_root <- spec$data_root; output_root <- spec$output_root
dir.create(output_root, recursive=TRUE, showWarnings=FALSE)
for (d in c("tables", "figures", "checks")) dir.create(file.path(output_root,d), showWarnings=FALSE)
jsonlite::write_json(list(status="running",started=as.character(started)),
  file.path(output_root,"run_summary.json"),auto_unbox=TRUE,pretty=TRUE)
options(error=function(){
  jsonlite::write_json(list(status="failed",error=geterrmessage(),ended=as.character(Sys.time())),
    file.path(output_root,"run_summary.json"),auto_unbox=TRUE,pretty=TRUE)
  q(save="no",status=1,runLast=FALSE)
})
access_log <- file.path(output_root, "input_access.txt")
writeLines(character(), access_log)
read_data <- function(name) read_input(name, input_root, access_log)
source("harness/examples/war-discourse/checks.R")
cat("[1/7] Reading allowed data and constructing the analysis samples.\n")
war <- validate_months(read_data("texts/war_indexes.rds"))
traded <- validate_months(read_data("traded_factors.rds"))
nontraded <- validate_months(read_data("nontraded_factors.rds"))
crisis <- validate_months(read_data("crisis_events_full_sample.rds"))
original <- read_data("test_portfolios_original.rds")
ff <- read_data("ff_portfolios.rds")
prepared <- lapply(original, prepare_portfolios)
sample_flow <- do.call(rbind, lapply(names(prepared), function(n) {
  z <- prepared[[n]]
  data.frame(assets=n, candidates=z$before, retained=z$retained, excluded=z$before-z$retained,
             months_before_factor_matching=z$months)
}))
write.csv(sample_flow, file.path(output_root,"tables/sample_flow.csv"), row.names=FALSE)
exclusions <- lapply(prepared, `[[`, "excluded")
jsonlite::write_json(exclusions, file.path(output_root,"checks/excluded_assets.json"), auto_unbox=TRUE, pretty=TRUE)

# Fingerprint only data actually used, before any analysis; compare at the end.
data_paths <- unique(c(readLines(access_log),"beta_portfolios.rds","narrative_factors.rds",
  "gw_macro_predictors.RDS","test_portfolios.rds","war_factors.rds"))
before_hash <- fingerprint_inputs(file.path(input_root, data_paths))
baseline <- list()
for (variant in c("calendar", "observed", "published_series")) {
  z <- data.frame(month=war$month)
  lag_mode <- if(variant=="calendar") "calendar" else "observed"
  index_name <- if(variant=="published_series") "War_main" else spec$primary_index
  z$WarFac <- ar_innovations(war$month, war[[index_name]], gap=lag_mode)
  z$WarFac_strict <- ar_innovations(war$month, war[[index_name]], gap=lag_mode, include_current=FALSE)
  for (nm in grep("^War", names(war), value=TRUE))
    z[[paste0(nm,"_reconstructed")]] <- ar_innovations(war$month, war[[nm]], gap=lag_mode)
  for (nm in setdiff(names(traded), c("ym","month"))) z[[nm]] <- traded[[nm]][match(z$month, traded$month)]
  for (nm in setdiff(names(nontraded), c("ym","month","yq"))) z[[nm]] <- nontraded[[nm]][match(z$month, nontraded$month)]
  for (nm in c("CrisisFac", "CWarFac")) {
    level <- if(nm=="CrisisFac") "Crisis" else "CWar"
    # Crisis-count history begins in 1918; no arbitrary restart in 1926.
    innovation <- ar_innovations(crisis$month, crisis[[level]], start=min(crisis$month), gap=lag_mode)
    z[[nm]] <- innovation[match(z$month, crisis$month)]
  }
  baseline[[variant]] <- z
}

models <- list(
  War=c("WarFac"), FF6=c("MKT","SMB","HML","RMW","CMA","MOM"),
  M4=c("MKT","SMB","MGMT","PERF"), DHS=c("MKT","PEAD","FIN"),
  Q5=c("R_MKT","R_ME","R_IA","R_ROE","R_EG"), War_MKT=c("WarFac","MKT"))
for (n in c("FF6","M4","DHS","Q5")) models[[paste0("War_",n)]] <- c("WarFac",models[[n]])
models$War_All <- unique(c("WarFac",models$FF6,models$M4,models$DHS,models$Q5[-1]))
single_factors <- c("MKT","SMB","HML","MOM","RMW","CMA","MGMT","PERF","PEAD","FIN","R_IA","R_ROE","R_EG")
results <- list(); objects <- list(); loading_rows <- list()
run_fit <- function(asset, factor_names, variant="calendar", table="II", model=paste(factor_names,collapse="+"),
                    end=2016L*12L+11L, factor_data=NULL, scale_factors=FALSE) {
  r <- prepared[[asset]]$data
  f <- if(is.null(factor_data)) baseline[[variant]] else factor_data
  ix <- match(r$month,f$month)
  F <- as.matrix(f[ix,factor_names,drop=FALSE])
  w <- f$WarFac[ix]
  keep <- is.finite(w) & r$month<=end & rowSums(!is.finite(F))==0L
  if (table=="IV") {
    comparison <- as.matrix(f[ix,c("WarFac","NVIX_War2Fac","GPRFac"),drop=FALSE])
    keep <- keep & rowSums(!is.finite(comparison))==0L
  }
  if (scale_factors) {
    multiplier <- sd(w[keep]) / apply(F[keep,,drop=FALSE],2,sd)
    F <- sweep(F,2,multiplier,`*`)
  }
  R <- as.matrix(r[keep,setdiff(names(r),"month"),drop=FALSE])
  F <- F[keep,,drop=FALSE]
  fit <- two_pass(R,F)
  fit$months <- r$month[keep][fit$used]
  fit$factor_names <- factor_names
  fit$inference <- "Shanken; T covariance divisors; factor covariance term; normal reference"
  fit$source <- "Paper equations 1-2 and stated assumptions in specification.json"
  results[[length(results)+1L]] <<- result_rows(fit,table,asset,model,variant)
  compact <- fit; compact$residuals <- NULL; compact$monthly_lambda <- NULL
  objects[[paste(table,asset,model,variant,sep="/")]] <<- compact
  fit
}

cat("[2/7] Estimating Tables I-II and the calendar-gap sensitivity.\n")
nontrade_names <- c("WarFac","CrisisFac","Ds16","Dstop16","NI","HNI","indp_factor","Macro_PC1","Macro_PC2","Macro_PC3","LevFactor")
for (variant in names(baseline)) {
  for (asset in names(prepared)) {
    for (nm in names(models)) run_fit(asset,models[[nm]],variant,"II",nm)
    for (nm in nontrade_names) {
      fit <- run_fit(asset,nm,variant,"I",nm,scale_factors=nm!="WarFac")
      loading_rows[[length(loading_rows)+1L]] <- data.frame(assets=asset,factor=nm,variant=variant,
        T=fit$T,N=fit$N,average_abs_beta_t=mean(abs(fit$beta_t)),significant_betas=sum(abs(fit$beta_t)>1.65),
        lambda=fit$lambda[2],t=fit$t[2])
    }
  }
}

cat("[3/7] Constructing mimicking portfolios and Tables III-IV.\n")
wmps <- list()
for (variant in names(baseline)) {
  tree_fit <- run_fit("tree","WarFac",variant,"WMP_construction","Tree_CS")
  z <- baseline[[variant]]
  z$WMP <- NA_real_
  z$WMP[match(tree_fit$months,z$month)] <- tree_fit$monthly_lambda[,2]
  wmps[[variant]] <- data.frame(month=tree_fit$months,WMP=tree_fit$monthly_lambda[,2])
  stopifnot(abs(mean(wmps[[variant]]$WMP)-tree_fit$lambda[2])<1e-12)
  baseline[[variant]] <- z
  for (asset in names(prepared)) {
    for (nm in c("WarFac","WMP",single_factors)) run_fit(asset,nm,variant,"III",nm)
    uncertainty <- list(War="WarFac",NVIX="NVIX_War2Fac",GPR="GPRFac",
                        All=c("WarFac","NVIX_War2Fac","GPRFac"))
    for (nm in names(uncertainty)) run_fit(asset,uncertainty[[nm]],variant,"IV",nm,
      end=2016L*12L+2L,scale_factors=TRUE)
    for (nm in names(models)) {
      m <- models[[nm]]; m[m=="WarFac"] <- "WMP"
      if ("WMP" %in% m) run_fit(asset,m,variant,"IA_C2",gsub("War","WMP",nm))
    }
  }
}
spanning <- list(); descriptive <- list()
for (variant in names(baseline)) {
  z <- baseline[[variant]]; z <- z[is.finite(z$WMP),]
  for (nm in c("WMP",single_factors,"R_ME")) {
    x<-z[[nm]]; keep<-is.finite(x)
    h<-hac_mean(x[keep],6,z$month[keep])
    descriptive[[length(descriptive)+1L]]<-data.frame(variant=variant,factor=nm,
      mean=mean(x[keep]),sd=sd(x[keep]),annual_sharpe=sqrt(12)*mean(x[keep])/sd(x[keep]),
      mean_t=h["t"],T=sum(keep))
  }
  spans<-c(models[c("FF6","M4","DHS","Q5")],list(All=setdiff(models$War_All,"WarFac")))
  for(nm in names(spans)) {
    ds<-z[,c("month","WMP",spans[[nm]]),drop=FALSE];ds<-ds[complete.cases(ds),]
    fit<-lm(reformulate(spans[[nm]],response="WMP"),data=ds)
    V<-calendar_hac_vcov(fit,ds$month,6)
    spanning[[length(spanning)+1L]]<-data.frame(variant=variant,model=nm,term=names(coef(fit)),
      estimate=coef(fit),se=sqrt(diag(V)),t=coef(fit)/sqrt(diag(V)),r2=summary(fit)$r.squared,T=nrow(ds),row.names=NULL)
  }
}

cat("[4/7] Estimating industry rolling-beta Fama-MacBeth tests (Table V).\n")
industry_results<-list();industry_paths<-list()
for(variant in names(baseline)) {
  z<-baseline[[variant]]
  for(asset in c("30ind","49ind")) {
    rr<-validate_months(ff[[asset]]);rr<-rr[rr$month<=2018*12+11L, setdiff(names(rr),"ym"),drop=FALSE]
    for(nm in c("WarFac","CrisisFac","CWarFac","All")) {
      crisis_names<-if(nm=="All") c("WarFac","CrisisFac","CWarFac") else nm
      fs<-z[,c("month",crisis_names,"MKT","SMB","HML"),drop=FALSE]
      fit<-industry_fmb(rr,fs,crisis_names,window_mode=if(variant=="calendar")"calendar" else "observed")
      for(lag in c(0L,3L,6L,12L)) {
        for(term in colnames(fit$slopes)) {
          h<-hac_mean(fit$slopes[,term],lag,fit$month)
          industry_results[[length(industry_results)+1L]]<-data.frame(table="V",assets=asset,model=nm,
            variant=variant,term=term,estimate=h["estimate"],se=h["se"],t=h["t"],hac_lag=lag,
            T=nrow(fit$slopes),N_min=min(fit$N),N_max=max(fit$N),r2=mean(fit$r2),
            start=month_label(min(fit$month)),end=month_label(max(fit$month)),
            missing_calendar_months=h["missing_months"],row.names=NULL)
        }
      }
      industry_paths[[paste(variant,asset,nm,sep="/")]]<-data.frame(month=fit$month,N=fit$N,r2=fit$r2,fit$slopes)
    }
  }
}

cat("[5/7] Estimating available appendix comparisons and robustness specifications.\n")
# Appendix D.2 uses supplied tail-beta portfolio returns, not reconstructed stock sorts.
tail_factors<-validate_months(read_data("beta_portfolios.rds"))
narrative<-validate_months(read_data("narrative_factors.rds"))
for(variant in names(baseline)) {
  z<-baseline[[variant]]
  tail_names<-setdiff(names(tail_factors),c("ym","month"))
  for(nm in tail_names) z[[nm]]<-tail_factors[[nm]][match(z$month,tail_factors$month)]
  topic_names<-setdiff(names(narrative),c("ym","month",grep("_AR1$",names(narrative),value=TRUE),"War"))
  for(nm in topic_names) {
    z[[paste0(nm,"Fac")]]<-ar_innovations(narrative$month,narrative[[nm]],gap=if(variant=="calendar")"calendar" else "observed")[match(z$month,narrative$month)]
  }
  z$WarPositive<-pmax(z$WarFac,0);z$WarNegative<-pmin(z$WarFac,0)
  # Time-series WMP construction: include a regression intercept, exclude it from returns.
  r<-prepared$tree$data;ix<-match(r$month,z$month);good<-is.finite(z$WarFac[ix])
  basis<-as.matrix(r[good,-1,drop=FALSE]);q<-qr(cbind(1,basis))
  ts_coef<-qr.coef(q,z$WarFac[ix][good])
  z$WMP_TS_Tree<-NA_real_;z$WMP_TS_Tree[ix[good]]<-drop(basis%*%ts_coef[-1])
  basis30<-validate_months(ff$ff30)
  ix30<-match(z$month,basis30$month);R30<-as.matrix(basis30[ix30,setdiff(names(basis30),c("ym","month")),drop=FALSE])
  good30<-is.finite(z$WarFac)&rowSums(!is.finite(R30))==0L
  ts30<-lm.fit(cbind(1,R30[good30,,drop=FALSE]),z$WarFac[good30])
  z$WMP_TS_FF30<-NA_real_;z$WMP_TS_FF30[good30]<-drop(R30[good30,,drop=FALSE]%*%ts30$coefficients[-1])
  for(asset in names(prepared)) {
    run_fit(asset,c("WarFac",tail_names),variant,"IA_D2","War_AllTailBetas",factor_data=z)
    for(nm in c("Bybee_War","Bybee_Financial_crisis","Bybee_Recession"))
      run_fit(asset,nm,variant,"IA_D3",nm,factor_data=z,scale_factors=TRUE)
    run_fit(asset,c("WarFac","Bybee_War","Bybee_Financial_crisis","Bybee_Recession"),variant,"IA_D3","All",factor_data=z,scale_factors=TRUE)
    run_fit(asset,c("WarFac",paste0(topic_names,"Fac")),variant,"IA_D4","AllTopics",factor_data=z)
    run_fit(asset,c("WarNegative",paste0(topic_names,"Fac")),variant,"IA_D5","Negative_AllTopics",factor_data=z)
    run_fit(asset,"WarFac",variant,"IA_E1","End2011",end=2011L*12L+11L)
    for(start in c(1945L,1965L)) {
      zz<-z;zz$WarFac<-ar_innovations(war$month,war[[if(variant=="published_series")"War_main" else spec$primary_index]],start=start*12L,gap=if(variant=="calendar")"calendar" else "observed")
      run_fit(asset,"WarFac",variant,"IA_E1",paste0("ARStart",start),factor_data=zz)
    }
    for(nm in c("WarPositive","WarNegative","WMP_TS_Tree","WMP_TS_FF30"))
      run_fit(asset,nm,variant,"IA_E2",nm,factor_data=z)
    for(nm in grep("_reconstructed$",names(z),value=TRUE))
      run_fit(asset,nm,variant,"IA_E3",nm,factor_data=z)
    run_fit(asset,c("WMP","MKT","MOM"),variant,"IA_H2","WMP_MKT_MOM",factor_data=z)
    strict<-z;strict$WarFac<-z$WarFac_strict
    run_fit(asset,"WarFac",variant,"Timing","ParametersThroughPreviousMonth",factor_data=strict)
  }
}

# Appendix F: reproduce the VAR identity with the predictors supplied in the data.
macro<-read_data("gw_macro_predictors.RDS")$dt;macro<-validate_months(macro)
var_outputs<-list()
for(k in c(0L,seq_len(10L))) {
  candidates<-c("EP","TBL","LTY","LTR","TMS","DFY","DFR","INFL","SVAR","NTIS")
  terms<-c("log_return","War","DP",if(k>0)candidates[seq_len(k)])
  ds<-data.frame(month=macro$month,log_return=log1p(traded$MKT[match(macro$month,traded$month)]+traded$RF[match(macro$month,traded$month)]),
                 War=war[[spec$primary_index]][match(macro$month,war$month)],macro[setdiff(names(macro),c("ym","month"))])
  ds<-ds[ds$month>=1972*12+6L&ds$month<=2016*12+11L,]
  lag_idx<-match(ds$month-1L,ds$month)
  Y<-as.matrix(ds[,terms,drop=FALSE]);L<-Y[lag_idx,,drop=FALSE]
  ok<-rowSums(!is.finite(Y))==0L&rowSums(!is.finite(L))==0L
  Y<-Y[ok,,drop=FALSE];L<-L[ok,,drop=FALSE];m<-ds$month[ok]
  model<-lm.fit(cbind(1,L),Y)
  if(model$rank<ncol(L)+1L) next
  A<-t(model$coefficients[-1,,drop=FALSE]);U<-model$residuals
  er<-model$fitted.values[,1];dr<-drop(U%*%t(.96*A%*%solve(diag(ncol(A))-.96*A))[ ,1]);cf<-Y[,1]-er+dr
  war_shock<-U[,2]/sd(U[,2])
  stopifnot(max(abs(Y[,1]-er-cf+dr))<1e-10)
  for(nm in c("Return","Expected","CF","DR")) {
    outcome<-switch(nm,Return=Y[,1],Expected=er,CF=cf,DR=dr)
    fit<-lm(outcome~war_shock)
    # Same shock scaling in all decomposition regressions preserves the identity.
    V<-calendar_hac_vcov(fit,m,6)
    var_outputs[[length(var_outputs)+1L]]<-data.frame(spec=k,variables=paste(terms,collapse="+"),component=nm,
      estimate=coef(fit)[2],se=sqrt(V[2,2]),t=coef(fit)[2]/sqrt(V[2,2]),T=length(m),row.names=NULL)
  }
}

cat("[6/7] Exporting numerical results, fitted objects and figures.\n")
all_results<-do.call(rbind,results)
write.csv(all_results,file.path(output_root,"tables/two_pass_results.csv"),row.names=FALSE)
write.csv(do.call(rbind,loading_rows),file.path(output_root,"tables/table_I_loadings.csv"),row.names=FALSE)
write.csv(do.call(rbind,industry_results),file.path(output_root,"tables/table_V_industries.csv"),row.names=FALSE)
write.csv(do.call(rbind,descriptive),file.path(output_root,"tables/wmp_descriptive.csv"),row.names=FALSE)
write.csv(do.call(rbind,spanning),file.path(output_root,"tables/wmp_spanning.csv"),row.names=FALSE)
write.csv(do.call(rbind,var_outputs),file.path(output_root,"tables/appendix_F_VAR.csv"),row.names=FALSE)
saveRDS(objects,file.path(output_root,"fitted_results.rds"))
saveRDS(industry_paths,file.path(output_root,"industry_monthly_slopes.rds"))
saveRDS(wmps,file.path(output_root,"reconstructed_wmp.rds"))
write.csv(baseline$calendar[,c("month","WarFac","WarFac_strict","WMP")],file.path(output_root,"tables/reconstructed_factors.csv"),row.names=FALSE)
ggplot2::theme_set(ggplot2::theme_minimal(base_size=12))
headline<-all_results[all_results$table=="II"&all_results$model=="War"&all_results$term=="WarFac",]
headline$assets<-factor(headline$assets,levels=c("lms","single","cz_decile","tree","anomalies","nonlinear"),
  labels=c("HXZ long-short","HXZ single sorts","CZ single sorts","Tree portfolios","Own anomalies","Own nonlinear"))
g<-ggplot2::ggplot(headline,ggplot2::aes(x=assets,y=100*estimate,color=variant))+
  ggplot2::geom_hline(yintercept=0,color="grey60")+
  ggplot2::geom_pointrange(ggplot2::aes(ymin=100*(estimate-1.96*se),ymax=100*(estimate+1.96*se)),
    position=ggplot2::position_dodge(width=.5))+
  ggplot2::coord_flip()+ggplot2::scale_color_manual(values=c(calendar="#14556B",observed="#B56439",published_series="#477748"),
    labels=c(calendar="War_base / calendar",observed="War_base / observed",published_series="War_main / observed (post hoc)"))+
  ggplot2::labs(x=NULL,y="Monthly WarFac premium (percentage points)",color="Index and lag",
    title="War exposure and expected portfolio returns",subtitle="Independent two-pass estimates; pointwise 95% Shanken intervals",
    caption=premium_caption())+
  ggplot2::theme(plot.caption=ggplot2::element_text(hjust=0),plot.caption.position="plot")
ggplot2::ggsave(file.path(output_root,"figures/war_premia.png"),g,width=9,height=5.5,dpi=180)
ggplot2::ggsave(file.path(output_root,"figures/war_premia.eps"),g,width=9,height=5.5,device=grDevices::postscript)
wx<-war[war$month>=1871*12&war$month<=2019*12+9,c("ym","War_base","month")]
g2<-ggplot2::ggplot(wx,ggplot2::aes(ym,100*War_base))+
  ggplot2::geom_line(linewidth=.35,color="#14556B")+
  ggplot2::labs(x="Year",y="War topic share (%)",title="The supplied War index, 1871-2019",
    subtitle="Text estimation is an input dependency; AR innovations are reconstructed independently")
ggplot2::ggsave(file.path(output_root,"figures/war_index.png"),g2,width=11,height=4,dpi=180)

cat("[7/7] Checking data integrity and independently reconstructed inputs.\n")
stopifnot(identical(before_hash,fingerprint_inputs(names(before_hash))))
write.csv(data.frame(path=names(before_hash),md5=unname(before_hash)),file.path(output_root,"checks/raw_input_hashes.csv"),row.names=FALSE)
# These supplied intermediate data are used for validation only, after independent estimation.
given<-read_data("test_portfolios.rds")
validation<-lapply(names(prepared),function(asset){
  own<-prepared[[asset]]$data; reference<-validate_months(given[[asset]])
  same_assets<-setequal(setdiff(names(own),"month"),setdiff(names(reference),c("ym","month")))
  data.frame(check="portfolio_membership",assets=asset,passed=same_assets,detail=paste("Own retained",ncol(own)-1L,"provided",ncol(reference)-2L))
})
given_factors<-validate_months(read_data("war_factors.rds"))
for(v in names(baseline)) {
  own<-baseline[[v]];idx<-match(own$month,given_factors$month)
  supplied_name<-if(v=="published_series")"War_main_AR1" else "War_base_AR1"
  supplied<-given_factors[[supplied_name]][idx]
  ok<-is.finite(own$WarFac)&is.finite(supplied)
  validation[[length(validation)+1L]]<-data.frame(check="factor_input_comparison",assets=v,passed=NA,
    detail=sprintf("Reconstructed vs supplied %s: correlation %.8f; RMSE %.8g; months %d",supplied_name,cor(own$WarFac[ok],supplied[ok]),sqrt(mean((own$WarFac[ok]-supplied[ok])^2)),sum(ok)))
}
write.csv(do.call(rbind,validation),file.path(output_root,"checks/data_comparison.csv"),row.names=FALSE)
capture.output(sessionInfo(),file=file.path(output_root,"session_info.txt"))
jsonlite::write_json(list(status="succeeded",started=as.character(started),ended=as.character(Sys.time()),
  elapsed_seconds=as.numeric(difftime(Sys.time(),started,units="secs")),
  two_pass_models=length(objects),numerical_rows=nrow(all_results),
  raw_inputs_unchanged=TRUE,author_code_read=FALSE,author_outputs_read=FALSE,
  note="Read declarations describe this runner; they do not prove an agent's earlier browsing behavior."),
  file.path(output_root,"run_summary.json"),auto_unbox=TRUE,pretty=TRUE)
print(headline[,c("assets","variant","estimate","t","r2","T","N")],row.names=FALSE)
cat("Finished. Results:",output_root,"\n")
