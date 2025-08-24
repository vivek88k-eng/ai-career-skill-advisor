import streamlit as st

st.set_page_config(page_title="AI Career & Skill Development Advisor", page_icon="🎯")

st.title("🎯 AI Career & Skill Development Advisor")
st.write("An agent that analyzes your interests & strengths, recommends career paths and courses, and tracks your progress toward career goals.")

# ---- Knowledge base (simple rule-based) ----
CAREERS = {
    "Software Developer": {
        "skills": ["DSA", "Git/GitHub", "Databases", "Web Framework"],
        "courses": ["Intro to DSA", "SQL Basics", "Build a Web App"],
    },
    "Data Scientist": {
        "skills": ["Python", "Statistics", "Machine Learning", "Data Visualization"],
        "courses": ["Python for Data Analysis", "ML Crash Course", "Visualize Data"],
    },
    "Cybersecurity Analyst": {
        "skills": ["Networking Basics", "Linux", "Threat Modeling"],
        "courses": ["Computer Networks 101", "Linux Essentials", "Intro to Cybersecurity"],
    },
    "Cloud/DevOps Engineer": {
        "skills": ["Linux", "Docker", "CI/CD", "Cloud Basics"],
        "courses": ["Docker Basics", "CI/CD Fundamentals", "Intro to Cloud"],
    },
    "AI/ML Engineer": {
        "skills": ["Python", "ML Algorithms", "Deep Learning"],
        "courses": ["ML Foundations", "Neural Networks Intro", "Model Deployment"],
    },
}

# ---- User Inputs ----
st.subheader("👤 Your Profile")
name = st.text_input("Name", value="Aditya")
strengths = st.multiselect("Your Strengths", ["Coding", "Math/Stats", "Communication", "Design/UI", "Research", "Leadership"])
interests = st.multiselect("Your Interests", ["Web", "App", "AI", "ML", "Data", "Security", "Cloud", "DevOps", "Product"])

if st.button("🔎 Get Recommendations"):
    if not interests and not strengths:
        st.warning("Please select at least one interest or strength.")
    else:
        # Simple logic: show top 3 careers
        st.success("Top Career Recommendations")
        for career, info in list(CAREERS.items())[:3]:
            with st.expander(f"{career}"):
                st.markdown("*Core Skills*")
                for s in info["skills"]:
                    st.write(f"- {s}")
                st.markdown("*Suggested Courses*")
                for c in info["courses"]:
                    st.write(f"- {c}")

        st.write("---")
        st.subheader("📊 Progress Tracker")
        selected = st.selectbox("Choose a target career to track progress:", list(CAREERS.keys()))
        progress = st.slider("Overall Progress (%)", 0, 100, 0)
        st.progress(progress / 100)
        st.write(f"{name}'s progress toward {selected}: {progress}%")

        st.write("---")
        st.subheader("💼 Internship Matches (Demo)")
        st.write("- Software Intern @ NeoSoft (Remote)")
        st.write("- Data Science Intern @ InsightX (Remote)")
        st.write("- Cybersecurity Intern @ ShieldSec (Hybrid)")
