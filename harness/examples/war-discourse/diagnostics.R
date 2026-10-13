# Post-implementation diagnostics, explicitly separate from independent AR construction.
source("harness/examples/war-discourse/methods.R")
spec<-jsonlite::fromJSON("harness/examples/war-discourse/specification.json")
root<-spec$data_root;out<-spec$output_root
access<-file.path(out,"diagnostic_input_access.txt");writeLines(character(),access)
read_data<-function(name) read_input(name,root,access)
war<-validate_months(read_data("war_factors.rds"))
factors<-validate_months(read_data("traded_factors.rds"))
portfolios<-lapply(read_data("test_portfolios_original.rds"),prepare_portfolios)
models<-list(War="WarFac",FF6=c("MKT","SMB","HML","RMW","CMA","MOM"),
  M4=c("MKT","SMB","MGMT","PERF"),DHS=c("MKT","PEAD","FIN"),
  Q5=c("R_MKT","R_ME","R_IA","R_ROE","R_EG"),War_MKT=c("WarFac","MKT"))
for(n in c("FF6","M4","DHS","Q5"))models[[paste0("War_",n)]]<-c("WarFac",models[[n]])
models$War_All<-unique(c("WarFac",models$FF6,models$M4,models$DHS,models$Q5[-1]))
rows<-list();loading<-list()
for(asset in names(portfolios)) {
  rr<-portfolios[[asset]]$data
  z<-data.frame(WarFac=war$War_main_AR1[match(rr$month,war$month)])
  for(nm in setdiff(names(factors),c("ym","month")))z[[nm]]<-factors[[nm]][match(rr$month,factors$month)]
  for(nm in names(models)) {
    keep<-is.finite(z$WarFac)&complete.cases(z[,models[[nm]],drop=FALSE])
    fit<-two_pass(rr[keep,-1,drop=FALSE],z[keep,models[[nm]],drop=FALSE])
    rows[[length(rows)+1L]]<-result_rows(fit,"II",asset,nm,"supplied_factor_control")
  }
  # The paper does not fully specify first-pass beta covariance. Diagnose rather than select.
  keep<-is.finite(z$WarFac);R<-as.matrix(rr[keep,-1,drop=FALSE]);F<-z$WarFac[keep]
  tt<-matrix(NA_real_,ncol(R),3L,dimnames=list(NULL,c("OLS","HC0","NW6")))
  for(j in seq_len(ncol(R))) {
    f<-lm(R[,j]~F)
    tt[j,"OLS"]<-coef(summary(f))[2,3]
    tt[j,"HC0"]<-coef(f)[2]/sqrt(sandwich::vcovHC(f,type="HC0")[2,2])
    tt[j,"NW6"]<-coef(f)[2]/sqrt(calendar_hac_vcov(f,rr$month[keep],6)[2,2])
  }
  for(nm in colnames(tt))loading[[length(loading)+1L]]<-data.frame(assets=asset,inference=nm,
    factor_source="supplied War_main_AR1; diagnostic only",average_abs_beta_t=mean(abs(tt[,nm])),
    significant_betas=sum(abs(tt[,nm])>1.65),N=ncol(R),T=nrow(R))
}
write.csv(do.call(rbind,rows),file.path(out,"tables/supplied_factor_control.csv"),row.names=FALSE)
write.csv(do.call(rbind,loading),file.path(out,"tables/first_pass_inference_diagnostics.csv"),row.names=FALSE)
cat("Supplied-factor control and first-pass inference diagnostics finished.\n")
