# GDELT Data Retriever

This repository provides a collection of Python scripts designed to interface with the **GDELT Project** (Global Database of Events, Language, and Tone). It contains tools to retrieve, process, and export both real-time news article lists and enriched Global Knowledge Graph (GKG) data.

## Overview

The GDELT Project monitors the world's broadcast, print, and web news in over 100 languages. This repository simplifies the process of accessing that data, offering scripts that range from simple API queries to complex data processing of the latest GKG updates.

## File Descriptions

### 1. `latest.py`
This script focuses on the **GDELT GKG (Global Knowledge Graph) v2**.
* **Functionality**: It automatically fetches the latest update from the GDELT master file list.
* **Data Processing**: Downloads the most recent ZIP file, extracts the TSV data, and maps it to the standard GKG headers (e.g., Themes, Locations, Persons, Organizations, and GCAM).
* **Sentiment Analysis**: Extracts the primary sentiment score from the `V2Tone` field.
* **Export**: Processes the records into a CSV file named `gdelt_gkg_labeled_sample.csv` and triggers an automatic browser download (optimized for Google Colab).

### 2. `news.py`
A lightweight script to query the **GDELT Doc API**.
* **Functionality**: Uses the `ArtList` mode to search for recent news articles based on a user-defined keyword (e.g., "Renewable Energy").
* **Output**: Returns a cleaned Pandas DataFrame containing article titles, URLs, source countries, languages, and publication dates.

### 3. `topic-gkg.py`
An advanced version of the news retriever with built-in error handling.
* **Functionality**: Similar to `news.py`, but includes a robust `gdelt_doc_collector` function.
* **Resiliency**: Features a retry mechanism (up to 3 attempts) and timeout handling to manage network instability or API delays.
* **Customization**: Pre-configured for specific topic filtering, such as searching for multiple related keywords (e.g., `"Elon Musk" Tesla`).

### Example Visualized data
<img width="2057" height="1230" alt="image" src="https://github.com/user-attachments/assets/eda32b19-c51f-44b1-abb0-a2e2a083a46b" />

## Requirements

To run these scripts, you will need:
* Python 3.x
* `pandas`
* `requests`

## Usage

1.  **For latest GKG data**: Run `python latest.py` to download and process the most recent 15-minute GKG update.
2.  **For specific news searches**: Edit the `user_query` variable in `news.py` or `topic-gkg.py` and run the script to see a list of matching global news articles.
