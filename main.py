import streamlit as st
import pandas as pd
import requests

# Function to read CSV file from GitHub repository
def read_csv_data(url):
    response = requests.get(url)
    df = pd.read_csv(url)
    return df

def main():
    st.title('MAS Finance Department : PDF Merger')

    # Replace 'raw_github_csv_link' with the raw GitHub link to your CSV file
    raw_github_csv_link_gl = 'https://raw.githubusercontent.com/SenalFernando712/mas-finance/main/GL_list1.csv'
    
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
            st.write('G/L Account:', row.iloc[0]['G/L Account'])
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
            #st.write('Cost Center Code:', row_cost.iloc[0]['Cost Center'])
            st.markdown(f'<p style="color: green;">Cost Center Code: {row.iloc[0]["Cost Center"]}</p>', unsafe_allow_html=True)
        else:
            st.write('No data found for the selected GL Account.')
            
    except Exception as f:
        st.error(f'Error reading Cost Center CSV file: {f}')

if __name__ == '__main__':
    main()
