import streamlit as st
import pandas as pd
import requests

# Function to read CSV file from GitHub repository
def read_csv_data(url):
    response = requests.get(url)
    df = pd.read_csv(url)
    return df

def main():
    st.title('Display CSV Data from GitHub')

    # Replace 'raw_github_csv_link' with the raw GitHub link to your CSV file
    raw_github_csv_link = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/GL_list1.csv'

    # Read CSV data
    try:
        df = read_csv_data(raw_github_csv_link)
        st.write('### First 5 rows of the CSV file:')
        st.write(df.head())
    except Exception as e:
        st.error(f'Error reading CSV file: {e}')

if __name__ == '__main__':
    main()
