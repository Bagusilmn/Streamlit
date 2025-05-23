import os
import streamlit as st

# Runtime patch: jika `st.secrets` kosong (deployment), isi dari env
if not st.secrets:
    st.secrets._secrets = {
        "connections": {
            "internship_RLO": {
                "dialect": os.getenv("INTERNSHIP_RLO_DIALECT"),
                "driver": os.getenv("INTERNSHIP_RLO_DRIVER"),
                "host": os.getenv("INTERNSHIP_RLO_HOST"),
                "port": int(os.getenv("INTERNSHIP_RLO_PORT")),
                "database": os.getenv("INTERNSHIP_RLO_DATABASE"),
                "username": os.getenv("INTERNSHIP_RLO_USERNAME"),
                "password": os.getenv("INTERNSHIP_RLO_PASSWORD"),
            },
            "ADOMobile": {
                "spreadsheet": os.getenv("ADOMOBILE_SPREADSHEET")
            },
            "MarketCompetition": {
                "spreadsheet": os.getenv("MARKETCOMPETITION_SPREADSHEET")
            },
            "ADOIH": {
                "spreadsheet": os.getenv("ADOIH_SPREADSHEET")
            }
        },
        "auth": {
            "redirect_uri": os.getenv("REDIRECT_URI"),
            "cookie_secret": os.getenv("COOKIE_SECRET"),
        },
        "auth.google": {
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "server_metadata_url": os.getenv("GOOGLE_METADATA_URL"),
        }
    }

# Streamlit connection functions
from streamlit_gsheets import GSheetsConnection

def get_connection():
    return st.connection('internship_RLO', type='sql')

def gsheet_ADOMobile_connection():
    return st.connection("ADOMobile", type=GSheetsConnection)

def gsheet_ADOIH_connection():
    return st.connection("ADOIH", type=GSheetsConnection)

def gsheet_MarketCompetition_connection():
    return st.connection("MarketCompetition", type=GSheetsConnection)
