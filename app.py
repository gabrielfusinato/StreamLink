from supabase import create_client
import os
from dotenv import load_dotenv

import random

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_PUBLISHABLE_KEY")

supabase = create_client(url, key)

def check_link_in_database(check_url):
    response = supabase.table("url").select("*").eq("long_url", check_url).execute()

    if response.data:
        return response.data[0]
     
    return None

def store_long_url(long_url):

    existing_link = check_link_in_database(long_url)

    if existing_link:
        return existing_link['tinyAlias']
    
    tiny_alias = eeeeeeeeeeeeegenerate_tiny_alias()

    data = {
        "long_url" : long_url,
        "tiny_alias" : tiny_alias
    }

    try:
        response = supabase.table("url").insert(data).execute()
        print(f"URL <{response.data}> guardada com sucesso!")
        return tiny_alias

    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")
        raise

def generate_tiny_alias():
    characters = "STREAMLINKstreamlink1234567890"

    tiny_alias = ''.join(random.choice(characters) for _ in range(10))

    return tiny_alias




if __name__ == "__main__":
    long_url = str(input("Enter your link: "))
    store_long_url(long_url)
