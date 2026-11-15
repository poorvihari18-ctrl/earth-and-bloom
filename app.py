
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
# SMALL LUXURY ICONS

st.markdown("""
<div style="
    display:flex;
    justify-content:center;
    gap:55px;
    padding:25px 10px;
    text-align:center;
    flex-wrap:wrap;
">
    <div>
        <div style="font-size:25px;">🌿</div>
        <small>BOTANICAL BEAUTY</small>
    </div>
    <div>
        <div style="font-size:25px;">💧</div>
        <small>DAILY HYDRATION</small>
    </div>
    <div>
        <div style="font-size:25px;">🌸</div>
        <small>GENTLE CARE</small>
    </div>
    <div>
        <div style="font-size:25px;">✨</div>
        <small>BEAUTY RITUALS</small>
    </div>
</div>
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

# ==========================================
# INTRODUCTION
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:35px 10px;">
    <p style="color:#B49A65; letter-spacing:4px; font-size:12px;">
        A LITTLE MOMENT FOR YOURSELF
    </p>
    <h2 style="font-family:Georgia,serif; font-size:38px;">
        Beauty in Every Ritual
    </h2>
    <p>Thoughtful essentials for your everyday beauty routine.</p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# ALL 20 PRODUCTS
# ==========================================

products.extend([
    {"id":"cleanser","name":"Gentle Facial Cleanser","price":11.99,"icon":"🫧"},
    {"id":"serum","name":"Vitamin C Face Serum","price":16.99,"icon":"✨"},
    {"id":"sunscreen","name":"Daily Face Sunscreen","price":14.99,"icon":"☀️"},
    {"id":"lipbalm","name":"Nourishing Lip Balm","price":5.99,"icon":"🌸"},
    {"id":"faceoil","name":"Botanical Face Oil","price":18.99,"icon":"🌿"},
    {"id":"ey cream","name":"Hydrating Eye Cream","price":13.99,"icon":"👁️"},
    {"id":"facemask","name":"Nourishing Face Mask","price":9.99,"icon":"🧖"},
    {"id":"scrub","name":"Gentle Face Scrub","price":10.99,"icon":"🌼"},
    {"id":"bodylotion","name":"Daily Body Lotion","price":12.99,"icon":"🤍"},
    {"id":"handcream","name":"Softening Hand Cream","price":7.99,"icon":"🌷"},
    {"id":"bodywash","name":"Gentle Body Wash","price":8.99,"icon":"🛁"},
    {"id":"hairmask","name":"Nourishing Hair Mask","price":14.99,"icon":"🌱"},
    {"id":"shampoo","name":"Botanical Shampoo","price":10.99,"icon":"🧴"},
    {"id":"conditioner","name":"Botanical Conditioner","price":10.99,"icon":"🌿"},
    {"id":"bodyoil","name":"Silky Body Oil","price":15.99,"icon":"💧"},
    {"id":"nightcream","name":"Overnight Face Cream","price":17.99,"icon":"🌙"},
    {"id":"balm","name":"Multi-Purpose Beauty Balm","price":9.99,"icon":"🌺"}
])


# ==========================================
# PRODUCT COLLECTION
# ==========================================

st.markdown("---")

st.markdown("""
<div style="padding:25px 0;">
    <p style="color:#B49A65; letter-spacing:4px; font-size:12px;">
        THE EARTH & BLOOM EDIT
    </p>
    <h2 style="font-family:Georgia,serif; font-size:38px;">
        Explore Our Collection
    </h2>
    <p>Find the little essentials that make a difference.</p>
</div>
""", unsafe_allow_html=True)

for start in range(0, len(products), 4):
    product_row = products[start:start + 4]
    cols = st.columns(4, gap="large")

    for product, col in zip(product_row, cols):
        with col:
            with st.container(border=True):
                if "image" in product and os.path.exists(product["image"]):
                    st.image(product["image"], use_container_width=True)
                else:
                    st.markdown(
                        f"<div style='background:#EAE5DA; padding:35px;"
                        f"text-align:center; font-size:42px;'>"
                        f"{product.get('icon','🌿')}</div>",
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"**{product['name']}**"
                )
                st.write(f"£{product['price']:.2f}")

                if st.button(
                    "ADD TO BASKET",
                    key="add_" + product["id"],
                    use_container_width=True
                ):
                    st.session_state.basket[product["id"]] = (
                        st.session_state.basket.get(product["id"], 0) + 1
                    )
                    st.rerun()


# ==========================================
# SECTION 2: SHOP BY CATEGORY
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:30px 10px;">
    <p style="color:#B49A65; letter-spacing:4px; font-size:12px;">
        FIND YOUR FAVOURITES
    </p>
    <h2 style="font-family:Georgia,serif; font-size:38px;">
        Shop by Category
    </h2>
</div>
""", unsafe_allow_html=True)

