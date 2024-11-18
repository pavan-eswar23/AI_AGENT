import os
import google.generativeai as genai

# Set the API key for Google Gemini
genai.configure(api_key='AIzaSyAamVcILZqSaT4wkDl_Bx1V0nYkbAWoshg')

# Create the model configuration for Gemini 1.5 Pro
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create a GenerativeModel for Google Gemini 1.5 Pro
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # Replace with actual model name if needed
    generation_config=generation_config,
)

def extract_info(prompt, search_results):
    """
    Function to extract information using Google Gemini 1.5 Pro based on the given prompt and search results.
    
    :param prompt: The prompt to ask the model to extract information from.
    :param search_results: The text data (e.g., search results or a content snippet) to extract information from.
    
    :return: Extracted information as a string.
    """
    # Create a chat session with history and the current user prompt
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"{prompt} Here are the web results: {search_results}"
                ],
            }
        ]
    )
    
    # Send the message to the chat session and get the response
    response = chat_session.send_message(search_results)
    
    # Return the extracted information from the response
    return response.text.strip()

# Example usage of the function
search_results = """
    Here is some information I gathered from the web about a company:
    The company email is contact@company.com, and their headquarters is located in New York.
    You can visit the website at www.company.com for more details.
"""

prompt = "Extract the email address from the following information"
extracted_info = extract_info(prompt, search_results)

# Print the extracted information (in this case, the email)
print("Extracted Info:", extracted_info)
