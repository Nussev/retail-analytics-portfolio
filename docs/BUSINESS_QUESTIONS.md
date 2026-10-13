# Business Questions

## Level 1 — Getting comfortable
1. What is total revenue by month?
2. What are the top 10 products by revenue?
3. Which product categories generate the most revenue?
4. Which stores generate the most revenue?
5. What is the average order value?
6. How many unique customers placed an order?
7. What percentage of customers have made more than one purchase?
8. What are the most common payment methods and channels?

## Level 2 — Business analysis
9. Which categories have the highest gross profit?
10. Which products have high revenue but relatively low gross margin?
11. Which stores have the highest average order value?
12. How does performance differ between Online, Store, and Mobile App?
13. Which customer tiers generate the most revenue?
14. Which customers have the highest lifetime revenue?
15. What are the most frequently returned products?
16. Which return reasons are most common?
17. How has the business changed month over month?

## Level 3 — Data quality
18. How many duplicate customer records exist?
19. How many orders reference customers that do not exist?
20. How many orders have missing store assignments?
21. How many order lines contain zero or negative quantities?
22. How many records contain invalid discount percentages?
23. How many duplicate order/order-line records appear to exist?
24. How much revenue could be affected by questionable transaction records?
25. Which source table appears to have the biggest data-quality problems?

## Portfolio questions
26. Build an executive dashboard showing revenue, orders, customers, AOV, gross profit, and return rate.
27. Build a customer dashboard explaining customer value and repeat purchasing.
28. Build a product/store dashboard identifying areas of strong and weak performance.
29. Write a short executive summary: What are the three most important findings?
30. Identify three data-quality issues that should be addressed upstream and explain their potential business impact.

## Suggested workflow
Do not immediately answer everything with SQL.
1. Profile the raw data in Python/pandas.
2. Document data-quality issues.
3. Clean/standardize the data.
4. Load/query the cleaned data with DuckDB.
5. Answer business questions with SQL.
6. Create a BI-ready analytical dataset.
7. Build the dashboard.
8. Write a short README describing your methodology and findings.
