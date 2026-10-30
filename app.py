
import streamlit as st

st.set_page_config(
    page_title="Ella's Divine Bridal Studio",
    page_icon="💄",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #fff7f3;
}
h1, h2, h3 {
    color: #76152f;
}
.stButton button, .stLinkButton a {
    background-color: #76152f;
    color: white;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# BRAND BANNER
st.image(
    "WhatsApp Image 2026-10-30 at 11.26.35 PM.jpeg",
    use_container_width=True
)

st.title("Ella's Divine")
st.subheader("Beauty & Bridal Studio & Academy")
st.markdown("### Your Dream Look, Our Promise ❤️")

st.divider()

# BRIDAL PACKAGES
st.header("💄 Signature Bridal Packages")

st.image(
    "WhatsApp Image 2026-10-30 at 11.24.32 PM.jpeg",
    use_container_width=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("BASIC")
    st.title("₹6,000")

with col2:
    st.subheader("HD")
    st.title("₹8,000")

with col3:
    st.subheader("GLOSSY")
    st.title("₹10,000")

st.caption("All packages include Face Makeup, Eye Makeup, Hair Styling, Saree Draping and Saree Pre-Pleating.")

st.divider()
st.link_button(
    "💬 Book Now on WhatsApp",
    "https://wa.me/918428909415?text=Hello%20Ella%27s%20Divine,%20I%20want%20to%20book%20an%20appointment."
)

# MUHURTHAM PACKAGES
st.header("👑 Muhurtham / Reception / Engagement")

st.image(
    "WhatsApp Image 2026-10-30 at 11.24.31 PM.jpeg",
    use_container_width=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("BASIC LEVEL")
    st.title("₹10,000")
    st.write("Very light & age-appropriate makeup")
    st.link_button(
    "💬 Book Now on WhatsApp",
    "https://wa.me/918428909415?text=Hello%20Ella%27s%20Divine,%20I%20want%20to%20book%20an%20appointment."
)

with col2:
    st.subheader("ADVANCED HD")
    st.title("₹15,000")
    st.write("Camera-friendly HD finish")

with col3:
    st.subheader("PREMIUM")
    st.title("₹20,000")
    st.write("Luxury glowing finish")

st.caption("Prices are per session.")

st.divider()

# GUEST SERVICES
st.header("🌸 Guest Packages")

guest_services = {
    "Face Makeup Only": "₹2,000",
    "Hair Styling Only": "₹1,500",
    "Saree Draping Only": "₹800",
    "Saree Pre-Pleating Only": "₹500",
    "Pre-Pleat with Fluffy Pleats": "₹700",
    "Face Makeup + Saree Draping": "₹3,500"
}

for service, price in guest_services.items():
    st.write(f"**{service}** — {price}")

st.divider()

# BOOKING
st.header("📅 Book Your Appointment")
st.link_button(
    "💬 Book Now on WhatsApp",
    "https://wa.me/918428909415?text=Hello%20Ella%27s%20Divine,%20I%20want%20to%20book%20an%20appointment."
)

name = st.text_input("Your Name")
phone = st.text_input("Your Phone Number")

service = st.selectbox(
    "Select Your Package",
    [
        "Basic Bridal - ₹6,000",
        "HD Bridal - ₹8,000",
        "Glossy Bridal - ₹10,000",
        "Muhurtham Basic - ₹10,000",
        "Muhurtham Advanced HD - ₹15,000",
        "Muhurtham Premium - ₹20,000",
        "Guest Services"
    ]
)

if st.button("Submit Booking Enquiry"):
    if name and phone:
        message = f"Hello Ella's Divine! My name is {name}. Phone: {phone}. I am interested in {service}."
        import urllib.parse
        whatsapp_url = "https://wa.me/918428909415?text=" + urllib.parse.quote(message)
        st.success("Your enquiry is ready!")
        st.link_button("Send Enquiry on WhatsApp", whatsapp_url)
    else:
        st.warning("Please enter your name and phone number.")

st.divider()

st.markdown("### 💗 Ella's Divine Beauty & Bridal Studio")
st.write("📍 Vaithiswarankovil")
st.write("📞 WhatsApp: +91 8428909415")
st.write("📸 Instagram: @ellas_divine_bridal_studio")
