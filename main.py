import streamlit as st
import pandas as pd

# Function to read Excel file and extract GL codes
def read_excel_data():
    # Replace 'your_excel_file.xlsx' with the path to your Excel file
    df = pd.read_excel('https://github.com/SenalFernando712/mas-finance/blob/main/GL_list.xlsx')
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
