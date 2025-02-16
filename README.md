# Youtube-Chatbot


## Overview
This Streamlit-based application enables users to interact with YouTube videos by extracting their transcripts and using Google's Gemini AI to answer questions based on the video's content.

## Features
- Extracts transcripts from YouTube videos.
- Uses Google Gemini AI to generate responses based on the video's transcript.
- Allows users to chat with the video content.

## Installation
### Prerequisites
Ensure you have Python installed (preferably Python 3.8 or higher) and the following dependencies:

```sh
pip install streamlit google-generativeai youtube-transcript-api
```

## Usage
1. Run the application:

```sh
streamlit run app.py
```

2. Enter your Google AI Studio API Key.
3. Provide a YouTube video URL.
4. Ask questions about the video content.

## Project Structure
```
├── app.py          # Main Streamlit app
├── README.md       # Documentation
```

## API Key Requirement
A Google AI Studio API Key is required to use Gemini AI. You can obtain one from [Google AI Studio](https://aistudio.google.com/).

## Limitations
- The app only works with videos that have transcripts available.
- Accuracy depends on the quality of the transcript and the AI model.

## License
This project is open-source under the MIT License.



