import requests
import streamlit as st

def get_groq_response(input_text, target_language):
    json_body = {
        "input": {
            "language": target_language,
            "text": f"{input_text}"
        },
        "config": {},
        "kwargs": {}
    }
    response = requests.post("http://localhost:8000/chain/invoke", json=json_body)

    try:
        response_data = response.json()
        output = response_data.get("output", "No result field in response")
        return output
    except ValueError:
        return "Error: Invalid JSON response"

# Streamlit app configuration
st.set_page_config(page_title="LLM Text Converter", page_icon="🌐", layout="centered")

# Custom CSS for modern styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        
        .stTextInput > label {
            font-size: 20px;
            font-weight: 500;
            color: #f0f0f0;
            margin-bottom: 10px;
        }
        .stTextInput > div, .stSelectbox > div {
            background: rgba(255, 255, 255, 0.1);
            padding: 12px;
            border-radius: 12px;
            border: 1px solid #fff;
            font-size: 18px;
        }
        .stButton > button {
            background-color: #ff7e5f;
            background-image: linear-gradient(135deg, #ff7e5f, #feb47b);
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        .stButton > button:hover {
            background-image: linear-gradient(135deg, #feb47b, #ff7e5f);
        }
        .output-container {
            margin-top: 30px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            font-size: 22px;
            font-weight: 500;
            line-height: 1.6;
            color: #fff;
            text-align: center;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🌐 Text Translator")
st.markdown(" Just type in your text, select the target language, and get an instant translation!")

# Text input
input_text = st.text_input("Enter the text : ")

# Language selection
languages = {
    "French": "French",
    "Spanish": "Spanish",
    "German": "German",
    "Italian": "Italian",
    "Chinese": "Chinese",
    "Japanese": "Japanese",
    "Korean": "Korean"
}
target_language = st.selectbox("Select the target language", options=list(languages.values()))

# Display output
if input_text:
    output_text = get_groq_response(input_text, target_language)
    st.markdown(f'<div class="output-container">{output_text}</div>', unsafe_allow_html=True)