cat1, cat2, cat3 = st.columns(3)

with cat1:
    st.markdown("## 🌸")
    st.subheader("Skincare")
    st.write("Cleansers, creams and serums.")

with cat2:
    st.markdown("## 🌿")
    st.subheader("Body Care")
    st.write("Everyday body care essentials.")

with cat3:
    st.markdown("## ✨")
    st.subheader("Hair Care")
    st.write("Simple hair care favourites.")


# ==========================================
# SECTION 3: OUR PHILOSOPHY
# ==========================================

st.markdown("---")

components.html("""
<style>
    .story {
        background:#26372D;
        color:#F7F4ED;
        text-align:center;
        padding:65px 25px;
        animation: rise 1s ease-out;
    }

    .story h2 {
        color:#F7F4ED;
        font-family:Georgia,serif;
        font-size:36px;
        font-weight:normal;
    }

    .story p {
        color:#F7F4ED;
        font-size:17px;
        line-height:1.8;
    }

    @keyframes rise {
        from {opacity:0; transform:translateY(30px);}
        to {opacity:1; transform:translateY(0);}
    }
</style>

<div class="story">
    <p style="color:#C5A66A; letter-spacing:4px;">
        OUR PHILOSOPHY
    </p>
    <h2>Less, but More Meaningful</h2>
    <p>
        Beauty is found in the little things.<br>
        Make space for simple rituals and moments of care.
    </p>
</div>
""", height=260)


# ==========================================
# SECTION 4: WHY CHOOSE US
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:30px 10px;">
    <p style="color:#B49A65; letter-spacing:4px; font-size:12px;">
        THE EARTH & BLOOM EXPERIENCE
    </p>
    <h2 style="font-family:Georgia,serif; font-size:38px;">
        The Little Details Matter
    </h2>
</div>
""", unsafe_allow_html=True)

benefit1, benefit2, benefit3 = st.columns(3)

with benefit1:
    st.markdown("## ♡")
    st.subheader("Thoughtful Choices")
    st.write("A considered collection of beauty essentials.")

with benefit2:
    st.markdown("## ✧")
    st.subheader("Everyday Rituals")
    st.write("Make a little time for your daily self-care.")

with benefit3:
    st.markdown("## 🌿")
    st.subheader("Inspired by Nature")
    st.write("A natural-inspired look and feel throughout our store.")


# ==========================================
# SHOPPING BASKET
# ==========================================

st.markdown("---")
st.header("Your Shopping Basket")

total = 0
item_count = 0

for product in products:
    quantity = st.session_state.basket.get(product["id"], 0)

    if quantity > 0:
        subtotal = quantity * product["price"]
        total += subtotal
        item_count += quantity

        st.write(
            f"{product['name']} × {quantity} — £{subtotal:.2f}"
        )

if item_count == 0:
    st.write("Your basket is currently empty.")

st.subheader(f"Basket total: £{total:.2f}")

if item_count > 0:
    if st.button("CLEAR BASKET"):
        st.session_state.basket = {}
        st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:45px 10px;">
    <h2 style="font-family:Georgia,serif;">🌿 EARTH & BLOOM</h2>
    <p style="color:#B49A65; letter-spacing:4px;">
        FEEL GOOD. NATURALLY.
    </p>
    <p>Beauty inspired by nature.</p>
    <p style="font-size:12px;">
        © 2026 EARTH & BLOOM
    </p>
</div>
""", unsafe_allow_html=True)

