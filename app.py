
import streamlit as st

# ==========================================
# EARTH & BLOOM - LUXURY SKINCARE STORE
# ==========================================

st.set_page_config(
    page_title="EARTH & BLOOM | Natural Skincare",
    page_icon="🌿",
    layout="wide"
)

# ==========================================
# WEBSITE DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #F7F4ED;
    color: #26372D;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1450px;
}

h1, h2, h3 {
    font-family: Georgia, serif !important;
    color: #26372D !important;
}

p, label {
    color: #45483F;
    font-family: Arial, sans-serif;
}

.brand-name {
    font-family: Georgia, serif;
    font-size: 48px;
    font-weight: bold;
    color: #26372D;
    letter-spacing: 2px;
    text-align: center;
    margin-bottom: 5px;
}

.brand-tagline {
    text-align: center;
    color: #B49A65;
    font-family: Georgia, serif;
    font-size: 17px;
    letter-spacing: 3px;
    margin-bottom: 35px;
}

.hero {
    background-color: #26372D;
    padding: 90px 30px;
    text-align: center;
    margin: 25px 0 55px 0;
}

.hero-label {
    color: #C5A66A !important;
    font-size: 12px;
    letter-spacing: 5px;
    text-transform: uppercase;
}

.hero h1 {
    color: #F7F4ED !important;
    font-family: Georgia, serif !important;
    font-size: 56px !important;
    font-weight: normal !important;
    line-height: 1.2;
    margin: 25px 0;
}

.hero-description {
    color: #F7F4ED !important;
    font-family: Georgia, serif;
    font-style: italic;
    font-size: 19px;
}

.section-label {
    color: #B49A65;
    font-size: 12px;
    letter-spacing: 4px;
    text-transform: uppercase;
    text-align: center;
}

.stButton button {
    background-color: #26372D;
    color: #F7F4ED;
    border: 1px solid #26372D;
    border-radius: 0;
    padding: 12px 22px;
    font-family: Georgia, serif;
    width: 100%;
}

.stButton button:hover {
    background-color: #B49A65;
    color: white;
    border-color: #B49A65;
}

[data-testid="stImage"] img {
    border-radius: 3px;
}

hr {
    border-color: #D8CFBE;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# BASKET
# ==========================================

if "basket" not in st.session_state:
    st.session_state.basket = []


# ==========================================
# BRAND HEADER
# ==========================================

st.markdown("""
<div class="brand-name">🌿 EARTH & BLOOM</div>
<div class="brand-tagline">FEEL GOOD. NATURALLY.</div>
""", unsafe_allow_html=True)

st.markdown(
    f"<p style='text-align:center;'>"
    f"Your basket: {len(st.session_state.basket)} item(s)"
    f"</p>",
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# LUXURY HERO BANNER
# ==========================================

st.markdown("""
<div class="hero">

    <p class="hero-label">
        THE NATURAL BEAUTY COLLECTION
    </p>

    <h1>
        Discover the Beauty<br>of Nature
    </h1>

    <p class="hero-description">
        Thoughtfully inspired skincare.<br>
        A little luxury in every ritual.
    </p>

    <p class="hero-label">
        FEEL GOOD. NATURALLY.
    </p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# INTRODUCTION
# ==========================================

st.markdown(
    '<p class="section-label">A LITTLE EVERYDAY LUXURY</p>',
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='text-align:center;'>Beauty Inspired by Nature</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>"
    "Discover thoughtful skincare essentials "
    "for your everyday beauty ritual."
    "</p>",
    unsafe_allow_html=True
)

st.write("")
st.divider()


# ==========================================
# PRODUCT COLLECTION
# ==========================================

st.markdown(
    '<p class="section-label">EXPLORE OUR COLLECTION</p>',
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='text-align:center;'>The Skincare Edit</h2>",
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "Screenshot 2026-11-14 141225.jpg",
        use_container_width=True
    )

    st.markdown("### Aloe Vera Face Cream")

    st.write("A simple skincare essential.")

    st.markdown("**£12.99**")

    if st.button("ADD TO BASKET", key="cream"):
        st.session_state.basket.append("Aloe Vera Face Cream")
        st.rerun()


with col2:
    st.image(
        "Screenshot 2026-11-14 141325.jpg",
        use_container_width=True
    )

    st.markdown("### Rose Water Toner")

    st.write("A refreshing addition to your routine.")

    st.markdown("**£8.99**")

    if st.button("ADD TO BASKET", key="toner"):
        st.session_state.basket.append("Rose Water Toner")
        st.rerun()


with col3:
    st.image(
        "Screenshot 2026-11-14 141349.jpg",
        use_container_width=True
    )

    st.markdown("### Shea Butter Moisturiser")

    st.write("A nourishing skincare essential.")

    st.markdown("**£10.99**")

    if st.button("ADD TO BASKET", key="shea"):
        st.session_state.basket.append("Shea Butter Moisturiser")
        st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.write("")
st.divider()

st.markdown("""
<div style="text-align:center; padding:35px 10px;">

    <h2 style="
        font-family:Georgia,serif;
        color:#26372D;
    ">
        EARTH & BLOOM
    </h2>

    <p style="
        color:#B49A65;
        letter-spacing:3px;
        font-size:12px;
    ">
        FEEL GOOD. NATURALLY.
    </p>

    <p style="font-size:13px;">
        Beauty and wellness inspired by nature.
    </p>

    <p style="font-size:12px;">
        © 2026 EARTH & BLOOM
    </p>

</div>
""", unsafe_allow_html=True)

