import streamlit as st
from PIL import Image
import random

# Page Configuration
st.set_page_config(page_title="Doctor AI", layout="wide", initial_sidebar_state="collapsed")

# Function to load external CSS file
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the external CSS file
load_css('assets/styles.css')

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

# Sections for the website
# Example sections
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
st.header("Welcome to HealthCare Center")
st.write("At Doctor AI, we leverage cutting-edge technology to deliver exceptional healthcare services tailored to your needs.")

# More sections can be added similar to this...
# Footer
st.markdown("""
    <footer>
        <p>Developed By: Irfan Ullah Khan</p>
        <p><a href="https://flowcv.me/ikm">https://flowcv.me/ikm</a></p>
        <p>Linkedin: https://www.linkedin.com/in/irfanullahkhanmarwat/</p>
    </footer>
""", unsafe_allow_html=True)
