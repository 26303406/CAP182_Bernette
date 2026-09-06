# CAP182_Bernette

---
<div style="width: 100%; overflow-x: auto;">
  <table style="width: 100%; min-width: 900px; border-collapse: collapse; text-align: left; font-family: sans-serif;">
    <thead>
      <tr style="background-color: #4CAF50; color: white; font-weight: bold;">
        <th style="padding: 12px; border: 1px solid #ddd;">Course & Code</th>
        <th style="padding: 12px; border: 1px solid #ddd;">Assignment</th>
        <th style="padding: 12px; border: 1px solid #ddd;">Student Name</th>
        <th style="padding: 12px; border: 1px solid #ddd;">Student No</th>
        <th style="padding: 12px; border: 1px solid #ddd;">Lecturer</th>
        <th style="padding: 12px; border: 1px solid #ddd;">Date Submitted</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 12px; border: 1px solid #ddd;">Capstone Project (CAP182)</td>
        <td style="padding: 12px; border: 1px solid #ddd;">SS1</td>
        <td style="padding: 12px; border: 1px solid #ddd;">Bernette Lesejane</td>
        <td style="padding: 12px; border: 1px solid #ddd;">26303406</td>
        <td style="padding: 12px; border: 1px solid #ddd;">Dr Mia Gerber</td>
        <td style="padding: 12px; border: 1px solid #ddd;">06 September 2026</td>
      </tr>
    </tbody>
  </table>
</div>
---

## Part A – Motivation

South Africa's fintech sector is growing rapidly, with platforms such as STADIOEquities expanding access to investment products for retail investors. While the platform has attracted 2.3 million registered accounts, a significant challenge remains: many users do not become active, funded investors. Although customer acquisition is cost effective, the platform's long-term profitability depends on converting registered users into engaged investors. Current trends show declining deposit conversion rates, increasing account dormancy, and reduced uptake of premium subscription services, resulting in operational costs without corresponding revenue growth.

The root causes include ineffective onboarding processes, limited ability to identify customers at risk of disengagement, and a lack of personalised engagement strategies for different investor types. Despite having several years of behavioural, financial, and customer interaction data, much of this information remains underutilised.

Data science offers an opportunity to address these challenges through predictive modelling and customer segmentation. Predictive analytics can identify accounts likely to remain unfunded or become dormant, enabling proactive interventions, while segmentation can support personalised communication and product recommendations. Integrating customer data into a unified analytical view will enable evidence-based decision-making, improve customer activation and retention, and support STADIOEquities' strategic objective of growing a sustainable, engaged investor base without significantly increasing operating costs.

---
## Part B: Problem Statement

STADIOEquities collects a large amount of information about customers during registration and onboarding, including demographic details, onboarding progress, and platform activity. However, the company does not currently know which customers are likely to make their first deposit and become active investors, and which are likely to stop engaging with the platform.

The purpose of this study is to establish whether customer information and early platform behaviour can be used to predict account activation. Using predictive analytics and classification models, the study will identify customers who are likely to become active investors, as well as those at risk of remaining inactive or abandoning the onboarding process.

The insights gained from this research can help STADIOEquities identify high-potential and high-risk customers early, enabling the company to provide targeted support, personalized communication, and more effective retention strategies. Ultimately, this could improve account activation rates, customer engagement, and the efficient use of marketing and retention resources.

---

## Part C: Data Request

### Table 1: Account Registration & Onboarding Data

**Purpose:** Track the user onboarding funnel from registration through first deposit. Identifies where users drop off and which segments complete the onboarding journey.

