# Google Sheets Formulas - Quick Reference

## Essential Formulas for Car Fitness Center Accounting

---

## BASIC CALCULATIONS

### Sum Total
```
=SUM(C2:C100)
```
Adds all values in range C2 to C100

### Average
```
=AVERAGE(E2:E100)
```
Calculates average of values in range

### Count
```
=COUNT(A2:A100)          // Counts numbers only
=COUNTA(A2:A100)         // Counts all non-empty cells
=COUNTBLANK(A2:A100)     // Counts empty cells
```

---

## CONDITIONAL CALCULATIONS

### SUMIF - Sum Based on Criteria
**Single Criteria:**
```
=SUMIF(B:B, "Partner 1", C:C)
```
Sums column C where column B equals "Partner 1"

**Example - Total expenses by category:**
```
=SUMIF(Expenses!B:B, "Facility Costs", Expenses!F:F)
```

**With Wildcards:**
```
=SUMIF(B:B, "Basic Services*", E:E)
```
Sums all entries starting with "Basic Services"

### SUMIFS - Sum with Multiple Criteria
```
=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)
```

**Example - Partner 1's equipment expenses:**
```
=SUMIFS(Expenses!F:F, Expenses!H:H, "Partner 1", Expenses!B:B, "Equipment & Tools")
```

**Example - Revenue for January 2025:**
```
=SUMIFS(Revenue!E:E, Revenue!A:A, ">=1/1/2025", Revenue!A:A, "<=1/31/2025")
```

### COUNTIF - Count Based on Criteria
```
=COUNTIF(B:B, "SUV")
```
Counts how many times "SUV" appears in column B

**Example - Number of detailing services:**
```
=COUNTIF(Revenue!B:B, "Detailing Services*")
```

### COUNTIFS - Count with Multiple Criteria
```
=COUNTIFS(criteria_range1, criteria1, criteria_range2, criteria2)
```

**Example - Count SUVs serviced in January:**
```
=COUNTIFS(Revenue!D:D, "SUV", Revenue!A:A, ">=1/1/2025", Revenue!A:A, "<=1/31/2025")
```

---

## DATE FORMULAS

### Today's Date
```
=TODAY()
```
Returns current date (updates daily)

### Current Month Start Date
```
=DATE(YEAR(TODAY()), MONTH(TODAY()), 1)
```

### Current Month End Date
```
=EOMONTH(TODAY(), 0)
```

### Previous Month Start
```
=DATE(YEAR(TODAY()), MONTH(TODAY())-1, 1)
```

### Previous Month End
```
=EOMONTH(TODAY(), -1)
```

### Extract Year/Month/Day
```
=YEAR(A2)      // Extracts year from date in A2
=MONTH(A2)     // Extracts month number
=DAY(A2)       // Extracts day
```

### Days Between Dates
```
=A2-B2         // Simple subtraction for days
=DAYS(A2, B2)  // Alternative method
```

---

## CURRENT MONTH REVENUE/EXPENSES

### Current Month Revenue
```
=SUMIFS(Revenue!$E:$E, 
        Revenue!$A:$A, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1), 
        Revenue!$A:$A, "<="&EOMONTH(TODAY(),0))
```

### Current Month Expenses
```
=SUMIFS(Expenses!$F:$F, 
        Expenses!$A:$A, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1), 
        Expenses!$A:$A, "<="&EOMONTH(TODAY(),0))
```

### Specific Month (e.g., January 2025)
```
=SUMIFS(Revenue!$E:$E, 
        Revenue!$A:$A, ">=1/1/2025", 
        Revenue!$A:$A, "<=1/31/2025")
```

### Using Cell References for Dates
```
=SUMIFS(Revenue!$E:$E, 
        Revenue!$A:$A, ">="&$B$2,    // Start date in B2
        Revenue!$A:$A, "<="&$C$2)     // End date in C2
```

---

## RUNNING TOTALS

### Running Total (Cumulative Sum)
```
=SUM($C$2:C2)
```
Place in D2 and drag down. The $ locks the starting cell.

**Example Result:**
| Amount | Running Total |
|--------|---------------|
| 100    | 100          |
| 50     | 150          |
| 75     | 225          |

---

## PROFIT MARGIN & PERCENTAGES

### Profit Margin
```
=(Revenue - Expenses) / Revenue
```
Format as percentage

**Example:**
```
=(B6-B5)/B6
```
Where B6 is revenue, B5 is expenses

