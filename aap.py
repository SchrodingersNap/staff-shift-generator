import streamlit as st
from fpdf import FPDF

# 1. THE STAFF LIST (Extracted from your image)
STAFF_NAMES = [
    "Pramod Kumar Meena", "Gourab Biswas", "Kingsuk Burman", "Rajib Kumar Paul",
    "Pankaj Chowdhury", "Joydeb Mandal", "PARTHA ROY", "Sumalya Chatterjee",
    "Azam Ali", "Anil Kumar", "Hemlal Sharma", "Sunit Kumar Das",
    "Mrityunjoy Saha", "Pradip Kumar Mondal", "Pardeep .", "Goutam Patra",
    "Mukesh Swami", "Amit Kumar", "Abhisake Chandan Tirkey", "Pradip Karmakar",
    "Bidhan Deb Barma", "Sanjay Paul", "Mohit .", "Tej Singh Meena",
    "BISWARUP CHAKRABORTY", "Sanjit Mondal", "Somenath Mandal", "Nitin Kumar",
    "SOMENATH DAS", "PALLAB KR. SAHA", "Naveen .", "Subhajit Saha",
    "Sukumar Maji", "Subhra Jyoti Banerjee", "Jitender .", "VARASALA AMBEDKAR",
    "Kalyan Mondal", "Chandra Nath Mitra", "Ashok Dasgupta", "Manjeet .",
    "Gopal Howli", "Soumen Mondal", "Alok Roy", "Dhirendar Kumar",
    "RAJIB SEN", "Rajendra Kumar", "Sarbeswar Hembram", "Shibendu Dutta",
    "Vikas Chhikara", "DIPANKAR DEY", "SK. SABIR AHMED", "Shyamal Kumar Ghosh",
    "Sudhir .", "Sanjib Kumar Mondal"
]


def create_pdf(selected_staff):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    pairs = []
    for i in range(0, len(selected_staff), 2):
        if i + 1 < len(selected_staff):
            pairs.append(f"{selected_staff[i]} + {selected_staff[i+1]} -")
        else:
            pairs.append(f"{selected_staff[i]} (Solo) -")

    for round_num in range(1, 8):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"ROUND {round_num}", ln=True, border='B')
        pdf.ln(2)
        
        pdf.set_font("Arial", size=10)
        for idx, pair in enumerate(pairs):
            if round_num == 1:
                # Round 1: Numbered
                pdf.cell(0, 8, f"{idx + 1}. {pair}", ln=True)
            else:
                # Rounds 2-7: Draw a literal square box
                current_y = pdf.get_y()
                pdf.rect(10, current_y + 2, 4, 4) # Draw the box (x, y, width, height)
                pdf.set_x(16) # Move text to the right of the box
                pdf.cell(0, 8, pair, ln=True)
        
        pdf.ln(5)
        
    return pdf.output(dest='S')
# --- STREAMLIT UI ---
st.title("📋 Staff Shift Scheduler")

st.subheader("Step 1: Select Staff")
num_to_select = st.number_input("How many staff members do you need?", min_value=2, max_value=len(STAFF_NAMES), value=22)

selected_staff = st.multiselect(
    "Select names from the list:",
    options=STAFF_NAMES,
    max_selections=num_to_select
)

if len(selected_staff) == num_to_select:
    st.success(f"All {num_to_select} staff selected!")
    
    if st.button("Generate PDF"):
        pdf_data = create_pdf(selected_staff)
        st.download_button(
            label="Download Shift Rounds PDF",
            data=pdf_data,
            file_name="staff_rounds.pdf",
            mime="application/pdf"
        )
else:
    st.info(f"Please select exactly {num_to_select} staff members to enable PDF generation.")

