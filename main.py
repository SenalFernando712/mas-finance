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
        selected_gl_index = st.selectbox('GL No', range(len(gl_codes)), format_func=lambda i: f"Row {i+1}: {gl_codes[i]}")
        
        # Display the selected GL No
        st.write('Selected GL No:', gl_codes[selected_gl_index])
        
        # Get the row number of the selected item
        selected_row_number = selected_gl_index + 1
        
        # Display the data from the third column of the selected row
        st.write(f'Data from third column of row {selected_row_number}:', df.iloc[selected_gl_index, 2])
    except Exception as e:
        st.error(f'Error reading CSV file: {e}')

if __name__ == '__main__':
    main()