### Percentage of Total
```
=Individual_Amount / Total_Amount
```

**Example - Partner's ownership %:**
```
=D2/SUM($D$2:$D$5)
```

### Percentage Change
```
=(New_Value - Old_Value) / Old_Value
```

**Example - Month-over-month growth:**
```
=(B3-B2)/B2
```
Format as percentage

---

## CONDITIONAL FORMULAS

### IF Statement
```
=IF(condition, value_if_true, value_if_false)
```

**Example - Profit or Loss:**
```
=IF(B7>0, "Profit", "Loss")
```

**Example - High-value transaction:**
```
=IF(E2>500, "High Value", "Standard")
```

### Nested IF
```
=IF(condition1, value1, IF(condition2, value2, value3))
```

**Example - Service tier:**
```
=IF(E2<50, "Basic", IF(E2<150, "Premium", "Elite"))
```

### IFERROR - Handle Errors Gracefully
```
=IFERROR(formula, value_if_error)
```

**Example - Safe division:**
```
=IFERROR(B7/B6, 0)
```
Returns 0 if division by zero, otherwise shows result

---

## LOOKUP FUNCTIONS

### VLOOKUP - Vertical Lookup
```
=VLOOKUP(search_key, range, index, [is_sorted])
```

**Example - Look up partner's total contribution:**
```
=VLOOKUP("Partner 1", A2:D5, 4, FALSE)
```
Searches for "Partner 1" in column A, returns value from 4th column

### XLOOKUP (if available)
```
=XLOOKUP(search_key, search_range, return_range, [if_not_found])
```

**Example:**
```
=XLOOKUP("Partner 1", A2:A5, D2:D5, "Not Found")
```

---

## TEXT FUNCTIONS

### Concatenate/Combine Text
```
=A2&" "&B2           // Using & operator
=CONCAT(A2, " ", B2) // Using CONCAT function
```

**Example - Full name:**
```
=A2&" - "&B2
```
Result: "Partner 1 - $10,000"

### Extract Text
```
=LEFT(text, num_chars)    // First N characters
=RIGHT(text, num_chars)   // Last N characters
=MID(text, start, length) // Middle portion
```

### Change Case
```
=UPPER(A2)  // UPPERCASE
=LOWER(A2)  // lowercase
=PROPER(A2) // Proper Case
```

---

## STATISTICAL FUNCTIONS

### Maximum/Minimum
```
=MAX(E2:E100)    // Highest value
=MIN(E2:E100)    // Lowest value
```

### Median
```
=MEDIAN(E2:E100)
```
Middle value in sorted list

### Standard Deviation
```
=STDEV(E2:E100)   // Sample standard deviation
=STDEVP(E2:E100)  // Population standard deviation
```

---

## SPECIFIC USE CASES FOR CAR FITNESS CENTER

### 1. Total Contributions by Partner
```
=SUMIF('Partner Contributions'!$B:$B, A2, 'Partner Contributions'!$C:$C)
```
Place in equity sheet where A2 contains partner name

### 2. Monthly Revenue Comparison
```
// Current Month
=SUMIFS(Revenue!$E:$E, Revenue!$A:$A, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1), 
        Revenue!$A:$A, "<="&EOMONTH(TODAY(),0))

// Previous Month
=SUMIFS(Revenue!$E:$E, Revenue!$A:$A, ">="&DATE(YEAR(TODAY()),MONTH(TODAY())-1,1), 
        Revenue!$A:$A, "<="&EOMONTH(TODAY(),-1))
```

### 3. Average Transaction Value
```
=SUM(Revenue!E:E) / (COUNTA(Revenue!E:E)-1)
```
-1 to exclude header row

### 4. Expense by Category Summary
```
// Create one formula for each category
=SUMIF(Expenses!$B:$B, "Facility Costs", Expenses!$F:$F)
=SUMIF(Expenses!$B:$B, "Equipment & Tools", Expenses!$F:$F)
=SUMIF(Expenses!$B:$B, "Labor Costs", Expenses!$F:$F)
// ... etc
```

### 5. Partner's Share of Profit
```
=(Dashboard!$B$7) * (Ownership_Percentage)
```
Where B7 is Net Profit/Loss and multiply by partner's ownership %

### 6. Days in Operation
```
=TODAY() - [Start_Date]
```

### 7. Average Daily Revenue
```
=SUM(Revenue!E:E) / (TODAY() - [Start_Date])
```