| Column Name | Data Type | Example | Additional Information |
|---|---|---|---|
| account_id | String, UUID | 550e8400-e29b-41d4-a716-446655440000 | Unique identifier for each registered account |
| registration_date | DateTime | 2025-06-15 09:34:22 | Date and time of initial sign-up (yyyy-MM-dd hh:mm:ss) |
| registration_day_of_week | String, categorical | Monday | Day of week account was created; values: Monday–Sunday |
| registration_hour | Numeric, integer | 14 | Hour of day registration occurred (0–23 24-hour format) |
| acquisition_channel | String, categorical | Facebook Ad | Source of user acquisition (e.g., "Facebook Ad", "Google Search", "Referral", "Organic", "Email Campaign", "In-App Promo") |
| onboarding_completion_status | String, categorical | Completed | Final status of onboarding; values: "Completed", "Abandoned at KYC", "Abandoned at Bank Details", "Abandoned at ID Verification", "Abandoned Partial" |
| onboarding_completion_date | DateTime | 2025-06-16 11:22:45 | Date/time onboarding was completed or abandoned (yyyy-MM-dd hh:mm:ss); NULL if still in progress |
| time_to_onboarding_completion | Numeric, integer | 1440 | Minutes elapsed from registration to onboarding completion; NULL if abandoned |
| num_onboarding_sessions | Numeric, integer | 3 | Count of distinct login sessions during onboarding period |
| onboarding_dropout_step | String, categorical | ID Verification | If abandoned, the specific step where user dropped off; values: "Personal Info", "Email Verification", "Phone Verification", "KYC", "Bank Details", "ID Verification", "Fund Account Setup" |
| activated | Binary, boolean | 1 | Target variable: 1 if first deposit made within 90 days of registration; 0 if no deposit or registration >90 days old without deposit |
| first_deposit_date | DateTime | 2025-07-10 16:45:30 | Date/time of first deposit (yyyy-MM-dd hh:mm:ss); NULL if never deposited |
| days_to_first_deposit | Numeric, integer | 25 | Days elapsed from registration to first deposit; NULL if never deposited |

---

### Table 2: Initial Session Behavior & Engagement

**Purpose:** Measure early app engagement patterns during first 7 days post-registration. Captures whether users explore the platform or bounce immediately.

| Column Name | Data Type | Example | Additional Information |
|---|---|---|---|
| account_id | String, UUID | 550e8400-e29b-41d4-a716-446655440000 | Foreign key linking to account_id in Table 1 |
| first_session_date | DateTime | 2025-06-15 10:15:00 | Date/time of first login after registration (yyyy-MM-dd hh:mm:ss) |
| first_session_duration_seconds | Numeric, integer | 1240 | Total time spent in app during first session (seconds) |
| screens_viewed_in_first_session | Numeric, integer | 8 | Count of unique screens/pages navigated in first session |
| education_content_viewed | Binary, boolean | 1 | Whether user viewed educational resources (tutorials, FAQs, learning modules) in first session; 1=Yes, 0=No |
| product_exploration_depth | String, categorical | Medium | Extent of product exploration in first week; values: "None" (landing page only), "Low" (1–2 product pages), "Medium" (3–5 pages), "High" (6+ pages, multiple product types) |
| pricing_page_viewed | Binary, boolean | 1 | Whether user viewed pricing/fee information; 1=Yes, 0=No |
| faq_viewed | Binary, boolean | 0 | Whether user accessed FAQ or help section; 1=Yes, 0=No |
| promoted_feature_viewed | Binary, boolean | 1 | Whether user clicked on promoted feature or offer (e.g., fractional shares, low fees); 1=Yes, 0=No |
| first_7day_session_count | Numeric, integer | 3 | Number of distinct sessions (logins) in first 7 days post-registration |
| first_30day_session_count | Numeric, integer | 7 | Number of distinct sessions in first 30 days post-registration |
| app_version_at_signup | String, categorical | 2.14.5 | Mobile app or web version used during sign-up (version number) |
| device_type | String, categorical | Mobile iOS | Device used for registration; values: "Mobile iOS", "Mobile Android", "Desktop Web", "Tablet" |

---

### Table 3: User Demographics & Identity Data

**Purpose:** Segment users by demographic characteristics. Identifies which cohorts activate at higher rates and enables segment-specific intervention strategies.

