import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged=customers.merge(orders,left_on="id",right_on="customerId",how="left")
    result=merged[merged["customerId"].isna()]
    result= result[["name"]].rename(columns={"name": "Customers"})
    return result
