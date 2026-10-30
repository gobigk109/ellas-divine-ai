
import streamlit as st

st.set_page_config(
    page_title="Ella's Divine Beauty Studio",
    page_icon="💄",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #fff5f7;
}
h1 {
    color: #9c315d;
    text-align: center;
}
h2, h3 {
    color: #9c315d;
}
.hero {
    background: linear-gradient(135deg, #f8d7e5, #fff0f5);
    padding: 35px;
    border-radius: 18px;
    text-align: center;
}
.service {
    background: white;
    padding: 22px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #f1c5d7;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Ella's Divine</h1>
    <h3>Beauty & Bridal Studio</h3>
    <p>Enhancing Your Natural Beauty</p>
    <p>Welcome to Our Beautiful World!</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.header("✨ Our Beauty Services")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="service"><h2>💄</h2><h3>Bridal Makeup</h3><p>Beautiful Bridal Makeover</p></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="service"><h2>💇</h2><h3>Hair Styling</h3><p>Beautiful Hairstyles</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="service"><h2>🌸</h2><h3>Facial</h3><p>Glow and Skin Care</p></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="service"><h2>✨</h2><h3>Threading</h3><p>Beauty and Grooming</p></div>', unsafe_allow_html=True)

st.write("")
st.header("📅 Book Your Appointment")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
service = st.selectbox(
    "Choose Your Service",
    ["Bridal Makeup", "Facial", "Hair Styling", "Threading"]
)

if st.button("Submit Enquiry"):
    if name and phone:
        st.success("Thank you! We will contact you soon.")
    else:
        st.warning("Please enter your name and phone number.")

st.markdown("---")
st.markdown(
    "<center>💗 Ella's Divine Beauty & Bridal Studio</center>",
    unsafe_allow_html=True
)

