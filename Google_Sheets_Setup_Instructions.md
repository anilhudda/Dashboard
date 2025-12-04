# Step-by-Step Google Sheets Setup Instructions

## Step 1: Create Sheet Structure

1. **Open your Google Sheet**: [Your provided link]
2. **Create 6 tabs** at the bottom (rename the sheets):
   - `Partner Contributions`
   - `Expenses`
   - `Revenue`
   - `Dashboard`
   - `Partner Equity`
   - `Monthly Reconciliation`

---

## Step 2: Partner Contributions Sheet

### Setup:
1. In Row 1, create headers:
   ```
   A1: Date
   B1: Partner Name
   C1: Amount
   D1: Payment Method
   E1: Category
   F1: Notes
   G1: Running Total
   ```

2. **Format the sheet:**
   - Row 1: Bold, Background color (light blue), Center align
   - Column A: Format as Date
   - Column C: Format as Currency ($)
   - Column G: Format as Currency ($)

3. **Add Data Validation for Column B (Partner Name):**
   - Select cells B2:B1000
   - Data → Data validation
   - Criteria: List of items
   - Enter: `Partner 1, Partner 2, Partner 3, Partner 4`
   - Check "Show dropdown list in cell"

4. **Add Data Validation for Column D (Payment Method):**
   - Select cells D2:D1000
   - Data → Data validation
   - List: `Cash, Bank Transfer, Credit Card, Check`

5. **Add Data Validation for Column E (Category):**
   - Select cells E2:E1000
   - Data → Data validation
   - List: `Initial Capital, Additional Investment, Equipment Purchase, Emergency Fund, Working Capital`

6. **Add Formula in G2 (Running Total):**
   ```
   =SUM($C$2:C2)
   ```
   - Drag down to copy formula

7. **Add Summary Box** (in a clear area, e.g., columns I-K):
   ```
   I2: Total Contributions
   J2: =SUM(C:C)
   
   I4: By Partner:
   I5: Partner 1
   J5: =SUMIF(B:B,"Partner 1",C:C)
   I6: Partner 2
   J6: =SUMIF(B:B,"Partner 2",C:C)
   I7: Partner 3
   J7: =SUMIF(B:B,"Partner 3",C:C)
   I8: Partner 4
   J8: =SUMIF(B:B,"Partner 4",C:C)
   ```
   - Format J2, J5:J8 as Currency
   - Bold I2, I4

---

## Step 3: Expenses Sheet

### Setup:
1. **Create headers in Row 1:**
   ```
   A1: Date
   B1: Category
   C1: Subcategory
   D1: Vendor/Supplier
   E1: Description
   F1: Amount
   G1: Payment Method
   H1: Paid By (Partner)
   I1: Receipt/Invoice #
   J1: Notes
   ```

2. **Format:**
   - Row 1: Bold, Background color, Center align
   - Column A: Date format
   - Column F: Currency format

3. **Add Data Validation:**
   
   **Column B (Category):**
   - Select B2:B1000
   - List: 
   ```
   Facility Costs, Equipment & Tools, Supplies & Consumables, Labor Costs, Marketing & Advertising, Administrative, Vehicle & Transportation, Miscellaneous
   ```

   **Column G (Payment Method):**
   - Select G2:G1000
   - List: `Cash, Bank Transfer, Credit Card, Check`

   **Column H (Paid By):**
   - Select H2:H1000
   - List: `Partner 1, Partner 2, Partner 3, Partner 4`

4. **Add Summary Section** (Rows above data or to the side):
   - Create a table in columns M-N, starting at row 2:
   ```
   M1: EXPENSE SUMMARY
   M2: Category
   N2: Total
   
   M3: Facility Costs
   N3: =SUMIF(B:B,"Facility Costs",F:F)
   
   M4: Equipment & Tools
   N4: =SUMIF(B:B,"Equipment & Tools",F:F)
   
   M5: Supplies & Consumables
   N5: =SUMIF(B:B,"Supplies & Consumables",F:F)
   
   M6: Labor Costs
   N6: =SUMIF(B:B,"Labor Costs",F:F)
   
   M7: Marketing & Advertising
   N7: =SUMIF(B:B,"Marketing & Advertising",F:F)
   
   M8: Administrative
   N8: =SUMIF(B:B,"Administrative",F:F)
   
   M9: Vehicle & Transportation
   N9: =SUMIF(B:B,"Vehicle & Transportation",F:F)
   
   M10: Miscellaneous
   N10: =SUMIF(B:B,"Miscellaneous",F:F)
   
   M12: TOTAL EXPENSES
   N12: =SUM(N3:N10)
   ```
   - Format N3:N12 as Currency
   - Bold M1, M12, N12

