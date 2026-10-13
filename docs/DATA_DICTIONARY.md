# Retail Analytics Project — Data Dictionary

## Business scenario
You are an analyst supporting a fictional omnichannel retailer, **Northstar Retail Group**.
Leadership wants to understand sales performance, customer behavior, product profitability, store performance, and data quality.

The source data is intentionally messy. Treat the raw CSV files as source-system extracts, not trusted analytical tables.

## Relationships
- `customers.customer_id` → `orders.customer_id`
- `orders.order_id` → `order_items.order_id`
- `products.product_id` → `order_items.product_id`
- `stores.store_id` → `orders.store_id`
- `employees.employee_id` → `orders.employee_id`
- `orders.order_id` + `products.product_id` → `returns.order_id` + `returns.product_id`

## Tables
### customers
Customer master data. Contains intentional duplicate customers, missing contact fields, inconsistent capitalization, and inconsistent state formats.

### products
Product master data. Contains intentional category inconsistencies and missing costs.

### stores
Store/location master data.

### employees
Employee roster. Employees are assigned to stores; some records contain inconsistent role/store values.

### orders
Order-level transactions. Contains intentional duplicate orders, invalid customer references, missing store assignments, inconsistent channel casing, and mixed date representations.

### order_items
Line-level transaction detail. Contains intentional duplicate rows, zero/negative quantities, and invalid discount values.

### returns
Returned item transactions. Contains intentional invalid order references and mixed date representations.

## Important metric definitions
- Revenue: normally `quantity * unit_price * (1 - discount_pct)`.
- Gross profit: revenue minus `quantity * unit_cost`.
- Average order value: revenue / distinct completed orders.
- Return rate: returned quantity / sold quantity, where appropriate.
- Unless a question explicitly says otherwise, investigate data quality before trusting a metric.
