import os
import pandas as pd
import requests
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Set the API key for Google Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Create the model configuration for Gemini 1.5 Pro
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
)
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Generate a Comprehensive engaging blog post relevant to the given title \"Effects of Generative Ai\" and keywords \"Artificial Creativity , Ethical Implication , Technology Innovation , Machine Learning Applications , AI Impact on Society\". Make sure to incorporate these keywords in the blog post . The Blog should be Approximately( num_words ) words in length ,Suitable for an online audience(Ensure the Content is Original ,informative and maintains a consistent tone throughout.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Effects of Generative AI: Shaping Society and Technology**\n\n**Introduction**\n\nThe advent of Generative Artificial Intelligence (AI) has sparked a profound transformation across diverse sectors. This technology, empowered by machine learning algorithms, enables the creation of novel content, ranging from art and music to text and code. As Generative AI continues to evolve, it is imperative to explore its multifaceted effects on creativity, ethics, innovation, and society as a whole.\n\n**Artificial Creativity and the Impact on Human Expression**\n\nGenerative AI has emerged as a powerful tool for expanding the boundaries of human creativity. AI-generated content can complement and enhance human expression, fostering new ideas and sparking inspiration. However, it also raises questions about the role of originality and the value of human creativity. As AI-generated works become increasingly sophisticated, it is crucial to establish clear guidelines and foster conversations on authenticity and attribution.\n\n**Ethical Implications and the Responsibility of AI**\n\nThe rapid development of Generative AI has brought to the forefront ethical concerns. The ability of AI to generate deepfakes and spread misinformation poses a significant threat to trust and transparency. It is essential to develop robust ethical frameworks and regulations to ensure responsible use and prevent malicious applications of Generative AI.\n\n**Technology Innovation and the Role of Machine Learning**\n\nGenerative AI is a testament to the transformative power of machine learning. Machine learning algorithms learn patterns and generate new content based on vast datasets. This technology has the potential to revolutionize industries, from healthcare to entertainment, by automating tasks, improving efficiency, and creating novel solutions.\n\n**Applications in the Real World and the Impact on Society**\n\nThe applications of Generative AI are far-reaching and touch upon various aspects of our lives. In medicine, AI-generated models can aid in disease diagnosis and drug discovery. In education, personalized content and tailored learning experiences can be created. The impact of Generative AI on society is profound, with potential benefits ranging from enhanced productivity to improved access to information.\n\n**Conclusion**\n\nGenerative AI is a transformative force that has profound effects on creativity, ethics, innovation, and society. While it offers immense potential for advancing technology and human expression, it also presents challenges that must be carefully addressed. By fostering meaningful conversations, developing ethical guidelines, and leveraging the technology responsibly, we can harness the power of Generative AI to create a future that is both innovative and equitable.",
      ],
    },
  ]
)


# Streamlit UI Setup
st.title("AI Agent Dashboard")

# File upload section
uploaded_file = st.file_uploader("Upload a CSV file")
google_sheet_url = st.text_input("Enter Google Sheet URL (optional)")

# Load and display data
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV Data", df.head())

# Select main column for querying
if df is not None:
    main_column = st.selectbox("Select the main column", df.columns)
    prompt_template = st.text_input("Enter your query (e.g., 'Get the email of {company}')")

# Function to perform web search using SerpAPI
def search_web(query):
    params = {
        "api_key": SERP_API_KEY,
        "q": query
    }
    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code == 200:
        return response.json().get("organic_results", [])
    return []

# Updated function to extract information using Google Gemini 1.5 Pro
def extract_info(prompt, search_results):
    """
    Function to extract information using Google Gemini 1.5 Pro based on the given prompt and search results.
    
    :param prompt: The prompt to ask the model to extract information from.
    :param search_results: The text data (e.g., search results or a content snippet) to extract information from.
    
    :return: Extracted information as a string.
    """
    # Start a chat session with history and the current user prompt
    
    
    # Send the message to the chat session and get the response
    response = chat_session.send_message(search_results)
    
    # Return the extracted information from the response
    return response.text.strip()

# Processing the entities from the selected column
if st.button("Run Query") and df is not None and prompt_template:
    results = []
    for entity in df[main_column]:
        query = prompt_template.replace("{company}", entity)
        search_results = search_web(query)
        
        # Prepare web result text for LLM
        search_text = " ".join([result.get("snippet", "") for result in search_results])
        extraction_prompt = f"Extract the email for {entity} from the following information: {search_text}"
        
        # Extract the information using Gemini 1.5 Pro
        extracted_info = extract_info(extraction_prompt, search_text)
        results.append({"Entity": entity, "Extracted Info": extracted_info})

    # Display the results
    results_df = pd.DataFrame(results)
    st.write("Extracted Information")
    st.dataframe(results_df)

    # Download results as CSV
    csv = results_df.to_csv(index=False)
    st.download_button("Download CSV", csv, "extracted_info.csv")
