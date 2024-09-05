import streamlit as st
from PIL import Image
import os

# Set the page configuration
st.set_page_config(page_title="Doctor AI", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for enhanced styling with background image
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(135deg, #f0f4f8, #d9e4f5);
        background-image: url('assets/doctor ai.png'); /* Ensure image is in the correct path */
        background-size: auto 100%; /* Adjusted for the image size 1500x400 */
        background-position: center top; /* Ensures the image is centered horizontally */
        background-attachment: fixed;
        background-repeat: no-repeat;
        color: #2c3e50;
    }
    
    .stButton>button {
        background-color: #3498db;
        color: white;
        padding: 15px 25px;
        font-size: 16px;
        border-radius: 50px;
        transition: background-color 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
    }
    
    .hero {
        height: 400px;  /* Adjust the height for the image */
        background-image: url('assets/doctor ai.png');  /* Same image used in hero section */
        background-size: auto 100%; /* Adjust to fit the hero section properly */
        background-position: center;
        position: relative;
        border-radius: 15px;
        margin-bottom: 30px;
    }

    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
        border-radius: 15px;
    }

    .hero-content {
        position: relative;
        color: white;
        text-align: center;
        top: 50%;
        transform: translateY(-50%);
    }

    .hero-content h1 {
        font-size: 60px;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .hero-content p {
        font-size: 24px;
        margin-bottom: 30px;
    }

    .hero-content .cta-btn {
        background-color: #e74c3c;
        color: white;
        padding: 15px 30px;
        font-size: 18px;
        border-radius: 50px;
        text-decoration: none;
    }

    .hero-content .cta-btn:hover {
        background-color: #c0392b;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    .stSelectbox>div>div {
        background-color: white;
        border-radius: 50px;
        padding: 10px;
    }

    .stTextInput>div>div>input {
        border-radius: 50px;
        padding: 10px;
    }

    footer {
        background-color: #34495e;
        color: white;
        padding: 20px 0;
        text-align: center;
        border-radius: 0 0 10px 10px;
    }

    footer a {
        color: #1abc9c;
        text-decoration: none;
    }

    footer a:hover {
        text-decoration: underline;
    }

    </style>
    """, unsafe_allow_html=True)

# Check if image exists
if os.path.exists('assets/doctor ai.png'):
    st.write("Background image loaded successfully.")
else:
    st.error("Error: Background image not found. Please check the image path.")

# Placeholder for API keys and sensitive data (if any)
api_key = st.secrets["api_key"] if "api_key" in st.secrets else "API_KEY_PLACEHOLDER"

# Hero Section with Call to Action
st.markdown("""
    <section class="hero">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>Doctor AI - Your Health, Our Priority</h1>
            <p>Providing top-notch healthcare services with AI-driven solutions.</p>
            <a class="cta-btn" href="#services">Explore Our Services</a>
        </div>
    </section>
""", unsafe_allow_html=True)

# Section for displaying services (example)
st.markdown("""
    ## Our Services
    ### AI-Driven Diagnostics
    Get personalized diagnostic insights powered by our advanced AI algorithms.
    """)
  
# Additional glass card section for service description or doctor profiles
st.markdown("""
    <div class="glass-card">
        <h3>Why Choose Doctor AI?</h3>
        <p>Our platform offers state-of-the-art AI-powered medical diagnostics, tailored to meet your healthcare needs. With real-time health insights and 24/7 online consultations, Doctor AI ensures you get the care you deserve.</p>
    </div>
""", unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <footer>
        <p>Developed By: Irfan Ullah Khan</p>
        <p><a href="https://flowcv.me/ikm" target="_blank">https://flowcv.me/ikm</a></p>
        <p>Developed For: Essential Generative AI Training</p>
        <p>Conducted By: PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN</p>
    </footer>
""", unsafe_allow_html=True)
