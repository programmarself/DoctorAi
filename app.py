import streamlit as st
import pandas as pd
import numpy as np
import re

# Load custom CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Placeholder for API keys and sensitive data
# API_KEY = 'your_api_key_here'  # Replace with your actual API key

# Function to simulate a chatbot response with improved logic
def chatbot_response(query):
    query = query.lower()
    
    # Simple symptom check
    if re.search(r'\b(symptom|fever|cough|pain|headache)\b', query):
        return "It sounds like you're experiencing symptoms. Please consult a doctor for a more accurate diagnosis."
    
    # Medication related queries
    elif re.search(r'\b(medication|medicine|pill|drug|prescription)\b', query):
        return "For medication advice, it's best to consult a healthcare professional. They can provide personalized recommendations based on your health condition."
    
    # General health advice
    elif re.search(r'\b(diet|exercise|nutrition|health)\b', query):
        return "Maintaining a balanced diet and regular exercise is crucial for good health. If you need specific advice, consult a nutritionist or health professional."
    
    # Doctor consultation
    elif re.search(r'\b(doctor|appointment|consult)\b', query):
        return "To book an appointment with a doctor, please use our 'Book Appointment' feature in the Client Interface."
    
    # Default fallback
    else:
        return "I'm not sure how to help with that. Please contact a doctor for more information."

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Home", "About Us", "Services", "Contact", "Health Blog",
    "Client Interface", "Admin Panel", "Chatbot", "New Doctor Profiles", "Admin Management"
])

# Apply custom CSS
load_css('assets/styles.css')

# Common Header
st.image("assets/doctor_ai.png")
st.title("Doctor AI - Professional Healthcare at Your Fingertips")

# Home Page
if page == "Home":
    st.subheader("Welcome to HealthCare Center")
    st.write("Providing the best healthcare services for you and your family.")

# About Us Page
elif page == "About Us":
    st.subheader("About Us")
    st.write("We are committed to providing excellent healthcare services with a team of experienced professionals dedicated to your well-being.")

# Services Page
elif page == "Services":
    st.subheader("Our Services")
    st.write("We offer a range of medical services including general consultations, specialist care, emergency services, and more.")

# Contact Page
elif page == "Contact":
    st.subheader("Contact Us")
    st.write("Get in touch with us through email, phone, or visit our office.")
    st.write("Email: contact@healthcare.com")
    st.write("Phone: +1 234 567 890")
    st.write("Address: 123 Health St, Wellness City")

# Health Blog Page
elif page == "Health Blog":
    st.subheader("Health Blog")
    st.write("Read our latest articles on health and wellness. Stay informed with expert advice and tips for a healthier lifestyle.")

# Client Interface Page
elif page == "Client Interface":
    st.subheader("Client Interface")
    
    # Search for Doctors
    st.text_input("Search for doctors based on specialty, location, or availability", key="search_term")
    
    # Book an Appointment
    st.selectbox("Select Doctor", ["Dr. Smith", "Dr. Johnson", "Dr. Lee"])  # Replace with dynamic list
    st.date_input("Select Date")
    st.time_input("Select Time")
    st.button("Book Appointment")
    
    # Access Medical History and Prescriptions
    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")
    st.button("Log In")
    
    # Receive Notifications and Reminders
    st.write("Manage your notifications and reminders for upcoming appointments and medication.")

# Admin Panel Page
elif page == "Admin Panel":
    st.subheader("Admin Panel")
    st.selectbox("Select Action", [
        "Manage Doctors", "Monitor Appointments", "Handle Billing", "Update Content"
    ])

# Chatbot Page
elif page == "Chatbot":
    st.subheader("Chatbot for Medication Suggestions")
    st.write("Ask me anything about your symptoms, medications, or general health advice!")

    user_query = st.text_input("Type your query here:")
    if user_query:
        response = chatbot_response(user_query)
        st.write(f"Chatbot: {response}")

# New Doctor Profiles Page
elif page == "New Doctor Profiles":
    st.subheader("New Doctor Profiles")
    st.text_input("Doctor's Name")
    st.text_input("Specialty")
    st.text_input("Availability")
    st.number_input("Consultation Fee")
    st.file_uploader("Upload Photo", type=["jpg", "png"])
    st.text_area("Bio")
    st.text_input("Social Media Links")
    st.button("Submit Profile")

# Admin Management Page
elif page == "Admin Management":
    st.subheader("Admin Management")
    st.write("Manage doctor profiles, monitor interactions, handle disputes, and ensure compliance.")
    st.write("This section is restricted to authorized admins.")
    
    st.write("Approve New Doctor Profiles")
    st.write("Monitor Doctor-Patient Interactions")
    st.write("Handle Disputes or Issues")
    st.write("Ensure Compliance")

# Footer
st.markdown("""
    <footer>
    <p>Developed By: Irfan Ullah Khan</p>
    <a href='https://flowcv.me/ikm'>https://flowcv.me/ikm</a>
  
    </footer>
""", unsafe_allow_html=True)
