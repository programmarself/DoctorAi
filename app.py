import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px

st.set_page_config(page_title="Doctor AI", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(135deg, #f0f4f8, #d9e4f5);
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
        height: 500px;
        background-image: url('https://via.placeholder.com/1920x500');
        background-size: cover;
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

# Hero Section
st.markdown("""
    <div class="hero">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>Welcome to Doctor AI</h1>
            <p>Your Health, Our Priority</p>
            <a href="#services" class="cta-btn">Explore Our Services</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Example Card Section
st.markdown("""
    <div class="card-container">
        <div class="glass-card">
            <h3>Consultation</h3>
            <p>Get expert advice from our team of specialists.</p>
        </div>
        <div class="glass-card">
            <h3>Emergency Services</h3>
            <p>Our emergency team is available 24/7 to assist you.</p>
        </div>
        <div class="glass-card">
            <h3>Health Checkups</h3>
            <p>Regular health checkups to keep you in the best shape.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Placeholder for actual services implementation
st.header("Our Services")
st.write("Explore the wide range of healthcare services we offer to cater to your needs.")

# Footer
st.markdown("""
    <footer>
        <p>Developed by <a href="#">Irfan Ullah Khan</a></p>
        <p>&copy; 2024 Doctor AI. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
