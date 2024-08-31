import streamlit as st
from fpdf import FPDF

# Function to generate the rental agreement PDF
def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()

    # Title without emoji
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="RENTAL AGREEMENT", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"This RENTAL AGREEMENT is executed on this {data['lease_start_date']} by and between:")
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 10, txt=f"{data['landlord_name']}")
    pdf.multi_cell(0, 10, txt="(hereinafter called the 'OWNER', which expression shall include their heirs, legal representatives, successors, and assigns) of the ONE PART;")
    pdf.ln(5)
    
    pdf.multi_cell(0, 10, txt=f"AND,")
    pdf.ln(5)
    
    pdf.multi_cell(0, 10, txt=f"{data['tenant_name']}")
    pdf.multi_cell(0, 10, txt="(hereinafter called the 'TENANT', which expression shall include its legal representatives, successors, and assigns) of the OTHER PART.")
    pdf.ln(10)
    
    pdf.multi_cell(0, 10, txt=f"WHEREAS the Owner is the absolute owner of the property situated at {data['rental_property_address']} as detailed in Annexure-I, hereinafter referred to as 'Demised Premises'.")
    pdf.ln(5)
    
    pdf.multi_cell(0, 10, txt="WHEREAS the Tenant has requested the Owner to grant Rent with respect to the Schedule Premises, and the Owner has agreed to rent out to the Tenant the Property for residential purposes only, on the following terms and conditions:")
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, txt="Terms and Conditions", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"1. The rent in respect of the 'Demised Premises' shall commence from {data['lease_start_date']} and shall be valid till {data['lease_end_date']}. Thereafter, the same may be extended further on mutual consent of both parties.")
    pdf.multi_cell(0, 10, txt=f"2. The Tenant shall pay to the Owner a monthly rent of Rs. {data['monthly_rent']}, excluding electricity and water bill. The rent shall be paid on or before {data['rent_due_date']} of each month without fail.")
    pdf.multi_cell(0, 10, txt=f"3. The Tenant shall pay to the Owner a monthly maintenance charge of Rs. (Amount in Numbers) towards maintenance, etc.")
    pdf.multi_cell(0, 10, txt=f"4. The Tenant will pay to the Owner an interest-free refundable security deposit of Rs. {data['security_deposit']} at the time of signing the Rent Agreement.")
    pdf.multi_cell(0, 10, txt="5. The Tenant shall not sublet, assign, or part with the demised premises in whole or part thereof to any person in any circumstances whatsoever, and the same shall be used for bona fide residential purposes only.")
    pdf.multi_cell(0, 10, txt="6. The Tenant shall maintain the Demised Premises in good and tenable condition, and all the minor repairs such as leakage in the sanitary fittings, water taps, and electrical usage etc., shall be carried out by the Tenant.")
    pdf.multi_cell(0, 10, txt="7. Both parties shall observe and adhere to the terms and conditions contained hereinabove.")
    pdf.ln(10)

    pdf.multi_cell(0, 10, txt="IN WITNESS WHEREOF BOTH PARTIES AGREES AND SIGNS THIS AGREEMENT ON THIS DAY AND YEAR")
    pdf.ln(20)
    
    pdf.cell(0, 10, txt="_____________________________", ln=True)
    pdf.cell(0, 10, txt="Signature of Landlord", ln=True)
    
    pdf.ln(10)
    
    pdf.cell(0, 10, txt="_____________________________", ln=True)
    pdf.cell(0, 10, txt="Signature of Tenant", ln=True)
    
    # Save the PDF
    pdf_filename = "Rental_Agreement.pdf"
    pdf.output(pdf_filename)

    return pdf_filename

def main():
    # Page configuration
    st.set_page_config(page_title="BONDSPHERE", page_icon="🏠")
    
    st.title("🏠 BONDSPHERE")
    st.subheader("Your Trusted Platform for Rental Agreements 🤝")

    # Tabs for navigation
    tabs = st.tabs(["🔑 Sign-In", "📝 Agreement Details", "📄 Preview and Download Agreement"])

    with tabs[0]:
        # Sign-In Tab
        st.subheader("🔐 Please enter your login details")

        email = st.text_input("📧 Email ID")
        password = st.text_input("🔑 Password", type="password")
        if st.button("Sign Up ✍️"):
            st.success("Sign up successful ✅")

    with tabs[1]:
        # Agreement Details Tab
        st.header("📄 Rental Agreement Form")
        
        st.subheader("👤 Landlord Details")
        landlord_name = st.text_input("Landlord's Name and Address")

        st.subheader("👥 Tenant Details")
        tenant_name = st.text_input("Tenant's Name and Address")

        st.subheader("🏠 Property Details")
        rental_property_address = st.text_input("Rental Property Address")
        
        st.subheader("🗓️ Agreement Details")
        monthly_rent = st.number_input("💰 Monthly Rent Amount", min_value=0)
        security_deposit = st.number_input("💼 Security Deposit Amount", min_value=0)
        lease_start_date = st.date_input("📅 Lease Start Date")
        lease_end_date = st.date_input("📅 Lease End Date")
        rent_due_date = st.text_input("📅 Rent Due Date")
        maintenance_responsibilities = st.text_input("🔧 Maintenance Responsibilities")
        termination_notice_period = st.text_input("📋 Termination Notice Period")

        if st.button("Submit Agreement Details ✍️"):
            st.session_state['agreement_data'] = {
                "landlord_name": landlord_name,
                "tenant_name": tenant_name,
                "rental_property_address": rental_property_address,
                "monthly_rent": monthly_rent,
                "security_deposit": security_deposit,
                "lease_start_date": lease_start_date,
                "lease_end_date": lease_end_date,
                "rent_due_date": rent_due_date,
                "maintenance_responsibilities": maintenance_responsibilities,
                "termination_notice_period": termination_notice_period,
            }
            st.success("Agreement details submitted successfully ✅")

    with tabs[2]:
        # Preview and Download Agreement Tab
        st.header("👀 Preview Rental Agreement")
        if 'agreement_data' in st.session_state:
            data = st.session_state['agreement_data']
            st.write("### 👤 Landlord's Name and Address:", data['landlord_name'])
            st.write("### 👥 Tenant's Name and Address:", data['tenant_name'])
            st.write("### 🏠 Rental Property Address:", data['rental_property_address'])
            st.write("### 💰 Monthly Rent Amount:", data['monthly_rent'])
            st.write("### 💼 Security Deposit Amount:", data['security_deposit'])
            st.write("### 📅 Lease Start Date:", data['lease_start_date'])
            st.write("### 📅 Lease End Date:", data['lease_end_date'])
            st.write("### 📅 Rent Due Date:", data['rent_due_date'])
            st.write("### 🔧 Maintenance Responsibilities:", data['maintenance_responsibilities'])
            st.write("### 📋 Termination Notice Period:", data['termination_notice_period'])

            # Generate and download the PDF
            pdf_file = generate_pdf(data)

            st.markdown("<h3 style='color: red;'>📥 Download Rental Agreement PDF</h3>", unsafe_allow_html=True)
            with open(pdf_file, "rb") as file:
                st.download_button(
                    label="Download PDF",
                    data=file,
                    file_name=pdf_file,
                    mime="application/pdf"
                )
        else:
            st.warning("⚠️ Please submit the agreement details in the '📝 Agreement Details' tab first.")

if __name__ == "__main__":
    main()
