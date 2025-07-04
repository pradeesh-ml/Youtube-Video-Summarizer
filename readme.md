# 🎥 YouTube Deep Dive Summarizer (Llama 3 + Streamlit)

Tired of clickbait titles and 2-hour videos that could’ve been a 5-minute read? This tool acts as your **personal research analyst**, transforming any YouTube video into a structured, detailed **Intelligence Brief**.

Powered by a **locally-run Llama 3 model**, this app goes beyond basic summarization — it intelligently filters out fluff and distills core content into actionable insights, deep explanations, and key quotes.

<p align="center">
  <img src="images/screenshot1.png" width="45%" alt="Screenshot 1">
  <img src="images/screenshot2.png" width="45%" alt="Screenshot 2">
</p>


---

## ✨ Key Features

- **🧠 Deep Dive Analysis**  
  The summary is broken into a multi-part brief:
  - ⚡ **Executive Brief**: One-sentence summary of the core thesis.
  - 🎯 **Actionable Intelligence**: Most critical insights and takeaways.
  - 📚 **Comprehensive Breakdown**: Detailed explanation of concepts, examples, and key messages.
  - 🎙️ **Key Quotables**: Impactful quotes from the video.

- **🚫 Intelligent Content Filtering**  
  Automatically skips:
  - “Like, comment, and subscribe”
  - Sponsored messages
  - Channel promotion and filler talk

- **🔒 100% Local & Private**  
  Runs fully on your machine using [**Ollama**](https://ollama.com/).  
  No external API calls for summarization — your data stays with you.

- **⚡ Fast & Interactive UI**  
  Built using **Streamlit** with session caching for smooth experience.

- **🎯 Precision Prompting**  
  Backed by a powerful system prompt designed to act like a professional analyst.

---

## 🛠️ Tech Stack

| Component         | Tool/Framework                  |
|------------------|---------------------------------|
| Language         | Python                          |
| UI Framework     | Streamlit                       |
| LLM Orchestration| LangChain                       |
| Local LLM Engine | Ollama                          |
| Model            | Llama 3 (8B recommended)        |
| YouTube Access   | `google-api-python-client`, `youtube-transcript-api` |

---

## 🚀 Getting Started

### 1. ✅ Prerequisites

- Python 3.8+
- [Ollama installed & running](https://ollama.com/)

### 2. 📥 Pull the Recommended Model

```bash
ollama pull llama3:8b

```


### 3.Clone and setup the project
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

