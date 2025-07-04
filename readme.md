# YouTube Deep Dive Summarizer (Llama 3 & Streamlit)

Tired of clickbait titles and 2-hour videos that could have been a 5-minute read? This tool acts as your personal research analyst, transforming any YouTube video into a structured, detailed "Intelligence Brief."

Using a locally-run Llama 3 model, this application goes beyond simple summarization. It intelligently filters out promotional fluff ("like and subscribe!") and deconstructs the core content into actionable insights, detailed explanations, and key quotes.

![App Demo GIF](URL_TO_YOUR_DEMO_GIF)

---

### ✨ Key Features

- **Deep Dive Analysis**: Instead of a simple summary, the app generates a multi-part brief including:
  - **⚡ Executive Brief**: A one-sentence summary of the core thesis.
  - **🎯 Actionable Intelligence**: The most critical insights and takeaways.
  - **📚 Comprehensive Breakdown**: A detailed, educational explanation of the video's main points, concepts, and examples.
  - **🎙️ Key Quotables**: The most impactful quotes from the video.
- **Intelligent Content Filtering**: The prompt is specifically engineered to ignore and omit common YouTube creator jargon, such as requests to "like, subscribe, comment," sponsor messages, and self-promotion.
- **Completely Local & Private**: Powered by **Ollama**, the entire AI analysis runs on your local machine. No data is sent to external APIs, ensuring 100% privacy.
- **Interactive & Efficient UI**: Built with **Streamlit**, the app uses caching and session state for a smooth, responsive experience without unnecessary re-processing.
- **Advanced Prompt Engineering**: The quality of the output is driven by a highly detailed, role-playing system prompt designed to maximize the analytical capabilities of Llama 3.

### 🛠️ Tech Stack

- **Language**: Python
- **Web Framework**: Streamlit
- **LLM Orchestration**: LangChain
- **Local LLM Provider**: Ollama
- **LLM**: Llama 3 (8B parameter model recommended)
- **YouTube Integration**: `google-api-python-client`, `youtube-transcript-api`

---

### 🚀 Getting Started

Follow these steps to run the project locally.

#### 1. Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running.

#### 2. Install the Recommended LLM

For the best results with the detailed prompt, the 8-billion parameter Llama 3 model is recommended.

```sh
ollama pull llama3:8b

#### 3.Clone and setup the project
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

#### 4.Configure API Keys
- The app uses the YouTube Data API to fetch video details.

    1. Get a YouTube Data API v3 key from the Google Cloud Console.
    2. In your project's root directory, create a folder named .streamlit.
    3. Inside that folder, create a file named secrets.toml.
    4. Add your key to the file:
    # .streamlit/secrets.toml
    YOUTUBE_API_KEY = "YOUR_API_KEY_HERE"
#### 5. Run the App
- streamlit run app.py



```
