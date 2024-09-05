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
st.write("At Doctor AI, we leverage state-of-the-art technology to revolutionize healthcare services, offering solutions that are specifically tailored to your unique needs. Our platform integrates cutting-edge AI tools with the expertise of seasoned medical professionals to deliver a comprehensive and personalized health experience.

Our mission is to enhance the quality and accessibility of healthcare by providing intelligent, data-driven insights and solutions. Whether you're seeking general consultations, specialist care, or emergency services, our technology ensures that you receive accurate and timely support.

Our team of healthcare experts is dedicated to guiding you through every step of your health journey. From virtual consultations to real-time health monitoring, we are here to ensure that you have access to the best possible care, no matter where you are.

By combining innovative AI capabilities with compassionate medical guidance, Doctor AI is committed to making healthcare more efficient, accessible, and personalized. Trust us to be your partner in achieving better health and wellness.")

st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.header("About Us")
st.write("Doctor AI stands at the cutting edge of digital health innovation, merging advanced artificial intelligence technology with the expertise of highly skilled medical professionals to offer unparalleled healthcare services. We are dedicated to transforming the healthcare experience by harnessing the power of AI to provide exceptional care that is both efficient and personalized.

Our core mission is to revolutionize healthcare accessibility and quality by integrating sophisticated AI solutions with the compassionate touch of experienced clinicians. We believe that every individual deserves healthcare that is tailored to their unique needs and preferences. By leveraging AI, we aim to streamline processes, enhance diagnostic accuracy, and deliver insights that empower patients to make informed decisions about their health.

Doctor AI is committed to breaking down barriers to healthcare, making it more accessible and effective for everyone. Our platform offers a seamless blend of technology and human touch, ensuring that every patient receives timely, relevant, and personalized care. Whether you're seeking routine check-ups, specialist consultations, or emergency services, our advanced AI tools and dedicated medical professionals work together to provide a holistic and efficient healthcare experience.

At Doctor AI, we are passionate about using innovation to improve health outcomes and make quality care more attainable for all. Join us on our journey to redefine healthcare with the perfect balance of technology and human expertise.")

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
st.write("Welcome to the Doctor AI Health Blog, your go-to source for the latest updates, insights, and advice on maintaining a healthy lifestyle. Here, we cover a broad range of topics to help you stay informed and make better decisions about your health. Our blog features articles written by healthcare professionals, medical researchers, and wellness experts who are dedicated to providing accurate, evidence-based information.

**1. Latest Health Trends and Innovations

Stay updated with the most recent advancements in healthcare technology and wellness trends. From breakthroughs in medical research to the latest innovations in AI and digital health tools, we bring you comprehensive updates on how technology is transforming the landscape of healthcare. Learn about new treatments, cutting-edge devices, and how emerging technologies are enhancing patient care and improving health outcomes.

**2. Healthy Living Tips

Discover practical tips and strategies for leading a healthier lifestyle. Our articles cover a wide range of topics, including nutrition, exercise, mental health, and sleep hygiene. Find expert advice on creating balanced meal plans, incorporating physical activity into your daily routine, managing stress, and ensuring you get quality sleep. We also provide guidance on setting achievable health goals and maintaining motivation.

**3. Disease Prevention and Management

Learn how to prevent and manage common health conditions through lifestyle changes and medical interventions. Our blog features in-depth articles on topics such as heart disease, diabetes, hypertension, and respiratory conditions. Gain insights into the causes, symptoms, and risk factors associated with various diseases, and discover evidence-based strategies for prevention and management.

**4. Patient Stories and Testimonials

Read inspiring stories from individuals who have overcome health challenges and achieved positive outcomes with the help of Doctor AI. Our patient testimonials highlight personal journeys, experiences with our services, and the impact of our innovative AI solutions on their health. These stories offer valuable perspectives and motivation for others facing similar health issues.

**5. Expert Interviews and Q&A

Get direct answers to your health-related questions through our interviews with medical experts and specialists. We feature exclusive Q&A sessions where professionals share their insights on various health topics, answer common questions, and provide valuable advice. These interviews aim to bridge the gap between complex medical knowledge and everyday health concerns.

**6. Wellness Resources and Guides

Access a wealth of resources designed to support your well-being. Our blog includes downloadable guides, checklists, and educational materials on topics such as healthy eating, fitness routines, mental health strategies, and more. These resources are crafted to help you implement practical changes in your daily life and track your progress toward better health.

**7. Healthcare Policy and Advocacy

Stay informed about the latest developments in healthcare policy and advocacy. Our blog provides updates on health regulations, insurance changes, and initiatives aimed at improving healthcare systems. We discuss how these changes affect patients and healthcare providers and explore ways to advocate for better health policies and practices.

Join the Doctor AI Health Blog community and stay engaged with content that matters to you. Whether you’re looking for tips to enhance your well-being, seeking information on managing a health condition, or simply interested in the latest health trends, our blog is here to provide you with the knowledge and resources you need to live a healthier, more informed life.")

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
