import requests
import pandas as pd
import json

def get_gdelt_news(query, max_records=10):
    """
    Fetches news articles from GDELT Doc API based on a search query.
    """
    # The API Endpoint
    endpoint = "https://api.gdeltproject.org/api/v2/doc/doc"

    params = {
        "query": query,
        "mode": "ArtList",
        "format": "json",
        "maxrecords": max_records,
        "sort": "hybridrel"
    }
    
    print(f"Searching GDELT for: {query}...")
    
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if articles were found
        if 'articles' in data:
            articles = data['articles']
            df = pd.DataFrame(articles)         
            # Cleaning up
            columns_to_keep = ['title', 'url', 'sourcecountry', 'language', 'seendate', 'socialimage']
            return df[columns_to_keep]
        else:
            print("No articles found for this query.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Search for any topic (e.g., 'Artificial Intelligence', 'Tesla', 'Global Warming')
user_query = "Renewable Energy" 
news_data = get_gdelt_news(user_query, max_records=20)

if news_data is not None:
    display(news_data.head())
