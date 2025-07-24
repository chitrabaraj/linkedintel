import streamlit as st
import pandas as pd
from datetime import datetime

# --- Page Settings ---
st.set_page_config(
    page_title="LinkedIntel – Free AI Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Global Styles for Dark Theme ---
st.markdown("""
    <style>
        body { background-color: #0F1116; color: #E5E5E5; }
        .stSidebar { background-color: #13151D; }
        .stButton>button { background-color: #2563EB; color: white; }
        .stDownloadButton>button { background-color: #10B981; color: white; }
        .stTextInput>div>div>input, .stSelectbox>div>div>div>select {
            background-color: #1F2026; color: #E5E5E5; border: 1px solid #2A2C34;
        }
        .stDataFrame { border: none; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: Your Photo & Profile ---
with st.sidebar:
    st.markdown("### Chitra")
    st.image("https://i.imgur.com/YourImgurID.png", width=160)  # replace with your actual Imgur URL
    st.markdown("High‑end AI tool to surface the latest LinkedIn content strategies.")

# --- Main Header & Description ---
st.markdown("## LinkedIntel – Free AI Tool")
st.markdown("Discover the top-performing LinkedIn content in your industry and role, and get an editable 7‑day content calendar—all in one place.")

# --- Input Section ---
st.markdown("#### Step 1: Tell me about yourself")
with st.form("plan_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", placeholder="e.g. Chitra")
        industry = st.selectbox("Industry", ["Marketing", "Product", "Design", "Tech", "Finance", "Consulting"], index=0)
    with col2:
        role = st.selectbox("Role", ["Marketing Manager", "Product Manager", "Designer", "Founder", "Content Creator", "Freelancer"], index=5)
        email = st.text_input("Email (optional)", placeholder="email@domain.com")
    go = st.form_submit_button("Generate Insights")

if go:
    st.markdown(f"**Hi {name}, generating current LinkedIn insights for {role} in {industry}…**")

    # --- Simulated Trend Output ---
    st.markdown("### 🔍 Top LinkedIn Posts")
    cols = st.columns(2)
    with cols[0]:
        st.markdown("- How AI is reshaping marketing in 2025")
        st.markdown("- 10 viral frameworks for content creators")
        st.markdown("- Freelancer to founder: 3‑year journey")
        st.markdown("- Visual storytelling tips for carousels")
        st.markdown("- Decoding LinkedIn algorithm 2025")
    with cols[1]:
        st.markdown("### 👥 Top Influencers")
        st.markdown("- Justin Welsh")
        st.markdown("- Katelyn Bourgoin")
        st.markdown("- Shaan Puri")
        st.markdown("- Amanda Natividad")
        st.markdown("- Ross Simmonds")

    st.markdown("### 🏷️ Trending Hashtags")
    st.write(["#MarketingStrategy", "#ContentCreation", "#LinkedInTips", "#GrowthHacking", "#FreelancerLife"])

    st.markdown("### 🛠️ Free AI Tools (by category)")
    cols = st.columns(3)
    tools = {
        "Writing": [("ChatGPT Free", "https://chat.openai.com"), ("Notion", "https://notion.com")],
        "Design": [("Canva", "https://canva.com"), ("Remove.bg", "https://remove.bg")],
        "Video": [("CapCut", "https://capcut.com"), ("Pexels Videos", "https://pexels.com")],
        "Audio": [("Audacity", "https://audacityteam.org")]
    }
    for i, (cat, items) in enumerate(tools.items()):
        with cols[i % 3]:
            st.markdown(f"**{cat}**")
            for name, url in items:
                st.markdown(f"- [{name}]({url})")

    # --- 7-Day Calendar ---
    st.markdown("### 📅 7‑Day Content Calendar")
    days = [f"Day {i+1}" for i in range(7)]
    posts = ["Carousel", "Poll", "Memes", "Text Post", "Video", "Carousel", "Quote"]
    topics = ["AI trends", "Ask audience", "Lighthearted meme", "Personal story", "Tool demo", "Industry insight", "Motivational CTA"]
    captions = ["Deep dive into AI today...", "What’s your biggest LinkedIn struggle?", "When client says…", "3 lessons I learned…", "Here’s how I use X tool", "The biggest myth in Y is…", "Don’t wait, create now."]
    times = ["10:00", "12:00", "09:30", "11:00", "14:00", "10:30", "08:45"]
    cta = ["Save this", "Vote below", "Tag someone", "Share your thoughts", "Try this tool", "Agree or disagree", "Drop a ❤️"]

    df = pd.DataFrame({
        "Day": days,
        "Post Type": posts,
        "Topic": topics,
        "Caption": captions,
        "Hashtags": ["#MarketingStrategy" for _ in days],
        "Best Time": times,
        "CTA": cta
    })
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV", csv, "LinkedIntel.csv")

    st.markdown("---")
    st.markdown("**💡 Tip:** Use this calendar as a daily guide—customize captions, swap media formats, and post at ideal times.")

# --- Footer ---
st.markdown("<div style='text-align:center; padding:10px;'>Built by Chitra with no‑code tools · Share on LinkedIn</div>", unsafe_allow_html=True)
