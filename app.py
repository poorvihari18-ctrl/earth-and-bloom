
import streamlit as st
import os

# ==========================================
# EARTH & BLOOM
# LUXURY BEAUTY AND WELLNESS STORE
# ==========================================

st.set_page_config(
    page_title="EARTH & BLOOM | Feel Good Naturally",
    page_icon="🌿",
    layout="wide"
)

# ==========================================
# WEBSITE DESIGN
# ==========================================

st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.stApp {
    background-color: #F7F4ED;
    color: #26372D;
}

.block-container {
    max-width: 1450px;
    padding-top: 1rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: Georgia, serif !important;
    color: #26372D !important;
}

p, label {
    color: #45483F;
}

@keyframes riseIn {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero {
    background: #26372D;
    color: #F7F4ED;
    text-align: center;
    padding: 85px 25px;
    margin: 35px 0 55px 0;
    animation: riseIn 1s ease-out;
}

.hero-label {
    color: #C5A66A;
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
    color: #F7F4ED;
    font-family: Georgia, serif;
    font-size: 20px;
    font-style: italic;
    line-height: 1.8;
}

.hero-footer {
    color: #C5A66A;
    font-family: Arial, sans-serif;
    font-size: 12px;
    letter-spacing: 4px;
    margin-top: 25px;
}

.brand-name {
    text-align: center;
    font-family: Georgia, serif;
    font-size: 48px;
    font-weight: bold;
    letter-spacing: 3px;
    color: #26372D;
}

.brand-slogan {
    text-align: center;
    color: #B49A65;
    font-family: Georgia, serif;
    font-size: 16px;
    letter-spacing: 5px;
    margin-bottom: 25px;
}

.eb-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
    padding: 17px 5px;
    border-top: 1px solid #DED7CA;
    border-bottom: 1px solid #DED7CA;
}

.eb-nav a {
    color: #26372D !important;
    text-decoration: none !important;
    font-family: Arial, sans-serif;
    font-size: 11px;
    letter-spacing: 1.5px;
    margin: 0 8px;
}

.eb-nav a:hover {
    color: #B49A65 !important;
}

.eb-icons {
    font-size: 20px;
    letter-spacing: 9px;
}

.section-label {
    color: #B49A65;
    font-size: 12px;
    letter-spacing: 4px;
}

.product-name {
    font-family: Georgia, serif;
    font-size: 21px;
    font-weight: bold;
    color: #26372D;
}

.product-price {
    font-size: 18px;
    color: #45483F;
}

.stButton button {
    background-color: #26372D;
    color: white;
    border: 1px solid #26372D;
    border-radius: 0;
    padding: 12px 15px;
    width: 100%;
}

.stButton button:hover {
    background-color: #B49A65;
    color: white;
    border-color: #B49A65;
}

.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: #FFFFFF;
}

hr {
    border-color: #DED7CA;
}

