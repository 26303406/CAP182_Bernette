# CAP182_Bernette
This is the repository for the Capstone (CAP182) Project module for PGD: Data Science course

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PART A - Motivation

**Part A – Motivation**

South Africa's fintech sector is growing rapidly, with platforms such as STADIOEquities expanding access to investment products for retail investors. While the platform has attracted 2.3 million registered accounts, a significant challenge remains: many users do not become active, funded investors. Although customer acquisition is cost effective, the platform's long-term profitability depends on converting registered users into engaged investors. Current trends show declining deposit conversion rates, increasing account dormancy, and reduced uptake of premium subscription services, resulting in operational costs without corresponding revenue growth.

The root causes include ineffective onboarding processes, limited ability to identify customers at risk of disengagement, and a lack of personalised engagement strategies for different investor types. Despite having several years of behavioural, financial, and customer interaction data, much of this information remains underutilised.

Data science offers an opportunity to address these challenges through predictive modelling and customer segmentation. Predictive analytics can identify accounts likely to remain unfunded or become dormant, enabling proactive interventions, while segmentation can support personalised communication and product recommendations. Integrating customer data into a unified analytical view will enable evidence-based decision-making, improve customer activation and retention, and support STADIOEquities' strategic objective of growing a sustainable, engaged investor base without significantly increasing operating costs.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**PART E**

1. **RAAIDD Log**

The **RAAIDD Log** is a project governance tool used to record and track **Risks, Actions, Assumptions, Issues, Decisions, and Dependencies** throughout the project lifecycle. It provides a single source of information to support monitoring, decision-making, and effective project control from initiation to handover.

As a **living document**, the RAAIDD Log will be continuously reviewed and updated to reflect the current status of project risks, actions, assumptions, issues, decisions, and dependencies as the project progresses.

- 1. **Risks**

<div class="joplin-table-wrapper"><table><tbody><tr><th><p><strong>Risk No</strong></p></th><th><p><strong>Description</strong></p></th><th><p><strong>Impact</strong></p></th><th><p><strong>Probability</strong></p></th><th><p><strong>Mitigation Strategy</strong></p></th></tr><tr><td><p>R1</p></td><td><p>Incomplete Historical Data - Data may not cover full 12–18 months or have tracking gaps</p></td><td><p>High</p></td><td><p>High</p></td><td><ul><li>Perform a comprehensive data audit during week 2–3</li><li>Document quality issues</li><li>Plan subset analysis if critical gaps exist.</li></ul></td></tr><tr><td><p>R2</p></td><td><p>Class imbalance on never funded accounts (41%)</p></td><td><p>Medium</p></td><td><p>High</p></td><td><p>Stratified sampling, class weighting and SMOTE</p></td></tr><tr><td><p>R3</p></td><td><p>Temporal Drifts in User behaviour</p></td><td><p>High</p></td><td><p>High</p></td><td><p>Test on recent cohorts, recommend quarterly retraining.</p></td></tr><tr><td><p>R4</p></td><td><p>Ambiguity in Activation Definition</p></td><td><p>Medium</p></td><td><p>High</p></td><td><p>Confirm in writing by Week 1</p></td></tr><tr><td><p>R5</p></td><td><p>Privacy &amp; Compliance Barriers: Behavioral data may face regulatory scrutiny under POPIA</p></td><td><p>Medium</p></td><td><p>Medium</p></td><td><p>Engage compliance review Week 1; use pseudonymized IDs; ensure analysis is for internal use only</p></td></tr></tbody></table></div>

- 1. **Actions**

| **Action No** | **Description**                    | **Owner**            | **Timeline**   | **Status** |
| ------------- | ---------------------------------- | -------------------- | -------------- | ---------- |
| A1            | Kick-off Meeting & Project Charter | Project Manager      | Week 1 – Day 1 | Started    |
| A2            | Data Request and Formal Extract    | Data Collection Team | Week 1 – 2     | Pending    |
| A3            | Data Assessment and Quality Audit  | Data Analysis Team   | Week 2 – 4     | Pending    |
| A4            | Exploratory Data Analysis          | Data Analysis Team   | Week 4 – 6     | Pending    |
| A5            | Funnel and Cohort Analysis         | Data Analysis Team   | Week 6         | Pending    |

- 1. **Assumptions**

| **Assumption ID** | **Statement**                                       | **Criticality**    | **Validation Date** |
| ----------------- | --------------------------------------------------- | ------------------ | ------------------- |
| AS1               | Data Availability: ≥100K accounts, 12–18 months     | CRITICAL           | Week 3              |
| AS2               | Feature Reliability: Consistent tracking throughout | CRITICAL           | Week 4              |
| AS3               | Behavioral Signals Predictive: Correlation >0.1     | HIGH               | Week 4              |
| AS4               | Activation Definition Stable: No changes            | Data Analysis Team | Week 1              |
| AS5               | No Major Business Changes: Stable product           | Data Analysis Team | Week 2              |

- 1. **Issues**

The project is at pre-planning phase with no work commenced yet, with no data collected yet.

- At the pre-project planning phase (proposal stage):
- No data has been extracted yet (cannot have data quality issues)
- No models have been trained (cannot have overfitting or performance issues)
- No stakeholder presentations have occurred (cannot have misalignment issues)
- No decisions have been made (cannot have decision-based issues)
  1. **Decisions**

| **Decision ID** | **Decision Description**           | **Reason/ Rationale**                                            | **Impact**                         |
| --------------- | ---------------------------------- | ---------------------------------------------------------------- | ---------------------------------- |
| DEC1            | Focus on Activation (not churn)    | 41% non-activation is largest revenue leakage                    | Scopes to 90-day window            |
| DEC2            | 90-Day Activation Window           | Standard fintech metric; balances decision time vs. intervention | Defines target variable            |
| DEC3            | Six Data Domains (52 Features)     | Comprehensive coverage reduces missing-driver risk               | Increases extraction complexity    |
| DEC4            | Stratified 60-20-20 Train-Val-Test | Preserves class distribution; prevents overfitting               | Standard practice                  |
| DEC5            | Logistic Regression as Baseline    | Simple, interpretable; establishes performance floor             | Clarifies complexity justification |

- 1. **Dependencies**

| **Action No** | **Predecessor** | **Successor**              | **Type**             | **Risk if Delayed**              |
| ------------- | --------------- | -------------------------- | -------------------- | -------------------------------- |
| DEP1          | A1 (Kick-off)   | A2 (Data Request)          | Must Start After     | Wrong scope; SLA not agreed      |
| DEP2          | A2 (Data)       | A3 (Audit)                 | Must Complete Before | Project blocked                  |
| DEP3          | A3 (Audit)      | A4–A8 (All Analysis)       | Must Complete Before | Cannot proceed safely            |
| DEP4          | A4 (EDA)        | A5–A6 (Funnel, Clustering) | Must Start After     | Findings guide analysis          |
| DEP5          | A4–A6 (All EDA) | A7 (Feature Eng)           | Must Complete Before | Domain insights inform decisions |