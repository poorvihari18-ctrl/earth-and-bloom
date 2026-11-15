
import streamlit as st

# EARTH & BLOOM WEBSITE

st.set_page_config(
    page_title="EARTH & BLOOM",
    page_icon="🌿",
    layout="wide"
)

# LUXURY WEBSITE DESIGN

st.markdown("""
<style>

    .hero {
        background-color: #26372D;
        color: #F7F4ED;
        padding: 90px 55px;
        text-align: center;
        border-radius: 3px;
        margin: 35px 0;
    }

    .hero h1 {
        color: #F7F4ED !important;
        font-family: Georgia, serif !important;
        font-size: 48px;
        letter-spacing: 1px;
    }

    .hero p {
        color: #E8E0D0;
        font-size: 18px;
    }
    .stApp {
        background-color: #F7F4ED;
        color: #26372D;
    }

    h1, h2, h3 {
        font-family: Georgia, serif !important;
        color: #26372D !important;
    }

    p, label, span {
        color: #45483F;
    }

    [data-testid="stHeader"] {
        background-color: #F7F4ED;
    }

    .stButton button {
        background-color: #26372D;
        color: white;
        border: 1px solid #26372D;
        border-radius: 2px;
        padding: 10px 24px;
        font-family: Georgia, serif;
    }

    .stButton button:hover {
        background-color: #B49A65;
        color: white;
        border-color: #B49A65;
    }

    hr {
        border-color: #D8CFBE;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌿 EARTH & BLOOM")

st.subheader("Feel good. Naturally.")

st.write(
    "Welcome to EARTH & BLOOM! "
    "Discover beauty and wellness inspired by nature."
)

st.divider()

st.header("Welcome to our online store")

st.write("Explore our beauty and wellness collection.")

st.success("Our shop is growing. Come and explore!")

st.divider()

st.header("Our Skincare Collection")

st.write("Discover simple beauty essentials.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Aloe Vera Face Cream")
    st.image("Screenshot 2026-11-14 141225.jpg", use_container_width=True)
    st.write("£12.99")
    st.button("Add to Basket", key="cream")
   
with col2:
    st.subheader("Rose Water Toner")
    st.image("Screenshot 2026-11-14 141325.jpg", use_container_width=True)
    st.write("£8.99")
    st.button("Add to Basket", key="toner")

with col3:
    st.subheader("Shea Butter Moisturiser")
    st.image("Screenshot 2026-11-14 141349.jpg", use_container_width=True)
    st.write("£10.99")
    st.button("Add to Basket", key="shea")

