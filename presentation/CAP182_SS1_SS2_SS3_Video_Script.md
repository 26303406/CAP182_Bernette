# CAP182 SS1–SS3 video presentation script

**Target runtime:** approximately 11 minutes at a measured pace  
**Slides:** `CAP182_SS1_SS2_SS3_Presentation.pptx`

## Recording checklist

- Record in landscape, 16:9, with clear audio and readable slides.
- Show your face on camera for the opening and closing. Keep your camera on if comfortable and technically possible.
- Start with your face visible before sharing the title slide; finish with your face visible after the final slide.
- Speak at a measured pace. Pause briefly on the performance and outreach charts.
- This script is approximately 1,350 spoken words. At roughly 125–130 words per minute, with brief pauses on the graphs, it should run for about 11 minutes. Rehearse with a timer and keep the final recording between 10 and 12 minutes.
- Do not present the historical SS2 result as validated performance or the SS3 outreach simulation as proven campaign impact.

## Slide 1 — Predicting account activation
**Time: 0:00–0:40**

**Camera cue:** Show your face. Introduce yourself before sharing the title slide.

Good day. My name is Bernette Lesejane, and this presentation brings together my CAP182 capstone work across SS1, SS2, and SS3. The project asks a practical question for STADIOEquities: can we identify which newly registered accounts are likely to make a first deposit, and use that information to improve onboarding support? I’ll explain the business problem, how the modelling work developed, what the latest test results show, and what should happen before any real-world use.

## Slide 2 — Four-part story
**Time: 0:40–1:05**

The presentation follows the sample’s four sections: problem statement, solution performance, modelling approach, and next steps. For business stakeholders, I’ll focus on how account ranking could guide outreach. For data science stakeholders, I’ll explain the data, validation, limitations, and why the latest results are more credible than the earlier prototype scores.

## Slide 3 — Problem statement
**Time: 1:05–2:20**

The business problem is the gap between account registration and a customer’s first deposit. A registered account represents acquisition effort, but it is not yet an active investor. If the customer stalls, that effort may not lead to activation.

SS1 framed this as an activation and retention problem and requested twelve data tables covering onboarding, early engagement, communications, campaigns, compliance, and customer context.

In SS3, the client’s `activated` field is the target: one means a first deposit within 90 days; zero means no deposit in that period. Of 4,906 unique accounts, 2,093 activated and 2,813 did not. That is 42.7 percent activated and 57.3 percent not activated in this dataset—not an assumed business-wide rate.

The proposed solution is to estimate activation likelihood and prioritize support for accounts most at risk of stalling.

The score should guide helpful interventions—such as onboarding assistance or clearer product education—not restrict access or make decisions about customers automatically.

## Slide 4 — How the work evolved: SS1 to SS3
**Time: 2:20–3:30**

The three submissions progress from framing, to experimentation, to a more defensible client-data analysis.

SS1 defined the activation problem and specified the data needed to connect onboarding activity with customer outcomes.

SS2 built a retail analytics workflow with preprocessing, customer-level feature engineering, and Random Forest, XGBoost, and ensemble models. Its evaluation files report perfect scores. But the target was created from recency and purchase frequency, and those same fields remained predictors. The models could learn the rule used to create the label. Those scores do not show perfect performance on real account activation.

SS3 uses the client activation label, explicit leakage checks, and a separate unseen test set. The lesson is that credible evaluation matters more than an impressive score.

The business question stayed the same, but SS3 improved the label, data source, and evaluation design. That makes its results more relevant to the client decision, while still leaving real-world validation to do.

## Slide 5 — Solution performance: what the test shows
**Time: 3:30–5:05**

This chart compares ROC curves across training, validation, and unseen test subsets, and compares the three models on the test set. The test is the headline because the models did not train on those accounts.

Test ROC-AUC was 0.943 for Random Forest, 0.940 for XGBoost, and 0.942 for the probability-averaged ensemble—very similar results. At threshold 0.5, the ensemble achieved 86.1 percent accuracy, 79.4 percent precision, 91.1 percent recall, an F1 score of 0.849, and PR-AUC of 0.915.

For business stakeholders, the score can rank accounts, but a threshold creates trade-offs between precision and recall for activation. The outreach use case is to find likely non-activators, so we also assess the ranking from that direction.

For technical stakeholders, training scores are much higher than validation and test, especially for XGBoost. This generalisation gap needs investigation and monitoring. The held-out ROC-AUC is around 0.94, but that does not make the model production-ready. No model clearly dominates; the ensemble is retained for SS2 alignment, not because it is proven superior.

Accuracy alone is not enough: the dataset is imbalanced, and the business must decide the relative cost of missing a future activator versus contacting someone who would activate without help.

## Slide 6 — Solution performance: prioritising outreach
**Time: 5:05–6:15**

