
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

