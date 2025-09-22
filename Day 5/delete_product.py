import os
from supabase import Client,create_client
from dotenv import load_dotenv

load_dotenv()

url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

sb:Client=create_client(url,key)

def delete_product(product_id):
    resp=sb.table("products").delete().eq("product_id",product_id).execute()
    return resp.data
if __name__=='__main__':
    id=int(input("Enter the product id to be deleted:"))
    s=input(f"Are you sure you want to delete product{id}?(Type (yes/no)):")
    if s.strip().lower()=='yes':
        delr=delete_product(id)
        if delr:
            print("Deleted product is:",delr)
        else:
            print("Unexpected error occured.Please try again.")
    else:
        print("Cancelled.")