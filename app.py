import streamlit as st
import pdfplumber


# Page Title
st.set_page_config(page_title="AI Resume Analyzer",
                    page_icon="📄",
                    layout="wide",
                    initial_sidebar_state="expanded"
)

#Main title
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get an instant analysis.")


# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

text = ""

if uploaded_file is None:
    st.stop()
  #PDF Processing
if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully!")
    st.write("**File Name:**", uploaded_file.name)

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    st.subheader("📃 Resume Text")
    st.text_area("Extracted Text", text, height=250)

    st.markdown("----------")

    # ==========================
    # Skills Detection
    # ==========================

    skills = [
        "Python", "Java", "C", "C++",
        "HTML", "CSS", "JavaScript",
        "SQL", "Git", "Machine Learning",
        "Data Science", "Streamlit"
    ]

    st.subheader("💻 Detected Skills")

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    if found_skills:
        for skill in found_skills:
            st.success(skill)
    else:
        st.warning("No Skills Found")

        st.markdown("----------")

    # ==========================
    # Resume Score
    # ==========================

    score = int((len(found_skills) / len(skills)) * 100)

    missing_skills = []
    
    for skill in skills:
            if skill not in found_skills:
                missing_skills.append(skill)

    st.subheader("📊 Resume Score")

    st.progress(score)

    st.success(f"Resume Score : {score}/100")

    

st.markdown("----------")

    # ==========================
    # Missing Skills
    # ==========================

   

st.subheader("❌ Missing Skills")

if missing_skills:
        for skill in missing_skills:
            st.warning(skill)
else:
        st.success("Excellent! No Missing Skills")

        st.markdown("----------")

        # ==========================
    # AI Suggestions
    # ==========================

st.subheader("🤖 AI Suggestions")

suggestions = []

if "github" not in text.lower():
    suggestions.append("🔹 Add your GitHub profile link")

    if "linkedin" not in text.lower():
        suggestions.append("🔹 Add your LinkedIn profile")

    if "project" not in text.lower():
        suggestions.append("🔹 Add at least 2-3 projects")

    if "certification" not in text.lower():
        suggestions.append("🔹 Add your certifications")

    if score < 70:
        suggestions.append("🔹 Improve your resume by adding more technical skills")

    if suggestions:
        for item in suggestions:
                    st.info(item)
    else:
        st.success("🎉 Excellent Resume! No major improvements needed.")

        st.markdown("----------")

        # ==========================
    # Download Report
    # ==========================

    report = f"""
    AI RESUME ANALYZER REPORT

    Resume Score : {score}/100

    Detected Skills:
    {', '.join(found_skills)}

    Missing Skills:
    {', '.join(missing_skills)}

    Suggestions:
    {chr(10).join(suggestions)}
    """

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="Resume_Report.txt",
        mime="text/plain"
    )
    st.markdown("----------")

    # ==========================
    # Job Role Prediction
    # ==========================

    st.subheader("💼 Predicted Job Role")
    

    role = "General"

    text_lower = text.lower()

    if ("python" in text_lower and "sql" in text_lower and "machine learning" in text_lower):
        role = "Data Scientist"

    elif ("python" in text_lower and "streamlit" in text_lower):
        role = "Python Developer"

    elif ("html" in text_lower and "css" in text_lower and "javascript" in text_lower):
        role = "Frontend Web Developer"

    elif ("java" in text_lower):
        role = "Java Developer"

    elif ("sql" in text_lower and "excel" in text_lower):
        role = "Data Analyst"

    st.success(role)
    if role == "Data Scientist":
         st.info("Build machine learning models,analyze data, and create AI solutions.")
    elif role == "Python Developer":
         st.info("Develop Python applications,APIs, automation scripts, and backend systems.")
    elif role == "Frontend Web Developer":
         st.info("Build responsive websites using HTML,CSS, Javascript, and modern frameworks." )
    elif role == "Java Developer":
         st.info("Develop Java applications, Spring Boot projects, and enterprise software.")
    elif role == "Data Analyst":
         st.info("Analyze business data, create dashboards, and generate reports using SQL and Excel.")
    else:
         st.info("General Software Development and Programming ")