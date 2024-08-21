# Jazz Analysis

## Contents
0. [Introduction](Introduction)
1. [Installation](Installation)
2. [Usage](Usage)
3. [Project Architecture](Project Architecture)
4. [Future Improvements](Future Improvements)
5. [How to Contribute](How to Contribute)

## Introduction
Welcome to the Jazz Analysis Project! This project is designed to explore trends in jazz music over time using data from the Spotify API. It allows you to analyze the popularity of jazz music and visualize trends across different decades.

## Installation
**Pre-Requisites**
- Python
- Spotipy
- Google Cloud SDK (for interacting with Google Cloud Storage)

**Setup**

Clone the repository:
```
git clone https://github.com/your_username/jazz-analysis-project.git
cd jazz-analysis-project
```

Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

Install the required Python packages:
```
pip install -r requirements.txt
```

Set up Google Cloud authentication:
```
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
```


## Usage
1. Data Generation and Analysis:
Run the main script to generate data on jazz albums, analyze the popularity of jazz over time, and save the results locally and in Google Cloud Storage:

bash
Copy code
python main.py

3. Store Results in Google Cloud Storage:
The script will automatically upload the raw data and analysis results (e.g., plots) to a specified Google Cloud Storage bucket.

## Project Architecture
The project is structured as follows:

- ```generate_jazz_data.py```: Contains the logic to query the Spotify API for jazz albums, process the data, and analyze trends.
- ```gcs_utils.py```: Utility functions for interacting with Google Cloud Storage, including uploading and downloading files.
- ```main.py```: The main script that ties together the data generation, analysis, and storage operations.
- ```data/```: Directory where local copies of raw and processed data are stored (this directory is included in .gitignore).

## Workflow
1. **Data Retrieval:** Extracts data on jazz albums using Spotipy and saves it as a CSV file.
2. **Data Analysis:** Processes the data to analyze popularity trends over time and generates visualizations.
3. **Data Storage:** Saves the generated data locally and uploads it to Google Cloud Storage for backup and sharing.

## Future Improvements
1. **Data and Analysis Improvements**
Expand Dataset: Increase the number of albums analyzed by iterating over a broader range of years or by querying more tracks and albums.
Detailed Genre Analysis: Break down the analysis further by sub-genres within jazz to identify more specific trends.

2. **Platform Improvements**
Automate Data Retrieval: Implement a scheduled task (e.g., using Google Cloud Functions or a cron job) to automatically update the dataset periodically.
Web Interface: Develop a web interface to allow users to interact with the data and visualizations dynamically.

3. **Code Quality Improvements**
Refactoring: Improve modularity and reusability of code by further breaking down functions and classes.
Testing: Add unit tests for the key functions to ensure the reliability of data processing and analysis steps.

## How to Contribute
1. **Fork the Repository:** Start by forking the repository to your GitHub account.
2. **Create a Branch:** Create a new branch for your feature or bug fix.
3. **Make Your Changes:** Implement your changes in the new branch.
4. **Submit a Pull Request:** Once your changes are complete, submit a pull request to the main repository.
