import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Doctor AI", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(135deg, #f0f4f8, #d9e4f5);
        background-image: url('assets/doctor ai.png'); /* Add your image URL here */
        background-size: cover;
        background-position: center;
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
    
    /* Hero section styling */
    .hero {
        position: relative;
        height: 400px;
        background-image: url('assets/doctor ai.png'); /* Updated to your image path */
        background-size: cover;
        background-position: center;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
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

# Placeholder for API keys and sensitive data
api_key = st.secrets["api_key"]

# Function to simulate a chatbot response
def chatbot_response(query):
    if 'fever' in query.lower():
        return "It seems you have a fever. It's recommended to stay hydrated, rest, and monitor your temperature. If it persists, consult a doctor."
    elif 'headache' in query.lower():
        return "For headaches, try to relax in a quiet, dark room. Over-the-counter pain relievers may help. Persistent headaches should be evaluated by a doctor."
    elif 'cold' in query.lower():
        return "Common cold symptoms usually resolve within a week. Rest, fluids, and over-the-counter cold remedies can ease symptoms."
    else:
        return "I'm here to assist with basic symptoms. For specific medical advice, please consult a healthcare professional."

# Load custom CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
load_css('assets/styles.css')  # Ensure you have a 'styles.css' file in the 'assets' folder

# Custom Navbar
st.markdown("""
    <nav class="navbar">
    <h3>
        <a class="nav-link" href="#home">Home |</a>
        <a class="nav-link" href="#about">About Us |</a>
        <a class="nav-link" href="#services">Services |</a>
        <a class="nav-link" href="#contact">Contact |</a>
        <a class="nav-link" href="#blog">Health Blog |</a>
        <a class="nav-link" href="#client">Client Interface |</a>
        <a class="nav-link" href="#admin">Admin Panel |</a>
        <a class="nav-link" href="#chatbot">Chatbot |</a>
        <a class="nav-link" href="#new-doctors">New Doctor Profiles |</a>
        <a class="nav-link" href="#admin-management">Admin Management</a>
    </nav></h3>
""", unsafe_allow_html=True)

# Hero Section
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

# Sections
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
st.header("Welcome to HealthCare Center")
st.write("""At Doctor AI, we leverage state-of-the-art technology to revolutionize healthcare services, offering solutions that are specifically tailored to your unique needs. Our platform integrates cutting-edge AI tools with the expertise of seasoned medical professionals to deliver a comprehensive and personalized health experience.

Our mission is to enhance the quality and accessibility of healthcare by providing intelligent, data-driven insights and solutions. Whether you're seeking general consultations, specialist care, or emergency services, our technology ensures that you receive accurate and timely support.

Our team of healthcare experts is dedicated to guiding you through every step of your health journey. From virtual consultations to real-time health monitoring, we are here to ensure that you have access to the best possible care, no matter where you are.

By combining innovative AI capabilities with compassionate medical guidance, Doctor AI is committed to making healthcare more efficient, accessible, and personalized. Trust us to be your partner in achieving better health and wellness.""")

st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.header("About Us")
st.write("""Doctor AI stands at the cutting edge of digital health innovation, merging advanced artificial intelligence technology with the expertise of highly skilled medical professionals to offer unparalleled healthcare services. We are dedicated to transforming the healthcare experience by harnessing the power of AI to provide exceptional care that is both efficient and personalized.

Our core mission is to revolutionize healthcare accessibility and quality by integrating sophisticated AI solutions with the compassionate touch of experienced clinicians. We believe that every individual deserves healthcare that is tailored to their unique needs and preferences. By leveraging AI, we aim to streamline processes, enhance diagnostic accuracy, and deliver insights that empower patients to make informed decisions about their health.

Doctor AI is committed to breaking down barriers to healthcare, making it more accessible and effective for everyone. Our platform offers a seamless blend of technology and human touch, ensuring that every patient receives timely, relevant, and personalized care. Whether you're seeking routine check-ups, specialist consultations, or emergency services, our advanced AI tools and dedicated medical professionals work together to provide a holistic and efficient healthcare experience.

At Doctor AI, we are passionate about using innovation to improve health outcomes and make quality care more attainable for all. Join us on our journey to redefine healthcare with the perfect balance of technology and human expertise.""")

st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.header("Our Services")
st.write("""We offer a comprehensive range of medical services to meet the diverse needs of our patients:""")
st.markdown("""
    <div class="card-container">
        <div class="card">
            <h3>General Consultations</h3>
            <p>Our experienced physicians provide consultations for a wide variety of health concerns, offering expert advice and treatment plans.</p>
        </div>
        <div class="card">
            <h3>Specialist Care</h3>
            <p>Access to specialized medical care from top specialists in various fields, ensuring you get the expertise you need for specific health issues.</p>
        </div>
        <div class="card">
            <h3>Emergency Services</h3>
            <p>Quick and efficient emergency care, available 24/7 to handle urgent medical situations with the utmost urgency and expertise.</p>
        </div>
        <div class="card">
            <h3>Virtual Consultations</h3>
            <p>Connect with healthcare professionals from the comfort of your home through our secure and convenient virtual consultation platform.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.header("Contact Us")
st.write("""For inquiries, support, or further information, feel free to reach out to us through the following channels:""")
st.markdown("""
    <div class="contact-info">
        <p><strong>Email:</strong> support@doctorai.com</p>
        <p><strong>Phone:</strong> +1 (555) 123-4567</p>
        <p><strong>Address:</strong> 123 Health St, Suite 100, Wellness City, HC 12345</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.header("Health Blog")
st.write("""Stay updated with the latest in health and wellness through our blog, featuring expert articles, tips, and news on various health topics.""")

st.markdown("<div id='client'></div>", unsafe_allow_html=True)
st.header("Client Interface")
st.write("""Our client interface allows you to manage your health records, schedule appointments, and access personalized health insights and recommendations.""")

st.markdown("<div id='admin'></div>", unsafe_allow_html=True)
st.header("Admin Panel")
st.write("""The admin panel provides tools for managing doctor profiles, overseeing client interactions, and monitoring platform performance.""")

st.markdown("<div id='chatbot'></div>", unsafe_allow_html=True)
st.header("Chatbot")
st.write("""Our AI-powered chatbot is available to provide quick responses to your health-related queries and guide you through common medical concerns.""")

st.markdown("<div id='new-doctors'></div>", unsafe_allow_html=True)
st.header("New Doctor Profiles")
st.write("""New doctors can create their profiles and get listed on our platform, allowing them to connect with patients and showcase their expertise.""")

st.markdown("<div id='admin-management'></div>", unsafe_allow_html=True)
st.header("Admin Management")
st.write("""Our admin management tools allow for efficient administration of doctor profiles, client interactions, and overall platform functionality.""")

# Footer
st.markdown("""
    <footer>
        <p>Developed By: Irfan Ullah Khan</p>
        <p><a href="https://flowcv.me/ikm">https://flowcv.me/ikm</a></p>
        <p>Developed For: Essential Generative AI Training</p>
        <p>Conducted By: PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN</p>
    </footer>
""", unsafe_allow_html=True)