| Column Name | Data Type | Example | Additional Information |
|---|---|---|---|
| account_id | String, UUID | 550e8400-e29b-41d4-a716-446655440000 | Foreign key linking to account_id in Table 1 |
| age_group | String, categorical | 25-34 | Age bracket; values: "18-24", "25-34", "35-44", "45-54", "55+" |
| gender | String, categorical | M | Inferred from KYC process (if provided); values: "M", "F", "Other", "Not Provided" |
| province | String, categorical | GP | Province of residence (South African); values: "GP", "EC", "FS", "KZN", "LP", "MP", "NC", "NW", "WC" |
| metro_status | String, categorical | Metro | Whether user is in major metro area or non-metro; values: "Metro", "Non-Metro" |
| employment_status | String, categorical | Employed | Inferred from profile or KYC; values: "Employed", "Self-Employed", "Student", "Unemployed", "Retired", "Not Disclosed" |
| investor_experience_level | String, categorical | Beginner | Self-reported during onboarding; values: "Beginner", "Intermediate", "Advanced", "Not Disclosed" |
| stated_investment_goal | String, categorical | Long-term Growth | Primary investment objective from profile; values: "Day Trading", "Short-term Gains", "Long-term Growth", "Dividend Income", "Savings/Emergency", "Learning/Experimentation", "Not Stated" |

---

### Table 4: Communication & Support Interactions

**Purpose:** Track basic user communication engagement: email responses and support interactions during onboarding. Identifies communication barriers and engagement with app assistance.

| Column Name | Data Type | Example | Additional Information |
|---|---|---|---|
| account_id | String, UUID | 550e8400-e29b-41d4-a716-446655440000 | Foreign key linking to account_id in Table 1 |
| onboarding_emails_sent | Numeric, integer | 3 | Number of system-generated onboarding emails sent during sign-up and 7-day window |
| onboarding_email_open_rate | Numeric, decimal | 0.67 | Proportion of onboarding emails opened by user (0.0–1.0); 0.67 means 2 of 3 opened |
| promotional_emails_sent | Numeric, integer | 2 | Number of promotional/engagement emails sent in first 30 days |
| promotional_email_open_rate | Numeric, decimal | 0.50 | Proportion of promotional emails opened (0.0–1.0) |
| support_tickets_opened | Numeric, integer | 1 | Count of support requests or inquiries raised during onboarding and 30-day window |
| support_ticket_type | String, categorical | Account Setup Question | If support_tickets_opened > 0, the primary type of inquiry; values: "Account Setup Question", "Technical Issue", "Fee/Pricing Question", "KYC/Verification Issue", "Other" |
| support_resolution_time_hours | Numeric, decimal | 4.5 | Time in hours from support ticket creation to resolution; NULL if unresolved |
| in_app_help_viewed | Binary, boolean | 0 | Whether user accessed in-app help/chat feature; 1=Yes, 0=No |
| feedback_submitted | Binary, boolean | 0 | Whether user submitted in-app feedback or feature request; 1=Yes, 0=No |

---

### Table 5: Platform Interaction Before First Deposit (or Abandonment Window)

**Purpose:** Track platform feature usage BEFORE first deposit. Measures investment research behaviors, intent signals, and platform familiarity that predict deposit likelihood.

| Column Name | Data Type | Example | Additional Information |
|---|---|---|---|
| account_id | String, UUID | 550e8400-e29b-41d4-a716-446655440000 | Foreign key linking to account_id in Table 1 |
| pre_deposit_window_days | Numeric, integer | 30 | Number of days analyzed before first deposit or abandonment threshold (typically 30–90 days from registration) |
| search_page_visits | Numeric, integer | 5 | Count of visits to stock/ETF search or discovery pages |
| watchlist_created | Binary, boolean | 1 | Whether user created a watchlist; 1=Yes, 0=No |
| watchlist_items | Numeric, integer | 4 | Number of stocks/ETFs added to watchlist if watchlist_created=1 |
| detailed_stock_views | Numeric, integer | 8 | Count of times user opened detailed stock/ETF information pages |
| price_alert_set | Binary, boolean | 0 | Whether user set any price alerts; 1=Yes, 0=No |
| comparison_tool_used | Binary, boolean | 1 | Whether user used product comparison or calculator tools; 1=Yes, 0=No |
| trading_simulation_engaged | Binary, boolean | 0 | Whether user engaged with paper trading or simulation feature; 1=Yes, 0=No |
| account_balance_before_first_action | Numeric, decimal | 0.00 | Available balance (in ZAR) before first deposit; 0.00 if never deposited |
| total_pre_deposit_minutes | Numeric, integer | 4230 | Total minutes spent on platform before first deposit (or in 90-day abandonment window) |

