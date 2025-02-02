import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
import os
import tempfile
from dotenv import load_dotenv
load_dotenv()
# Load API key from secrets
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found. Please check your configuration.")

# Set Page Configuration
st.set_page_config(page_title="CineMind: AI-Driven Contextual Video Summarization", page_icon="🎥", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .title {text-align: center; font-size: 50px; font-weight: bold; color: #FF4B4B;}
        .subtitle {text-align: center; font-size: 22px; font-weight: 500; color: #6C757D;}
        .analyze-btn {background-color: #FF4B4B; color: white; font-size: 18px; padding: 10px 20px; border-radius: 10px;}
        .result-container {background-color: #f8f9fa; padding: 20px; border-radius: 10px; color: black;}
    </style>
    """,
    unsafe_allow_html=True
)

# Display Title & Subtitle
st.markdown('<h1 class="title">CineMind: AI-Driven Contextual Video Summarization 🎬</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Transform lengthy videos into concise summaries using AI.</p>', unsafe_allow_html=True)

# Author Section
st.markdown("### 🔥 Built with passion by **Muhammad Shoaib** 🚀")

# Cache Agent Initialization
@st.cache_resource()
def initialize_agent():
    return Agent(
        name="AI Video Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )

# Initialize agent
multimodel_agent = initialize_agent()

# File Uploader with Expander for Clean UI
with st.expander("📤 Upload Video File (mp4, mov, avi)"):
    video_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"], help="Upload a video for AI analysis.")

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name
    
    st.video(video_path, format="video/mp4", start_time=0)
    
    user_query = st.text_area("🔍 What insights are you seeking?", placeholder="Ask anything about the video content...")
    
    if st.button("Analyze Video", key="analyze_video_button", help="Click to process the video"):
        if not user_query:
            st.warning("Please enter a question to analyze the video.")
        else:
            try:
                with st.spinner("🚀 Processing video and gathering insights..."):
                    processed_video = upload_file(video_path)
                    
                    # Real-time progress update
                    st.info("Processing the video, please wait...")  
                    progress_bar = st.progress(0)  

                    for i in range(100):  
                        time.sleep(0.02)  
                        progress_bar.progress(i + 1)

                    
                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)
                    
                    analysis_prompt = f"""
                    Analyze the uploaded video for content and context. Respond to the following query using video insights and supplementary web search:
                    {user_query}
                    Provide a detailed, user-friendly, and actionable response.
                    """
                    
                    response = multimodel_agent.run(analysis_prompt, videos=[processed_video])
                    
                    # Display result in an interactive container
                    st.markdown("### 📊 Analysis Result")
                    st.markdown(f'<div class="result-container">{response.content}</div>', unsafe_allow_html=True)
            
            except Exception as error:
                st.error(f"⚠️ An error occurred: {error}")
            
            finally:
                if os.path.exists(video_path):
                    os.unlink(video_path)
