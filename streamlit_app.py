import streamlit as st
import os
import base64

# Page config
st.set_page_config(page_title="Kelvin Ufegbunem - Digital Resume", page_icon="📄", layout="wide")

# Injecting Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Flex Container to put items close together */
    .header-flex {
        display: flex;
        align-items: center;
        gap: 25px; /* This controls how close the name is to the picture */
        margin-bottom: 20px;
    }
    
    .profile-img-container {
        width: 140px; 
        height: 140px; 
        border-radius: 50%; 
        border: 4px solid #3B82F6; 
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); 
        overflow: hidden;
        flex-shrink: 0;
    }
    
    .profile-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .name-contact-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .main-header {
        font-family: 'Times New Roman', Times, serif;
        font-size: 3.5rem;
        font-weight: bold;
        color: #111827;
        margin: 0;
        line-height: 1.1;
    }
    
    .contact-info {
        font-size: 1.1rem;
        color: #6B7280;
        font-weight: 500;
        margin-top: 5px;
        margin-bottom: 0;
    }
    
    .sub-header {
        font-size: 1.8rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-top: 30px;
        margin-bottom: 15px;
        padding-bottom: 8px;
        border-bottom: 3px solid #DBEAFE;
    }
    
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
        transition: transform 0.2s ease-in-out;
        border-left: 5px solid #3B82F6;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .experience-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: #1F2937;
        margin-bottom: 5px;
    }
    
    .experience-subtitle {
        font-size: 1rem;
        color: #4B5563;
        font-weight: 500;
        margin-bottom: 15px;
    }
    
    .skill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 10px;
    }
    
    .skill-tag {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        color: #1E40AF;
        padding: 10px 20px;
        border-radius: 30px;
        font-size: 1rem;
        font-weight: 600;
        border: 1px solid #BFDBFE;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .skill-tag:hover {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
        color: white;
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4);
    }
    
    .summary-text {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #374151;
        background: #F9FAFB;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #6366F1;
    }
    
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- HEADER HTML GENERATION -----------------
# Read picture directly from directory to place it right next to the name via HTML/CSS Flexbox
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

img_b64 = get_base64_image("profile.png")
if not img_b64:
    img_b64 = get_base64_image("profile.jpg")

if img_b64:
    img_html = f'<img src="data:image/png;base64,{img_b64}">'
else:
    # A simple clean gray circle if no picture is found
    img_html = '<div style="width: 100%; height: 100%; background: linear-gradient(135deg, #F3F4F6 0%, #E5E7EB 100%);"></div>'

st.markdown(f"""
<div class="header-flex">
    <div class="profile-img-container">
        {img_html}
    </div>
    <div class="name-contact-container">
        <p class="main-header">KELVIN UFEGBUNEM</p>
        <p class="contact-info">📧 ugbekelvin@gmail.com | 📍 Nigeria (Remote) | 🕒 GMT+1 | 📱 WhatsApp: +234 905 993 0383</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------- SUMMARY -----------------
st.markdown('<p class="sub-header">Professional Summary</p>', unsafe_allow_html=True)
st.markdown('<div class="summary-text">As a dedicated and data-fascinated Computer Operator and Junior Data Analyst, I am eager to contribute my skills in data management and analysis to your esteemed team. With a strong foundation in computer appreciation and a passion for leveraging data to drive insights. I am excited about the opportunity to collaborate with like-minded professionals. I am committed to delivering high-quality results and supporting the team\'s success through my analytical abilities and technical expertise.</div>', unsafe_allow_html=True)

# ----------------- EXPERIENCE & EDUCATION -----------------
col_exp, col_edu = st.columns(2)

with col_exp:
    st.markdown('<p class="sub-header">Experience</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="experience-title">Junior Data Analyst</div>
        <div class="experience-subtitle">🏢 AFA Engineering construction company | 📍 River State, Nigeria <br>📅 Oct 2023 - Feb 2024</div>
        <ul style="color: #4B5563; font-size: 1.05rem; line-height: 1.6;">
            <li>Transformed raw data into actionable insights for strategic decisions.</li>
            <li>Enhanced reporting accuracy by 50% through data validation techniques.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="experience-title">Computer Operator / Computer Appreciation</div>
        <div class="experience-subtitle">🏢 WAECO international | 📍 Port Harcourt, Nigeria <br>📅 Aug 2018 - Nov 2018</div>
        <ul style="color: #4B5563; font-size: 1.05rem; line-height: 1.6;">
            <li>Managed daily computer operations with 99% uptime efficiency.</li>
            <li>Streamlined data entry processes, reducing errors by 30%.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_edu:
    st.markdown('<p class="sub-header">Education</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card" style="border-left-color: #8B5CF6;">
        <div class="experience-title">Higher National Diploma (HND), Computer Science</div>
        <div class="experience-subtitle">🎓 Elechi Amadi Polytechnic, Port Harcourt, Nigeria | 📅 2024</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card" style="border-left-color: #8B5CF6;">
        <div class="experience-title">National Diploma (ND), Computer Science</div>
        <div class="experience-subtitle">🎓 Elechi Amadi Polytechnic, Port Harcourt, Nigeria | 📅 2021 - 2023</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="border-left-color: #8B5CF6;">
        <div class="experience-title">Senior Secondary Certificate Examination (SSCE)</div>
        <div class="experience-subtitle">🏫 Zion International High School | 📅 2018 - 2020</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ----------------- SKILLS -----------------
st.markdown('<p class="sub-header">Core Competencies</p>', unsafe_allow_html=True)
skills = ["Power BI", "Data Cleansing", "Internet Research", "Communication", "Data Entry", "Data Visualization", "Data Management", "Analytical Thinking"]

skills_html = '<div class="skill-container">'
for skill in skills:
    skills_html += f'<div class="skill-tag">{skill}</div>'
skills_html += '</div>'
st.markdown(skills_html, unsafe_allow_html=True)

st.markdown("---")

# ----------------- ACHIEVEMENTS -----------------
st.markdown('<p class="sub-header">Key Achievements</p>', unsafe_allow_html=True)
st.markdown("""
<div class="card" style="border-left-color: #10B981;">
    <ul style="color: #4B5563; font-size: 1.1rem; line-height: 1.8; margin-bottom: 0;">
        <li>🏆 Completed multiple data analysis projects using <b>Power BI</b>.</li>
        <li>📈 Created interactive dashboards and reports.</li>
        <li>🎯 Analyzed student performance data to improve tracking.</li>
        <li>📁 Assisted in digital record management during SIWES.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.95rem; font-weight: 600;'>Designed with ❤️ using Streamlit & Python</p>", unsafe_allow_html=True)
