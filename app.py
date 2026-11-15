
import streamlit as st
import os

# ==========================================
# EARTH & BLOOM - LUXURY SKINCARE STORE
# ==========================================

st.set_page_config(
    page_title="EARTH & BLOOM | Natural Skincare",
    page_icon="🌿",
    layout="wide"
)

# ==========================================
# COLOURS AND WEBSITE STYLING
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #F7F4ED;
    color: #26372D;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: Georgia, serif !important;
    color: #26372D !important;
}

p, label, span {
    color: #45483F;
}

.brand-title {
    font-family: Georgia, serif;
    font-size: 56px;
    font-weight: bold;
    letter-spacing: 3px;
    color: #26372D;
    text-align: center;
}

.brand-slogan {
    color: #B49A65;
    font-family: Georgia, serif;
    font-size: 17px;
    letter-spacing: 5px;
    text-align: center;
    margin-bottom: 35px;
}

.hero {
    background-color: #26372D;
    padding: 90px 30px;
    text-align: center;
    margin: 35px 0 55px 0;
}

.hero-label {
    color: #C5A66A !important;
    font-family: Arial, sans-serif;
    font-size: 12px;
    letter-spacing: 5px;
}

.hero h1 {
    color: #F7F4ED !important;
    font-family: Georgia, serif !important;
    font-size: 58px !important;
    font-weight: normal !important;
    line-height: 1.2;
}

.hero-description {
    color: #F7F4ED !important;
    font-family: Georgia, serif;
    font-size: 20px;
    font-style: italic;
    line-height: 1.8;
}

.hero-footer {
    color: #C5A66A !important;
    font-family: Arial, sans-serif;
    font-size: 12px;
    letter-spacing: 4px;
    margin-top: 30px;
}

.section-heading {
    font-family: Georgia, serif;
    font-size: 38px;
    color: #26372D;
    margin-top: 35px;
}

.product-name {
    font-family: Georgia, serif;
    font-size: 23px;
    color: #26372D;
    min-height: 60px;
}

.product-price {
    font-family: Georgia, serif;
    font-size: 20px;
    color: #26372D;
    margin-top: 15px;
}

.stButton button {
    background-color: #26372D;
    color: #FFFFFF;
    border: 1px solid #26372D;
    border-radius: 0;
    padding: 12px 20px;
    width: 100%;
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


# ==========================================
# BASKET SETUP
# ==========================================

if "basket" not in st.session_state:
    st.session_state.basket = {}


# ==========================================
# PRODUCT INFORMATION
# ==========================================

products = [
    {
        "id": "cream",
        "name": "Aloe Vera Face Cream",
        "price": 12.99,
        "image": "Screenshot 2026-11-14 141225.jpg",
        "description": "A gentle skincare essential for your daily routine."
    },
    {
        "id": "toner",
        "name": "Rose Water Toner",
        "price": 8.99,
        "image": "Screenshot 2026-11-14 141325.jpg",
        "description": "A refreshing addition to your skincare ritual."
    },
    {
        "id": "shea",
        "name": "Shea Butter Moisturiser",
        "price": 10.99,
        "image": "Screenshot 2026-11-14 141349.jpg",
        "description": "A rich moisturiser for everyday care."
    }
]


# ==========================================
# WEBSITE HEADER
# ==========================================

st.markdown("""
<div class="brand-title">🌿 EARTH & BLOOM</div>
<div class="brand-slogan">FEEL GOOD. NATURALLY.</div>
""", unsafe_allow_html=True)

basket_count = sum(st.session_state.basket.values())

st.markdown(
    f"<p style='text-align:center; font-size:17px;'>"
    f"YOUR BASKET: {basket_count} ITEM(S)</p>",
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

    <p class="hero-footer">
        FEEL GOOD. NATURALLY.
    </p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# INTRODUCTION
# ==========================================

st.markdown(
    '<div class="section-heading">A More Beautiful Daily Ritual</div>',
    unsafe_allow_html=True
)

st.write(
    "Explore our collection of beauty and skincare essentials, "
    "thoughtfully selected to bring a little luxury into your everyday routine."
)

st.divider()


# ==========================================
# PRODUCT COLLECTION
# ==========================================

st.markdown(
    '<div class="section-heading">The Skincare Collection</div>',
    unsafe_allow_html=True
)

st.write("Discover your new everyday favourites.")

col1, col2, col3 = st.columns(3, gap="large")

columns = [col1, col2, col3]

for product, column in zip(products, columns):

    with column:

        st.markdown(
            f'<div class="product-name">{product["name"]}</div>',
            unsafe_allow_html=True
        )

        if os.path.exists(product["image"]):
            st.image(
                product["image"],
                use_container_width=True
            )
        else:
            st.warning(
                f"Image not found: {product['image']}"
            )

        st.write(product["description"])

        st.markdown(
            f'<div class="product-price">£{product["price"]:.2f}</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "ADD TO BASKET",
            key=product["id"],
            use_container_width=True
        ):
            st.session_state.basket[product["id"]] = (
                st.session_state.basket.get(product["id"], 0) + 1
            )
            st.rerun()


# ==========================================
# SHOPPING BASKET
# ==========================================

st.divider()

st.markdown(
    '<div class="section-heading">Your Shopping Basket</div>',
    unsafe_allow_html=True
)

total = 0

if st.session_state.basket:

    for product in products:

        quantity = st.session_state.basket.get(
            product["id"], 0
        )

        if quantity > 0:

            item_total = product["price"] * quantity
            total += item_total

            st.write(
                f"**{product['name']}** — "
                f"Quantity: {quantity} — "
                f"£{item_total:.2f}"
            )

    st.markdown("---")

    st.subheader(f"Your total: £{total:.2f}")

    if st.button("CLEAR BASKET"):
        st.session_state.basket = {}
        st.rerun()

else:
    st.write("Your basket is currently empty.")


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
<div style="text-align:center; padding:35px 10px;">

    <h2 style="font-family:Georgia,serif;">
        EARTH & BLOOM
    </h2>

    <p style="color:#B49A65; letter-spacing:4px;">
        FEEL GOOD. NATURALLY.
    </p>

    <p>
        Beauty inspired by nature.
    </p>

    <p style="font-size:13px;">
        © 2026 EARTH & BLOOM. All rights reserved.
    </p>

</div>
""", unsafe_allow_html=True)