---

### Table 6: Feature Requests & In-App Messaging Responses

**Purpose:** Track user response to in-app promotions, notifications, and feature requests. Identifies messaging effectiveness and what users want from the platform.

| Column Name | Data Type | Example | Additional Information |
|---|---|---|---|
| account_id | String, UUID | 550e8400-e29b-41d4-a716-446655440000 | Foreign key linking to account_id in Table 1 |
| app_notification_opt_in | Binary, boolean | 1 | Whether user opted in to push notifications during onboarding; 1=Yes, 0=No |
| push_notifications_received | Numeric, integer | 5 | Count of push notifications sent to user in pre-deposit window |
| push_notification_open_rate | Numeric, decimal | 0.40 | Proportion of push notifications opened (0.0–1.0) |
| in_app_promo_banner_impressions | Numeric, integer | 12 | Count of times promotional banners were displayed to user |
| in_app_promo_banner_clicks | Numeric, integer | 2 | Count of clicks on promotional banners |
| premium_subscription_offer_shown | Binary, boolean | 1 | Whether premium subscription offer was displayed during onboarding/early engagement; 1=Yes, 0=No |
| premium_subscription_offer_clicked | Binary, boolean | 0 | Whether user clicked on premium offer; 1=Yes, 0=No |
| feature_request_submitted | Binary, boolean | 0 | Whether user submitted feature request; 1=Yes, 0=No |

---

### Table 7: Support Ticket and Customer Service Interactions

**Purpose:** Track detailed customer support interactions during onboarding and early engagement. Identifies support barriers, friction points, resolution quality, and support-driven abandonment.

| Column Name                 | Data Type              | Example                    | Additional Information                                        |
| --------------------------- | ---------------------- | -------------------------- | ------------------------------------------------------------- |
| account_id                  | String, UUID           | 550e8400-...               | Foreign key to Table 1                                        |
| ticket_id                   | String, UUID           | T-20250615-00347           | Unique ticket identifier                                      |
| ticket_category             | String, categorical    | Account Verification Issue | Type: Account Setup, KYC, Technical, Fee Question, etc.       |
| ticket_priority             | String, categorical    | High                       | Values: Urgent, High, Medium, Low                             |
| support_channel             | String, categorical    | In-app Chat                | Channel: Chat, Email, Phone, Social, FAQ, Help Center         |
| first_response_time_minutes | Numeric, integer       | 12                         | Minutes to first response                                     |
| resolution_time_minutes     | Numeric, integer       | 187                        | Minutes to resolution                                         |
| resolution_status           | String, categorical    | Resolved                   | Status: Resolved, Workaround, Closed Without Resolution, etc. |
| follow_up_rating            | Numeric, integer (1-5) | 3                          | User satisfaction rating; NULL if no survey                   |

---

### Table 8: Marketing Campaing and spend data

**Purpose:** Track marketing campaigns, user acquisition attribution, and campaign performance. Identifies which marketing channels and messages drive activation.

| Column Name                 | Data Type           | Example                      | Additional Information                                           |
| --------------------------- | ------------------- | ---------------------------- | ---------------------------------------------------------------- |
| account_id                  | String, UUID        | 550e8400-...                 | Foreign key to Table 1                                           |
| marketing_campaign_id       | String, categorical | SUMMER_2025_FACEBOOK         | Campaign identifier                                              |
| campaign_channel            | String, categorical | Facebook Ads                 | Channels: FB, Google, Instagram, LinkedIn, Email, Referral, etc. |
| campaign_message_theme      | String, categorical | Fractional Shares / Low Cost | Message: Fractional Shares, Low Fees, Easy Onboarding, etc.      |
| user_exposed_date           | DateTime            | 2025-06-10 08:15:22          | Campaign exposure date                                           |
| user_clicked                | Binary, boolean     | 1                            | Whether user clicked on campaign asset                           |
| conversion_within_30days    | Binary, boolean     | 1                            | Activation within 30 days of exposure                            |
| campaign_spend_per_user_zar | Numeric, decimal    | 2.47                         | Cost per user (ZAR)                                              |
| campaign_roi_percent        | Numeric, decimal    | 18.5                         | ROI of campaign (%)                                              |
| is_first_touch_attribution  | Binary, boolean     | 1                            | Was this campaign first marketing touch                          |