5. **Conditional Formatting** (highlight large expenses):
   - Select column F (Amount)
   - Format → Conditional formatting
   - Format cells if: Greater than 500
   - Background: Light red

---

## Step 4: Revenue Sheet

### Setup:
1. **Create headers in Row 1:**
   ```
   A1: Date
   B1: Service Type
   C1: Customer Name
   D1: Vehicle Type
   E1: Amount
   F1: Payment Method
   G1: Received By
   H1: Invoice #
   I1: Notes
   ```

2. **Format:**
   - Row 1: Bold, Background color, Center align
   - Column A: Date format
   - Column E: Currency format

3. **Add Data Validation:**
   
   **Column B (Service Type):**
   - Select B2:B1000
   - List: 
   ```
   Basic Services - Exterior Wash Basic, Basic Services - Exterior Wash Premium, Basic Services - Interior Cleaning Basic, Basic Services - Interior Cleaning Deep, Basic Services - Full Service, Premium Services - Waxing, Premium Services - Polishing, Premium Services - Paint Protection, Premium Services - Ceramic Coating, Detailing Services - Interior Detailing, Detailing Services - Exterior Detailing, Detailing Services - Full Detailing, Packages & Memberships - Monthly, Packages & Memberships - Quarterly, Other Revenue
   ```

   **Column D (Vehicle Type):**
   - List: `Sedan, SUV, Truck, Van, Sports Car, Luxury Sedan, Luxury SUV, Other`

   **Column F (Payment Method):**
   - List: `Cash, Credit Card, Debit Card, Bank Transfer, Digital Wallet`

4. **Add Summary Section** (columns K-M):
   ```
   K1: REVENUE SUMMARY
   
   K2: Total Revenue
   L2: =SUM(E:E)
   
   K3: Total Transactions
   L3: =COUNTA(E:E)-1
   
   K4: Average Transaction
   L4: =L2/L3
   
   K6: By Service Type:
   K7: Basic Services
   L7: =SUMIF(B:B,"Basic Services*",E:E)
   
   K8: Premium Services
   L8: =SUMIF(B:B,"Premium Services*",E:E)
   
   K9: Detailing Services
   L9: =SUMIF(B:B,"Detailing Services*",E:E)
   
   K10: Packages & Memberships
   L10: =SUMIF(B:B,"Packages & Memberships*",E:E)
   
   K11: Other Revenue
   L11: =SUMIF(B:B,"Other Revenue",E:E)
   ```
   - Format L2, L4, L7:L11 as Currency
   - Bold K1, K2, K6

5. **Daily Revenue Tracker** (separate section or new area):
   - Create a pivot table or use QUERY function
   - Or manually create with SUMIF by date

---

## Step 5: Dashboard Sheet

### Setup:
This is your main overview sheet with key metrics and charts.

1. **Create a visually appealing layout:**

```
                CAR FITNESS CENTER
            FINANCIAL DASHBOARD
        ================================

FINANCIAL OVERVIEW
------------------
Total Partner Contributions:    $________
Total Expenses:                  $________
Total Revenue:                   $________
Net Profit/Loss:                 $________
Profit Margin:                   ____%
Current Cash Position:           $________


MONTHLY PERFORMANCE
-------------------
Month       Revenue    Expenses   Profit/Loss
Jan 2025    $___       $___       $___
Feb 2025    $___       $___       $___
Mar 2025    $___       $___       $___
...


TOP METRICS
-----------
Average Daily Revenue:           $________
Average Transaction Value:       $________
Total Transactions:              ________
Days in Operation:               ________
```

2. **Add the actual formulas:**

   **Cell B4 (Total Partner Contributions):**
   ```
   =SUM('Partner Contributions'!C:C)
   ```

   **Cell B5 (Total Expenses):**
   ```
   =SUM(Expenses!F:F)
   ```

   **Cell B6 (Total Revenue):**
   ```
   =SUM(Revenue!E:E)
   ```

   **Cell B7 (Net Profit/Loss):**
   ```
   =B6-B5
   ```

   **Cell B8 (Profit Margin):**
   ```
   =IF(B6=0,0,B7/B6*100)
   ```
   Format as Percentage

   **Cell B9 (Current Cash Position):**
   ```
   =B4+B7
   ```

