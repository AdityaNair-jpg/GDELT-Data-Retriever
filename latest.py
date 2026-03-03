import pandas as pd
import requests
import zipfile
import io
from google.colab import files

def download_labeled_gkg_sample():
    master_url = "http://data.gdeltproject.org/gdeltv2/lastupdate.txt"
    update_text = requests.get(master_url).text
    gkg_zip_url = update_text.split('\n')[2].split(' ')[2]
    
    print(f"Downloading latest enriched data from: {gkg_zip_url}")
    
    response = requests.get(gkg_zip_url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        file_name = z.namelist()[0]

        all_headers = [
            "GKGRECORDID", "DATE", "SourceCollectionIdentifier", "SourceCommonName",
            "DocumentIdentifier", "Counts", "V2Counts", "Themes", "V2Themes",
            "Locations", "V2Locations", "Persons", "V2Persons", "Organizations",
            "V2Organizations", "V2Tone", "Dates", "GCAM", "SharingImage",
            "RelatedImages", "SocialImageEmbeds", "SocialVideoEmbeds", "Quotations",
            "AllNames", "Amounts", "TranslationInfo", "ExtrasXML"
        ]
        
        df = pd.read_csv(z.open(file_name), sep='\t', encoding='latin-1', 
                         names=all_headers, low_memory=False)

        df['Sentiment'] = df['V2Tone'].str.split(',').str[0].astype(float)
        
        # 6. Export to CSV 
        output_name = "gdelt_gkg_labeled_sample.csv"
        df.to_csv(output_name, index=False)
        print(f"Successfully processed {len(df)} news records.")     
        # Trigger browser download
        files.download(output_name)
        return df

gkg_data = download_labeled_gkg_sample()
