import re
import streamlit as st

#page styling
st.set_page_config(
    page_title="Password Strength Meter checker by @Raees",
    page_icon=":🔑:",
    layout="centered",
)

#custom css
st.markdown("""
<style>
    .main{text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton:hover {background-color: #45a049;}

</style>
""", unsafe_allow_html=True)

# page title
st.title(" 🔒Password Strength Generator")
st.write("Enter your password to generate a strong  💪 password ")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
        feedback.append("Password is at least 8 characters long")
    else:
        feedback.append("Password is too short")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include both uppercase and lowercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include at least one number")

    if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character")   

    #display password strength
    if score == 4:
        st.success("Password is strong")
    elif score == 3:
        st.info("Password is medium")
    else:
        st.error("Password is weak")

    #feedback
    if feedback:
        with st.expander("Imporve Your Password"):
            for item in feedback:
                st.write(item)

#password input
password = st.text_input("Enter your password", type="password", help="Password should be at least 8 characters long and include both uppercase and lowercase letters, at least one number, and at least one special character")

#generate password button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password")
    

        
        
        
        
        