3. **Monthly Performance Table:**
   
   For January 2025 Revenue (adjust cell references as needed):
   ```
   =SUMIFS(Revenue!$E:$E, Revenue!$A:$A, ">="&DATE(2025,1,1), Revenue!$A:$A, "<="&DATE(2025,1,31))
   ```
   
   For January 2025 Expenses:
   ```
   =SUMIFS(Expenses!$F:$F, Expenses!$A:$A, ">="&DATE(2025,1,1), Expenses!$A:$A, "<="&DATE(2025,1,31))
   ```
   
   Profit/Loss: `=Revenue-Expenses`

4. **Add Charts:**

   **Expense Breakdown (Pie Chart):**
   - Insert → Chart
   - Chart type: Pie chart
   - Data range: Select the Expenses summary from Expenses sheet (M3:N10)
   - Title: "Expense Distribution by Category"

   **Revenue by Service Type (Pie Chart):**
   - Insert → Chart
   - Chart type: Pie chart
   - Data range: Revenue summary (K7:L11 from Revenue sheet)
   - Title: "Revenue by Service Type"

   **Monthly Trend (Line Chart):**
   - Insert → Chart
   - Chart type: Line chart
   - Data range: Monthly Performance table
   - Series: Revenue, Expenses, Profit/Loss
   - Title: "Monthly Financial Trends"

5. **Conditional Formatting:**
   - Highlight Net Profit/Loss:
     - Green if positive
     - Red if negative

---

## Step 6: Partner Equity Sheet

### Setup:
1. **Create the equity table:**
   ```
   Row 1: Headers
   A1: Partner Name
   B1: Initial Investment
   C1: Additional Contributions
   D1: Total Contributions
   E1: Ownership %
   F1: Share of Profit/Loss
   G1: Distributions Taken
   H1: Net Equity
   
   Row 2-5: Partner data
   A2: Partner 1
   A3: Partner 2
   A4: Partner 3
   A5: Partner 4
   ```

2. **Add formulas:**

   **B2-B5 (Initial Investment):**
   ```
   =SUMIFS('Partner Contributions'!$C:$C, 'Partner Contributions'!$B:$B, A2, 'Partner Contributions'!$E:$E, "Initial Capital")
   ```
   Copy down for all partners

   **C2-C5 (Additional Contributions):**
   ```
   =SUMIFS('Partner Contributions'!$C:$C, 'Partner Contributions'!$B:$B, A2)-B2
   ```
   Copy down

   **D2-D5 (Total Contributions):**
   ```
   =B2+C2
   ```
   Copy down

   **E2-E5 (Ownership %):**
   ```
   =D2/SUM($D$2:$D$5)
   ```
   Format as Percentage
   Copy down

   **F2-F5 (Share of Profit/Loss):**
   ```
   =Dashboard!$B$7*E2
   ```
   (Adjust cell reference to point to Net Profit/Loss on Dashboard)
   Copy down

   **G2-G5 (Distributions Taken):**
   - Manual entry (enter any distributions partners have taken)

   **H2-H5 (Net Equity):**
   ```
   =D2+F2-G2
   ```
   Copy down

3. **Add totals row:**
   ```
   A6: TOTAL
   B6: =SUM(B2:B5)
   C6: =SUM(C2:C5)
   D6: =SUM(D2:D5)
   E6: =SUM(E2:E5)  (should equal 100%)
   F6: =SUM(F2:F5)
   G6: =SUM(G2:G5)
   H6: =SUM(H2:H5)
   ```
   Bold row 6

4. **Add Distribution History Table** (below main table):
   ```
   Row 10: Distribution History
   
   Row 11: Headers
   A11: Date
   B11: Partner Name
   C11: Amount
   D11: Payment Method
   E11: Notes
   ```

---

## Step 7: Monthly Reconciliation Sheet

