# CAP182 SS1–SS3 Part C — Speaker Notes

**Presenter:** Bernette Lesejane (26303406)  
**Target recording length:** approximately 10 minutes 50 seconds  
**Audience:** STADIOEquities decision-makers and academic/data-science assessors

## Recording and delivery cues

- Start with the camera showing your face for the opening, then share the slides. Return to the camera for the final slide and closing.
- Speak to the audience rather than reading the slide text. Use the notes as a script guide; pause briefly when pointing to a chart.
- The timings below total 10:50. Allow for short pauses and keep the full recording between 10 and 12 minutes.

## Slide 1 — From registration to first deposit
**Time: 0:00–0:45 (45 seconds)**

**On camera:** Begin with your face visible. Use the first sentence as the attention hook.

“Every funded investor begins as a sign-up—but not every sign-up reaches a first deposit. In this project, I ask how STADIOEquities could recognise accounts that may need help completing that journey. I will connect the business problem and governance plan from SS1, the evidence and model choices from SS2, and the account-activation analysis from SS3. The goal is not to put a label on a customer. It is to learn whether early information can help the business offer timely, useful support. I’ll show what the data and models can tell us, where the evidence is still limited, and what should be tested before any real-world rollout.”

## Slide 2 — The business problem and motivation
**Time: 0:45–1:35 (50 seconds)**

“The SS1 brief describes a large registered customer base and a business challenge: registration does not necessarily turn into funded investing. The brief cites 2.3 million registered accounts, but that is context—not the sample used in SS3. The project question is whether account information and early behaviour can help predict a first deposit within 90 days. That prediction could help prioritise onboarding education or human support when staff capacity is limited. The business outcome should not be model accuracy alone. It should be more incremental first deposits at an acceptable cost, achieved with fair and compliant customer treatment. That final impact must be demonstrated through an intervention test, not assumed from a prediction.”

## Slide 3 — Exploratory analysis: early signals
**Time: 1:35–2:35 (60 seconds)**

“These two charts summarise early exploratory patterns in the 4,906-account modelling population. In the first-session table, accounts that viewed education content had a 49.5 percent activation rate, compared with 36.2 percent among those that did not. In the second chart, activation rises from about 34.8 percent in the shortest first-session-duration quartile to about 50.2 percent in the longest. These are useful clues: educational content and deeper early engagement may help us understand where onboarding support could be relevant. But they are associations, not evidence that making someone watch more content will cause a deposit. Other factors may explain the difference, and the extract is a limited sample. We use these findings to motivate tests, not to prescribe customer behaviour.”

## Slide 4 — SS1 governance: RAAIDD
**Time: 2:35–3:25 (50 seconds)**

“SS1 used a RAAIDD log to track risks, actions, assumptions, issues, decisions and dependencies. SS3 makes several of those assumptions concrete. The plan anticipated at least 100,000 accounts over 12 to 18 months; the available modelling extract contains 4,906 unique accounts. That is enough for a development exercise, but not evidence that the model represents the full customer base. SS1 also identified temporal drift and privacy as risks. The SS3 evaluation uses a random split rather than a later-time cohort, so drift remains untested. Before any pilot, the business must confirm event timestamps, data permissions, and a POPIA-compliant purpose and access process. This is a living governance log, not a box-ticking exercise.”

## Slide 5 — Data overview and preparation
**Time: 3:25–4:25 (60 seconds)**

“The data dictionary specified 12 linked source tables: registration and onboarding, early behaviour, communications, marketing, KYC and device context, among others. Nine were used fully or partly. Support tickets were excluded because timestamps could not confirm they were available before activation; feedback was incomplete and included a label-related field; and post-deposit activity existed only for activated accounts. The target is a first deposit within 90 days. We removed 14 exact duplicate rows, standardised category labels and dates, and removed deposit- and outcome-derived fields to reduce leakage. Numeric and categorical preprocessing was fitted on training data. The final split was stratified 70/15/15—different from the 60/20/20 originally planned—and one-hot encoding produced 169 model inputs. These choices are recorded so results can be interpreted and reproduced.”

## Slide 6 — What SS2 and the literature contributed
**Time: 4:25–5:20 (55 seconds)**

“SS2 provided both context and a modelling benchmark. Its UCI Bank Marketing dataset contains 45,211 records from a Portuguese bank campaign, with roughly 11 percent positive outcomes. After dropping call duration because it is only known after a call, XGBoost achieved the strongest SS2 F1 score: 0.459 on its test set and about 0.446 in cross-validation. The literature review also highlighted activation modelling, interpretable event histories, and the value of time-aware evaluation and lift-based targeting. Those sources helped motivate the SS3 model candidates and safeguards. However, the UCI campaign outcome is not the same as STADIOEquities 90-day account activation. So SS2 guides our choices; its F1 values cannot be compared directly with SS3 or treated as proof that XGBoost must win here.”

## Slide 7 — SS3 modelling method
**Time: 5:20–6:20 (60 seconds)**

