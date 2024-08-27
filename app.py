import streamlit as st
import re

# Function to validate email format
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def main():
    # Welcome message and login details
    st.markdown("<h1 style='text-align: center; color: teal;'>Welcome to the Rental Agreement App</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: purple;'>Please enter your login details</h3>", unsafe_allow_html=True)

    email = st.text_input("Email ID")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if validate_email(email):
            st.success("Sign up successful")
        else:
            st.error("Please enter a valid email address")

    # DOCS section with dropdown for rental agreements
    st.sidebar.markdown("<h2 style='color: orange;'>DOCS</h2>", unsafe_allow_html=True)
    doc_option = st.sidebar.selectbox("Select Document", ["Rental Agreements"])

    if doc_option == "Rental Agreements":
        st.markdown("<h2 style='color: blue;'>Rental Agreement Form</h2>", unsafe_allow_html=True)
        
        # Input fields for rental agreement details
        landlord_name = st.text_input("Landlord's Name and Address")
        tenant_name = st.text_input("Tenant's Name and Address")
        rental_property_address = st.text_input("Rental Property Address")
        monthly_rent = st.number_input("Monthly Rent Amount", min_value=0)
        security_deposit = st.number_input("Security Deposit Amount", min_value=0)
        lease_start_date = st.date_input("Lease Start Date")
        lease_end_date = st.date_input("Lease End Date")
        rent_due_date = st.text_input("Rent Due Date")
        maintenance_responsibilities = st.text_input("Maintenance Responsibilities")
        termination_notice_period = st.text_input("Termination Notice Period")
        
        # Display user details and rental agreement
        if st.button("Submit Rental Agreement"):
            st.markdown("<h2 style='color: green;'>Rental Agreement Details</h2>", unsafe_allow_html=True)
            st.write("### Landlord's Name and Address:", landlord_name)
            st.write("### Tenant's Name and Address:", tenant_name)
            st.write("### Rental Property Address:", rental_property_address)
            st.write("### Monthly Rent Amount:", monthly_rent)
            st.write("### Security Deposit Amount:", security_deposit)
            st.write("### Lease Start Date:", lease_start_date)
            st.write("### Lease End Date:", lease_end_date)
            st.write("### Rent Due Date:", rent_due_date)
            st.write("### Maintenance Responsibilities:", maintenance_responsibilities)
            st.write("### Termination Notice Period:", termination_notice_period)

    # Display user details section
    st.sidebar.markdown("<h3 style='color: green;'>User Details</h3>", unsafe_allow_html=True)
    if email and password:
        st.sidebar.write(f"Logged in as: {email}")

if __name__ == "__main__":
    main()
