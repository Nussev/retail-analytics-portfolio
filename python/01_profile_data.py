import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

customers = pd.read_csv(DATA_DIR / "customers.csv")
orders = pd.read_csv(DATA_DIR / "orders.csv")
order_items = pd.read_csv(DATA_DIR / "order_items.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
stores = pd.read_csv(DATA_DIR / "stores.csv")
employees = pd.read_csv(DATA_DIR / "employees.csv")
returns = pd.read_csv(DATA_DIR / "returns.csv")

print("Customers:", customers.shape)
print("Orders:", orders.shape)
print("Order items:", order_items.shape)
print("Products:", products.shape)
print("Stores:", stores.shape)
print("Employees:", employees.shape)
print("Returns:", returns.shape)

# Start your investigation here.

print(customers.info());
duplicates = customers.duplicated(subset=['customer_id']).sum()
print(duplicates)
