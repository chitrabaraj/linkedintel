import streamlit as st
import pandas as pd
import requests

st.title("LinkedIntel: LinkedIn Trend Finder")

st.write("Hey! I’m Chitra — marketer, creator, and your LinkedIn growth partner. LinkedIntel uncovers the top trending LinkedIn topics by industry or role to help you craft impactful content. Ready to elevate your LinkedIn game? Let’s connect!")

industry = st.text_input("Enter your Industry or Role")

if st.button("Find Trends"):
    if industry:
        st.write(f"Searching trends for: {industry}")

        # Call Perplexity API (replace with your API key)
        api_key = "YOUR_PERPLEXITY_API_KEY"
        query = f"Trending LinkedIn topics and hashtags for {industry} this week"
        
        response = requests.post(
            "https://api.perplexity.ai/v1/ask",
            json={"query": query},
            headers={"Authorization": f"Bearer {api_key}"}
        )
        data = response.json()
        
        # For demo purposes, replace below with actual extracted data
        trends = ["#MarketingTips", "#GrowthHacking", "#ContentStrategy"]
        
        # Generate 7-day calendar
        calendar = pd.DataFrame({
            "Day": [f"Day {i}" for i in range(1, 8)],
            "Content Topic": [f"Post idea about {trend}" for trend in trends*3][:7]
        })
        
        st.table(calendar)
        
        # Export CSV
        csv = calendar.to_csv(index=False).encode('utf-8')
        st.download_button("Download 7-day content calendar as CSV", csv, "LinkedIntelContentCalendar.csv", "text/csv")
    else:
        st.error("Please enter an industry or role")
