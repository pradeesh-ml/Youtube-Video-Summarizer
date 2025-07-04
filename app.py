
import streamlit as st
from googleapiclient.discovery import build
from langchain_community.llms import Ollama 
from youtube_video_summarizer import (
    get_video_id, 
    get_transcript_segments, 
    format_transcript_text,
    format_transcript_with_timestamps,
    generate_summary
)

st.set_page_config(
    page_title="YouTube Video Summarizer",
    layout='wide',
    initial_sidebar_state='expanded'
)

@st.cache_resource
def load_model():
    return Ollama(model="llama3:8b")

def get_video_details(api_key, video_id):
    try:
        yt = build('youtube', 'v3', developerKey=api_key)
        request = yt.videos().list(part='snippet', id=video_id)
        response = request.execute()
        snippet = response['items'][0]['snippet']
        return {
            'title': snippet['title'],
            'author': snippet['channelTitle'],
            'thumbnail': snippet['thumbnails']['high']['url']
        }
    except Exception as e:
        st.error(f"Failed to fetch video details: {e}")
        return None

st.title('YouTube Video Summarizer')
llm = load_model()

if 'video_details' not in st.session_state:
    st.session_state.video_details = None
if 'summary' not in st.session_state:
    st.session_state.summary = None
if 'formatted_transcript' not in st.session_state:
    st.session_state.formatted_transcript = None
if 'last_url' not in st.session_state:
    st.session_state.last_url = ""

with st.sidebar:
    st.header("Video Input")
    url = st.text_input("Enter YouTube URL:", key="youtube_url")
    API_KEY = st.secrets.get('YOUTUBE_API_KEY')

    if url != st.session_state.last_url:
        st.session_state.video_details = None
        st.session_state.summary = None
        st.session_state.formatted_transcript = None
        st.session_state.last_url = url

    summarize_button = st.button('Summarize', type="primary")

    if summarize_button and url:
        if not API_KEY:
            st.error("YOUTUBE_API_KEY is not found in Streamlit secrets.")
        else:
            video_id = get_video_id(url)
            if video_id:
                with st.spinner('Fetching video data and generating summary... This may take a moment.'):

                    st.session_state.video_details = get_video_details(API_KEY, video_id)
                    transcript_segments = get_transcript_segments(video_id)

                    if transcript_segments:
                        transcript_text = format_transcript_text(transcript_segments)
                        st.session_state.formatted_transcript = format_transcript_with_timestamps(transcript_segments, interval=65)
       
                        st.session_state.summary = generate_summary(llm, transcript_text)
                    else:
                        st.error("Could not retrieve transcript for this video. It might be disabled or unavailable.")
                        st.session_state.video_details = None
                        st.session_state.summary = None
            else:
                st.error("Invalid YouTube URL. Please enter a valid URL.")

if st.session_state.video_details:
    st.header("Video Details")
    details = st.session_state.video_details
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(details['thumbnail'], use_container_width=True)
    with col2:
        st.subheader(details['title'])
        st.caption(f"By: {details['author']}")
        
    st.divider()

    if st.session_state.summary:
        st.header("Video Summary")
        
        display_option = st.radio(
            "Display Options",
            ["Summary Only", "Summary with Transcript"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.markdown(st.session_state.summary)

        if display_option == "Summary with Transcript" and st.session_state.formatted_transcript:
            with st.expander("Show Full Transcript"):
                st.text_area(
                    'Formatted Transcript',
                    value=st.session_state.formatted_transcript,
                    height=400,
                    disabled=True
                )
else:
    st.info("Enter a YouTube URL in the sidebar and click 'Analyze Video' to begin.")