---

### Table 9: Compliance and KYC Verification Data

**Purpose:** Track regulatory compliance, KYC verification, and risk assessments. Identifies compliance barriers to activation.

| Column Name              | Data Type                | Example      | Additional Information                                          |
| ------------------------ | ------------------------ | ------------ | --------------------------------------------------------------- |
| account_id               | String, UUID             | 550e8400-... | Foreign key to Table 1                                          |
| kyc_status               | String, categorical      | Verified     | Status: Not Started, In Progress, Verified, Rejected, Suspended |
| kyc_days_to_verification | Numeric, integer         | 1            | Days from submission to verification                            |
| kyc_rejection_count      | Numeric, integer         | 0            | Number of rejections and resubmissions                          |
| aml_risk_score           | Numeric, integer (0-100) | 23           | AML risk score (0=Low, 100=High)                                |
| pep_list_check           | Binary, boolean          | 0            | Politically Exposed Person match (1=Match)                      |
| sanctions_list_check     | Binary, boolean          | 0            | International sanctions list match                              |
| compliance_flags_count   | Numeric, integer         | 0            | Count of compliance concerns                                    |
| document_expired         | Binary, boolean          | 0            | Identity document expired                                       |

---
### Table 10: User Feedback and Satisfaction Survey Data

**Purpose:** Track NPS, CSAT, feature requests, and user feedback. Identifies pain points and satisfaction drivers.

| Column Name               | Data Type                  | Example      | Additional Information                                          |
| ------------------------- | -------------------------- | ------------ | --------------------------------------------------------------- |
| account_id                | String, UUID               | 550e8400-... | Foreign key to Table 1                                          |
| feedback_type             | String, categorical        | NPS Survey   | Type: NPS, CSAT, Feature Request, Bug Report, etc.              |
| nps_score                 | Numeric, integer (0-10)    | 8            | Net Promoter Score (0-10)                                       |
| nps_category              | String, categorical        | Promoter     | Classification: Promoter (9-10), Passive (7-8), Detractor (0-6) |
| csat_score                | Numeric, integer (1-5)     | 4            | Customer Satisfaction (1=Unsatisfied, 5=Satisfied)              |
| feature_request_submitted | Binary, boolean            | 1            | Whether feature was requested                                   |
| pain_point_mentioned      | Binary, boolean            | 1            | Whether friction/barrier identified                             |
| barrier_to_activation     | Binary, boolean            | 0            | Whether barrier to first deposit identified                     |
| sentiment_analysis_score  | Numeric, decimal (-1 to 1) | 0.67         | ML sentiment score of open-text feedback                        |

---
### Table 11: Device, Browser and Technical Environment Data

**Purpose**: Track device, browser, and technical environment. Identifies technical barriers and platform-specific activation patterns.

| Column Name         | Data Type           | Example       | Additional Information                       |
| ------------------- | ------------------- | ------------- | -------------------------------------------- |
| account_id          | String, UUID        | 550e8400-...  | Foreign key to Table 1                       |
| signup_device_type  | String, categorical | Mobile iPhone | Device at sign-up                            |
| signup_os_name      | String, categorical | iOS           | OS: iOS, Android, Windows, macOS             |
| signup_browser_name | String, categorical | Safari        | Browser: Safari, Chrome, Firefox, Edge, etc. |
| connection_type     | String, categorical | WiFi          | Network: WiFi, Mobile 4G, Mobile 5G, etc.    |
| device_switch_count | Numeric, integer    | 0             | Times user switched devices                  |
| vpn_detected        | Binary, boolean     | 0             | VPN usage detected (compliance flag)         |
| ad_blocker_detected | Binary, boolean     | 0             | Ad blocker enabled                           |
| timezone_offset     | String, categorical | UTC+2         | User timezone (e.g., SAST)                   |

