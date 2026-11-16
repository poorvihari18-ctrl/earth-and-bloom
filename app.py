
import streamlit as st
import os
import streamlit.components.v1 as components
# ==========================================
# EARTH & BLOOM - LUXURY BEAUTY STORE
# ==========================================

st.set_page_config(
    page_title="EARTH & BLOOM | Feel Good Naturally",
    page_icon="🌿",
    layout="wide"
)

# ==========================================
# WEBSITE DESIGN AND ANIMATIONS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@400;500;600;700&display=swap');

.stApp {
    background: #F7F4ED;
    color: #26372D;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, serif !important;
    color: #26372D !important;
}

p, label {
    color: #55564E;
}

/* Smooth scrolling */

html {
    scroll-behavior: smooth;
}

/* Upward entrance animation */

@keyframes riseIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Brand */

.brand-title {
    text-align: center;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(36px, 6vw, 76px);
    font-weight: 600;
    letter-spacing: 3px;
    color: #26372D;
    margin-top: 15px;
}

.brand-slogan {
    text-align: center;
    color: #B49A65;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 16px;
    letter-spacing: 5px;
    margin-bottom: 25px;
}

/* Navigation */

.eb-nav {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 38px;
    padding: 22px 10px;
    margin: 20px 0;
    border-top: 1px solid #DED8CC;
    border-bottom: 1px solid #DED8CC;
}

.eb-nav a {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    text-decoration: none !important;
    color: #26372D !important;
    font-size: 10px;
    letter-spacing: 2px;
    transition: all 0.3s ease;
}

.eb-nav a:hover {
    color: #B49A65 !important;
    transform: translateY(-5px);
}

.eb-nav svg {
    width: 21px;
    height: 21px;
    stroke: #26372D;
    fill: none;
    stroke-width: 1.4;
}

/* Hero banner */

.hero {
    background: #26372D;
    color: #F7F4ED;
    text-align: center;
    padding: 95px 25px;
    margin: 45px 0;
    animation: riseIn 1s ease both;
}

.hero-label {
    color: #C5A66A;
    font-size: 12px;
    letter-spacing: 6px;
    margin-bottom: 25px;
}

.hero h1 {
    color: #F7F4ED !important;
    font-family: 'Playfair Display', Georgia, serif !important;
    font-size: clamp(38px, 5vw, 68px) !important;
    font-weight: 400 !important;
    line-height: 1.2;
}

.hero-description {
    color: #F7F4ED;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 20px;
    font-style: italic;
    line-height: 1.8;
}

.hero-footer {
    color: #C5A66A;
    font-size: 12px;
    letter-spacing: 5px;
    margin-top: 30px;
}

/* Section headings */

.section-label {
    color: #B49A65;
    font-size: 12px;
    letter-spacing: 4px;
    text-align: center;
    margin-top: 35px;
}

.section-title {
    text-align: center;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 38px;
    color: #26372D;
    margin-bottom: 10px;
}

.section-description {
    text-align: center;
    margin-bottom: 35px;
}

/* Small icons */

.icon-box {
    text-align: center;
    padding: 20px 5px;
}

.icon-box .icon {
    font-size: 30px;
}

.icon-box p {
    color: #26372D;
    font-size: 11px;
    letter-spacing: 2px;
}

/* Product cards */

.product-placeholder {
    background: #EAE5DA;
    min-height: 190px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 55px;
    text-align: center;
}

.product-name {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 21px;
    font-weight: 600;
    color: #26372D;
    min-height: 55px;
    margin-top: 15px;
}

.product-description {
    font-size: 13px;
    min-height: 40px;
}

.product-price {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 20px;
    color: #26372D;
    margin: 12px 0;
}

/* Product hover movement */

[data-testid="stVerticalBlockBorderWrapper"] {
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(38, 55, 45, 0.10);
}

[data-testid="stImage"] img {
    transition: transform 0.5s ease;
}

[data-testid="stImage"] img:hover {
    transform: scale(1.03);
}

/* Buttons */

.stButton button {
    background: #26372D;
    color: white !important;
    border: 1px solid #26372D;
    border-radius: 0;
    min-height: 43px;
    width: 100%;
    transition: all 0.3s ease;
}

.stButton button:hover {
    background: #B49A65;
    border-color: #B49A65;
    color: white !important;
    transform: translateY(-3px);
}

/* Philosophy banner */

.philosophy {
    background: #26372D;
    color: #F7F4ED;
    padding: 65px 25px;
    text-align: center;
    margin: 55px 0;
}

