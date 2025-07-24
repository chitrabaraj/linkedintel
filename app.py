import streamlit as st
import pandas as pd

# ------------------ CONFIG ------------------
st.set_page_config(page_title="LinkedIntel – Free AI Content Tool", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    body {
        background-color: #0d1117;
        color: #e6edf3;
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        padding: 1rem 2rem;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #161b22;
    }
    .stButton>button {
        background-color: #238636;
        color: white;
        font-weight: bold;
        border-radius: 6px;
    }
    .stDownloadButton>button {
        background-color: #2d88ff;
        color: white;
        font-weight: bold;
        border-radius: 6px;
    }
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div>select {
        background-color: #21262d;
        color: white;
        border: 1px solid #30363d;
    }
    a {
        color: #58a6ff;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.image("https://freeimage.host/uploads/2025/07/24/Fejzx7R.jpg", width=150)
    st.markdown("## Chitra")
    st.markdown("Built with no-code to help you discover LinkedIn trends and create smarter content.")
    st.markdown("[Connect on LinkedIn](https://linkedin.com/in/chitrabaraj)")

# ------------------ HEADER ------------------
st.title("LinkedIntel – Free AI Tool to Discover LinkedIn Trends")
st.subheader("Get smart content ideas, trends, top creators, and an editable 7-day calendar in one click.")

# ------------------ USER INPUT ------------------
st.markdown("### Step 1: Tell me who you are")

industries = ["Marketing", "Product", "Design", "SaaS", "E-commerce", "Finance", "HR", "Tech", "Freelancing"]
roles = ["Founder", "Marketing Manager", "Product Manager", "Designer", "Content Creator", "Recruiter", "Growth Lead", "Freelancer"]

with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", placeholder="e.g. Chitra")
        industry = st.selectbox("Your Industry", industries, index=0)
    with col2:
        role = st.selectbox("Your Role", roles, index=0)
    submitted = st.form_submit_button("Generate Plan")

# ------------------ OUTPUT ------------------
if submitted:
    st.markdown(f"### Showing trends for a {role} in {industry}")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Top LinkedIn Post Themes")
        st.markdown("""
        - AI applications in your domain  
        - Storytelling with frameworks  
        - Behind-the-scenes of your process  
        - Lessons from failures  
        - Community polls & debates  
        """)

        st.markdown("#### Trending Hashtags")
        st.write(["#ContentStrategy", "#LinkedInGrowth", "#BuildInPublic", "#MarketingTips", "#GenZCreator"])

    with col2:
        st.markdown("#### Top Voices to Follow")
        st.markdown("""
        - [Justin Welsh](https://linkedin.com)  
        - [Amanda Natividad](https://linkedin.com)  
        - [Shaan Puri](https://linkedin.com)  
        - [Katelyn Bourgoin](https://linkedin.com)  
        - [Niharikaa Kaur Sodhi](https://linkedin.com)  
        """)

    # ------------------ TOOLS SECTION ------------------
    st.markdown("---")
    st.markdown("### Free AI Tools to Help You Create")

    tools = {
        "Writing": {
            "Notion AI": "https://notion.so",
            "ChatGPT": "https://chat.openai.com",
            "Typefully": "https://typefully.com"
        },
        "Design": {
            "Canva": "https://canva.com",
            "Remove.bg": "https://remove.bg",
            "Looka": "https://looka.com"
        },
        "Video Editing": {
            "CapCut": "https://capcut.com",
            "Runway ML": "https://runwayml.com",
            "Pexels Videos": "https://pexels.com/videos"
        }
    }

    col1, col2, col3 = st.columns(3)
    for i, (category, links) in enumerate(tools.items()):
        with [col1, col2, col3][i]:
            st.markdown(f"**{category}**")
            for tool, url in links.items():
                st.markdown(f"- [{tool}]({url})")

    # ------------------ CALENDAR ------------------
    st.markdown("---")
    st.markdown("### Your 7-Day Editable Content Calendar")

    calendar = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(7)],
        "Post Type": ["Carousel", "Poll", "Meme", "Text", "Video", "Carousel", "Quote"],
        "Topic": [
            "AI in your field", "Audience question", "Relatable humor", "Your origin story",
            "Tool demo", "Industry insight", "Motivational nudge"
        ],
        "Time": ["10:00", "12:30", "09:45", "11:00", "14:15", "10:30", "08:00"],
        "CTA": [
            "Save this", "Vote below", "Tag someone", "Comment yours",
            "Try this", "Agree or disagree?", "Let’s go!"
        ]
    })

    edited = st.data_editor(calendar, use_container_width=True, num_rows="dynamic")
    csv = edited.to_csv(index=False).encode()
    st.download_button("Download Calendar as CSV", csv, "LinkedIntel-7Day-Plan.csv", "text/csv")

    st.markdown("---")
    st.markdown("**Use this calendar to stay consistent and relevant — powered by real trends.**")

# ------------------ FOOTER ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:0.9rem;'>Built with no-code by Chitra · LinkedIntel © 2025</div>", unsafe_allow_html=True)
