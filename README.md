# AI Assistant Dashboard

This project, **AI Assistant Dashboard**, is a Streamlit-based web application designed to automate data extraction and enhance productivity. The dashboard integrates **Google Gemini 1.5 Pro** for AI-driven information extraction and **SerpAPI** for seamless web search capabilities. Users can upload datasets, define queries, and extract valuable insights effortlessly.

---

## Features

- **File Upload**: Upload CSV files for processing.
- **Google Sheets Integration**: Optionally input data via a Google Sheets URL.
- **Web Search Integration**: Fetch web search results using SerpAPI.
- **AI-Powered Information Extraction**: Uses Google Gemini 1.5 Pro for advanced text analysis and information extraction.
- **Custom Query Templates**: Define queries like `Get the email of {entity}` for targeted data extraction.
- **Downloadable Results**: Export extracted information as a CSV file.

---

## Setup Instructions

### Prerequisites

1. Python 3.8 or above installed.
2. Access to **SerpAPI** and **Google Gemini 1.5 Pro** with API keys.
3. Environment variables set up in a `.env` file:
   - `SERP_API_KEY`
   - `GEMINI_API_KEY`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pavan_eswar23/ai_agent.git
   cd ai_agent