.philosophy h2 {
    color: #F7F4ED !important;
}

/* Footer */

.footer {
    background: #26372D;
    color: #F7F4ED;
    padding: 40px 15px;
    text-align: center;
    margin-top: 60px;
}

.footer p {
    color: #F7F4ED;
}

/* Scroll reveal where supported */

@supports (animation-timeline: view()) {
    .reveal-section {
        animation: riseIn 0.8s ease both;
        animation-timeline: view();
        animation-range: entry 0% entry 35%;
    }
}

/* Mobile design */

@media (max-width: 600px) {
    .hero {
        padding: 60px 15px;
    }

    .brand-slogan {
        letter-spacing: 3px;
    }

    .eb-nav {
        gap: 20px;
    }
}

/* Reduced motion accessibility */

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation: none !important;
        transition: none !important;
        scroll-behavior: auto !important;
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
# PRODUCT COLLECTIONS - 17 PRODUCTS
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
        "description": "A gentle everyday moisturising essential."
    },
    {
        "id": "toner",
        "name": "Rose Water Toner",
        "price": 8.99,
        "category": "Skincare",
        "image": "Screenshot 2026-11-14 141325.jpg",
        "icon": "🌸",
        "description": "A refreshing addition to your skincare ritual."
    },
    {
        "id": "shea",
        "name": "Shea Butter Moisturiser",
        "price": 10.99,
        "category": "Skincare",
        "image": "Screenshot 2026-11-14 141349.jpg",
        "icon": "🌼",
        "description": "A rich moisturiser for daily care."
    },
    {
        "id": "cleanser",
        "name": "Gentle Facial Cleanser",
        "price": 11.99,
        "category": "Skincare",
        "image": "Screenshot 2026-11-16 115817.png",
        "icon": "🫧",
        "description": "A simple first step in your skincare routine."
    },
    {
        "id": "serum",
        "name": "Vitamin C Face Serum",
        "price": 16.99,
        "category": "Skincare",
        "image": "Screenshot 2026-11-16 115923.png",
        "icon": "✨",
        "description": "A bright addition to your daily routine."
    },

    # BODY CARE - 5 PRODUCTS

    {
        "id": "bodywash",
        "name": "Botanical Body Wash",
        "price": 9.99,
        "category": "Body Care",
        "image": None,
        "icon": "🌿",
        "description": "A refreshing everyday body wash."
    },
    {
        "id": "bodyscrub",
        "name": "Rose Body Scrub",
        "price": 12.99,
        "category": "Body Care",
        "image": None,
        "icon": "🌹",
        "description": "A lovely addition to your body-care ritual."
    },
    {
        "id": "bodylotion",
        "name": "Nourishing Body Lotion",
        "price": 13.99,
        "category": "Body Care",
        "image": None,
        "icon": "🌼",
        "description": "A daily moisturising essential."
    },
    {
        "id": "handcream",
        "name": "Soft Hands Hand Cream",
        "price": 6.99,
        "category": "Body Care",
        "image": None,
        "icon": "🤍",
        "description": "A little everyday care for your hands."
    },
    {
        "id": "bodybutter",
        "name": "Cocoa Body Butter",
        "price": 14.99,
        "category": "Body Care",
        "image": None,
        "icon": "🥥",
        "description": "A rich body-care treat."
    },

    # HAIR CARE - 5 PRODUCTS

    {
        "id": "shampoo",
        "name": "Botanical Shampoo",
        "price": 10.99,
        "category": "Hair Care",
        "image": None,
        "icon": "🌿",
        "description": "An everyday hair-care essential."
    },
    {
        "id": "conditioner",
        "name": "Nourishing Conditioner",
        "price": 11.99,
        "category": "Hair Care",
        "image": None,
        "icon": "🌸",
        "description": "A soft finishing step after shampoo."
    },
    {
        "id": "hairmask",
        "name": "Repair Hair Mask",
        "price": 15.99,
        "category": "Hair Care",
        "image": None,
        "icon": "🥑",
        "description": "A little extra care for your hair."
    },
    {
        "id": "hairserum",
        "name": "Silky Hair Serum",
        "price": 12.99,
        "category": "Hair Care",
        "image": None,
        "icon": "💧",
        "description": "A lightweight finishing touch for your hair."
    },
    {
        "id": "hairoil",
        "name": "Botanical Hair Oil",
        "price": 13.99,
        "category": "Hair Care",
        "image": None,
        "icon": "🌿",
        "description": "An addition to your hair-care ritual."
    },

    # WELLNESS - 2 PRODUCTS

    {
        "id": "teas",
        "name": "Botanical Herbal Tea",
        "price": 7.99,
        "category": "Wellness",
        "image": None,
        "icon": "🍵",
        "description": "A comforting tea-time moment."
    },
    {
        "id": "candle",
        "name": "Natural Scented Candle",
        "price": 15.99,
        "category": "Wellness",
        "image": None,
        "icon": "🕯️",
        "description": "Create a peaceful atmosphere at home."
    }

]


