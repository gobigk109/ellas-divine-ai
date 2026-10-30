import streamlit as st
from google import genai

st.set_page_config(
    page_title="Ella's Divine Bridal Studio",
    page_icon="💄",
    layout="wide"
)

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.markdown("""
<style>
.stApp {
    background: #fff7f3;
}

h1, h2, h3 {
    color: #76152f;
}

.stButton button {
    background-color: #76152f;
    color: white;
    border-radius: 12px;
}

.stLinkButton a {
    background-color: #25D366 !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: bold !important;
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
st.link_button(
    "📍 Find Our Studio – Google Maps",
    "https://share.google/9JXUSVzi2tXfncoiO"
)
st.write("📸 Instagram: @ellas_divine_bridal_studio")

# ELLA'S DIVINE CHAT ASSISTANT

st.divider()
st.header("🤖 Ella's Divine AI Assistant")
st.write("Ask me about Bridal Makeup, Packages, Prices and Booking!")
st.caption("தமிழ் அல்லது English-ல் கேள்வி கேட்கலாம்.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)

user_question = st.chat_input("Ask Ella's Divine...")

if user_question:
    st.session_state.chat_history.append(
        ("user", user_question)
    )

    try:
        conversation = "\n".join(
            [
                f"{role}: {message}"
                for role, message in st.session_state.chat_history[-10:]
            ]
        )

        prompt = f"""
You are the official AI assistant of Ella's Divine
Beauty & Bridal Studio & Academy in Vaithiswarankovil.

BUSINESS DETAILS:

Location: Vaithiswarankovil, Tamil Nadu
WhatsApp: +91 8428909415

BRIDAL PACKAGES:
Basic Bridal: ₹6,000
HD Bridal: ₹8,000
Glossy Bridal: ₹10,000

MUHURTHAM / RECEPTION / ENGAGEMENT:
Basic: ₹10,000
Advanced HD: ₹15,000
Premium: ₹20,000

GUEST SERVICES:
Face Makeup: ₹2,000
Hair Styling: ₹1,500
Saree Draping: ₹800
Saree Pre-Pleating: ₹500
Pre-Pleat with Fluffy Pleats: ₹700
Face Makeup + Saree Draping: ₹3,500

ACADEMY COURSES:

- Professional Makeup Classes
- Personal Grooming
- Skin Care
- Hair Care
- Side Draping
- Saree Draping
- Saree Box Folding
- Saree Pre-Pleating

SPECIAL FEATURES:
- Live Practical Demonstrations
- Portfolio Creation for Students

INSTRUCTIONS:
1. Reply in Tamil or English based on the customer's language.
2. Be friendly, polite and professional.
3. Answer questions about services and prices.
4. Never invent prices or booking availability.
5. For appointments, direct customers to WhatsApp.
6. Keep replies simple and helpful.

CONVERSATION:
{conversation}

Answer the latest customer question.
"""

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        answer = response.text or "Please contact us on WhatsApp."

    except Exception as e:
        answer = f"AI Assistant Error: {e}"

    st.session_state.chat_history.append(
        ("assistant", answer)
    )

    st.rerun()
    
# CUSTOMER BOOKING FORM

st.divider()
st.header("💍 Bridal Booking Enquiry")

with st.form("bridal_booking_form"):
    customer_name = st.text_input("Customer Name")
    customer_phone = st.text_input("WhatsApp Number")
    wedding_date = st.date_input("Wedding Date")

    makeup_package = st.selectbox(
        "Select Makeup Package",
        [
            "Basic - ₹6,000",
            "HD - ₹8,000",
            "Glossy - ₹10,000",
            "Muhurtham Basic - ₹10,000",
            "Muhurtham Advanced HD - ₹15,000",
            "Muhurtham Premium - ₹20,000"
        ]
    )

    submit_booking = st.form_submit_button("Submit Booking Enquiry")

    
    if submit_booking:
        if customer_name and customer_phone:

            import json
            import urllib.request
            import urllib.parse

            booking_data = {
                "name": customer_name,
                "phone": customer_phone,
                "date": str(wedding_date),
                "package": makeup_package
            }

            script_url = "https://script.google.com/macros/s/AKfycbxxwDkpqDUu4Rr4kSz4CIAxwfBuKLYA9KukR-irPAqpTHrQB8i7VAPRyVnIMu4Pc_G97w/exec"

            try:
                data = json.dumps(booking_data).encode("utf-8")

                request = urllib.request.Request(
                    script_url,
                    data=data,
                    headers={"Content-Type": "application/json"},
                    method="POST"
                )

                with urllib.request.urlopen(request, timeout=30) as response:
                    result = json.loads(response.read().decode("utf-8"))

                if result.get("status") == "success":
                    st.success("Booking saved successfully!")

                    message = (
                        f"Hello Ella's Divine! "
                        f"Name: {customer_name}, "
                        f"Phone: {customer_phone}, "
                        f"Date: {wedding_date}, "
                        f"Package: {makeup_package}"
                    )

                    whatsapp_url = (
                        "https://wa.me/918428909415?text="
                        + urllib.parse.quote(message)
                    )

                    st.link_button(
                        "Send Booking on WhatsApp",
                        whatsapp_url
                    )
                else:
                    st.error("Booking could not be saved.")

            except Exception as e:
                st.error(f"Database Error: {e}")

        else:
            st.warning("Please enter your name and phone number.")



