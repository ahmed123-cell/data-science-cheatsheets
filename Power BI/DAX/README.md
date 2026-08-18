# Basic DAX Functions Cheat Sheet

## What is DAX?
**DAX (Data Analysis Expressions)** is the formula language used in Power BI, Power Pivot, and SSAS Tabular.

It is used to create:
- Calculated Columns
- Measures
- Calculated Tables

---

# 1. SUM

Adds all values in a column.

```DAX
Total Sales = SUM(Sales[Revenue])
```

---

# 2. AVERAGE

Returns the average value of a column.

```DAX
Average Sales = AVERAGE(Sales[Revenue])
```

---

# 3. MIN

Returns the smallest value.

```DAX
Minimum Sales = MIN(Sales[Revenue])
```

---

# 4. MAX

Returns the largest value.

```DAX
Maximum Sales = MAX(Sales[Revenue])
```

---

# 5. COUNT

Counts numeric values.

```DAX
Number of Sales = COUNT(Sales[Revenue])
```

---

# 6. DISTINCTCOUNT

Counts unique values.

```DAX
Unique Customers = DISTINCTCOUNT(Sales[CustomerID])
```

---

# 7. SUMX

Iterates through rows and then sums the result.

```DAX
Total Revenue = SUMX(
    Sales,
    Sales[Quantity] * Sales[UnitPrice]
)
```

---

# 8. CALCULATE

Modifies filter context.

```DAX
Cairo Sales =
CALCULATE(
    SUM(Sales[Revenue]),
    Customers[City] = "Cairo"
)
```

---

# 9. FILTER

Returns a filtered table.

```DAX
High Sales =
FILTER(
    Sales,
    Sales[Revenue] > 1000
)
```

---

# 10. ALL

Removes filters.

```DAX
Total Sales All Products =
CALCULATE(
    SUM(Sales[Revenue]),
    ALL(Products)
)
```

---

# 11. IF

Conditional logic.

```DAX
Category =
IF(
    Sales[Revenue] > 1000,
    "High",
    "Low"
)
```

---

# 12. SWITCH

Multiple conditions.

```DAX
Grade =
SWITCH(
    TRUE(),
    [Score] >= 90, "A",
    [Score] >= 80, "B",
    [Score] >= 70, "C",
    "D"
)
```

---

# 13. RELATED

Gets a value from a related table.

```DAX
Product Category =
RELATED(Products[Category])
```

---

# 14. DIVIDE

Safe division.

```DAX
Profit Margin =
DIVIDE(
    [Profit],
    [Revenue],
    0
)
```

---

# 15. TODAY

Returns today's date.

```DAX
Today Date = TODAY()
```

---

# 16. YEAR

Extracts year from a date.

```DAX
Year = YEAR(Sales[OrderDate])
```

---

# 17. MONTH

Extracts month from a date.

```DAX
Month = MONTH(Sales[OrderDate])
```

---

# 18. DAY

Extracts day from a date.

```DAX
Day = DAY(Sales[OrderDate])
```

---