
import streamlit as st
import os
import streamlit.components.v1 as components
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

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        font-family: Georgia, serif;
    }

    .hero {
        background: #26372D;
        color: #F7F4ED;
        text-align: center;
        padding: 85px 25px;
        min-height: 390px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        animation: riseIn 1s ease-out;
    }

    .eyebrow {
        color: #C5A66A;
        font-family: Arial, sans-serif;
        font-size: 12px;
        letter-spacing: 5px;
        margin-bottom: 22px;
    }

    h1 {
        color: #F7F4ED;
        font-size: 58px;
        font-weight: normal;
        line-height: 1.2;
        margin: 0 0 22px;
    }

    .description {
        color: #F7F4ED;
        font-size: 19px;
        font-style: italic;
        line-height: 1.8;
    }

    .slogan {
        color: #C5A66A;
        font-family: Arial, sans-serif;
        font-size: 12px;
        letter-spacing: 4px;
        margin-top: 25px;
    }

    @keyframes riseIn {
        from {
            opacity: 0;
            transform: translateY(35px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @media (max-width: 600px) {
        h1 {
            font-size: 36px;
        }
        .hero {
            padding: 65px 15px;
        }
    }
</style>
</head>

<body>
    <div class="hero">
        <div class="eyebrow">THE NATURAL BEAUTY COLLECTION</div>

        <h1>Discover the Beauty<br>of Nature</h1>

        <div class="description">
            Thoughtfully inspired skincare.<br>
            A little luxury in every ritual.
        </div>

        <div class="slogan">FEEL GOOD. NATURALLY.</div>
    </div>
</body>
</html>
""", height=420, scrolling=False)

