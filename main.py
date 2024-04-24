import streamlit as st

def main():
    st.title('MAS Finance Department : PDF Merger')
    
    # Input fields
    gl_code = st.text_input('GL Code', '')
    cost_center_number = st.text_input('Cost Center Number', '')
    internal_order_number = st.text_input('Internal Order Number', '')

    # Displaying input values
    st.write('### Input Values:')
    st.write(f'GL Code: {gl_code}')
    st.write(f'Cost Center Number: {cost_center_number}')
    st.write(f'Internal Order Number: {internal_order_number}')

if __name__ == '__main__':
    main()

