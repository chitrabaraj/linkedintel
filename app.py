import streamlit as st
import pandas as pd
import base64

# --- Page Config ---
st.set_page_config(
    page_title="LinkedIntel – Free AI Content Tool",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Dark Theme and Modern Look ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #e6e6e6; /* Light gray for text */
    }

    body {
        background-color: #0e1117; /* Dark background */
    }

    .stApp {
        padding: 2rem 3rem; /* More generous padding */
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff; /* White for headers */
        font-weight: 600;
    }

    /* Sidebar */
    .st-emotion-cache-vk33gh { /* Target the sidebar container */
        background-color: #1a1e26; /* Slightly lighter dark for sidebar */
        border-right: 1px solid #282c34;
        padding: 1rem;
    }
    .st-emotion-cache-vk33gh .stImage { /* Adjust image in sidebar */
        border-radius: 8px;
        margin-bottom: 1rem;
    }

    /* Containers and Cards */
    .st-emotion-cache-uf99v8 { /* Main container */
        background-color: #161b22; /* Darker background for main content area */
        border-radius: 12px;
        padding: 2.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    .st-emotion-cache-1ftrzg7 { /* Column containers */
        background-color: #1a1e26;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #282c34;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2f81f7; /* Primary blue */
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        transition: background-color 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #4b90f9;
        cursor: pointer;
    }

    .stDownloadButton>button {
        background-color: #10b981; /* Green for download */
        color: white;
        font-weight: 600;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        border: none;
        transition: background-color 0.2s ease-in-out;
    }
    .stDownloadButton>button:hover {
        background-color: #14cd91;
    }

    /* Input fields */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div>div {
        background-color: #0e1117;
        color: white;
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 0.75rem 1rem;
        transition: border-color 0.2s ease-in-out;
    }
    .stTextInput>div>div>input:focus,
    .stSelectbox>div>div>div>div:focus {
        border-color: #2f81f7;
        outline: none;
        box-shadow: 0 0 0 2px rgba(47, 129, 247, 0.3);
    }

    /* Links */
    a {
        color: #58a6ff;
        text-decoration: none;
        transition: color 0.2s ease-in-out;
    }
    a:hover {
        color: #8cc4ff;
        text-decoration: underline;
    }

    /* Table/DataFrame */
    .dataframe {
        color: #e6e6e6;
        background-color: #1a1e26;
        border-radius: 8px;
        overflow: hidden;
    }
    .dataframe th {
        background-color: #282c34;
        color: #ffffff;
        font-weight: 600;
        padding: 0.8rem;
    }
    .dataframe td {
        padding: 0.8rem;
        border-top: 1px solid #282c34;
    }
</style>
""", unsafe_allow_html=True)

# Function to encode image to base64
@st.cache_data
def get_image_as_base64(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
        return base64.b64encode(response.content).decode()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching image: {e}. Please ensure the image URL is correct and accessible.")
        return None

# Placeholder for actual AI integration (if you get API access)
# This function would call an LLM API to generate content dynamically
def get_ai_generated_content(role, industry):
    # This is where you would integrate with an LLM like Google Gemini or OpenAI GPT
    # For now, it's simulated based on input.
    # If you get an API key, replace this with actual API calls.

    # Example: Simulating different outputs based on industry/role
    if industry == "Marketing" and role == "Content Creator":
        post_themes = [
            "Latest AI tools for content marketing",
            "Building a personal brand on LinkedIn",
            "SEO strategies for LinkedIn articles",
            "Storytelling frameworks for engagement",
            "Leveraging short-form video on LinkedIn"
        ]
        hashtags = ["#ContentMarketing", "#LinkedInTips", "#PersonalBranding", "#AIContent", "#DigitalMarketing"]
        top_voices = [
            {"name": "Ann Handley", "linkedin": "https://www.linkedin.com/in/annhandley/"},
            {"name": "Seth Godin", "linkedin": "https://www.linkedin.com/in/sethgodin/"},
            {"name": "Gary Vaynerchuk", "linkedin": "https://www.linkedin.com/in/garyvaynerchuk/"}
        ]
        calendar_topics = [
            "How AI is transforming content creation",
            "Your biggest content marketing challenge & solution",
            "A relatable meme about content deadlines",
            "My journey to becoming a content creator",
            "A walkthrough of my favorite content planning tool",
            "Insights on recent content consumption trends",
            "Call to action for collaboration"
        ]
    elif industry == "Tech" and role == "Product Manager":
        post_themes = [
            "Agile methodologies in product development",
            "User feedback loops for product iteration",
            "The future of AI in product management",
            "Scaling product teams effectively",
            "Lessons from failed product launches"
        ]
        hashtags = ["#ProductManagement", "#TechProduct", "#Agile", "#AIinProduct", "#StartupLife"]
        top_voices = [
            {"name": "Marty Cagan", "linkedin": "https://www.linkedin.com/in/martycagan/"},
            {"name": "Julie Zhuo", "linkedin": "https://www.linkedin.com/in/juliezhuo/"},
            {"name": "Nir Eyal", "linkedin": "https://www.linkedin.com/in/nireyal/"}
        ]
        calendar_topics = [
            "Impact of AI on product roadmaps",
            "The most common product management challenge",
            "Humorous take on sprint reviews",
            "My journey into product management",
            "A deep dive into a product analytics tool",
            "Key metrics for product success",
            "Share your product development insights"
        ]
    else: # Default or generic content
        post_themes = [
            "AI in your field", "Behind-the-scenes work",
            "Frameworks & checklists", "Lessons from failure",
            "Community-driven questions"
        ]
        hashtags = ["#ContentStrategy", "#LinkedInGrowth", "#AIforProfessionals", "#Storytelling", "#CreatorTools"]
        top_voices = [
            {"name": "Justin Welsh", "linkedin": "https://linkedin.com/in/justinwelsh"},
            {"name": "Amanda Natividad", "linkedin": "https://linkedin.com/in/amandanatividad"},
            {"name": "Shaan Puri", "linkedin": "https://linkedin.com/in/shaanpuri"}
        ]
        calendar_topics = [
            "AI trends in your industry", "Audience pain point", "Relatable humor", "Personal journey",
            "Tool you use", "Market insight", "Motivational CTA"
        ]

    return {
        "post_themes": post_themes,
        "hashtags": hashtags,
        "top_voices": top_voices,
        "calendar_topics": calendar_topics
    }

# --- Sidebar ---
with st.sidebar:
    st.image("https://freeimage.host/images/2025/07/24/Fejzx7R.jpg", width=160, use_column_width="auto") # Better image handling
    st.markdown("### LinkedIntel")
    st.markdown("""
    Free AI tool by Chitra to help creators and professionals discover LinkedIn trends & build high-impact content calendars.
    """)
    st.markdown("[Connect on LinkedIn](https://linkedin.com/in/chitrabaraj)")
    st.markdown("---")
    st.markdown("Developed with ❤️ by Chitra")


# --- Hero Section ---
st.title("LinkedIntel – Free AI Tool for LinkedIn Content")
st.markdown("""
<p style='font-size:1.2rem; color:#b0b0b0;'>
Search what’s trending in your industry and generate a complete 7-day content calendar instantly.
</p>
""", unsafe_allow_html=True)

# --- Input Form ---
st.markdown("## Step 1: Tell us about yourself")
with st.form("user_info_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        industry = st.selectbox(
            "Select your Industry",
            [
                "Marketing", "Product", "Design", "SaaS", "E-commerce", "Finance", "HR", "Tech", "Freelancing",
                "Education", "Healthcare", "Consulting", "Real Estate", "Media", "Food & Beverage"
            ],
            key="industry_select"
        )
    with col2:
        role = st.selectbox(
            "Your Role",
            [
                "Founder", "Marketing Manager", "Product Manager", "Designer",
                "Content Creator", "Recruiter", "Growth Lead", "Freelancer",
                "Sales Professional", "Engineer", "Data Scientist", "Educator", "Consultant"
            ],
            key="role_select"
        )
    st.markdown("---") # Separator within the form
    submit_button = st.form_submit_button("✨ Generate My Content Plan ✨")

# --- Output Section ---
if submit_button:
    st.markdown("## Step 2: Your Personalized LinkedIn Content Plan")
    st.info(f"Generating insights for **{role}** in **{industry}**...")

    # Call the AI (simulated or actual) to get content
    ai_content = get_ai_generated_content(role, industry)

    st.markdown("### Trending Insights")
    col_trends, col_voices = st.columns(2)

    with col_trends:
        st.markdown("#### 💡 Top Performing Post Themes")
        for theme in ai_content["post_themes"]:
            st.markdown(f"- **{theme}**")
        st.markdown("") # Add a bit of space

        st.markdown("#### #️⃣ Trending Hashtags")
        st.markdown(" ".join([f"`{tag}`" for tag in ai_content["hashtags"]]))

    with col_voices:
        st.markdown("#### 👤 Top Voices to Follow")
        for voice in ai_content["top_voices"]:
            st.markdown(f"- [{voice['name']}]({voice['linkedin']})")

    st.markdown("---")

    # --- Free Tools ---
    st.markdown("### 🛠️ Free Tools to Boost Your Content Creation")
    tools = {
        "Writing & Scripting": {
            "Notion": "https://notion.so",
            "ChatGPT Free": "https://chat.openai.com",
            "Typefully": "https://typefully.com",
            "Google Docs": "https://docs.google.com"
        },
        "Design & Visuals": {
            "Canva": "https://canva.com",
            "Remove.bg": "https://remove.bg",
            "Looka (Logo)": "https://looka.com",
            "Unsplash (Photos)": "https://unsplash.com"
        },
        "Video & Editing": {
            "CapCut": "https://capcut.com",
            "Pexels Videos": "https://pexels.com/videos",
            "Runway ML (AI Video)": "https://runwayml.com",
            "DaVinci Resolve (Desktop)": "https://www.blackmagicdesign.com/products/davinciresolve/"
        }
    }

    tool_cols = st.columns(len(tools))
    for i, (category, links) in enumerate(tools.items()):
        with tool_cols[i]:
            st.markdown(f"**{category}**")
            for name, url in links.items():
                st.markdown(f"- [{name}]({url})")

    # --- 7 Day Calendar ---
    st.markdown("---")
    st.markdown("### 🗓️ Your 7-Day Content Calendar")
    calendar_data = {
        "Day": [f"Day {i+1}" for i in range(7)],
        "Post Type": ["Carousel", "Poll", "Meme", "Text Post", "Video", "Carousel", "Quote"],
        "Topic Suggestion": ai_content["calendar_topics"], # Dynamically generated topics
        "Ideal Time (IST)": ["10:00 AM", "12:00 PM", "09:30 AM", "11:00 AM", "02:00 PM", "10:30 AM", "08:45 AM"],
        "Call to Action": [
            "Save this post!", "Vote in the poll!", "Tag a friend!", "Share your thoughts!",
            "Try this tool!", "What's your perspective?", "Let's connect!"
        ]
    }
    calendar = pd.DataFrame(calendar_data)
    st.dataframe(calendar, use_container_width=True, hide_index=True) # hide_index for cleaner look

    csv = calendar.to_csv(index=False).encode()
    st.download_button(
        "Download 7-Day Calendar as CSV",
        csv,
        "LinkedIntel_Content_Calendar.csv",
        "text/csv",
        help="Download your personalized 7-day content calendar."
    )

# --- Footer ---
st.markdown("<hr style='margin-top: 3rem;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:0.9rem; color:#888;'>Built with ❤️ by Chitra · No-code. AI-powered. Trend-smart.</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:0.8rem; color:#555; margin-top:0.5rem;'><i>Disclaimer: This tool provides content suggestions. Always verify information and tailor content to your audience.</i></div>", unsafe_allow_html=True)
