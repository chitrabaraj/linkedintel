import streamlit as st
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="LinkedIntel – Free AI Tool", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
body {
    font-family: 'Inter', sans-serif;
    background-color: #ffffff;
    color: #1c1c1c;
}
h1, h2, h3 {
    color: #0a66c2;
}
.stApp {
    padding: 2rem 3rem;
}
.stButton > button {
    background-color: #0a66c2;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 0.6rem 1rem;
    font-weight: 600;
}
.stDownloadButton > button {
    background-color: #1064ea;
    color: white;
    font-weight: bold;
    border-radius: 6px;
}
input, select {
    background-color: #f0f2f5 !important;
    color: #1c1c1c !important;
    border: 1px solid #ccc !important;
    border-radius: 5px !important;
}
a {
    color: #0a66c2;
    text-decoration: none;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- MAIN UI ---
st.image("https://freeimage.host/uploads/2025/07/24/Fejzx7R.jpg", width=120)

st.title("LinkedIntel")
st.subheader("The Free AI Tool for Smarter LinkedIn Growth")
st.markdown("Built by **Chitra** to help founders and creators generate LinkedIn content ideas with real-time trends, top voices, and a downloadable content calendar.")

st.markdown("---")

# --- INPUT SECTION ---
st.markdown("### Step 1: Who Are You?")

industries = ["Marketing", "Product", "Design", "SaaS", "E-commerce", "Finance", "HR", "Tech", "Freelancing"]
roles = ["Founder", "Marketing Manager", "Product Manager", "Designer", "Content Creator", "Recruiter", "Growth Lead", "Freelancer"]

with st.form("user_info"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", placeholder="e.g. Chitra")
        industry = st.selectbox("Select Your Industry", industries)
    with col2:
        role = st.selectbox("Select Your Role", roles)
    submitted = st.form_submit_button("Generate Content Plan")

# --- RESULTS ---
if submitted:
    st.markdown(f"### 🔍 Results for a {role} in {industry}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🔥 Trending Hashtags")
        tags = [
            "#ContentStrategy", "#LinkedInGrowth", "#MarketingTips", "#PersonalBranding",
            "#BuildInPublic", "#AIforBusiness", "#DesignThinking", "#B2BMarketing"
        ]
        for tag in tags:
            st.markdown(f"- {tag}")

    with col2:
        st.markdown("#### 👥 Top Creators to Follow")
        voices = {
            "Justin Welsh": "https://linkedin.com/in/justinwelsh",
            "Amanda Natividad": "https://linkedin.com/in/amandanat",
            "Shaan Puri": "https://linkedin.com/in/shaanpuri",
            "Katelyn Bourgoin": "https://linkedin.com/in/kbourgoin",
            "Niharikaa Sodhi": "https://linkedin.com/in/niharikaa"
        }
        for name, url in voices.items():
            st.markdown(f"- [{name}]({url})")

    with col3:
        st.markdown("#### ✍️ Post Ideas")
        ideas = [
            "What AI changed in your work",
            "A story behind your product",
            "A lesson you wish you knew sooner",
            "Behind the scenes of your process",
            "Your best-performing post breakdown"
        ]
        for idea in ideas:
            st.markdown(f"- {idea}")

    st.markdown("---")
    st.markdown("### 🛠️ Free Tools to Create Content")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("**Writing Tools**")
        st.markdown("- [Notion AI](https://notion.so)")
        st.markdown("- [Typefully](https://typefully.com)")
        st.markdown("- [ChatGPT](https://chat.openai.com)")
    with col5:
        st.markdown("**Visual Tools**")
        st.markdown("- [Canva](https://canva.com)")
        st.markdown("- [Looka](https://looka.com)")
        st.markdown("- [Remove.bg](https://remove.bg)")
    with col6:
        st.markdown("**Video Tools**")
        st.markdown("- [CapCut](https://capcut.com)")
        st.markdown("- [Runway ML](https://runwayml.com)")
        st.markdown("- [Pexels](https://pexels.com/videos)")

    st.markdown("---")
    st.markdown("### 📅 7-Day Content Calendar (Editable)")

    calendar = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(7)],
        "Post Type": ["Carousel", "Poll", "Meme", "Text", "Video", "Listicle", "Quote"],
        "Topic": [
            "AI in your industry", "Poll: What's trending?", "Meme on tools",
            "Your origin story", "Tool breakdown", "Hot take", "Lessons from failure"
        ],
        "Hashtags": [", ".join(tags[:3])] * 7,
        "Time": ["10:00 AM"] * 7,
        "CTA": ["Comment", "Vote", "Tag", "DM me", "Save this", "Try it", "What's your view?"]
    })

    edited_calendar = st.data_editor(calendar, use_container_width=True, num_rows="dynamic")
    csv = edited_calendar.to_csv(index=False).encode()
    st.download_button("⬇️ Download CSV", csv, "LinkedIntel-Calendar.csv", "text/csv")

st.markdown("---")
st.markdown("<center style='color:#888'>Built with no-code by Chitra · LinkedIntel © 2025</center>", unsafe_allow_html=True)
