# fetches data with topic filters 
import requests
import pandas as pd
import time

def gdelt_doc_collector(query, max_records=250):
    endpoint = "https://api.gdeltproject.org/api/v2/doc/doc"
    
    params = {
        "query": query,
        "mode": "ArtList",
        "format": "json",
        "maxrecords": max_records,
        "sort": "date"
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"Collecting news for: {query}...")
    
    for attempt in range(3):  # Try up to 3 times
        try:
            # timeout=30
            res = requests.get(endpoint, params=params, headers=headers, timeout=30)
            res.raise_for_status()
            
            data = res.json()
            if 'articles' in data:
                return pd.DataFrame(data['articles'])
            else:
                print("No articles found for this query.")
                return None
                
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
            print(f"Timeout on attempt {attempt + 1}. Retrying...")
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")
            break
            
    print("Failed to reach GDELT after 3 attempts.")
    return None

user_query = '"Elon Musk" Tesla' 
news_df = gdelt_doc_collector(user_query)

if news_df is not None:
    display(news_df.head())
