# Car Fitness Center - Accounting System Template

## Overview
This template provides a complete accounting structure for a car fitness center business with 4 partners.

---

## SHEET 1: PARTNER CONTRIBUTIONS

### Purpose
Track capital contributions from each partner over time.

### Columns:
| Date | Partner Name | Amount | Payment Method | Category | Notes | Running Total |
|------|-------------|--------|----------------|----------|-------|---------------|

### Partner Names (Update these):
- Partner 1
- Partner 2
- Partner 3
- Partner 4

### Categories:
- Initial Capital
- Additional Investment
- Equipment Purchase
- Emergency Fund
- Working Capital

### Formula for Running Total:
`=SUM($C$2:C2)` (for cell G2, drag down)

---

## SHEET 2: EXPENSES

### Purpose
Track all business expenses by category.

### Columns:
| Date | Category | Subcategory | Vendor/Supplier | Description | Amount | Payment Method | Paid By (Partner) | Receipt/Invoice # | Notes |
|------|----------|-------------|-----------------|-------------|--------|----------------|-------------------|-------------------|-------|

### Expense Categories:

#### 1. **Facility Costs**
- Rent/Lease
- Utilities (Electricity, Water, Gas)
- Internet/Phone
- Property Tax
- Insurance (Property)
- Maintenance & Repairs
- Security

#### 2. **Equipment & Tools**
- Washing Equipment
- Detailing Tools
- Vacuums & Cleaners
- Polishing Machines
- Air Compressors
- Lifts/Jacks
- Diagnostic Tools
- Equipment Maintenance
- Equipment Repairs

#### 3. **Supplies & Consumables**
- Car Wash Chemicals
- Wax & Polish
- Microfiber Cloths
- Sponges & Brushes
- Air Fresheners
- Tire Shine
- Glass Cleaner
- Interior Cleaners
- Water

#### 4. **Labor Costs**
- Salaries (Regular Staff)
- Wages (Hourly Workers)
- Overtime Pay
- Bonuses & Incentives
- Benefits (Health, Retirement)
- Training & Development
- Uniforms

#### 5. **Marketing & Advertising**
- Digital Marketing (Social Media, Google Ads)
- Print Materials (Flyers, Banners)
- Website Maintenance
- Promotional Events
- Customer Loyalty Programs
- Referral Incentives

#### 6. **Administrative**
- Office Supplies
- Software Subscriptions
- Accounting/Bookkeeping Services
- Legal Fees
- Bank Fees
- Licenses & Permits
- Professional Services

#### 7. **Vehicle & Transportation**
- Company Vehicle Fuel
- Vehicle Maintenance
- Vehicle Insurance
- Parking Fees

#### 8. **Miscellaneous**
- Other Expenses

### Summary by Category (Use SUMIF):
Create a summary section at the top or side:
```
Category          | Total
------------------|--------
Facility Costs    | =SUMIF(B:B,"Facility Costs",F:F)
Equipment & Tools | =SUMIF(B:B,"Equipment & Tools",F:F)
...
```

---

## SHEET 3: REVENUE

### Purpose
Track all income sources.

### Columns:
| Date | Service Type | Customer Name | Vehicle Type | Amount | Payment Method | Received By | Invoice # | Notes |
|------|--------------|---------------|--------------|--------|----------------|-------------|-----------|-------|

### Service Types:

#### 1. **Basic Services**
- Exterior Wash (Basic)
- Exterior Wash (Premium)
- Interior Cleaning (Basic)
- Interior Cleaning (Deep Clean)
- Full Service (Exterior + Interior)

#### 2. **Premium Services**
- Waxing
- Polishing
- Paint Protection
- Ceramic Coating
- Headlight Restoration

#### 3. **Detailing Services**
- Interior Detailing
- Exterior Detailing
- Full Detailing
- Engine Bay Cleaning
- Undercarriage Cleaning

#### 4. **Specialized Services**
- Scratch Removal
- Dent Repair (Minor)
- Odor Removal
- Pet Hair Removal
- Stain Removal

#### 5. **Packages & Memberships**
- Monthly Membership
- Quarterly Package
- Annual Package
- Gift Cards

#### 6. **Other Revenue**
- Retail Products (Car Care Products)
- Vending Machines
- Other

### Summary by Service Type:
```
Service Type      | Count | Total Revenue
------------------|-------|---------------
Basic Services    | =COUNTIF(B:B,"Basic*") | =SUMIF(B:B,"Basic*",E:E)
...
```

### Daily Revenue Summary:
```
Date       | Total Revenue
-----------|---------------
[Date]     | =SUMIF(A:A,[Date],E:E)
```

---

## SHEET 4: DASHBOARD / SUMMARY

### Purpose
Provide a quick overview of business financial health.

### Key Metrics:

#### A. FINANCIAL SUMMARY
```
Metric                          | Formula/Value
--------------------------------|----------------------------------
Total Partner Contributions     | =SUM('Partner Contributions'!C:C)
Total Expenses                  | =SUM('Expenses'!F:F)
Total Revenue                   | =SUM('Revenue'!E:E)
Net Profit/Loss                 | =Total Revenue - Total Expenses
Profit Margin (%)               | =(Net Profit/Loss / Total Revenue) * 100
Cash Position                   | =Total Contributions + Net Profit/Loss
```

#### B. MONTHLY BREAKDOWN
Create a table with months and track:
- Monthly Revenue
- Monthly Expenses
- Monthly Profit/Loss
- Cumulative Profit/Loss

```
Month    | Revenue | Expenses | Profit/Loss | Cumulative
---------|---------|----------|-------------|------------
Jan 2025 | formula | formula  | formula     | formula
Feb 2025 | formula | formula  | formula     | formula
...
```