# ==========================================
# WEBSITE HEADER
# ==========================================

st.markdown(
    '<div class="brand-title">🌿 EARTH & BLOOM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="brand-slogan">FEEL GOOD. NATURALLY.</div>',
    unsafe_allow_html=True
)


# ==========================================
# LUXURY NAVIGATION ICONS
# ==========================================

basket_count = sum(st.session_state.basket.values())

st.markdown("""
<div class="eb-nav">

<a href="#skincare">
<svg viewBox="0 0 24 24">
<path d="M12 22V11M12 15C4 15 4 7 4 7s8-1 8 8M12 12c0-7 8-8 8-8s0 8-8 8"/>
</svg>
SHOP
</a>

<a href="#body-care">
<svg viewBox="0 0 24 24">
<path d="M12 2C9 7 5 11 5 15a7 7 0 0014 0c0-4-4-8-7-13z"/>
</svg>
RITUALS
</a>

<a href="#ingredients">
<svg viewBox="0 0 24 24">
<path d="M12 22V11M12 15C5 15 5 7 5 7s7-1 7 8M12 12c0-7 7-8 7-8s0 8-7 8"/>
</svg>
INGREDIENTS
</a>

<a href="#about">
<svg viewBox="0 0 24 24">
<circle cx="12" cy="8" r="4"/>
<path d="M4 21c0-5 3-8 8-8s8 3 8 8"/>
</svg>
ABOUT
</a>

<a href="#journal">
<svg viewBox="0 0 24 24">
<path d="M5 3h14v18H5zM8 7h8M8 11h8M8 15h5"/>
</svg>
JOURNAL
</a>

<a href="#contact">
<svg viewBox="0 0 24 24">
<rect x="3" y="5" width="18" height="14" rx="2"/>
<path d="m3 7 9 7 9-7"/>
</svg>
CONTACT
</a>

<a href="#basket">
<svg viewBox="0 0 24 24">
<path d="M5 8h14l1 13H4L5 8z"/>
<path d="M9 9V6a3 3 0 016 0v3"/>
</svg>
BAG """ + str(basket_count) + """
</a>

</div>
""", unsafe_allow_html=True)

st.divider()



# ==========================================
# HERO BANNER
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
    background: #F7F4ED;
    font-family: 'DM Sans', Arial, sans-serif;
}

.hero {
    background: #26372D;
    color: #F7F4ED;
    text-align: center;
    padding: 75px 20px;
    min-height: 390px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    animation: riseIn 1s ease both;
}

@keyframes riseIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-label {
    color: #C5A66A;
    font-size: 12px;
    letter-spacing: 6px;
    margin-bottom: 25px;
}

.hero h1 {
    color: #F7F4ED;
    font-family: Georgia, serif;
    font-size: clamp(38px, 5vw, 68px);
    font-weight: normal;
    line-height: 1.2;
    margin: 0 0 22px;
}

.hero-description {
    color: #F7F4ED;
    font-family: Georgia, serif;
    font-size: 19px;
    font-style: italic;
    line-height: 1.8;
}

.hero-footer {
    color: #C5A66A;
    font-size: 12px;
    letter-spacing: 5px;
    margin-top: 25px;
}

@media (max-width: 600px) {
    .hero {
        padding: 60px 15px;
    }
}
</style>
</head>
<body>
    <div class="hero">
        <div class="hero-label">
            THE NATURAL BEAUTY COLLECTION
        </div>

        <h1>Discover the Beauty<br>of Nature</h1>

        <div class="hero-description">
            Thoughtfully inspired skincare.<br>
            A little luxury in every ritual.
        </div>

        <div class="hero-footer">
            FEEL GOOD. NATURALLY.
        </div>
    </div>
