import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(
    page_title="LinkedIntel – Free AI Content Tool",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Dark Theme ---
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #e6e6e6;
    font-family: 'Inter', sans-serif;
}
.stApp {
    padding: 2rem;
}
h1, h2, h3, h4 {
    color: #ffffff;
}
.sidebar .sidebar-content {
    background-color: #161b22;
}
.st-bb {
    background-color: #21262d;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1.5rem;
}
.stButton>button {
    background-color: #2f81f7;
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 6px;
    font-weight: 600;
}
.stDownloadButton>button {
    background-color: #10b981;
    color: white;
    font-weight: 600;
}
.stTextInput>div>div>input,
.stSelectbox>div>div>div>select {
    background-color: #0e1117;
    color: white;
    border: 1px solid #30363d;
}
a {
    color: #58a6ff;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://freeimage.host/images/2025/07/24/Fejzx7R.jpg", width=160)
    st.markdown("### LinkedIntel")
    st.markdown("Free AI tool by Chitra to help creators and professionals discover LinkedIn trends & build high-impact content calendars.")
    st.markdown("[Connect on LinkedIn](https://linkedin.com/in/chitrabaraj)")

# --- Hero Section ---
st.title("LinkedIntel – Free AI Tool for LinkedIn Content")
st.subheader("Search what’s trending in your industry and generate a complete 7-day content calendar instantly.")

# --- Input Form ---
st.markdown("#### Step 1: Choose your role & industry")
with st.form("user_info"):
    col1, col2 = st.columns(2)
    with col1:
        industry = st.selectbox("Select your Industry", [
            "Marketing", "Product", "Design", "SaaS", "E-commerce", "Finance", "HR", "Tech", "Freelancing"
        ])
    with col2:
        role = st.selectbox("Your Role", [
            "Founder", "Marketing Manager", "Product Manager", "Designer",
            "Content Creator", "Recruiter", "Growth Lead", "Freelancer"
        ])
    submitted = st.form_submit_button("Generate Content Plan")

# --- Output Section ---
if submitted:
    st.markdown(f"### Trends for {role} in {industry}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Top Performing Post Themes")
        st.markdown("""
        • AI in your field  
        • Behind-the-scenes work  
        • Frameworks & checklists  
        • Lessons from failure  
        • Community-driven questions  
        """)

        st.markdown("#### Trending Hashtags")
        st.write(["#ContentStrategy", "#LinkedInGrowth", "#AIforProfessionals", "#Storytelling", "#CreatorTools"])

    with col2:
        st.markdown("#### Top Voices to Follow")
        st.markdown("""
        • [Justin Welsh](https://linkedin.com)  
        • [Amanda Natividad](https://linkedin.com)  
        • [Shaan Puri](https://linkedin.com)  
        • [Katelyn Bourgoin](https://linkedin.com)  
        • [Niharikaa Kaur Sodhi](https://linkedin.com)  
        """)

    st.markdown("---")
    st.markdown("### Free Tools to Build Content (Grouped by Use Case)")
    tools = {
        "Writing & Scripting": {
            "Notion": "https://notion.so",
            "ChatGPT Free": "https://chat.openai.com",
            "Typefully": "https://typefully.com"
        },
        "Design & Visuals": {
            "Canva": "https://canva.com",
            "Remove.bg": "https://remove.bg",
            "Looka": "https://looka.com"
        },
        "Video & Editing": {
            "CapCut": "https://capcut.com",
            "Pexels Videos": "https://pexels.com/videos",
            "Runway ML": "https://runwayml.com"
        }
    }

    for category, links in tools.items():
        st.markdown(f"**{category}**")
        for name, url in links.items():
            st.markdown(f"- [{name}]({url})")

    # --- 7 Day Calendar ---
    st.markdown("---")
    st.markdown("### 7-Day Content Calendar")
    calendar = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(7)],
        "Post Type": ["Carousel", "Poll", "Meme", "Text Post", "Video", "Carousel", "Quote"],
        "Topic": [
            "AI trends in your industry", "Audience pain point", "Relatable humor", "Personal journey",
            "Tool you use", "Market insight", "Motivational CTA"
        ],
        "Ideal Time": ["10:00", "12:00", "09:30", "11:00", "14:00", "10:30", "08:45"],
        "CTA": [
            "Save this", "Vote now", "Tag a friend", "Comment your story",
            "Try this", "What’s your take?", "Let’s go!"
        ]
    })
    st.dataframe(calendar, use_container_width=True)

    csv = calendar.to_csv(index=False).encode()
    st.download_button("Download 7-Day Calendar", csv, "LinkedIntel_Calendar.csv", "text/csv")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:0.9rem;'>Built by Chitra · No-code. AI-powered. Trend-smart.</div>", unsafe_allow_html=True)
