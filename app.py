# Import all necessary libraries
import streamlit as st
import openai
import json
import requests

# Define and structure HTML/CSS template
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Favicon and tab title
local_css("style.css")
st.set_page_config(page_title="Ingredient2Recipe", page_icon="🌽", layout='centered')

# Title and Intro
st.title("Ingredient2Recipe")
st.write("Enter ingredients available to you and we'll suggest a recipe!")

# Input box for users to enter their OpenAI API key
apiKey= st.text_input("Enter your OpenAI API Key", type="password")

ingredients= st.text_input("Enter the ingredients you have:")

if st.button('Submit'):
    openai.api_key = apiKey

    # Use openai.ChatCompletion to fetch possible recipes from the GPT-4 model
    message = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'What can I make with '+ingredients+'?'}]
    response = openai.ChatCompletion.create[model="gpt-4",messages=message]

    # Extract the message content
    message_content = response.choices[0].message.content.strip()

    # Display the suggested recipe
    st.write("Here's a recipe suggestion:")
    st.write(message_content)

 else:
    st.write("Please enter some ingredients!")