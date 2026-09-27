## 1. DATA PREPROCESSING TECHNIQUES

### 1.1 Data Loading & Initial Exploration

**Objective:** Load UCI Online Retail II dataset and understand its structure, missing values, and data types.

**Techniques Applied:**

1. **Dataset Source Handling and Importing Required Libraries**
   - Loaded 541,909 transactions with 8 columns from Excel (.csv) format

2. **Missing Value Analysis**
   - About 135,080 missing CustomerID, 406,829 remained after deletion
   - Missing Descriptions - majority of CustomerIDs already dropped had missing descriptions.
   - Remaining blank descriptions were imputed via StockCode lookup

3. **Removing Duplicates and Invalid Data**
   - After removing duplicates, 396,681 records remained
   - Transactions with zero or negative Quantities were removed
   - Transactions with zero/negative/extreme Unit Prices were removed

4. **Data Type Optimization**
   - Convert InvoiceDate to datetime format (enables time-based calculations)
   - Convert CustomerID, StockCode to categorical (memory efficiency)
   - Keep Quantity, Price as numeric (float64)

### 1.2 Outlier Detection & Handling

**Problem:** UCI Online Retail II contains extreme values (bulk orders, refunds, adjustments)

**Techniques Applied:**

1. **Quantile-Based Capping**
   - Identify outliers using 1st and 99th percentiles
   - Cap Quantity at [1st, 99th percentile] to preserve legitimate bulk orders
   - Cap Price at [1st, 99th percentile] to remove extreme adjustments
   - Rationale: Preserves legitimate high-value transactions while removing errors

2. **Handling Negative Values**
   - Negative Quantity = Cancellations/Returns
   - Strategy: Filter out negative quantities for primary analysis (focus on purchases)
   - Alternative: Separate "return rate" as feature for future enhancement

3. **Zero & Negative Price Handling**
   - Price ≤ 0 indicates promotional items or adjustments
   - Strategy: Set minimum price threshold (£0.01)
   - Rationale: These represent outliers in normal transaction patterns

### 1.3 Duplicate Record Removal

**Technique:** Identify and remove duplicate transaction records

- By composite key: (InvoiceNo, StockCode, CustomerID, InvoiceDate)
- Rationale: Prevents double-counting in customer aggregation metrics

### 1.4 Temporal Data Standardization

**Objective:** Create consistent time-based features for decay calculations

**Techniques:**

1. **Reference Date Selection**
   - Set reference date = Maximum InvoiceDate in dataset + 1 day
   - Rationale: Allows consistent "days since last purchase" calculation

2. **Date Range Validation**
   - Ensure all dates fall within 2009-12-01 to 2010-11-30
   - Remove outliers outside expected range

3. **Time-Based Aggregation Periods**
   - Define rolling windows: 30 days (1 month), 90 days (quarter), 365 days (year)
   - Enable calculation of recent vs. historical engagement

### 1.5 Customer-Level Aggregation

**Objective:** Transform transaction-level data to customer-level records

**Process:**

```
Input: 541,909 transaction records
↓
Group by CustomerID
↓
Aggregate metrics:
  - Number of transactions (Frequency)
  - Total spend (Monetary)
  - Date of first purchase (AccountAge)
  - Date of last purchase (Recency)
  - Various engagement metrics
↓
Output: 4338 customer records
```

**Aggregation Functions:**
- Sum: Quantity, Price (monetary value)
- Count: Distinct InvoiceNo (frequency)
- Min/Max: InvoiceDate (lifecycle dates)
- Mean/Std: Price per transaction (spending variability)

---