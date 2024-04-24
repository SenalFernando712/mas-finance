import streamlit as st
import pandas as pd
import requests
from io import BytesIO

#https://github.com/SenalFernando712/mas-finance/blob/main/GL_list.xlsx
# Function to read Excel file from GitHub repository and extract GL codes
def read_excel_data():
    # Replace 'github_username' with your GitHub username and 'repository_name' with your repository name
    url = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/GL_list1.csv'
    response = requests.get(url)
    df = pd.read_excel(BytesIO(response.content))
    gl_codes = df['Column 1'].astype(str) + ' : ' + df['Column 2'].astype(str)
    return gl_codes.tolist()

def main():
    st.title('MAS Finance Department: PDF Merger')
    
    # Input fields
    gl_codes = read_excel_data()
    gl_code = st.selectbox('GL Code', gl_codes)
    cost_center_number = st.text_input('Cost Center Number', '')
    internal_order_number = st.text_input('Internal Order Number', '')

    # Extracting GL code from selected option
    gl_code = gl_code.split(':')[0].strip() if gl_code else ''

    # Displaying input values
    st.write('### Input Values:')
    st.write(f'GL Code: {gl_code}')
    st.write(f'Cost Center Number: {cost_center_number}')
    st.write(f'Internal Order Number: {internal_order_number}')

if __name__ == '__main__':
    main()

