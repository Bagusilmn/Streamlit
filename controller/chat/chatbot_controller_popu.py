import os
import request
import streamlit as st

def get_chatbot_response_popu(query):
    response = requests.post("https://beckendapprlo.streamlit.app/", json={"question": query})
    return response.json().get("result")
