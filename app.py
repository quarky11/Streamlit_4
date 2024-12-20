from pathlib import Path

import streamlit as st
from PIL import Image



# GENERAL SETTING
PAGE_TITLE = "Digital CV | Hilal Fahri Husen"
PAGE_ICON = ":wave:"
NAME = "Hilal Fahri Husen"
DESCRIPTION = """
A fresh graduate with a degree in Mechanical Engineering and less than a year of experience in the related field. A 
rapid learner eager to acquire new knowledge and possessing a strong enthusiasm for self-development. Demonstrates 
good communication skills and is capable of working independently as well as collaboratively. Proficient in 
SolidWorks, ANSYS, and AutoCAD for mechanical analysis. Additionally experienced in using management tools 
such as Google Spreadsheet and MS Project for effective project tracking and management. 
"""
EMAIL = "hilalfahri11@email.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/husenhilal/",
    "LinkedIn": "https://www.linkedin.com/in/hilalfahri/",
    "GitHub": "https://github.com/quarky11",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- HERO SECTION ---

st.title(NAME)
st.write(DESCRIPTION)

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write(
    """
**Bandung Institute of Technology**                                                                                                     
Bachelor of Mechanical Engineering, Faculty of Mechanical Engineering and Aerospace
"""
)

# --- Work xperience ---
st.write('\n')
st.subheader("Work Experience")
st.markdown('<hr style="margin: 5px 0;">', unsafe_allow_html=True)

# --- JOB 1
st.write("🚧", "**Project Engineer | PT. ACTIV CONSULTANT TECH INDONESIA**")
st.write("05/2024 - 09/2024")
st.write(
    """
- ► Coordinated with 4+ vendors and teams to complete data center construction and commissioning, ensuring seamless integration and project efficiency. 
- ► Developed and managed a Google Spreadsheet-based tracker utilizing a room-by-room readiness system to monitor project progress in real-time, enhancing transparency and reporting. 
- ► Created and implemented Google App Script tools to boost Google Spreadsheet functionality, resulting in automated reporting and improved performance tracking.
- ► Utilized MS Project to monitor and analyze project progress, assessing the impact of task list success or failure on project timelines and making adjustments to mitigate delays.
- ► Prepared technical documentation and progress reports, providing essential information for decision-making and project performance evaluation. 
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Junior Mechanical Engineer | PT. MONTA CAKRA TEKNOLOGI**")
st.write("09/2023 - 01/2024")
st.write(
    """
- ► Supported senior engineers in the design and development of engineering projects using CAD software. 
- ► Participated in quality control processes, conducting test, and inspection to ensure projects comply with technical standards and specifications. 
- ► Compiled and maintained essential technical documentation, including project plans, JSA document,production drawing document, and as built drawing document. 
- ► Provided support in project management tasks, including scheduling, progress tracking, and resource allocation to ensure project completion within timelines.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Mechanical Engineer Intern | PT. STECHOQ ROBOTIKA INDONESIA**")
st.write("08/2022 - 12/2022")
st.write(
    """
- ► Assist in the development of mechanical product using CAD software, contributing to brainstorming sessions and design reviews to refine product concepts.
- ► Participate in the creation of prototypes and excute comprehensive testing plans to evaluate product peformace. 
- ► Work alongside professionals from different departments, including technical departement and non technical departement.
- ► Delivered final result through comprehensive pitch deck presentation, effectively communicating the project work and product development stages.
"""
)

# --- Organization experience ---
st.write('\n')
st.subheader("Organization Experience")
st.markdown('<hr style="margin: 5px 0;">', unsafe_allow_html=True)

# --- Ex 1
st.write("🚧", "**Himpunan Mahasiswa Mesin (HMM) ITB**")
st.write("as Staff DPA HMM ITB")
st.write("09/2021 - 09/2022")
st.write(
    """
- ► Collecting aspiration and give feedback  from member of Himpunan Mahasiswa Mesin ITB
- ► Monitoring and guiding operational activity of Badan Pengurus HMM ITB. 
- ► Managed and led people to actively respond the aspiration from member 
"""
)

# --- Ex 2
st.write("🚧", "**Bandung Institute of Technology Football Club (PS ITB)**")
st.write("as Staff BRT")
st.write("07/2020 - 07/2021")
st.write(
    """
- ► Organized the process of public leasing item.
- ► Ensured all logistic material are organized and easy to access. 
"""
)

# --- Training experience ---
st.write('\n')
st.subheader("Training or Certification")
st.markdown('<hr style="margin: 5px 0;">', unsafe_allow_html=True)

# --- Ex 1
st.write("🏆", "**UDEMY CERTIFICATE OF COMPLETION** - ► SOLIDWORKS: Become a Certified Professional Today (CSWP)")

# --- Ex 2
st.write("🏆", "**UDEMY CERTIFICATE OF COMPLETION** - ► ANSYS Training: An Easy Introduction with Applications")


# --- Ex 3
st.write("🏆", "**DICODING CLASS COMPLETON** - ► Belajar Dasar Data Science")


# --- Ex 4
st.write("🏆", "**DICODING CLASS COMPLETON** - ► Belajar Structured Query Language")


# --- Ex 5
st.write("🏆", "**SANBERCODE BOOTCAMP** - ► Full-Stack Data Science")



# --- SKILLS ---
st.write('\n')
st.subheader("Related Skill")
st.markdown('<hr style="margin: 5px 0;">', unsafe_allow_html=True)
st.write(
    """
- 📚 Mechanical Engineering: Solidworks, Ansys, Autocad    
- 👩‍💻 Programming: Python, SQL
- 📊 Data Visulization: Matplotlib, Seaborn, Spreadsheet, Excel
"""
)