### Setup:
1. **Create monthly template structure:**
   ```
   A1: MONTHLY RECONCILIATION
   
   A3: Month:
   B3: [Dropdown with months]
   
   A4: Closing Date:
   B4: [Date]
   
   A5: Prepared By:
   B5: [Name]
   
   A7: BANK RECONCILIATION
   A8: Opening Balance:
   B8: [Amount]
   
   A9: + Total Deposits (Revenue):
   B9: =SUMIFS(Revenue!$E:$E, Revenue!$A:$A, ">="&[StartDate], Revenue!$A:$A, "<="&[EndDate])
   
   A10: - Total Withdrawals (Expenses):
   B10: =SUMIFS(Expenses!$F:$F, Expenses!$A:$A, ">="&[StartDate], Expenses!$A:$A, "<="&[EndDate])
   
   A11: Closing Balance:
   B11: =B8+B9-B10
   
   A13: VARIANCE ANALYSIS
   A14: Expected Balance:
   B14: [From calculation]
   
   A15: Actual Balance:
   B15: [From bank statement]
   
   A16: Variance:
   B16: =B15-B14
   
   A17: Explanation:
   B17: [Text field]
   
   A20: MONTHLY CHECKLIST
   A21: ☐ All expenses entered with receipts
   A22: ☐ All revenue recorded
   A23: ☐ Bank statements reconciled
   A24: ☐ Partner contributions updated
   A25: ☐ Dashboard metrics reviewed
   A26: ☐ Discrepancies resolved
   ```

---

## Step 8: Final Touches

### 1. **Formatting & Colors:**
- Use a consistent color scheme across all sheets
- Suggestion:
  - Headers: Light blue (#4A86E8)
  - Summary sections: Light yellow (#FFE599)
  - Important metrics: Light green (#B6D7A8)
  - Negative values: Light red (#E06666)

### 2. **Freeze Rows:**
- On each sheet, freeze the header row (Row 1)
- View → Freeze → 1 row

### 3. **Protect Formulas:**
- Select cells with formulas
- Data → Protect sheets and ranges
- Set permissions so formulas can't be accidentally deleted

### 4. **Add Notes/Comments:**
- Add comments to important cells explaining formulas
- Right-click → Insert comment

### 5. **Create a Table of Contents:**
- Consider adding a first sheet called "Home" or "Instructions"
- Add links to each sheet
- Include quick instructions

### 6. **Set Up Sharing:**
- Click "Share" button (top right)
- Add all 4 partners with appropriate permissions
- Consider: Editor access for all or specific roles

### 7. **Enable Version History:**
- Already enabled by default in Google Sheets
- File → Version history → See version history
- Name important versions

### 8. **Set Up Notifications:**
- Tools → Notification rules
- Set up alerts for changes (optional)

---

## Step 9: Import Sample Data

1. **Copy sample data** from the `Sample_Data.csv` file
2. **Paste into appropriate sheets** to test formulas
3. **Verify all calculations** are working correctly
4. **Delete sample data** once confirmed
5. **Begin entering real data**

---

## Step 10: Training & Maintenance

### Training Checklist for Partners:
- [ ] How to enter expenses
- [ ] How to record revenue
- [ ] How to log contributions
- [ ] How to read the dashboard
- [ ] How to run monthly reconciliation
- [ ] Where to store receipts
- [ ] What to do if there's an error

### Weekly Tasks:
- [ ] Enter all transactions
- [ ] Review dashboard metrics
- [ ] Check for any unusual entries
- [ ] Backup important data

### Monthly Tasks:
- [ ] Complete monthly reconciliation
- [ ] Review with all partners
- [ ] Export monthly report as PDF
- [ ] Update any categories if needed
- [ ] Plan for next month

### Quarterly Tasks:
- [ ] Deep financial review
- [ ] Strategic planning based on data
- [ ] Adjust business operations based on insights
- [ ] Update projections

---

## Tips for Success

1. **Be Consistent:** Enter data daily, don't let it pile up
2. **Keep Receipts:** Link to digital copies in Google Drive
3. **Regular Reviews:** Weekly reviews prevent surprises
4. **Communicate:** All partners should understand the system
5. **Backup:** Regular exports of important data
6. **Evolve:** Adjust categories and structure as business grows

---

## Troubleshooting Common Issues

**Problem:** Formulas showing #REF! error
- **Solution:** Check that sheet names match exactly in formulas

**Problem:** SUMIF not working
- **Solution:** Verify the criteria matches exactly (case-sensitive)

**Problem:** Dates not sorting correctly
- **Solution:** Ensure column is formatted as Date, not Text

**Problem:** Charts not updating
- **Solution:** Edit chart and verify data range is correct

**Problem:** Percentages showing as decimals
- **Solution:** Format → Number → Percent

---

## Need More Help?

- Google Sheets Help Center: https://support.google.com/docs/
- Formula troubleshooting: Check syntax and cell references
- Consider hiring a bookkeeper for monthly review
- Set up monthly partner meetings to review finances together

---

Good luck with your Car Fitness Center! 🚗✨
