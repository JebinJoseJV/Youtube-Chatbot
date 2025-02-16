import tempfile
import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from typing import Tuple

def setup_gemini(api_key: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    return model

def extract_video_id(video_url: str) -> str:
    if "youtube.com/watch?v=" in video_url:
        return video_url.split("v=")[-1].split("&")[0]
    elif "youtube.com/shorts/" in video_url:
        return video_url.split("/shorts/")[-1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL")

def fetch_video_data(video_url: str) -> Tuple[str, str]:
    try:
        video_id = extract_video_id(video_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry["text"] for entry in transcript])
        return "Unknown", transcript_text  # Title is set to "Unknown" since we're not fetching it
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return "Unknown", "No transcript available for this video."


st.title("Chat with YouTube Video 📺")
st.caption("This app allows you to chat with a YouTube video using Gemini AI")


gemini_api_key = st.text_input("Google AI Studio API Key", type="password")


if gemini_api_key:
    model = setup_gemini(gemini_api_key)
    
    
    video_url = st.text_input("Enter YouTube Video URL", type="default")
    
    
    if video_url:
        try:
            title, transcript = fetch_video_data(video_url)
            if transcript != "No transcript available for this video.":
                st.success(f"Added video '{title}' to knowledge base!")
            else:
                st.warning(f"No transcript available for video '{title}'. Cannot add to knowledge base.")
        except Exception as e:
            st.error(f"Error processing video: {e}")
        
        
        prompt = st.text_input("Ask any question about the YouTube Video")
        
        
        if prompt:
            try:
                response = model.generate_content(f"Here is a video transcript: {transcript}\n\n{prompt}")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error chatting with the video: {e}")