This decile chart sorts unseen test accounts by predicted activation probability. High-scoring groups mostly activated; the lowest groups mostly did not. That indicates useful ranking beyond a yes-or-no prediction.

In a retrospective simulation, selecting the lowest-scoring 30 percent produced a list of 221 accounts. Of those, 218 were non-activators: 98.6 percent precision for identifying stalling accounts. The list reached 51.7 percent of all 422 non-activators in the test set.

This is a promising signal: a limited outreach list could cover about half the non-activators in this sample. It is not a campaign result. No messages were sent and no response or cost was measured, so a controlled pilot must test whether outreach increases deposits.

In practice, the list should be paired with a clear next action—for example, a helpful reminder, a KYC support offer, or education about funding—then measured against a comparison group.

## Slide 7 — Modeling approach
**Time: 6:15–7:40**

The pipeline begins with twelve client tables: nine are used fully or partly, and three are excluded for leakage, unclear timing, or redundancy. After removing fourteen exact duplicate rows, there are 4,906 unique accounts.

The client’s `activated` field is the target. Accounts are split 70 percent training, 15 percent validation, and 15 percent unseen test. Cleaning, imputation, scaling, winsorisation, and encoding are fitted on training data only. SMOTE is also applied only to training.

The workflow trains Random Forest and XGBoost, then averages their probabilities for the ensemble. Validation monitors training; the unseen test is reserved for final evaluation. The full model has 169 encoded features spanning onboarding, KYC, early engagement, communications, marketing, and device context.

Feature importance helps identify inputs for investigation, but it is not causality. A strong KYC signal does not prove changing KYC status will cause activation.

The split is stratified so activation proportions are similar across subsets, and accounts—not rows from the same account—are kept separate. That makes the test more representative of scoring new accounts.

## Slide 8 — Reliability, risks, and interpretation
**Time: 7:40–8:45**

The sensitivity analysis removes uncertain-timing snapshots, then pre-deposit counts. Test ROC-AUC changes from 0.942 in the full model to 0.940 without snapshots and 0.929 without the counts as well. Most ranking performance persists without snapshots, but some signal is lost when interaction counts are removed.

Important limitations remain. Snapshot fields lack exact measurement times, the data is a single extract, and feature importance does not explain individual predictions. These retrospective results also do not establish a causal lift in activation.

Before deployment, confirm point-in-time feature availability, assess calibration, review fairness and privacy, and define a human-approved policy. Monitor ranking quality, calibration, segment performance, and data drift.

The same checks should be repeated over time. A model can rank this extract well and still degrade when channels, products, or customer behaviour change.

## Slide 9 — Next steps
**Time: 8:45–10:15**

The next steps allow the business to learn safely before scaling.

First, agree on the intervention goal and measures: eligible accounts, type of support, successful activation, contact cost, and team capacity.

Second, validate on a newer time-based cohort. Confirm every predictor existed before the outreach decision, exclude future information, and calibrate probabilities if they will be treated as likelihoods.

Third, run a controlled pilot against an appropriate control group. Measure incremental first deposits, not just model accuracy, to separate prediction from intervention effectiveness.

Finally, document ownership, access controls, human review, monitoring thresholds, and retraining criteria. SS2 proposed validation, calibration, integration, and monitoring; SS3 provides a more realistic baseline for deciding whether to proceed.

The recommendation is to pilot ranking-assisted onboarding—not automate decisions or promise unmeasured uplift.

Success should mean the pilot improves incremental first deposits at an acceptable cost, without creating unfair outcomes or overwhelming the support team. If it does not, revise the intervention or stop before production.

## Slide 10 — Closing
**Time: 10:15–11:00**

To conclude, SS1 framed the activation problem and specified the data required. SS2 built an initial modelling workflow and taught an important lesson about target leakage. SS3 applied the client-defined outcome, stronger leakage controls, and an unseen test evaluation. The result is a promising ranking tool: it identifies a high-concentration group of non-activators in the test sample, while still requiring temporal validation and a controlled campaign pilot.

**Camera cue:** Return to full camera view, thank the audience, and invite questions.

Thank you for listening. I welcome your questions and feedback.

## Sources for slide footnotes and questions

- SS1: `README_SS1.md` and `data/26303406_Bernette_CAP182_SS1_PartC Data Request.pdf`
- SS2: `preprocessing/01_Data_Preprocessing.ipynb`, `feature-extraction/02_Feature_Engineering.ipynb`, `modelling/` and `evaluation/` outputs, and `client reports/26303406_Bernette_CAP182_SS2_Part D Recommendation (28-sep-26).pdf`
- SS3: `SS3_PartB.ipynb` and the audit, metrics, outreach, sensitivity, and figure files in `results/`
- Presentation structure: `Sample Data Science Project Presentation.pdf`
