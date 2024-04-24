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
    raw_github_csv_link_gl = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/GL_list1.csv'

    # Read CSV data
    try:
        df = read_csv_data(raw_github_csv_link_gl)
        gl_codes = df['Column 1'].astype(str) + ' : ' + df['Column 2'].astype(str)
        gl_no = st.selectbox('GL No', gl_codes)
        st.write('Selected GL No:', gl_no)
    except Exception as e:
        st.error(f'Error reading CSV file: {e}')

if __name__ == '__main__':
    main()