---
### Table 12: Account Activity Post-Deposit (Post-Activation Engagement)

**Purpose:** Track account activity AFTER first deposit to assess activation quality and long-term engagement.

| Column Name                       | Data Type           | Example             | Additional Information                              |
| --------------------------------- | ------------------- | ------------------- | --------------------------------------------------- |
| account_id                        | String, UUID        | 550e8400-...        | Foreign key to Table 1 (activated accounts only)    |
| first_deposit_date                | DateTime            | 2025-07-10 16:45:30 | First deposit date                                  |
| first_deposit_amount_zar          | Numeric, decimal    | 5000.00             | First deposit amount (ZAR)                          |
| post_deposit_session_count_90days | Numeric, integer    | 18                  | Sessions in first 90 days post-deposit              |
| first_trade_date                  | DateTime            | 2025-07-15 09:22:14 | Date of first trade/investment                      |
| total_trades_90days               | Numeric, integer    | 12                  | Count of trades in 90 days                          |
| account_balance_90days            | Numeric, decimal    | 4850.00             | Account balance 90 days later                       |
| realized_gains_losses_zar         | Numeric, decimal    | \-150.00            | P&L from executed trades                            |
| subsequent_deposit_made           | Binary, boolean     | 1                   | Additional deposit after first                      |
| quality_of_activation             | String, categorical | Genuine Active      | Classification: Genuine Active, Dormant, Suspicious |

---
### Summary: All 12 Data Domains

| Table | Domain                    | Features | Est. Rows | Purpose             |
| ----- | ------------------------- | -------- | --------- | ------------------- |
| 1     | Registration & Onboarding | 13       | 100K      | Funnel completion   |
| 2     | Session Behavior          | 10       | 100K      | Early engagement    |
| 3     | Demographics              | 7        | 100K      | Segmentation        |
| 4     | Communication & Support   | 8        | 250K      | Email engagement    |
| 5     | Platform Interaction      | 7        | 100K      | Pre-deposit intent  |
| 6     | Feature Requests          | 7        | 150K      | Engagement response |
| 7     | Support Tickets           | 16       | 200K      | Support friction    |
| 8     | Marketing Attribution     | 22       | 500K      | Channel ROI         |
| 9     | Compliance & KYC          | 19       | 100K      | Regulatory barriers |
| 10    | User Feedback             | 17       | 300K      | Pain points & NPS   |
| 11    | Device & Browser          | 18       | 100K      | Technical barriers  |
| 12    | Post-Deposit Activity     | 24       | 40K       | Activation quality  |

**TOTAL:** 12 domains | 168 features | 2.04M rows | 145 MB estimated size
---

## PART D - Repository set up and structure
```text
.
├── .gitignore
├── LICENSE
├── README.md
├── dashboards/
│   └── README.md
├── data/
│   └── README.md
├── evaluation/
│   └── README.md
├── feature-extraction/
│   └── README.md
├── modelling/
│   └── README.md
├── preprocessing/
│   └── README.md
├── retraining/
│   └── README.md
├── utils/
│   └── README.md
└── visualisation/
    └── README.md
```

## PART E - RAAIDD Log

The **RAAIDD Log** is a project governance tool used to record and track **Risks, Actions, Assumptions, Issues, Decisions, and Dependencies** throughout the project lifecycle. It provides a single source of information to support monitoring, decision-making, and effective project control from initiation to handover.

As a **living document**, the RAAIDD Log will be continuously reviewed and updated to reflect the current status of project risks, actions, assumptions, issues, decisions, and dependencies as the project progresses.

1. **Risks**

