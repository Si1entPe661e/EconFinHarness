# Experiment commands

df contains y, y_baseline, assigned, received, block and school. assigned/received are binary; school is the randomized cluster. All units remain classified by assignment. Complete-case estimation below needs an attrition discussion if outcomes are missing.

## R: blocked ANCOVA and compliance IV

~~~r
library(fixest)
itt_cols <- c("y", "y_baseline", "assigned", "block", "school")
itt_sample <- df[complete.cases(df[, itt_cols]), itt_cols]
itt <- feols(y ~ assigned + y_baseline | block, data = itt_sample, cluster = ~school)
iv_cols <- c(itt_cols, "received")
d <- df[complete.cases(df[, iv_cols]), iv_cols]
first_stage <- feols(received ~ assigned + y_baseline | block,
                     data = d, cluster = ~school)
complier <- feols(y ~ y_baseline | block | received ~ assigned,
                  data = d, cluster = ~school)
etable(itt, first_stage, complier)
~~~

Do not exclude missing receipt from the primary ITT if it is unnecessary for that regression. Use a separate common sample for comparing compliance IV and its first stage.

For arm coded 0/1/2, estimate separate contrasts against arm 0:

~~~r
multi <- feols(y ~ i(arm, ref = 0) + y_baseline | block,
               data = df, cluster = ~school)
summary(multi)
wald(multi, keep = "^arm::")
~~~

The joint Wald test is not a multiple-testing adjustment for every outcome and contrast.

## Stata

~~~stata
regress y assigned y_baseline i.block, vce(cluster school)
regress received assigned y_baseline i.block, vce(cluster school)
ivregress 2sls y y_baseline i.block (received = assigned), vce(cluster school)
estat firststage
regress y ib0.arm y_baseline i.block, vce(cluster school)
test 1.arm 2.arm
~~~

For independent individual randomization with no additional dependence, heteroskedastic robust covariance may suffice. Unequal probabilities and pair-randomized designs require the corresponding design treatment.
