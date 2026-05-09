import streamlit as st
import os
import base64
import asyncio

# Fix for Streamlit Cloud Python 3.14+ asyncio event loop RuntimeError
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Page config
st.set_page_config(page_title="Kelvin Ufegbunem - Digital Resume", page_icon="📄", layout="wide")

# Injecting Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Subtle Color Background that adapts to Light/Dark Mode */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%);
    }
    
    .header-flex {
        display: flex;
        align-items: center;
        gap: 30px; 
        margin-bottom: 20px;
        flex-wrap: wrap; /* Allows stacking on very small screens */
    }
    
    .profile-img-container {
        width: 160px; 
        height: 160px; 
        border-radius: 50%; 
        border: 4px solid var(--primary-color, #3B82F6); 
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
    
    /* Name Font Adjusted */
    .main-header {
        font-family: 'Times New Roman', Times, serif;
        font-size: 55px !important; /* Force exact pixel size */
        font-weight: 900 !important;
        color: var(--text-color);
        margin: 0;
        line-height: 1.1;
    }
    
    .job-title-header {
        font-family: 'Inter', sans-serif;
        font-size: 22px;
        font-weight: 600;
        color: #3B82F6;
        margin-top: 5px;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }
    
    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .header-flex {
            flex-direction: column;
            text-align: center;
            gap: 15px;
        }
        .main-header {
            font-size: 35px !important;
            white-space: normal; /* Let name wrap on tiny phones if necessary */
        }
        .contact-info {
            font-size: 1rem;
        }
        .profile-img-container {
            width: 130px;
            height: 130px;
        }
    }
    
    .contact-info {
        font-size: 1.15rem;
        color: var(--text-color);
        opacity: 0.8;
        font-weight: 500;
        margin-top: 8px;
        margin-bottom: 0;
    }
    
    .sub-header {
        font-size: 1.8rem;
        font-weight: 800;
        color: #3B82F6; /* Works well in light and dark */
        margin-top: 30px;
        margin-bottom: 15px;
        padding-bottom: 8px;
        border-bottom: 3px solid rgba(59, 130, 246, 0.2);
    }
    
    .card {
        background-color: var(--secondary-background-color);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        transition: transform 0.2s ease-in-out;
        border-left: 5px solid #3B82F6;
        color: var(--text-color);
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    .experience-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: var(--text-color);
        margin-bottom: 5px;
    }
    
    .experience-subtitle {
        font-size: 1rem;
        color: var(--text-color);
        opacity: 0.8;
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
        background: rgba(59, 130, 246, 0.1);
        color: #3B82F6;
        padding: 10px 20px;
        border-radius: 30px;
        font-size: 1rem;
        font-weight: 600;
        border: 1px solid rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        background: #3B82F6;
        color: white;
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4);
    }
    
    .summary-text {
        font-size: 1.15rem;
        line-height: 1.8;
        color: var(--text-color);
        background: var(--secondary-background-color);
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #8B5CF6;
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
    img_html = '<div style="width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(0,0,0,0.1) 100%);"></div>'

st.markdown(f"""
<div class="header-flex">
    <div class="profile-img-container">
        {img_html}
    </div>
    <div class="name-contact-container">
        <p class="main-header">KELVIN UFEGBUNEM</p>
        <p class="job-title-header">JUNIOR DATA ANALYST</p>
        <p class="contact-info">📧 ufegbunemkelvin45@gmail.com | 📍 Nigeria (Remote) | 🕒 GMT+1 | 📱 WhatsApp: +234 905 993 0383</p>
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
        <ul style="font-size: 1.05rem; line-height: 1.6; opacity: 0.9;">
            <li>Transformed raw data into actionable insights for strategic decisions.</li>
            <li>Enhanced reporting accuracy by 50% through data validation techniques.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="experience-title">Computer Operator / Computer Appreciation</div>
        <div class="experience-subtitle">🏢 WARCO international | 📍 Port Harcourt, Nigeria <br>📅 Aug 2018 - Nov 2018</div>
        <ul style="font-size: 1.05rem; line-height: 1.6; opacity: 0.9;">
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
    <ul style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 0; opacity: 0.9;">
        <li>🏆 Completed multiple data analysis projects using <b>Power BI</b>.</li>
        <li>📈 Created interactive dashboards and reports.</li>
        <li>🎯 Analyzed student performance data to improve tracking.</li>
        <li>📁 Assisted in digital record management during SIWES.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: var(--text-color); opacity: 0.5; font-size: 0.95rem; font-weight: 600;'>Designed with ❤️ using Streamlit & Python</p>", unsafe_allow_html=True)
