# DATA OBSERVATIONS

Source: `notebooks/01_data_exploration.ipynb`. Each table lists what was found, then the cleaning action to take.

## TABLES

### customers
**Observations**
- Email appears to be `first_name.last_name{digits of customer_id with leading zeros dropped}@example.com`
  - Customer ID = C00021 --> first_name.last_name21@example.com
- 8,120 rows; `email` has 350 nulls and `phone` has 250 nulls.
- `signup_date` is a string.

**Cleaning actions**
- [ ] Backfill missing `email` using the pattern above (confirm the pattern holds for all non-null rows first).
- [ ] Decide how to handle missing `phone` (leave null vs. flag); document the choice.
- [ ] Convert `signup_date` to datetime.

### employees
**Observations**
- 300 rows; each employee has exactly one `store_id`, so there are no multi-store employees.
- 20 employees have `store_id = "UNKNOWN"` (e.g. E0297, E0298).
  - Checked whether this relates to recent `hire_date` or to non-store roles (corporate/intern). Neither explains it.
- `role` has inconsistent casing (e.g. "Sales Lead" vs "sales lead", "Customer Service" vs "customer service").
- `hire_date` is a string.

**Cleaning actions**
- [ ] Standardize `role` to one casing (e.g. title case). Expected result: 5 roles (Sales Associate, Sales Lead, Assistant Manager, Store Manager, Customer Service).
- [ ] Convert `hire_date` to datetime.
- [ ] Replace `"UNKNOWN"` in `store_id` with a true null, or a documented placeholder, so it does not break joins to `stores`.
- [ ] Check whether the UNKNOWN employees appear in `orders.employee_id`; this decides whether they need a store for downstream analysis.

### order_items
**Observations**
- 123,699 rows with no nulls.
- 1,007 rows share an `order_id` + `product_id` with another row. A product should appear once per order, with a higher `quantity` instead.
  - Some are exact duplicate rows (e.g. O049917 / P0104).
  - Some differ in `quantity` or `discount_pct` (e.g. O000032 / P0045: qty 2 at 20% vs qty 1 at 10%).
- Possible explanation for the non-exact ones: items added after the initial order was submitted. This is unconfirmed.

**Cleaning actions**
- [ ] Check the data dictionary for whether repeat product lines on an order are expected.
- [ ] Drop exact duplicate rows.
- [ ] For rows that differ, consolidate to one line per `order_id` + `product_id`: sum `quantity` and `line_revenue`, and decide how to treat differing `discount_pct` (e.g. recompute a weighted discount).
- [ ] Decide whether to store money columns (`unit_price`, `line_revenue`) as Decimal/fixed precision rather than float64, since `line_revenue` is a financial value.
- [ ] Re-validate `line_revenue` = `quantity` * `unit_price` * (1 - `discount_pct`) after consolidating.

### orders
**Observations**
- 50,100 rows but only 50,000 unique `order_id`s. 200 rows are involved in duplicate `order_id`s (likely 100 duplicated pairs, to be verified).
- `store_id` has 120 nulls (49,980 of 50,100 non-null). In the rows sampled, nulls are on `channel = Store` orders. Not yet investigated.
- found '200' duplicate orders based on order_id
- `employee_id` has 22,598 nulls. All of them are Online / online orders, so these are expected, not errors.
- `channel` has inconsistent casing: "Online" vs "online" (other values: Mobile App, Store).
- `order_status`: Completed, Cancelled, Pending.
- `payment_method`: Apple Pay, Gift Card, PayPal, Credit Card, Debit Card. No issues seen.
- `order_date` is a string.

**Cleaning actions**
- [ ] Inspect the duplicate `order_id` rows: exact copies or conflicting values? Then dedupe (keep one row per `order_id`).
- [ ] Standardize `channel` casing ("online" -> "Online").
- [ ] Investigate the 120 null `store_id` rows: check `channel`, `order_status`, and whether `employee_id` can recover the store.
- [ ] Flag non-Online orders with a null `employee_id`, if any exist.
- [ ] Leave null `employee_id` on Online orders as-is, and document it.
- [ ] Convert `order_date` to datetime.

### products
**Observations**
- 480 rows; `unit_cost` has 35 nulls.
  - May be able to infer cost from `product_status`, `category`, or `subcategory`.
- `category` has duplicate casing variants (Electronics/electronics, Home/home, Apparel/apparel, Sports & Outdoors/sports & outdoors, Beauty/beauty, Office/office), so 12 values for 6 categories.

**Cleaning actions**
- [ ] Standardize `category` to one casing (6 categories).
- [ ] Impute or flag the 35 missing `unit_cost`: compare the cost-to-price ratio within category/subcategory/status, then decide between imputing and leaving null.
  - Exclude or flag these products in any margin calculation.
- [ ] Check `subcategory` for the same casing/naming problems as `category`.
- [ ] Review min and max `unit_cost` per category for outliers, and check that `unit_cost` < `list_price`.

### returns
**Observations**
- 8,000 rows with no nulls; nothing obvious from `info()`.
- `return_date` is a string.

**Cleaning actions**
- [ ] Check `return_id` for duplicates.
- [ ] Convert `return_date` to datetime.
- [ ] Confirm each return's `order_id` + `product_id` exists in `order_items`, and that `return_quantity` does not exceed the ordered quantity (re-check after the order_items consolidation).

### stores
**Observations**
- No obvious issues.
- Each `store_id` maps to exactly one `store_name`.

**Cleaning actions**
- None identified so far.