@media (max-width: 700px) {
    .brand-name {
        font-size: 30px;
    }

    .hero h1 {
        font-size: 36px !important;
    }

    .hero {
        padding: 55px 15px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# BASKET SETUP
# ==========================================

if "basket" not in st.session_state:
    st.session_state.basket = {}


# ==========================================
# PRODUCT COLLECTION
# 16 PRODUCTS IN TOTAL
# ==========================================

products = [

    # SKINCARE - 5 PRODUCTS

    {
        "id": "cream",
        "name": "Aloe Vera Face Cream",
        "price": 12.99,
        "category": "Skincare",
        "image": "Screenshot 2026-11-14 141225.jpg",
        "icon": "🌿",
        "description": "A gentle skincare essential."
    },
    {
        "id": "toner",
        "name": "Rose Water Toner",
        "price": 8.99,
        "category": "Skincare",
        "image": "Screenshot 2026-11-14 141325.jpg",
        "icon": "🌸",
        "description": "A refreshing addition to your routine."
    },
    {
        "id": "shea",
        "name": "Shea Butter Moisturiser",
        "price": 10.99,
        "category": "Skincare",
        "image": "Screenshot 2026-11-14 141349.jpg",
        "icon": "🤍",
        "description": "A rich everyday moisturiser."
    },
    {
        "id": "cleanser",
        "name": "Gentle Facial Cleanser",
        "price": 11.99,
        "category": "Skincare",
        "image": None,
        "icon": "🫧",
        "description": "A simple first step in your skincare ritual."
    },
    {
        "id": "serum",
        "name": "Vitamin C Face Serum",
        "price": 16.99,
        "category": "Skincare",
        "image": None,
        "icon": "✨",
        "description": "A lightweight serum for your daily routine."
    },

    # BODY CARE - 5 PRODUCTS

    {
        "id": "bodylotion",
        "name": "Daily Body Lotion",
        "price": 12.99,
        "category": "Body Care",
        "image": None,
        "icon": "🤍",
        "description": "A comforting daily body-care essential."
    },
    {
        "id": "handcream",
        "name": "Softening Hand Cream",
        "price": 7.99,
        "category": "Body Care",
        "image": None,
        "icon": "🌷",
        "description": "A little care for hardworking hands."
    },
    {
        "id": "bodywash",
        "name": "Gentle Body Wash",
        "price": 8.99,
        "category": "Body Care",
        "image": None,
        "icon": "🛁",
        "description": "A refreshing everyday wash."
    },
    {
        "id": "bodyoil",
        "name": "Silky Body Oil",
        "price": 15.99,
        "category": "Body Care",
        "image": None,
        "icon": "💧",
        "description": "A luxurious finishing touch."
    },
    {
        "id": "bodyscrub",
        "name": "Botanical Body Scrub",
        "price": 13.99,
        "category": "Body Care",
        "image": None,
        "icon": "🌼",
        "description": "A lovely addition to your bath ritual."
    },

    # HAIR CARE - 3 PRODUCTS

    {
        "id": "shampoo",
        "name": "Botanical Shampoo",
        "price": 10.99,
        "category": "Hair Care",
        "image": None,
        "icon": "🧴",
        "description": "An everyday hair-care essential."
    },
    {
        "id": "conditioner",
        "name": "Botanical Conditioner",
        "price": 10.99,
        "category": "Hair Care",
        "image": None,
        "icon": "🌿",
        "description": "A soft finishing step for your hair."
    },
    {
        "id": "hairmask",
        "name": "Nourishing Hair Mask",
        "price": 14.99,
        "category": "Hair Care",
        "image": None,
        "icon": "🌱",
        "description": "A special treat for your hair-care routine."
    },

    # WELLNESS - 3 PRODUCTS

    {
        "id": "lipbalm",
        "name": "Nourishing Lip Balm",
        "price": 5.99,
        "category": "Wellness",
        "image": None,
        "icon": "🌸",
        "description": "A handy everyday beauty essential."
    },
    {
        "id": "sunscreen",
        "name": "Daily Face Sunscreen",
        "price": 14.99,
        "category": "Wellness",
        "image": None,
        "icon": "☀️",
        "description": "A daily sun-care essential."
    },
    {
        "id": "facemask",
        "name": "Nourishing Face Mask",
        "price": 9.99,
        "category": "Wellness",
        "image": None,
        "icon": "🧖",
        "description": "A relaxing addition to your self-care routine."
    }

]


# ==========================================
# HEADER AND BRAND
# ==========================================

st.markdown("""
<div class="brand-name">🌿 EARTH & BLOOM</div>
<div class="brand-slogan">FEEL GOOD. NATURALLY.</div>
""", unsafe_allow_html=True)

basket_count = sum(st.session_state.basket.values())

st.markdown(f"""
<div class="eb-nav">
    <div>
        <a href="#shop">SHOP</a>
        <a href="#rituals">RITUALS</a>
        <a href="#ingredients">INGREDIENTS</a>
        <a href="#about">ABOUT</a>
        <a href="#journal">JOURNAL</a>
        <a href="#contact">CONTACT</a>
    </div>
    <div class="eb-icons">
        <a href="#shop" title="Search">⌕</a>
        <a href="#account" title="Account">♙</a>
        <a href="#basket" title="Basket">♧ {basket_count}</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# HERO / COVER PAGE
# ==========================================

st.markdown("""
<div class="hero">

    <div class="hero-label">
        THE NATURAL BEAUTY COLLECTION
    </div>

    <h1>
        Discover the Beauty<br>of Nature
    </h1>

    <div class="hero-description">
        Thoughtfully inspired skincare.<br>
        A little luxury in every ritual.
    </div>

    <div class="hero-footer">
        FEEL GOOD. NATURALLY.
    </div>

</div>
""", unsafe_allow_html=True)


# ==========================================
# SMALL ICONS / STORE VALUES
# ==========================================

icon1, icon2, icon3, icon4 = st.columns(4)

with icon1:
    st.markdown("<h2 style='text-align:center;'>🌿</h2>"
                "<p style='text-align:center;'>BOTANICAL BEAUTY</p>",
                unsafe_allow_html=True)

with icon2:
    st.markdown("<h2 style='text-align:center;'>💧</h2>"
                "<p style='text-align:center;'>DAILY HYDRATION</p>",
                unsafe_allow_html=True)

with icon3:
    st.markdown("<h2 style='text-align:center;'>🌸</h2>"
                "<p style='text-align:center;'>GENTLE CARE</p>",
                unsafe_allow_html=True)

with icon4:
    st.markdown("<h2 style='text-align:center;'>✨</h2>"
                "<p style='text-align:center;'>BEAUTY RITUALS</p>",
                unsafe_allow_html=True)


st.divider()


# ==========================================
# INTRODUCTION
# ==========================================

st.markdown("""
<div style="text-align:center; padding:30px 10px;">

    <p class="section-label">
        A LITTLE MOMENT FOR YOURSELF
    </p>

    <h2 style="font-size:38px;">
        Beauty in Every Ritual
    </h2>

    <p>
        Thoughtful essentials for your everyday beauty routine.
    </p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# SHOP AND PRODUCT SEARCH
# ==========================================

st.markdown('<div id="shop"></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<p class="section-label">THE EARTH & BLOOM EDIT</p>
<h2 style="font-size:38px;">Explore Our Collection</h2>
<p>Find the little essentials that make a difference.</p>
""", unsafe_allow_html=True)

search_text = st.text_input(
    "⌕ Search our collection",
    placeholder="Search for a product..."
)

selected_category = st.selectbox(
    "Choose a collection",
    ["All Products", "Skincare", "Body Care", "Hair Care", "Wellness"]
)

filtered_products = []

for product in products:

    matches_search = (
        search_text.lower() in product["name"].lower()
    )

    matches_category = (
        selected_category == "All Products"
        or product["category"] == selected_category
    )

    if matches_search and matches_category:
        filtered_products.append(product)


# ==========================================
# PRODUCT DISPLAY
# ==========================================

if not filtered_products:

    st.info("No products found. Try another search.")

else:

    for start in range(0, len(filtered_products), 4):

        product_row = filtered_products[start:start + 4]
        cols = st.columns(4, gap="large")

        for product, col in zip(product_row, cols):

            with col:

                with st.container(border=True):

                    image_path = product["image"]

                    if image_path and os.path.isfile(image_path):

                        st.image(
                            image_path,
                            use_container_width=True
                        )

                    else:

                        st.markdown(
                            f"""
                            <div style="
                                background:#EAE5DA;
                                height:180px;
                                display:flex;
                                justify-content:center;
                                align-items:center;
                                font-size:55px;
                            ">
                                {product["icon"]}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown(
                        f"<div class='product-name'>{product['name']}</div>",
                        unsafe_allow_html=True
                    )

                    st.caption(product["description"])

                    st.markdown(
                        f"<div class='product-price'>£{product['price']:.2f}</div>",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        "ADD TO BASKET",
                        key="add_" + product["id"],
                        use_container_width=True
                    ):

                        st.session_state.basket[product["id"]] = (
                            st.session_state.basket.get(
                                product["id"], 0
                            ) + 1
                        )

                        st.rerun()


# ==========================================
# SHOP BY CATEGORY
# ==========================================

st.markdown('<div id="rituals"></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="text-align:center; padding:30px 10px;">

    <p class="section-label">FIND YOUR FAVOURITES</p>

    <h2 style="font-size:38px;">Shop by Category</h2>

</div>
""", unsafe_allow_html=True)

cat1, cat2, cat3, cat4 = st.columns(4)

with cat1:
    st.markdown("<h1 style='text-align:center;'>🌸</h1>",
                unsafe_allow_html=True)
    st.subheader("Skincare")
    st.write("Cleansers, creams and serums.")

with cat2:
    st.markdown("<h1 style='text-align:center;'>🌿</h1>",
                unsafe_allow_html=True)
    st.subheader("Body Care")
    st.write("Everyday body-care essentials.")

with cat3:
    st.markdown("<h1 style='text-align:center;'>✨</h1>",
                unsafe_allow_html=True)
    st.subheader("Hair Care")
    st.write("Simple hair-care favourites.")

with cat4:
    st.markdown("<h1 style='text-align:center;'>☀️</h1>",
                unsafe_allow_html=True)
    st.subheader("Wellness")
    st.write("Little moments of self-care.")


# ==========================================
# INGREDIENTS SECTION
# ==========================================

st.markdown('<div id="ingredients"></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="text-align:center; padding:40px 15px;">

    <p class="section-label">INSPIRED BY NATURE</p>

    <h2 style="font-size:38px;">A Closer Look at Ingredients</h2>

    <p>
        Discover the ingredients and details behind your
        everyday beauty favourites.
    </p>

</div>
""", unsafe_allow_html=True)

ing1, ing2, ing3 = st.columns(3)

with ing1:
    st.markdown("## 🌿")
    st.subheader("Aloe Vera")
    st.write("A familiar botanical ingredient in skincare.")

with ing2:
    st.markdown("## 🌹")
    st.subheader("Rose Water")
    st.write("A refreshing ingredient used in beauty rituals.")

with ing3:
    st.markdown("## 🥥")
    st.subheader("Shea Butter")
    st.write("A rich ingredient often used in moisturisers.")


# ==========================================
# OUR PHILOSOPHY
# ==========================================

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="
    background:#26372D;
    color:#F7F4ED;
    text-align:center;
    padding:65px 25px;
    animation:riseIn 1s ease-out;
">

    <p style="color:#C5A66A; letter-spacing:4px;">
        OUR PHILOSOPHY
    </p>

    <h2 style="color:#F7F4ED !important; font-size:36px;">
        Less, but More Meaningful
    </h2>

    <p style="color:#F7F4ED; font-size:17px; line-height:1.8;">
        Beauty is found in the little things.<br>
        Make space for simple rituals and moments of care.
    </p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# WHY CHOOSE US
# ==========================================

st.divider()

st.markdown("""
<div style="text-align:center; padding:30px 10px;">

    <p class="section-label">THE EARTH & BLOOM EXPERIENCE</p>

    <h2 style="font-size:38px;">The Little Details Matter</h2>

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
# JOURNAL SECTION
# ==========================================

st.markdown('<div id="journal"></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="text-align:center; padding:35px 10px;">

    <p class="section-label">NOTES FROM EARTH & BLOOM</p>

    <h2 style="font-size:38px;">The Beauty Journal</h2>

    <p>Little ideas for making time for yourself.</p>

</div>
""", unsafe_allow_html=True)

journal1, journal2, journal3 = st.columns(3)

with journal1:
    st.markdown("## 🌸")
    st.subheader("Your Daily Skincare Ritual")
    st.write("Discover the joy of a simple daily routine.")

with journal2:
    st.markdown("## ☀️")
    st.subheader("A Moment of Self-Care")
    st.write("Make a little space for yourself every day.")

with journal3:
    st.markdown("## 🌿")
    st.subheader("Beauty Inspired by Nature")
    st.write("Explore the beauty of botanical inspiration.")


# ==========================================
# SHOPPING BASKET
# ==========================================

st.markdown('<div id="basket"></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<h2 style="font-size:38px;">Your Shopping Basket</h2>
""", unsafe_allow_html=True)

total = 0
item_count = 0

for product in products:

    quantity = st.session_state.basket.get(product["id"], 0)

    if quantity > 0:

        subtotal = quantity * product["price"]

        total += subtotal
        item_count += quantity

        basket_col1, basket_col2, basket_col3 = st.columns([4, 1, 2])

        with basket_col1:
            st.write(product["name"])

        with basket_col2:
            st.write(f"× {quantity}")

        with basket_col3:
            st.write(f"£{subtotal:.2f}")

if item_count == 0:

    st.write("Your basket is currently empty.")

st.divider()

st.subheader(f"Basket total: £{total:.2f}")

if item_count > 0:

    if st.button("CLEAR BASKET"):

        st.session_state.basket = {}
        st.rerun()


# ==========================================
# ACCOUNT SECTION
# ==========================================

st.markdown('<div id="account"></div>', unsafe_allow_html=True)

st.divider()

st.subheader("Your EARTH & BLOOM Account")

st.write(
    "Account registration and sign-in will be added "
    "as a future feature."
)


# ==========================================
# CONTACT SECTION
# ==========================================

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="text-align:center; padding:35px 10px;">

    <p class="section-label">WE WOULD LOVE TO HEAR FROM YOU</p>

    <h2 style="font-size:38px;">Contact EARTH & BLOOM</h2>

    <p>
        Thank you for visiting our little beauty world.
    </p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:35px 10px;">

    <h2>🌿 EARTH & BLOOM</h2>

    <p style="color:#B49A65; letter-spacing:4px;">
        FEEL GOOD. NATURALLY.
    </p>

    <p>Beauty inspired by nature.</p>

    <p style="font-size:12px;">
        © 2026 EARTH & BLOOM
    </p>

</div>
""", unsafe_allow_html=True)



