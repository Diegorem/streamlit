import streamlit as st
import pandas as pd
from google.cloud import firestore

service_account = firestore.Client.from_service_account_json("keys.json")

csv = pd.read_csv("movies.csv")

df = pd.DataFrame(csv)

for movie in df:
    print(movie)
