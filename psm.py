import re
import streamlit as st

# Page Styling
st.set_page_config(
    page_title="Password Strength Meter Checker by @Raees",
    page_icon="🔑",
    layout="centered",
)

# Custom CSS (Limited Support)
st.markdown("""
    <style>
        .main {text-align: center;}
        .stTextInput {width: 100% !important;}
        .stButton button {background-color: #4CAF50; color: yellow; font-size: 18px;}
        .stButton button:hover {background-color: blue;}
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("🔒 Password Strength Meter")
st.write("Enter your password to check its strength.")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password is too short (must be at least 8 characters).")

    # Upper & Lower Case Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Number Check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Special Character Check
    if re.search(r'[^\w\s]', password):  # Matches any non-alphanumeric character
        score += 1
    else:
        feedback.append("❌ Add at least one special character (e.g., !@#$%^&*).")

    # Display Password Strength
    strength_messages = {
        4: ("✅ Strong Password", "success"),
        3: ("⚠️ Medium Password", "info"),
        2: ("❗ Weak Password", "warning"),
        1: ("❌ Very Weak Password", "error"),
        0: ("❌ Extremely Weak Password", "error")
    }

    msg, alert_type = strength_messages.get(score, ("❌ Extremely Weak Password", "error"))
    getattr(st, alert_type)(msg)

    # Display Feedback
    if feedback:
        with st.expander("🔍 Improve Your Password"):
            for item in feedback:
                st.write(item)

# Password Input
password = st.text_input("Enter your password:", type="password", 
                         help="Must be at least 8 characters long and include uppercase, lowercase, a number, and a special character.")

# Check Strength Button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password.")
