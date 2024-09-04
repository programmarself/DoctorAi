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
        background-image: url('doctor_ai.png');
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

# Placeholder for API keys and sensitive data
API_KEY = 'your_api_key_here'  # Replace with your actual API key

# Function to simulate a chatbot response
def chatbot_response(query):
    if 'symptom' in query.lower():
        return "Based on your symptoms, you may need to consult a doctor for a precise diagnosis."
    elif 'medication' in query.lower():
        return "Please consult a healthcare professional for personalized medication recommendations."
    else:
        return "I'm not sure how to help with that. Please contact a doctor for more information."

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
    
        <a class="nav-link" href="#home">Home| </a>
        <a class="nav-link" href="#about">About | Us</a>
        <a class="nav-link" href="#services">Services |</a>
        <a class="nav-link" href="#contact">Contact |</a>
        <a class="nav-link" href="#blog">Health Blog |</a>
        <a class="nav-link" href="#client">Client Interface |</a>
        <a class="nav-link" href="#admin">Admin Panel |</a>
        <a class="nav-link" href="#chatbot">Chatbot |</a>
        <a class="nav-link" href="#new-doctors">New Doctor Profiles |</a>
        <a class="nav-link" href="#admin-management">Admin Management |</a>
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
st.write("Providing the best healthcare services for you and your family.")

st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.header("About Us")
st.write("We are committed to providing excellent healthcare services with a team of experienced professionals dedicated to your well-being.")

st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.header("Our Services")
st.write("We offer a range of medical services including general consultations, specialist care, emergency services, and more.")
st.markdown("""
    <div class="card-container">
        <div class="card">
            <h3>General Consultations</h3>
            <p>Our general consultations cover a wide range of health issues to provide you with the best care possible.</p>
        </div>
        <div class="card">
            <h3>Specialist Care</h3>
            <p>We have a team of specialists ready to address your specific medical needs.</p>
        </div>
        <div class="card">
            <h3>Emergency Services</h3>
            <p>We offer 24/7 emergency services to handle urgent health concerns.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.header("Contact Us")
st.write("Get in touch with us through email, phone, or visit our office.")
st.write("Email: contact@healthcare.com")
st.write("Phone: +1 234 567 890")
st.write("Address: 123 Health St, Wellness City")

st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.header("Health Blog")
st.write("Read our latest articles on health and wellness. Stay informed with expert advice and tips for a healthier lifestyle.")

st.markdown("<div id='client'></div>", unsafe_allow_html=True)
st.header("Client Interface")
st.subheader("Search for Doctors")
search_term = st.text_input("Search for doctors based on specialty, location, or availability")
if search_term:
    st.write(f"Searching for doctors with the term: {search_term}")

st.subheader("Book an Appointment")
doctor_name = st.selectbox("Select Doctor", ["Dr. Smith", "Dr. Johnson", "Dr. Lee"])  
appointment_date = st.date_input("Select Date")
appointment_time = st.time_input("Select Time")
if st.button("Book Appointment"):
    st.success(f"Appointment booked with {doctor_name} on {appointment_date} at {appointment_time}.")

st.subheader("Access Medical History and Prescriptions")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Log In"):
    st.success("Login successful. Displaying your medical history and prescriptions.")

st.subheader("Receive Notifications and Reminders")
st.write("Manage your notifications and reminders for upcoming appointments and medication.")

st.markdown("<div id='admin'></div>", unsafe_allow_html=True)
st.header("Admin Panel")
admin_action = st.selectbox("Select Action", ["Manage Doctors", "Monitor Appointments", "Handle Billing", "Update Content"])

if admin_action == "Manage Doctors":
    st.write("Add, edit, or delete doctor profiles here.")

elif admin_action == "Monitor Appointments":
    st.write("View and manage appointments.")

elif admin_action == "Handle Billing":
    st.write("Manage billing and payments.")

elif admin_action == "Update Content":
    st.write("Update website content.")

st.markdown("<div id='chatbot'></div>", unsafe_allow_html=True)
st.header("Chatbot for Medication Suggestions")
user_query = st.text_input("Ask the chatbot:")
if user_query:
    response = chatbot_response(user_query)
    st.write(f"Chatbot: {response}")

st.markdown("<div id='new-doctors'></div>", unsafe_allow_html=True)
st.header("New Doctor Profiles")
doctor_name = st.text_input("Doctor's Name")
doctor_specialty = st.text_input("Specialty")
doctor_availability = st.text_input("Availability")
doctor_fee = st.number_input("Consultation Fee")
doctor_photo = st.file_uploader("Upload Photo", type=["jpg", "png"])
doctor_bio = st.text_area("Bio")
doctor_social_media = st.text_input("Social Media Links")

if st.button("Submit Profile"):
    st.success("Doctor profile submitted for approval.")

st.markdown("<div id='admin-management'></div>", unsafe_allow_html=True)
st.header("Admin Management")
st.write("Manage doctor profiles, monitor interactions, handle disputes, and ensure compliance.")

# Footer
st.markdown("""
    <footer>
    <p>Developed By: Irfan Ullah Khan</p>
    <a href='https://flowcv.me/ikm'>https://flowcv.me/ikm</a>
    <p>Developed For: Essential Generative AI Training</p>
    <p>Conducted By: PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN</p>
    </footer>
""", unsafe_allow_html=True)

# Random Health Tip
health_tips = [
    "Drink plenty of water throughout the day.",
    "Regular exercise is key to maintaining good health.",
    "Eat a balanced diet rich in fruits and vegetables.",
    "Get at least 7-8 hours of sleep each night.",
    "Practice mindfulness and stress management techniques."
]
st.sidebar.markdown(f"**Health Tip:** {random.choice(health_tips)}")
