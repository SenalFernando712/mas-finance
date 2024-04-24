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
        gl_codes = df['SAP B1 - A/C Name'].astype(str) + ' : ' + df['G/L Acct Long Text'].astype(str)
        selected_gl_index = st.selectbox('GL No', range(len(gl_codes)))
        selected_gl_no = gl_codes[selected_gl_index]
        # Display the selected GL No
        st.write('Selected GL No:', selected_gl_no)
        # Display the data from the third column of the selected row
        st.write('Data from third column:', df.iloc[selected_gl_index, 2])
    except Exception as e:
        st.error(f'Error reading CSV file: {e}')

if __name__ == '__main__':
    main()