### 8. Most Popular Service
```
// Use QUERY or create summary with COUNTIF
=COUNTIF(Revenue!B:B, "Basic Services - Full Service")
```

### 9. Cash vs Card Payment Split
```
=SUMIF(Revenue!F:F, "Cash", Revenue!E:E)
=SUMIF(Revenue!F:F, "Credit Card", Revenue!E:E)
```

### 10. Partner-Specific Expenses
```
=SUMIF(Expenses!H:H, "Partner 1", Expenses!F:F)
```

---

## FORMATTING TIPS

### Format as Currency
1. Select cells
2. Format → Number → Currency
Or use formula:
```
=TEXT(A2, "$#,##0.00")
```

### Format as Percentage
1. Select cells
2. Format → Number → Percent
Or multiply by 100 and add %:
```
=B7/B6*100 & "%"
```

### Conditional Formatting with Formulas

**Highlight Negative Values (Red):**
- Select range
- Format → Conditional formatting
- Format cells if: Custom formula is: `=A1<0`
- Background: Light red

**Highlight Values Above Threshold (Green):**
- Format cells if: Custom formula is: `=A1>500`
- Background: Light green

---

## CELL REFERENCES

### Relative Reference
```
=A1
```
Changes when copied (A1 → B2 → C3...)

### Absolute Reference
```
=$A$1
```
Stays fixed when copied

### Mixed Reference
```
=$A1    // Column fixed, row relative
=A$1    // Row fixed, column relative
```

### Reference Another Sheet
```
='Sheet Name'!A1
='Partner Contributions'!C2
```

---

## ARRAY FORMULAS (Advanced)

### ARRAYFORMULA
```
=ARRAYFORMULA(formula)
```

**Example - Apply formula to entire column:**
```
=ARRAYFORMULA(IF(A2:A="",,A2:A*B2:B))
```
Multiplies columns A and B, skipping empty rows

---

## DATA VALIDATION FORMULAS

### Create Dropdown from Range
```
=Sheet1!$A$2:$A$10
```

### Dynamic Dropdown (only non-empty)
```
=FILTER(A2:A100, A2:A100<>"")
```

---

## COMMON ERRORS & FIXES

| Error | Meaning | Common Fix |
|-------|---------|------------|
| `#DIV/0!` | Division by zero | Use `IFERROR` or check denominator |
| `#REF!` | Invalid reference | Check if sheet/cells were deleted |
| `#NAME?` | Formula name wrong | Check spelling, sheet names in quotes |
| `#VALUE!` | Wrong data type | Check if text where number expected |
| `#N/A` | Value not available | Common in VLOOKUP, check search key |

---

## PRO TIPS

1. **Name Your Ranges:**
   - Select range → Data → Named ranges
   - Use descriptive names: `TotalRevenue`, `PartnerList`
   - Reference: `=SUM(TotalRevenue)`

2. **Use Absolute References ($) for:**
   - Total rows when calculating percentages
   - Fixed lookup ranges
   - Constants in formulas

3. **Combine Functions:**
   ```
   =IFERROR(SUMIFS(Revenue!E:E, Revenue!A:A, ">="&B2, Revenue!A:A, "<="&C2), 0)
   ```
   Handles errors gracefully in complex formulas

4. **Document Complex Formulas:**
   - Add comments (right-click → Insert comment)
   - Explain what formula does
   - Note any assumptions

5. **Test Formulas:**
   - Start simple, add complexity gradually
   - Test with known values first
   - Check edge cases (zero, negative, empty)

---

## QUICK FORMULA BUILDER

### Template for Monthly Summary:
```
Month: [Cell with month/year]
Revenue: =SUMIFS(Revenue!$E:$E, Revenue!$A:$A, ">="&[start_date], Revenue!$A:$A, "<="&[end_date])
Expenses: =SUMIFS(Expenses!$F:$F, Expenses!$A:$A, ">="&[start_date], Expenses!$A:$A, "<="&[end_date])
Profit: =Revenue-Expenses
Margin: =Profit/Revenue
```

---

## PRACTICE EXERCISES

Try creating these formulas yourself:

1. Total revenue from "SUV" vehicles
2. Average expense per transaction
3. Count of services in past 7 days
4. Partner 2's share of total contributions (%)
5. Running total of cash received
6. Highest single transaction this month
7. Number of unique customers (approximate with COUNTIF)
8. Percentage of revenue from memberships

---

Need more help? Google Sheets has extensive documentation:
https://support.google.com/docs/table/25273?hl=en

---

Good luck! 🚗✨
