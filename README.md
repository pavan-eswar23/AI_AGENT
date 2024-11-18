# AI Assistant Dashboard

This project is a Streamlit-based AI-powered dashboard designed to automate data extraction and enhance productivity. It leverages **Google Gemini 1.5 Pro** for text generation and information extraction, and **SerpAPI** for web search integration. The dashboard is highly customizable, allowing users to upload datasets, query relevant information, and download results.

---

## Features

- **File Upload**: Upload CSV files for processing.
- **Google Sheets Integration**: Optionally provide a Google Sheet URL for input data.
- **Web Search Integration**: Fetches web search results using SerpAPI.
- **AI-Powered Information Extraction**: Utilizes Google Gemini 1.5 Pro to extract insights from web search results or other contexts.
- **Custom Queries**: Define query templates to extract specific information.
- **Download Results**: Export the extracted data as a CSV file for further use.

---

## Setup Instructions

### Prerequisites

1. Python 3.8 or above installed.
2. Access to **SerpAPI** and **Google Gemini 1.5 Pro** with API keys.
3. Environment variables set in a `.env` file:
   - `SERP_API_KEY`
   - `GEMINI_API_KEY`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
