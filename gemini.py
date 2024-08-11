
from dotenv import load_dotenv # Load environment variables from .env file 
load_dotenv() # Load environment variables from .env file 


import streamlit as st # Streamlit library for building web applications 
import google.generativeai as genai # Google generative AI library for generating content 
import os # Operating system dependent functionality 

genai.configure(api_key="GOOGLE_API_KEY") # Configure generative AI model with Google API key 


from pyngrok import ngrok # Public URL for exposing local web server 

model = genai.GenerativeModel("gemini-pro") # Initialize generative AI model (Gemini) 

chat = model.start_chat(history=[]) #To store the chat

def get_gemini(question): # Function to get response from generative AI model (Gemini) 
  response = model.generate_content(question) # Generate response from generative AI model (Gemini) 
  return response.text # Return response from generative AI model (Gemini) 


st.set_page_config(page_title="AI Chatbot") # Set page title of web application 
st.header("AI Chatbot") # Add header to web application 

if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []
input = st.text_input("input", key="input") # Add input text box to web application 
submit = st.button("submit")    # Add submit button to web application 

if submit and input: # If submit button is clicked 
  output = get_gemini(input) # Get response from generative AI model (Gemini)

  st.session_state['chat_history'].append(['You', input])
  
  st.subheader("output") # Add subheader to web application 

  st.write(output) # Display response from generative AI model (Gemini)
  st.session_state['chat_history'].append(("Bot", output))

st.subheader("The Chat history is")

for role,text in st.session_state["chat_history"]:
  st.write(f'{role}:{text}')
