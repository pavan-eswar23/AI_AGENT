# AI Assistant Dashboard

The **AI Assistant Dashboard** is a Streamlit-based application designed to streamline data extraction and enhance productivity. By integrating **Google Gemini 1.5 Pro** for AI-driven insights and **SerpAPI** for web search, it empowers users to query and extract valuable information efficiently. 

---

## Features

- **File Upload**: Supports CSV file uploads for batch processing.
- **Google Sheets Integration**: Use Google Sheet URLs as input data sources.
- **Web Search Integration**: Automates information retrieval using **SerpAPI**.
- **AI-Powered Insights**: Leverages **Google Gemini 1.5 Pro** to analyze text and extract key information.
- **Custom Queries**: Define templates (e.g., `Get the email of {entity}`) for tailored information extraction.
- **Downloadable Results**: Export results as a CSV file for further analysis.
- **User-Friendly Interface**: Simple and intuitive design built with Streamlit.
- **Scalability**: Handles large datasets efficiently for broader use cases.

---

## Setup Instructions

### Prerequisites

1. **Python**: Ensure Python 3.8 or above is installed.
2. **API Access**: Obtain the following API keys:
   - **SerpAPI Key**: [Get your SerpAPI Key](https://serpapi.com/users/sign_up).
   - **Google Gemini Key**: Requires access to Google Gemini AI. Contact [Google AI](https://ai.google/) for API details.

3. **Environment Variables**: Store API keys in a `.env` file:
   ```plaintext
   SERP_API_KEY=your_serp_api_key
   GEMINI_API_KEY=your_gemini_api_key
## Usage Guide

**Step 1**: Launch the Application
Open the app in your browser via the provided URL.

**Step 2**: Upload Your Data
Upload a CSV file or provide a Google Sheet URL with your dataset.

**Step 3**: Configure Query
Select the main column containing the entities (e.g., "Company Names").
Enter a custom query template (e.g., Get the email of {entity}).

**Step 4**: Extract Information
Click Run Query to process the data.
The app uses SerpAPI for web searches and Google Gemini AI to extract meaningful information.

**Step 5**: Review and Download
Review extracted information displayed in the app.
Download results as a CSV file using the Download CSV button.

# Technologies Used
**Streamlit**: Interactive web application framework.

**Google Gemini 1.5 Pro**: AI model for text generation and analysis.

**SerpAPI**: Web search API for automated queries.

## Python Libraries:

**pandas**: For data manipulation.

**requests**: For API communication.

**dotenv**: For managing environment variables.
# Output Video Link
(https://drive.google.com/file/d/13sZBHvV_NnktGaEpO5IUlpU-Pia8Jafp/view?usp=drive_link)
