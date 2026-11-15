
import streamlit as st

# EARTH & BLOOM WEBSITE

st.set_page_config(
    page_title="EARTH & BLOOM",
    page_icon="🌿",
    layout="wide"
)

# LUXURY WEBSITE DESIGN

st.markdown("""


st.markdown("""
<div class="hero" style="
    background: #26372D;
    padding: 100px 35px;
    text-align: center;
    margin: 35px 0;
">
    <p style="
        color: #C5A66A !important;
        font-family: Arial, sans-serif;
        font-size: 13px;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 25px;
    ">
        THE NATURAL BEAUTY COLLECTION
    </p>

    <h1 style="
        color: #F7F4ED !important;
        font-family: Georgia, serif !important;
        font-size: 58px !important;
        font-weight: normal !important;
        letter-spacing: 1px;
        line-height: 1.15;
        margin-bottom: 25px;
    ">
        Discover the Beauty<br>of Nature
    </h1>

    <p style="
        color: #F7F4ED !important;
        font-family: Georgia, serif;
        font-size: 20px;
        font-style: italic;
        margin-bottom: 35px;
    ">
        Thoughtfully inspired skincare.<br>
        A little luxury in every ritual.
    </p>

    <p style="
        color: #C5A66A !important;
        font-family: Arial, sans-serif;
        font-size: 12px;
        letter-spacing: 4px;
    ">
        FEEL GOOD. NATURALLY.
    </p>
</div>
""", unsafe_allow_html=True)


</style>
""", unsafe_allow_html=True)

st.title("🌿 EARTH & BLOOM")

st.subheader("Feel good. Naturally.")

st.write(
    "Welcome to EARTH & BLOOM! "
    "Discover beauty and wellness inspired by nature."
)

st.divider()

st.markdown("""
<div class="hero">
    <h1>Discover the Beauty of Nature</h1>
    <p>Thoughtfully inspired skincare. A little luxury in every ritual.</p>
    <p>FEEL GOOD. NATURALLY.</p>
</div>
""", unsafe_allow_html=True)

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

