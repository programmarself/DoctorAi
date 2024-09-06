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
    
    .hero {
        height: 680px;
        background-image: url('assets/doctor ai.png');
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

st.markdown("""
    <style>
    body {
        background-image: url('assets/doctor ai.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
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
st.write("At Doctor AI, we leverage cutting-edge technology to deliver exceptional healthcare services tailored to your needs. Our team of experts is here to support your health journey.")

st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.header("About Us")
st.write("Doctor AI is at the forefront of digital health, combining AI technology with experienced medical professionals to deliver quality care. Our mission is to make healthcare more accessible, personalized, and efficient for everyone.")

st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.header("Our Services")
st.write("We offer a comprehensive range of medical services to meet the diverse needs of our patients:")
st.markdown("""
    <div class="card-container">
        <div class="card">
            <h3>General Consultations</h3>
            <p>Our experienced physicians provide consultations for a wide variety of health concerns, offering expert advice and treatment plans.</p>
        </div>
        <div class="card">
            <h3>Specialist Care</h3>
            <p>Access to a network of specialists across various fields, ensuring you receive the precise care you need.</p>
        </div>
        <div class="card">
            <h3>Emergency Services</h3>
            <p>We provide round-the-clock emergency services, ensuring immediate care when you need it most.</p>
        </div>
        <div class="card">
            <h3>Telemedicine</h3>
            <p>Consult with our doctors from the comfort of your home through our secure telemedicine platform.</p>
        </div>
        <div class="card">
            <h3>Health Monitoring</h3>
            <p>Our AI-driven tools help you monitor your health in real-time, providing insights and recommendations.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.header("Contact Us")
st.write("We're here to help. Reach out to us via email, phone, or visit us at our clinic.")
st.write("**Email:** contact@doctorai.com")
st.write("**Phone:** +92 234 567 890")
st.write("**Address:** 123 Health St, Peshawar, Pakistan")

st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.header("Health Blog")
st.write("Stay updated with the latest health news, tips, and expert advice on our blog. We cover a range of topics to help you stay informed and healthy.")

st.markdown("<div id='client'></div>", unsafe_allow_html=True)
st.header("Client Interface")
st.subheader("Search for Doctors")
search_term = st.text_input("Search for doctors based on specialty, location, or availability")
if search_term:
    st.write(f"Searching for doctors specializing in '{search_term}'...")

st.subheader("Book an Appointment")
selected_doctor = st.selectbox("Choose a doctor", ["Dr. Ali - Cardiologist", "Dr. Ahmed - Dermatologist", "Dr. Sara - Pediatrician"])
appointment_date = st.date_input("Select Appointment Date")
appointment_time = st.time_input("Select Appointment Time")
st.button("Book Appointment")

st.subheader("Access Medical History")
st.text_input("Enter your Patient ID to view your medical history")

st.markdown("<div id='admin'></div>", unsafe_allow_html=True)
st.header("Admin Panel")
st.write("This section is for administrators to manage doctors, appointments, and billing.")
admin_action = st.selectbox("Admin Actions", ["Add New Doctor", "Monitor Appointments", "Manage Billing"])
if admin_action == "Add New Doctor":
    st.text_input("Enter Doctor's Name")
    st.text_input("Enter Specialty")
    st.text_input("Enter Contact Information")
    st.button("Add Doctor")

st.markdown("<div id='chatbot'></div>", unsafe_allow_html=True)
st.header("Chatbot")
user_query = st.text_input("Ask the Doctor AI about your symptoms")
if user_query:
    st.write(chatbot_response(user_query))

st.markdown("<div id='new-doctors'></div>", unsafe_allow_html=True)
st.header("New Doctor Profiles")
st.write("Are you a new doctor? Submit your profile here.")
st.text_input("Full Name")
st.text_input("Specialty")
st.text_input("Contact Information")
st.button("Submit Profile")

st.markdown("<div id='admin-management'></div>", unsafe_allow_html=True)
st.header("Admin Management")
st.write("Manage all doctors, appointments, and patient records from this section.")
if page == "Admin Management":
    st.title("Admin Management")
    st.write("Manage doctor profiles, monitor interactions, handle disputes, and ensure compliance.")
    st.write("This section is restricted to authorized admins.")
    
    st.subheader("Approve New Doctor Profiles")
    st.write("Review and approve or reject new doctor profiles submitted.")

    st.subheader("Monitor Doctor-Patient Interactions")
    st.write("Oversee interactions between doctors and patients to ensure quality and compliance.")

    st.subheader("Handle Disputes or Issues")
    st.write("Address and resolve any disputes or issues that arise.")

    st.subheader("Ensure Compliance")
    st.write("Ensure all practices are in line with medical regulations and standards.")

# Sidebar - Random Health Tip
health_tips = [
    "Stay hydrated by drinking at least 8 glasses of water a day.",
    "Regular exercise boosts your immune system.",
    "Eat a balanced diet rich in fruits and vegetables.",
    "Get at least 7-8 hours of sleep every night.",
    "Regular check-ups help detect health issues early."
]
st.sidebar.markdown(f"**Health Tip of the Day:** {random.choice(health_tips)}")

# Footer
st.markdown("""
    <footer>
        <p>Developed By: Irfan Ullah Khan</p>
        <p><a href="https://flowcv.me/ikm">https://flowcv.me/ikm</a></p>
        <p>Linkedin: https://www.linkedin.com/in/irfanullahkhanmarwat/</p>
        
    </footer>
""", unsafe_allow_html=True)
