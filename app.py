import streamlit as st
import datetime

# --- Branding ---
st.set_page_config(page_title="LinkedIntel by Chitra", page_icon="📊")

# Profile + Intro
st.image("https://chat.openai.com/mnt/data/file-WoTfKVgMU6xUr5fyG21t9V", width=120)
st.markdown("""
### Hey, I’m Chitra 👋  
I built **LinkedIntel** to help you show up smarter on LinkedIn.  
Want help with your personal brand? [Connect with me on LinkedIn](https://linkedin.com/in/chitrabaraj)
""")

# --- Input Form ---
st.markdown("#### Tell me about you:")

with st.form("input_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    industry = st.text_input("Your Industry")
    role = st.selectbox("Your Role", [
        "Marketing Manager", "Product Manager", "Designer",
        "Founder", "Content Creator", "Recruiter",
        "Analyst", "Sales Executive", "Freelancer"
    ])
    submitted = st.form_submit_button("Trend Builder")

if submitted:
    st.success(f"Awesome, {name}! We’re fetching LinkedIn trends for a {role} in {industry}...")
    st.markdown("🔄 *(Trend data, influencers, hashtags, and tools will show here in Step 3)*")
    st.markdown("📅 *(Auto-generating a content calendar next...)*")