“SS3 compares Logistic Regression, Random Forest and XGBoost, with an ensemble that averages predicted probabilities. Logistic Regression is the interpretable baseline; Random Forest combines many decision trees; and boosting builds trees sequentially to correct earlier errors. We stratified account IDs into training, validation and unseen test sets at 70, 15 and 15 percent. Imputation, scaling, category encoding and outlier caps were learned from training data. SMOTE was also applied only to training data, so validation and test retain the natural class balance. This matters because resampling before the split could let information from held-out examples influence training. The validation set supports development checks; the unseen test set is reserved for final performance reporting.”

## Slide 8 — Results on unseen accounts
**Time: 6:20–7:30 (70 seconds)**

“The unseen test set contains 736 accounts, including 314 activated accounts. At the 0.5 classification threshold, Random Forest gives the highest F1 at 0.857, recall of 0.943 and ROC AUC of 0.943. Logistic Regression has the highest accuracy, 0.870, and precision, 0.810, with F1 almost tied at 0.856. XGBoost’s test F1 is 0.835. This is not a universal winner story: the best choice depends on whether the business wants to reduce missed activations, avoid unnecessary outreach, or preserve interpretability. The chart shows why accuracy alone is insufficient. A decision-maker should choose the operating point with a clearly stated cost of false positives and false negatives, then validate that choice prospectively.”

## Slide 9 — Turning a score into a service
**Time: 7:30–8:25 (55 seconds)**

“To make the results practical, the analysis simulated selecting the 30 percent of test accounts with the lowest ensemble activation scores. That gave a list of 221 accounts; 218 were non-activators, so the retrospective list precision was 98.6 percent. The list covered 51.7 percent of all non-activators in the test set. This is a capacity scenario, not a campaign result. It does not show that contacting these people would change their behaviour; it only shows how the model ranked this held-out sample. The next step is to randomise eligible high-risk accounts between supportive outreach and business-as-usual. Then compare incremental 90-day activation and cost, while ensuring the intervention is helpful and appropriate.”

## Slide 10 — Interpretation and model complexity
**Time: 8:25–9:20 (55 seconds)**

“The feature-importance chart highlights KYC status, KYC verification time and onboarding completion as strong predictive signals. Importance tells us what the fitted model used; it does not establish cause or customer intent. It also raises a timing question: was each KYC value genuinely available at the moment the business would score an account? If not, it must be removed. The model pipeline contains 169 encoded inputs, so the project has not yet demonstrated a simpler production model. Logistic Regression gives a useful lower-complexity benchmark. The next technical step is a controlled feature-ablation study: reduce inputs, then compare performance, calibration, stability and operational cost. Complexity should only be reduced when evidence shows the smaller model is still fit for purpose.”

## Slide 11 — Reliability, limits and next validation
**Time: 9:20–10:10 (50 seconds)**

“Repeated stratified cross-validation used five folds and ten repeats. Mean F1 was about 0.852 for Random Forest, 0.848 for Logistic Regression, and 0.848 for XGBoost. Their confidence intervals overlap, so the small difference does not justify claiming a decisive model winner. The tree models also score extremely highly on training data, which warrants attention to overfitting. Most importantly, the split was random, not chronological. It cannot tell us how performance changes on newer customers or after product changes. A time-based holdout, event-time audit, and prospective monitoring of calibration, drift, missingness and precision at the available contact capacity are needed before operational use.”

## Slide 12 — Recommendation and conclusion
**Time: 10:10–10:50 (40 seconds)**

“My recommendation is a staged, privacy-reviewed pilot—not automated deployment. First confirm when each feature becomes available; then test on later cohorts; finally randomise supportive outreach and measure incremental activation, customer experience and cost. Keep human oversight, data minimisation and clear rollback criteria in place. The project’s contribution is an end-to-end, leakage-aware starting point that connects the business question to a testable account-ranking approach. It has not yet proven that a model-driven intervention increases deposits. The decision now is whether to fund that next experiment. Thank you.”

**On camera:** Return to your face for the final sentence and sign-off.

## References and evidence used

- Isen, B. et al. (2026), “The impact of customer analytics on sales funnel conversion and customer retention in the e-commerce industry,” *Asian Journal of Economics, Business and Accounting*, 26(1), pp. 207–224. As summarised in the SS2 literature review.
- Moro, S., Cortez, P. and Rita, P. (2014), “A data-driven approach to predict the success of bank telemarketing,” *Decision Support Systems*, 62, pp. 22–31. https://doi.org/10.1016/j.dss.2014.03.001
- Moro, S., Cortez, P. and Rita, P. (2014), *Bank Marketing* dataset, UCI Machine Learning Repository. https://doi.org/10.24432/C5K306
- Weterings, K., Bromuri, S. and van Eekelen, M. (2019), “Explaining customer activation with deep attention models,” Proceedings of ECIS 2019, Research Paper 151. https://aisel.aisnet.org/ecis2019_rp/151/
- Project evidence: `README_SS1.md`; `CAP182-SS2 (resubmission)/READMEPartB&C.md`; `SS3_PartB.ipynb`; and aggregate tables and figures in `results/`. The presentation uses aggregate metrics only; do not include customer-level identifiers or predictions in public materials.