#### C. EXPENSE BREAKDOWN (PIE CHART)
- Show percentage of each expense category
- Use data from Expenses sheet summary

#### D. REVENUE BREAKDOWN (PIE CHART)
- Show percentage of each service type
- Use data from Revenue sheet summary

#### E. TREND ANALYSIS (LINE CHART)
- Monthly Revenue Trend
- Monthly Expense Trend
- Monthly Profit Trend

#### F. TOP METRICS
```
Average Daily Revenue           | =Total Revenue / Days in Operation
Average Transaction Value       | =Total Revenue / Number of Transactions
Customer Frequency              | Track repeat customers
Best Service (by revenue)       | Use MAX function on Revenue summary
Most Expensive Category         | Use MAX function on Expense summary
```

---

## SHEET 5: PARTNER EQUITY

### Purpose
Track each partner's ownership, contributions, and profit distribution.

### Partner Equity Table:

| Partner Name | Initial Investment | Additional Contributions | Total Contributions | Ownership % | Share of Profit/Loss | Distributions Taken | Net Equity |
|--------------|-------------------|-------------------------|---------------------|-------------|---------------------|-------------------|-----------|
| Partner 1    | [Amount]          | =SUMIFS(...)            | formula             | formula     | formula             | [Amount]          | formula   |
| Partner 2    | [Amount]          | =SUMIFS(...)            | formula             | formula     | formula             | [Amount]          | formula   |
| Partner 3    | [Amount]          | =SUMIFS(...)            | formula             | formula     | formula             | [Amount]          | formula   |
| Partner 4    | [Amount]          | =SUMIFS(...)            | formula             | formula     | formula             | [Amount]          | formula   |

### Column Formulas:

1. **Total Contributions**: 
   `=Initial Investment + Additional Contributions`

2. **Ownership %**:
   `=Total Contributions / SUM(All Total Contributions)`
   OR set fixed percentages if agreed (e.g., 25% each)

3. **Share of Profit/Loss**:
   `=Net Profit/Loss (from Dashboard) * Ownership %`

4. **Net Equity**:
   `=Total Contributions + Share of Profit/Loss - Distributions Taken`

### Distribution History Table:

| Date | Partner Name | Amount | Payment Method | Notes |
|------|-------------|--------|----------------|-------|

---

## SHEET 6: MONTHLY RECONCILIATION

### Purpose
Monthly closing and verification of accounts.

### Monthly Checklist:
- [ ] All expenses entered with receipts
- [ ] All revenue recorded
- [ ] Bank statements reconciled
- [ ] Partner contributions updated
- [ ] Dashboard metrics reviewed
- [ ] Discrepancies resolved

### Monthly Template:

```
Month: [Month Year]
Closing Date: [Date]
Prepared By: [Name]

BANK RECONCILIATION:
Opening Balance:              $______
+ Total Deposits (Revenue):   $______
- Total Withdrawals (Expenses): $______
Closing Balance:              $______

VARIANCE ANALYSIS:
Expected Balance:             $______
Actual Balance:               $______
Variance:                     $______
Explanation: ________________
```

---

## ADDITIONAL RECOMMENDATIONS

### 1. **Data Validation**
Set up dropdown lists for:
- Partner Names
- Expense Categories
- Service Types
- Payment Methods (Cash, Card, Bank Transfer, Check)

### 2. **Conditional Formatting**
- Highlight expenses over a certain threshold (e.g., >$500) in red
- Highlight revenue over daily target in green
- Color-code different partners

### 3. **Protection**
- Protect cells with formulas
- Allow editing only in data entry cells

### 4. **Backup**
- Set up automatic backups
- Export monthly reports as PDF

### 5. **Access Control**
- Share sheet with all 4 partners
- Consider who has edit vs. view permissions

### 6. **Receipt Management**
- Use Google Drive folder structure:
  - Receipts/2025/January/
  - Receipts/2025/February/
- Link receipt files in Notes column

### 7. **Regular Reviews**
- Weekly: Review cash flow
- Monthly: Full reconciliation and partner meeting
- Quarterly: Strategic financial review
- Annually: Tax preparation and planning

---

## FORMULAS QUICK REFERENCE

### Common SUMIF for Date Ranges:
```
=SUMIFS(Amount Column, Date Column, ">="&Start_Date, Date Column, "<="&End_Date)
```

### Current Month Revenue:
```
=SUMIFS(Revenue!E:E, Revenue!A:A, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1), Revenue!A:A, "<="&EOMONTH(TODAY(),0))
```

### Partner-Specific Expenses:
```
=SUMIF(Expenses!H:H, "Partner 1", Expenses!F:F)
```

### Average Daily Revenue:
```
=AVERAGEIFS(Revenue!E:E, Revenue!A:A, ">="&Start_Date, Revenue!A:A, "<="&End_Date)
```

---

## GETTING STARTED

### Week 1 Setup:
1. Create all 6 sheets in your Google Sheet
2. Set up column headers
3. Create data validation dropdowns
4. Enter initial partner contributions
5. Set up summary formulas on Dashboard

### Week 2-4:
1. Start recording daily transactions
2. Test all formulas
3. Adjust categories as needed
4. Train all partners on data entry

### Ongoing:
1. Daily: Record all transactions
2. Weekly: Review cash flow and metrics
3. Monthly: Full reconciliation and partner review
4. Document any issues or questions

---

## SUPPORT & MAINTENANCE

### Keep Track Of:
- When was the last backup?
- Are all formulas working correctly?
- Are categories sufficient or need updates?
- Any recurring expenses to automate?

### Regular Updates:
- Add new service types as business grows
- Adjust expense categories if needed
- Update ownership percentages if partners invest more
- Archive old data annually

---

Good luck with your car fitness center business! 🚗✨
