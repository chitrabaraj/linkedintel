import streamlit as st
import pandas as pd
from datetime import datetime

# --- Page Settings ---
st.set_page_config(
    page_title="LinkedIntel by Chitra",
    page_icon="📊",
    layout="wide"
)

# --- Sidebar Branding ---
with st.sidebar:
    st.image("https://i.imgur.com/Jz4X1kO.png", width=150)  # You can upload your own image and host it on Imgur
    st.markdown("### Hey, I’m Chitra 👋")
    st.markdown("""
    I built **LinkedIntel** to help you show up smarter on LinkedIn.

    Want help with your personal brand?  
    👉 [Connect with me on LinkedIn](https://linkedin.com/in/chitrabaraj)
    """)
    st.markdown("---")
    st.markdown("💌 Reach me: hellochitraba@gmail.com")

# --- Main Section ---
st.title("🚀 LinkedIntel – LinkedIn Trend Planner")
st.markdown("Tell me about you and I’ll build your 7-day LinkedIn calendar with smart trend insights ✨")

# --- Input Form ---
with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name", placeholder="e.g., Chitra")
        email = st.text_input("Your Email")

    with col2:
        industry = st.text_input("Your Industry", placeholder="e.g., Marketing")
        role = st.selectbox("Your Role", [
            "Marketing Manager", "Product Manager", "Designer",
            "Founder", "Content Creator", "Recruiter",
            "Analyst", "Sales Executive", "Freelancer"
        ])

    submitted = st.form_submit_button("⚡ Build My Plan")

# --- Output Section ---
if submitted:
    st.success(f"Awesome, {name}! Here's what’s trending for a **{role}** in **{industry}** 👇")

    st.markdown("## 🔥 Top LinkedIn Trends")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔗 Top 5 LinkedIn Posts")
        st.markdown("""
        1. [How AI is transforming marketing in 2025](https://linkedin.com)
        2. [10 viral frameworks for content creators](https://linkedin.com)
        3. [From freelancer to founder: 3-year journey](https://linkedin.com)
        4. [Visual storytelling tips for carousels](https://linkedin.com)
        5. [LinkedIn algorithm decoded in 2025](https://linkedin.com)
        """)

    with col2:
        st.markdown("### 👤 Top 5 Influencers")
        st.markdown("""
        - [Justin Welsh](https://linkedin.com)
        - [Katelyn Bourgoin](https://linkedin.com)
        - [Shaan Puri](https://linkedin.com)
        - [Amanda Natividad](https://linkedin.com)
        - [Ross Simmonds](https://linkedin.com)
        """)

    st.markdown("### 🏷️ Top 10 Hashtags")
    st.write(["#MarketingStrategy", "#ContentCreation", "#LinkedInTips", "#GrowthHacking", "#FreelancerLife",
              "#PersonalBrand", "#AIforMarketing", "#Storytelling", "#SocialSelling", "#CreatorEconomy"])

    st.markdown("### 🛠️ Free Tools to Use")
    st.write([
        "🧠 ChatGPT Free", "🎨 Canva", "✍️ Notion", "📊 Tally.so", "📷 Pexels", 
        "📹 CapCut", "🧼 Remove.bg", "📈 Google Trends", "📌 Typefully", "🖌️ Looka"
    ])

    st.markdown("---")
    st.markdown("## 📅 7-Day LinkedIn Content Calendar")
    
    calendar_data = {
        "Day": [f"Day {i+1}" for i in range(7)],
        "Post Type": ["Carousel", "Poll", "Meme", "Text Post", "Video", "Carousel", "Quote"],
        "Topic": [
            "AI Trends in Marketing", "Audience Pain Points", "Marketing Humor", 
            "Personal Story", "Tool Demo", "Industry Insight", "Motivational CTA"
        ],
        "Caption": [
            "Here's how AI is changing marketing (and how to stay ahead) 🧠",
            "What's your biggest LinkedIn struggle? 🗳️",
            "POV: Client wants it viral in 2 days 😂",
            "3 things I wish I knew before freelancing…",
            "Here’s how I use Canva + Notion to plan content 🔧",
            "The biggest myth in growth marketing is…",
            "Don’t wait to be chosen. Start creating. 🚀"
        ],
        "Hashtags": [
            "#AIforMarketing #LinkedInTips",
            "#Poll #PersonalBrand",
            "#MarketingMeme #Humor",
            "#CareerTips #FreelancerLife",
            "#Canva #CapCut #Productivity",
            "#GrowthMarketing #ContentStrategy",
            "#Motivation #StartNow"
        ],
        "Best Time to Post": [
            "10:00 AM", "12:00 PM", "9:30 AM", "11:00 AM", "2:00 PM", "10:30 AM", "8:45 AM"
        ],
        "CTA": [
            "Save this!", "Vote below!", "Tag a friend!", "Share your story", 
            "Try this tool", "Agree or disagree?", "Drop a ❤️ if you relate"
        ]
    }

    df = pd.DataFrame(calendar_data)
    st.dataframe(df, use_container_width=True)

    # Download Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Calendar as CSV",
        data=csv,
        file_name='LinkedIntel_Calendar.csv',
        mime='text/csv',
    )

    st.markdown("✅ Your LinkedIn calendar is ready. Now go post like a pro 💼")
