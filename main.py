import streamlit as st
import pandas as pd
import requests
from fpdf import FPDF

# Function to read CSV file from GitHub repository
def read_csv_data(url):
    response = requests.get(url)
    df = pd.read_csv(url)
    return df

def create_pdf(vendor, gl_pdf, cost_pdf, internal_pdf, assignment, text, amount):
    # Create instance of FPDF class
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # Set font for the entire document
    pdf.set_font("Arial", size = 12)
    
    # Add a cell
    pdf.cell(200, 10, txt = "MAS Finance Department: PDF Table", ln = True, align = 'C')
    
    # Add line break
    pdf.ln(10)
    
    # Set font for table headers
    pdf.set_font("Arial", size = 10)
    
    # Add table headers
    pdf.cell(40, 10, "Vendor", 1, 0, 'C')
    pdf.cell(40, 10, "G/L Account", 1, 0, 'C')
    pdf.cell(40, 10, "Cost Center", 1, 0, 'C')
    pdf.cell(40, 10, "Internal Order", 1, 0, 'C')
    pdf.cell(40, 10, "Assignment", 1, 0, 'C')
    pdf.cell(40, 10, "Text", 1, 0, 'C')
    pdf.cell(40, 10, "Amount", 1, 1, 'C')
    
    # Set font for table data
    pdf.set_font("Arial", size = 8)
    
    # Add table data
    pdf.cell(40, 10, vendor, 1, 0, 'L')
    pdf.cell(40, 10, gl_pdf, 1, 0, 'L')
    pdf.cell(40, 10, cost_pdf, 1, 0, 'L')
    pdf.cell(40, 10, internal_pdf, 1, 0, 'L')
    pdf.cell(40, 10, assignment, 1, 0, 'L')
    pdf.cell(40, 10, text, 1, 0, 'L')
    pdf.cell(40, 10, amount, 1, 1, 'L')
    
    # Save the pdf with name .pdf
    pdf_file_name = "MAS_Finance_PDF_Table.pdf"
    pdf.output(pdf_file_name)
    
    return pdf_file_name

def main():
    st.title('MAS Finance Department: PDF Merger')

    # Replace 'raw_github_csv_link' with the raw GitHub link to your CSV file
    raw_github_csv_link_gl = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/GL_list1.csv'
    raw_github_csv_link_cost = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/Cost_Centre_list1.csv'

    vendor = st.text_input('Vendor Name:')
    
    # Read GL CSV data
    try:
        df_gl = read_csv_data(raw_github_csv_link_gl)
        gl_codes = df_gl['SAP B1 - A/C Name'].astype(str) + ' : ' + df_gl['G/L Acct Long Text'].astype(str)
        gl_no = st.selectbox('G/L Account', gl_codes)
        
        # Split the selected gl_no to get the actual GL Account
        selected_gl_account = gl_no.split(':')[0].strip()
        
        # Find the row where the GL Account matches the selected GL Account
        row_gl = df_gl[df_gl['SAP B1 - A/C Name'] == selected_gl_account]
        
        # Display the data from the third column (G/L Account) of the selected row
        if not row_gl.empty:
            gl_pdf = row_gl.iloc[0]['G/L Account']
            st.write('G/L Account:', gl_pdf)
        else:
            st.write('No data found for the selected G/L Account.')
            
    except Exception as e:
        st.error(f'Error reading GL List CSV file: {e}')

    # Read Cost Center CSV data
    try:
        df_cost = read_csv_data(raw_github_csv_link_cost)
        cost_codes = df_cost['Tier - 3'].astype(str)
        cost_no = st.selectbox('Cost Center', cost_codes)
        
        # Find the row where the Cost Center matches the selected Cost Center
        row_cost = df_cost[df_cost['Tier - 3'] == cost_no]
        
        # Display the data from the third column (Cost Center) of the selected row
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
    
    if st.button('Generate PDF'):
        if vendor and gl_pdf and cost_pdf and internal_pdf and assignment and text and amount:
            pdf_file_name = create_pdf(vendor, gl_pdf, cost_pdf, internal_pdf, assignment, text, amount)
            st.success(f'PDF generated successfully: [Download PDF]({pdf_file_name})')
        else:
            st.error('Please fill in all fields to generate the PDF.')

if __name__ == '__main__':
    main()
