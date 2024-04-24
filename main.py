import streamlit as st
import pandas as pd
import requests
from fpdf import FPDF

# Function to read CSV file from GitHub repository
def read_csv_data(url):
    response = requests.get(url)
    df = pd.read_csv(url)
    return df

# Function to create PDF
def create_pdf(vendor, gl_pdf, cost_pdf, internal_pdf, assignment, text, amount):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="MAS Finance Department: PDF Merger", ln=True, align="C")
    pdf.cell(200, 10, txt=" ", ln=True, align="C")  # Add empty line

    # Add fields to PDF
    pdf.cell(200, 10, txt=f"Vendor: {vendor}", ln=True)
    pdf.cell(200, 10, txt=f"G/L Account: {gl_pdf}", ln=True)
    pdf.cell(200, 10, txt=f"Cost Center Code: {cost_pdf}", ln=True)
    pdf.cell(200, 10, txt=f"Internal Order Code: {internal_pdf}", ln=True)
    pdf.cell(200, 10, txt=f"Assignment: {assignment}", ln=True)
    pdf.cell(200, 10, txt=f"Text: {text}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {amount}", ln=True)

    pdf.output("MAS_Finance_Document.pdf")

def main():
    st.title('MAS Finance Department : PDF Merger')

    # Replace 'raw_github_csv_link' with the raw GitHub link to your CSV file
    raw_github_csv_link_gl = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/GL_list1.csv'

    vendor = st.text_input('Vendor Name:')
    
    # Read CSV data
    try:
        df = read_csv_data(raw_github_csv_link_gl)
        gl_codes = df['SAP B1 - A/C Name'].astype(str) + ' : ' + df['G/L Acct Long Text'].astype(str)
        gl_no = st.selectbox('GL Description', gl_codes)
        
        # Split the selected gl_no to get the actual GL Account
        selected_gl_account = gl_no.split(':')[0].strip()
        
        # Find the row where the GL Account matches the selected GL Account
        row = df[df['SAP B1 - A/C Name'] == selected_gl_account]
        
        # Display the data from the third column (G/L Account) of the selected row
        if not row.empty:
            gl_pdf = row.iloc[0]['G/L Account']
            st.write('G/L Account:', gl_pdf)
        else:
            st.write('No data found for the selected GL Account.')
            
    except Exception as e:
        st.error(f'Error reading GL List CSV file: {e}')

    raw_github_csv_link_cost = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/Cost_Centre_list1.csv'
    
    # Read CSV data
    try:
        df = read_csv_data(raw_github_csv_link_cost)
        cost_codes = df['Tier - 3'].astype(str)
        cost_no = st.selectbox('Cost Center', cost_codes)
        
        # Split the selected gl_no to get the actual GL Account
        selected_cost_account = cost_no
        
        # Find the row where the GL Account matches the selected GL Account
        row_cost = df[df['Tier - 3'] == selected_cost_account]
        
        # Display the data from the third column (G/L Account) of the selected row
        if not row_cost.empty:
            cost_pdf = row_cost.iloc[0]['Cost Center']
            internal_pdf = row_cost.iloc[0]['Internal Order']
            st.write('Cost Center Code:', cost_pdf)
            st.write('Internal Order Code:', internal_pdf)
        else:
            st.write('No data found for the selected Cost Center.')
            
    except Exception as f:
        st.error(f'Error reading Cost Center CSV file: {f}')

    assignment = st.text_input('Assignment:')
    text = st.text_input('Text:')
    amount = st.text_input('Amount:')
    
    # Button to generate PDF
    if st.button("Generate PDF"):
        create_pdf(vendor, gl_pdf, cost_pdf, internal_pdf, assignment, text, amount)

if __name__ == '__main__':
    main()