</body>
</html>
""", height=420, scrolling=False)



# ==========================================
# STORE VALUES / SMALL ICONS
# ==========================================

icon1, icon2, icon3, icon4 = st.columns(4)

with icon1:
    st.markdown("""
    <div class="icon-box">
        <div class="icon">🌿</div>
        <p>BOTANICAL BEAUTY</p>
    </div>
    """, unsafe_allow_html=True)

with icon2:
    st.markdown("""
    <div class="icon-box">
        <div class="icon">💧</div>
        <p>DAILY HYDRATION</p>
    </div>
    """, unsafe_allow_html=True)

with icon3:
    st.markdown("""
    <div class="icon-box">
        <div class="icon">🌸</div>
        <p>GENTLE CARE</p>
    </div>
    """, unsafe_allow_html=True)

with icon4:
    st.markdown("""
    <div class="icon-box">
        <div class="icon">✨</div>
        <p>BEAUTY RITUALS</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# INTRODUCTION
# ==========================================

st.divider()

st.markdown("""
<div class="reveal-section">

<p class="section-label">A LITTLE MOMENT FOR YOURSELF</p>

<h2 class="section-title">
Beauty in Every Ritual
</h2>

<p class="section-description">
Thoughtful essentials for your everyday beauty routine.
</p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# PRODUCT DISPLAY FUNCTION
# ==========================================

def show_collection(category, anchor, label, title, description):

    st.markdown(
        f'<div id="{anchor}" class="reveal-section"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<p class="section-label">{label}</p>'
        f'<h2 class="section-title">{title}</h2>'
        f'<p class="section-description">{description}</p>',
        unsafe_allow_html=True
    )

    collection = [
        product for product in products
        if product["category"] == category
    ]

    columns = st.columns(3)

    for index, product in enumerate(collection):

        with columns[index % 3]:

            with st.container(border=True):

                image_path = product["image"]

                if image_path and os.path.isfile(image_path):

                    st.image(
                        image_path,
                        use_container_width=True
                    )

                else:

                    st.markdown(
                        f'<div class="product-placeholder">'
                        f'{product["icon"]}</div>',
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f'<div class="product-name">{product["name"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="product-description">'
                    f'{product["description"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="product-price">£{product["price"]:.2f}</div>',
                    unsafe_allow_html=True
                )

                if st.button(
                    "ADD TO BASKET",
                    key="add_" + product["id"],
                    use_container_width=True
                ):

                    product_id = product["id"]

                    st.session_state.basket[product_id] = (
                        st.session_state.basket.get(product_id, 0) + 1
                    )

                    st.rerun()


# ==========================================
# FOUR PRODUCT COLLECTIONS
# ==========================================

show_collection(
    "Skincare",
    "skincare",
    "THE SKINCARE EDIT",
    "Everyday Skincare",
    "Thoughtful essentials for your daily beauty routine."
)

st.divider()

show_collection(
    "Body Care",
    "body-care",
    "A LITTLE BODY CARE",
    "Body Care Collection",
    "Make everyday care feel like a special ritual."
)

st.divider()

show_collection(
    "Hair Care",
    "hair-care",
    "NATURE FOR YOUR HAIR",
    "Hair Care Collection",
    "Discover little essentials for your hair-care routine."
)

st.divider()

show_collection(
    "Wellness",
    "wellness",
    "SLOW DOWN AND UNWIND",
    "Wellness Collection",
    "Thoughtful little moments for your everyday wellbeing."
)


# ==========================================
# SHOPPING BASKET
# ==========================================

st.markdown(
    '<div id="basket"></div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown("""
<p class="section-label">YOUR SELECTED FAVOURITES</p>
<h2 class="section-title">Your Shopping Basket</h2>
""", unsafe_allow_html=True)

if st.session_state.basket:

    total = 0

    for product_id, quantity in list(st.session_state.basket.items()):

        product = next(
            item for item in products
            if item["id"] == product_id
        )

        item_total = product["price"] * quantity
        total += item_total

        left, middle, right = st.columns([4, 1, 1])

        with left:
            st.write(product["name"])

        with middle:
            st.write(f"Quantity: {quantity}")

        with right:
            st.write(f"£{item_total:.2f}")

            if st.button("REMOVE", key="remove_" + product_id):
                del st.session_state.basket[product_id]
                st.rerun()

    st.divider()

    st.markdown(
        f"<h3 style='text-align:right;'>TOTAL: £{total:.2f}</h3>",
        unsafe_allow_html=True
    )

    if st.button("CLEAR BASKET"):
        st.session_state.basket = {}
        st.rerun()

else:
    st.info("Your basket is currently empty. Explore our collections!")



# ==========================================
# ABOUT OUR BRAND
# ==========================================

st.markdown(
    '<div id="about"></div>',
    unsafe_allow_html=True
)

components.html("""
<div style="
    background:#26372D;
    color:#F7F4ED;
    width:100%;
    min-height:320px;
    padding:55px 25px;
    margin:0;
    box-sizing:border-box;
    text-align:center;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
">

    <p style="
        color:#C5A66A;
        letter-spacing:5px;
        font-size:12px;
        margin:0 0 25px 0;
    ">
        OUR PHILOSOPHY
    </p>

    <h2 style="
        color:#F7F4ED;
        font-family:Georgia,serif;
        font-size:38px;
        margin:0 0 25px 0;
    ">
        Less, but More Meaningful
    </h2>

    <p style="
        color:#F7F4ED;
        font-size:17px;
        line-height:1.8;
        margin:0;
    ">
        Beauty is found in the little things.<br>
        Make space for simple rituals and moments of care.
    </p>

</div>
""", height=380, scrolling=False)


# ==========================================
# INGREDIENTS SECTION
# ==========================================

st.markdown(
    '<div id="ingredients"></div>',
    unsafe_allow_html=True
)

st.markdown("""
<p class="section-label">INSPIRED BY NATURE</p>

<h2 class="section-title">
A Closer Look at Ingredients
</h2>

<p class="section-description">
Discover the ingredients and details behind your everyday beauty favourites.
</p>
""", unsafe_allow_html=True)

a, b, c = st.columns(3)

with a:
    st.markdown("### 🌿 Botanical Inspiration")
    st.write("Explore nature-inspired beauty essentials.")

with b:
    st.markdown("### 🌹 Floral Touches")
    st.write("Discover lovely floral-inspired rituals.")

with c:
    st.markdown("### 🥥 Everyday Care")
    st.write("Find thoughtful additions to your routine.")


# ==========================================
# JOURNAL SECTION
# ==========================================

st.markdown(
    '<div id="journal"></div>',
    unsafe_allow_html=True
)

st.markdown("""
<p class="section-label">NOTES FROM EARTH & BLOOM</p>

<h2 class="section-title">
The Beauty Journal
</h2>

<p class="section-description">
Little ideas for making time for yourself.
</p>
""", unsafe_allow_html=True)

j1, j2, j3 = st.columns(3)

with j1:
    st.markdown("### 🌸 Simple Skincare Rituals")
    st.write("A little time for your everyday skincare routine.")

with j2:
    st.markdown("### 🌿 Finding Your Favourites")
    st.write("Explore the products that suit your personal routine.")

with j3:
    st.markdown("### ✨ Everyday Moments")
    st.write("Make space for small moments of self-care.")


# ==========================================
# CONTACT SECTION
# ==========================================

st.markdown(
    '<div id="contact"></div>',
    unsafe_allow_html=True
)

st.markdown("""
<p class="section-label">WE WOULD LOVE TO HEAR FROM YOU</p>

<h2 class="section-title">
Contact EARTH & BLOOM
</h2>

<p class="section-description">
Thank you for visiting our little beauty world.
</p>
""", unsafe_allow_html=True)

with st.form("contact_form"):

    customer_name = st.text_input("Your name")
    customer_email = st.text_input("Your email")
    customer_message = st.text_area("Your message")

    submitted = st.form_submit_button("SEND MESSAGE")

    if submitted:

        if customer_name and customer_email and customer_message:

            st.success("Thank you! Your message has been entered.")

        else:

            st.warning("Please complete all three fields.")




# ==========================================
# FOOTER
# ==========================================

components.html("""
<div style="
    background:#26372D;
    color:#F7F4ED;
    width:100%;
    min-height:260px;
    padding:40px 20px;
    box-sizing:border-box;
    text-align:center;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
">

    <h2 style="
        color:#F7F4ED;
        font-family:Georgia,serif;
        font-size:32px;
        margin:0 0 15px 0;
    ">
        🌿 EARTH & BLOOM
    </h2>

    <p style="
        color:#C5A66A;
        letter-spacing:4px;
        font-size:13px;
        margin:0 0 18px 0;
    ">
        FEEL GOOD. NATURALLY.
    </p>

    <p style="
        color:#F7F4ED;
        font-size:15px;
        margin:0 0 18px 0;
    ">
        Beauty inspired by nature.
    </p>

    <p style="
        color:#F7F4ED;
        font-size:12px;
        margin:0;
    ">
        © 2026 EARTH & BLOOM
    </p>

</div>
""", height=280, scrolling=False)