| Risk No | Description | Impact | Probability | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| R1 | Incomplete Historical Data - Data may not cover full 12–18 months or have tracking gaps | High | High | • Perform a comprehensive data audit during week 2–3<br>• Document quality issues<br>• Plan subset analysis if critical gaps exist. |
| R2 | Class imbalance on never funded accounts (41%) | Medium | High | Stratified sampling, class weighting and SMOTE |
| R3 | Temporal Drifts in User behaviour | High | High | Test on recent cohorts, recommend quarterly retraining. |
| R4 | Ambiguity in Activation Definition | Medium | High | Confirm in writing by Week 1 |
| R5 | Privacy & Compliance Barriers: Behavioral data may face regulatory scrutiny under POPIA | Medium | Medium | Engage compliance review Week 1; use pseudonymized IDs; ensure analysis is for internal use only |

2. **Actions**

| **Action No** | **Description**                    | **Owner**            | **Timeline**   | **Status** |
| ------------- | ---------------------------------- | -------------------- | -------------- | ---------- |
| A1            | Kick-off Meeting & Project Charter | Project Manager      | Week 1 – Day 1 | Started    |
| A2            | Data Request and Formal Extract    | Data Collection Team | Week 1 – 2     | Pending    |
| A3            | Data Assessment and Quality Audit  | Data Analysis Team   | Week 2 – 4     | Pending    |
| A4            | Exploratory Data Analysis          | Data Analysis Team   | Week 4 – 6     | Pending    |
| A5            | Funnel and Cohort Analysis         | Data Analysis Team   | Week 6         | Pending    |

3. **Assumptions**

| **Assumption ID** | **Statement**                                       | **Criticality**    | **Validation Date** |
| ----------------- | --------------------------------------------------- | ------------------ | ------------------- |
| AS1               | Data Availability: ≥100K accounts, 12–18 months     | CRITICAL           | Week 3              |
| AS2               | Feature Reliability: Consistent tracking throughout | CRITICAL           | Week 4              |
| AS3               | Behavioral Signals Predictive: Correlation >0.1     | HIGH               | Week 4              |
| AS4               | Activation Definition Stable: No changes            | Data Analysis Team | Week 1              |
| AS5               | No Major Business Changes: Stable product           | Data Analysis Team | Week 2              |

4. **Issues**

There are no issues at the because the project is at pre-planning phase with no work commenced and no data collected as yet.

- No data has been extracted yet (cannot have data quality issues)
- No models have been trained (cannot have overfitting or performance issues)
- No stakeholder presentations have occurred (cannot have misalignment issues)
- No decisions have been made (cannot have decision-based issues)

  5. **Decisions**

| **Decision ID** | **Decision Description**           | **Reason/ Rationale**                                            | **Impact**                         |
| --------------- | ---------------------------------- | ---------------------------------------------------------------- | ---------------------------------- |
| DEC1            | Focus on Activation (not churn)    | 41% non-activation is largest revenue leakage                    | Scopes to 90-day window            |
| DEC2            | 90-Day Activation Window           | Standard fintech metric; balances decision time vs. intervention | Defines target variable            |
| DEC3            | Six Data Domains (52 Features)     | Comprehensive coverage reduces missing-driver risk               | Increases extraction complexity    |
| DEC4            | Stratified 60-20-20 Train-Val-Test | Preserves class distribution; prevents overfitting               | Standard practice                  |
| DEC5            | Logistic Regression as Baseline    | Simple, interpretable; establishes performance floor             | Clarifies complexity justification |

6. **Dependencies**

| **Action No** | **Predecessor** | **Successor**              | **Type**             | **Risk if Delayed**              |
| ------------- | --------------- | -------------------------- | -------------------- | -------------------------------- |
| DEP1          | A1 (Kick-off)   | A2 (Data Request)          | Must Start After     | Wrong scope; SLA not agreed      |
| DEP2          | A2 (Data)       | A3 (Audit)                 | Must Complete Before | Project blocked                  |
| DEP3          | A3 (Audit)      | A4–A8 (All Analysis)       | Must Complete Before | Cannot proceed safely            |
| DEP4          | A4 (EDA)        | A5–A6 (Funnel, Clustering) | Must Start After     | Findings guide analysis          |
| DEP5          | A4–A6 (All EDA) | A7 (Feature Eng)           | Must Complete Before | Domain insights inform decisions |