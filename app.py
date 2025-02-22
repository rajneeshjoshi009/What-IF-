import streamlit as st
import logging
import google.generativeai as genai
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Google AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_creative_response(scenario):
    """Generate a creative response using Google's Gemini model"""
    try:
        if not scenario.lower().startswith("what if"):
            scenario = f"What if {scenario}"

        # Define a humorous chatbot personality
        personality = (
            "You are a funny, sarcastic, and witty AI that loves answering hypothetical 'What If' questions in a humorous way. "
            "Make your responses entertaining, use jokes, and add a playful tone. Keep the answer engaging and fun!"
        )

        # Use Google's Gemini Pro model
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"{personality}\nUser: {scenario}\nAI:")

        return response.text.strip()
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return "Oops! My circuits got tangled! Please try again with a different question. 🤖💥"

def main():
    logger.info("Starting What-If Machine app...")

    try:
        # Page config
        st.set_page_config(
            page_title="What-If Machine",
            page_icon="🤔",
            layout="centered",
            initial_sidebar_state="collapsed"
        )
        logger.info("Page config set successfully")

        # Custom CSS
        st.markdown("""
            <style>
            .stApp {
                max-width: 100%;
                padding: 1rem;
                background: linear-gradient(to bottom right, #1E2130, #2C3E50);
            }
            .stTextArea > div > div > textarea {
                font-size: 1.1rem;
                background-color: rgba(255, 255, 255, 0.1) !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                color: #FFFFFF !important;
            }
            .stButton > button {
                width: 100%;
                padding: 0.5rem;
                font-size: 1.2rem;
                background: linear-gradient(45deg, #FF4B4B, #FF8F8F) !important;
                border: none !important;
                color: white !important;
                transition: transform 0.2s ease !important;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
            }
            .css-1d391kg {
                padding: 1rem 0.5rem;
            }
            .stTitle {
                background: linear-gradient(120deg, #FF4B4B, #FF8F8F);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 2.5rem !important;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            }
            .stSelectbox > div > div {
                background-color: rgba(255, 255, 255, 0.1) !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                color: #FFFFFF !important;
            }
            .stMarkdown {
                color: #FFFFFF !important;
            }
            .stSuccess {
                background-color: rgba(40, 167, 69, 0.2) !important;
                border-color: rgba(40, 167, 69, 0.3) !important;
            }
            .stInfo {
                background-color: rgba(0, 123, 255, 0.2) !important;
                border-color: rgba(0, 123, 255, 0.3) !important;
            }
            .stWarning {
                background-color: rgba(255, 193, 7, 0.2) !important;
                border-color: rgba(255, 193, 7, 0.3) !important;
            }
            @media (max-width: 640px) {
                .stTitle {
                    font-size: 1.8rem !important;
                }
                .stMarkdown {
                    font-size: 1rem;
                }
            }
            </style>
        """, unsafe_allow_html=True)

        # Title and description
        st.title("🤔 What-If Machine")
        st.markdown("""
        Ever wondered about life's craziest "What If" questions? 
        Type your scenario below and let's explore the possibilities using AI!
        """)

        logger.info("UI elements rendered successfully")

        # Input for the what-if scenario
        scenario = st.text_area(
            "Type your 'What If' scenario here:",
            placeholder="Example: What if cats could talk?",
            height=80
        )

        # Category selection
        category = st.selectbox(
            "Choose scenario type:",
            ["Funny", "Scientific", "Magical", "Historical", "Random"]
        )

        # Generate response button
        if st.button("🎲 Get Creative Answer!", type="primary"):
            if scenario:
                with st.spinner("🤔 Thinking up something creative..."):
                    response = get_creative_response(scenario)
                    st.success("### Here's what might happen...")
                    st.markdown(f"## {response}")
                    st.markdown("---")
                    st.info(
                        "**Fun Fact:** This response was generated using AI magic! ✨"
                    )
            else:
                st.warning("Please type a 'What If' scenario first! 🤔")

        st.markdown("---")
        st.markdown("""
        💫 Powered by Google's Gemini AI and digital magic!

        Share your wildest "What If" ideas and see what happens!
        """)

        logger.info("App running successfully")

    except Exception as e:
        logger.error(f"Error in main app: {str(e)}")
        st.error("Oops! Something went wrong. Please try refreshing the page.")

if __name__ == "__main__":
    main()