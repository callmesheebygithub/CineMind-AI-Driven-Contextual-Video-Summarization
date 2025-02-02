Here's the `README.md` file for your project:

```markdown
# CineMind: AI-Driven Contextual Video Summarization 🎬

**CineMind** is an AI-powered platform that transforms lengthy videos into concise, insightful summaries. By leveraging Google's Gemini model, CineMind can analyze video content, answer specific questions, and provide detailed insights based on video context and supplementary web search.

## Features

- **AI Video Summarization**: Transform videos into easy-to-digest summaries.
- **Contextual Insights**: Ask questions and receive answers based on the video content.
- **Real-Time Processing**: The app processes your video and provides insights with a smooth, interactive experience.
- **Web Integration**: Uses AI and web tools for enhanced content analysis.

## Requirements

- Python 3.7 or later
- Streamlit
- Google Generative AI (Gemini) API
- DuckDuckGo for search integration
- Python libraries: `phi`, `google.generativeai`, `dotenv`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the **Google API key**:
   - Create a `.env` file in the root directory and add your API key:
     ```bash
     GOOGLE_API_KEY=your_api_key_here
     ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## How It Works

1. **Upload Video**: Upload a video in `.mp4`, `.mov`, or `.avi` format.
2. **Ask Questions**: Enter your questions about the video content in the text area.
3. **Analyze**: Click the "Analyze Video" button to process the video and get insights.
4. **View Results**: The app provides a contextual summary and analysis based on the uploaded video.

## Technologies Used

- **Streamlit**: For building the interactive web app.
- **Google Gemini Model**: For analyzing video content.
- **DuckDuckGo**: For supplementary web search.
- **Python**: The core programming language.
- **dotenv**: To manage API keys securely.

## Author

- **Muhammad Shoaib**  
  Built with passion 🚀
```
