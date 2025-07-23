import streamlit as st
from perplexity_scraper import get_trending_posts

st.set_page_config(page_title="LinkedIntel", layout="centered")

st.title("🔍 LinkedIntel: Trending LinkedIn Content Ideas")
industry = st.text_input("Enter your industry or role (e.g., B2B marketing, HR, SaaS founder):")

if industry:
    st.info("Finding what's trending for you...")
    results = get_trending_posts(industry)
    if results:
        st.success("Here's what we found:")
        for idx, idea in enumerate(results, 1):
            st.markdown(f"**{idx}. {idea}**")
    else:
        st.error("No trends found. Try a different keyword.")
