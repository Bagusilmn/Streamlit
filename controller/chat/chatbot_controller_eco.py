import os
import requests
import streamlit as st

def get_chatbot_response_eco(query):
    response = requests.post("https://beckendapprlo.streamlit.app/", json={"question": query})
    return response.json().get("result")
