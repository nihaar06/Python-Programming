import os
from supabase import create_client,Client
from dotenv import load_dotenv

load_dotenv()

url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

sb:Client=create_client(url,key)

def list_products():
    resp=sb.table("products").select("*").order("product_id",desc=False).execute()
    return resp.data

if __name__=="__main__":
    p=list_products()
    if p:
        print("**PRODUCTS**")
        for i in p:
            print(f"{i['product_id']}:{i['name']}(SKU:{i['sku']})-Rs.{i['price']}-Stock:{i['stock']}")
    else:
        print("No products found")