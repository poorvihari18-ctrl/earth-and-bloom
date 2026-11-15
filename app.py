
import streamlit as st

# EARTH & BLOOM WEBSITE

st.set_page_config(
    page_title="EARTH & BLOOM",
    page_icon="🌿",
    layout="wide"
)

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

