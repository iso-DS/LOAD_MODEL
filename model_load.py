import streamlit as st
import tensorflow as tf
import numpy as np

# Charger le modèle
model = tf.keras.models.load_model('model.h5')

st.title('Prédiction des anomalies')

# Interface utilisateur
heartbeat = st.text_input('Entrer les valeurs de heartbeat séparées par des virgules (par exemple: 123,125,130,127)')

if heartbeat:
    # Convertir l'entrée en tableau numpy
    heartbeat_values = np.array([float(x) for x in heartbeat.split(',')]).reshape(1, 4, 1)

    # Effectuer la prédiction
    prediction = model.predict(heartbeat_values)

    st.write(f"Prédiction de l'anomalie : {prediction}")
