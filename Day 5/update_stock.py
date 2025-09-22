import os
from supabase import Client,create_client
from dotenv import load_dotenv

load_dotenv()

url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

sb:Client=create_client(url,key)

def update_stock(p_id,new_stock):
    resp=sb.table("products").update({"stock":new_stock}).eq("product_id",p_id).execute()
    return resp.data
if __name__=="__main__":
    pid=int(input("Enter the product id:"))
    st=int(input("Enter the stock value:"))
    ud=update_stock(pid,st)
    if ud:
        print("Updated stock:",ud)
    else:
        print("No product updated. Try again")