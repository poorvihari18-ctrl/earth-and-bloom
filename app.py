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

st.markdown('<div id="basket"></div>', unsafe_allow_html=True)
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

st.markdown('<div id="contact"></div><div id="journal"></div><div id="account"></div>', unsafe_allow_html=True)
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

