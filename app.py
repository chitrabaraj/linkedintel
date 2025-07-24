import streamlit as st
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="LinkedIntel – Free AI Tool", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
body {
    background-color: #0d1117;
    color: #e6edf3;
    font-family: 'Inter', sans-serif;
}
.stApp { padding: 1rem 2rem; }
h1, h2, h3 { color: #ffffff; }
.stButton > button {
    background-color: #238636;
    color: white;
    font-weight: bold;
    border-radius: 6px;
}
.stDownloadButton > button {
    background-color: #2d88ff;
    color: white;
    font-weight: bold;
    border-radius: 6px;
}
.stTextInput > div > div > input,
.stSelectbox > div > div > div > select {
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

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://freeimage.host/uploads/2025/07/24/Fejzx7R.jpg", width=160)
    st.markdown("## Chitra")
    st.markdown("Built LinkedIntel to help you show up smarter on LinkedIn with real-time trends.")
    st.markdown("[Connect on LinkedIn](https://linkedin.com/in/chitrabaraj)")

# --- HEADER ---
st.title("LinkedIntel")
st.subheader("Free AI Tool to Discover LinkedIn Trends")
st.markdown("Instantly get hashtags, post ideas, top voices, and an editable 7-day content calendar based on your role and industry.")

# --- USER INPUT ---
st.markdown("### Step 1: Tell me who you are")

industries = ["Marketing", "Product", "Design", "SaaS", "E-commerce", "Finance", "HR", "Tech", "Freelancing"]
roles = ["Founder", "Marketing Manager", "Product Manager", "Designer", "Content Creator", "Recruiter", "Growth Lead", "Freelancer"]

with st.form("form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", placeholder="e.g. Chitra")
        industry = st.selectbox("Your Industry", industries)
    with col2:
        role = st.selectbox("Your Role", roles)
    submitted = st.form_submit_button("Generate Plan")

# --- OUTPUT ---
if submitted:
    st.markdown(f"### Trends for a {role} in {industry}")

    col1, col2, col3 = st.columns(3)

    # Trending Hashtags
    with col1:
        st.markdown("#### 🔥 Trending Hashtags")
        hashtags = [
            "#MarketingStrategy", "#LinkedInGrowth", "#ContentCreators", "#AIForBusiness",
            "#DesignThinking", "#BuildInPublic", "#ProductMarketing", "#FounderLife",
            "#PersonalBranding", "#B2BMarketing"
        ]
        for tag in hashtags:
            st.markdown(f"- {tag}")

    # Top Voices
    with col2:
        st.markdown("#### 🧠 Top Voices to Follow")
        voices = {
            "Justin Welsh": "https://linkedin.com/in/justinwelsh",
            "Amanda Natividad": "https://linkedin.com/in/amandanat",
            "Shaan Puri": "https://linkedin.com/in/shaanpuri",
            "Katelyn Bourgoin": "https://linkedin.com/in/kbourgoin",
            "Niharikaa Kaur Sodhi": "https://linkedin.com/in/niharikaa"
        }
        for name, link in voices.items():
            st.markdown(f"- [{name}]({link})")

    # Post Themes
    with col3:
        st.markdown("#### ✍️ Viral Content Topics")
        topics = [
            "AI use cases in your field",
            "Lessons from a client fail",
            "1 thing your team gets right",
            "Tools you can't live without",
            "A meme that speaks truth",
        ]
        for t in topics:
            st.markdown(f"- {t}")

    st.markdown("---")

    # --- AI Tool Suggestions ---
    st.markdown("### 🛠️ Free Tools to Help You Create")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Writing**")
        st.markdown("- [Notion AI](https://notion.so)")
        st.markdown("- [Typefully](https://typefully.com)")
        st.markdown("- [ChatGPT](https://chat.openai.com)")

    with col2:
        st.markdown("**Design**")
        st.markdown("- [Canva](https://canva.com)")
        st.markdown("- [Remove.bg](https://remove.bg)")
        st.markdown("- [Looka](https://looka.com)")

    with col3:
        st.markdown("**Video / Reels**")
        st.markdown("- [CapCut](https://capcut.com)")
        st.markdown("- [Runway ML](https://runwayml.com)")
        st.markdown("- [Pexels](https://pexels.com/videos)")

    st.markdown("---")

    # --- Calendar ---
    st.markdown("### 📅 Editable 7-Day Content Calendar")

    calendar = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(7)],
        "Post Type": ["Carousel", "Poll", "Meme", "Text", "Video", "Carousel", "Quote"],
        "Topic": [
            "AI in your role", "Question for your network", "Funny take on trends",
            "Story from your journey", "Tool you love", "Work tip", "Lessons learned"
        ],
        "Hashtags": [", ".join(hashtags[:3])] * 7,
        "Ideal Time": ["10:00 AM"] * 7,
        "CTA": ["Comment", "Vote", "Tag someone", "DM me", "Click link", "Reply", "Save this"]
    })

    updated_calendar = st.data_editor(calendar, use_container_width=True, num_rows="dynamic")
    csv = updated_calendar.to_csv(index=False).encode()
    st.download_button("Download Calendar as CSV", csv, "LinkedIntel_7DayCalendar.csv", "text/csv")

# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center>Built with no-code by Chitra · LinkedIntel © 2025</center>", unsafe_allow_html=True)
