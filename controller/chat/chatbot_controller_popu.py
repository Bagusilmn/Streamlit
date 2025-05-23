import os
import requests
import streamlit as st

def get_chatbot_response_popu(query):
    try:
        response = requests.post("https://beckendapprlo.streamlit.app/", json={"question": query})

        # Log respons mentah
        print("Status:", response.status_code)
        print("Response:", response.text)

        # Pastikan response adalah JSON valid
        return response.json().get("result", "Tidak ada hasil dari server.")
    except requests.exceptions.RequestException as e:
        return f"⚠️ Gagal terhubung ke server: {e}"
    except ValueError as e:
        return f"⚠️ Response bukan JSON valid: {e}"
