import streamlit as st
import pickle
import pandas as pd
import numpy as np
from data_preprocessing import data_cleaning


# Configurar a página
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title('Otimização de ofertas comerciais de passagens aéreas')

# Carregar dados
df_raw = pd.read_csv('data/flight_data.csv')
df = data_cleaning(df_raw)

df2 = pd.read_csv('data/flight_.csv')
df2 = df2[df.columns]

# Carregar o classificador
with open('model/decision_tree.pkl', 'rb') as file:
    classifier = pickle.load(file)

# Carregar scalers  
scalers = {}
scaler_files = [
    'salary_scaler.pkl', 'clv_scaler.pkl', 
    'year_scaler.pkl', 'month_scaler.pkl', 
    'flights_booked_scaler.pkl', 'flights_with_companions_scaler.pkl', 
    'total_flights_scaler.pkl', 'distance_scaler.pkl', 
    'points_accumulated_scaler.pkl'
]

for scaler_file in scaler_files:
    feature_name = scaler_file.replace('_scaler.pkl', '')
    try:
        with open(f'model/encoder/{scaler_file}', 'rb') as file:
            scalers[feature_name] = pickle.load(file)
    except FileNotFoundError:
        st.warning(f"O scaler '{scaler_file}' não foi encontrado.")

# Função para classificar o modelo de ML
def prediction(features):
    return classifier.predict_proba([features])

# Página principal
col3, col4 = st.columns(2)

with col3:
    year_option = st.selectbox("Ano de viagem", df['year'].unique())
    month_option = st.select_slider("Mês de viagem:", sorted(df['month'].unique()))
    flights_booked_option = st.select_slider("Quantidade de voos agendados:", sorted(df['flights_booked'].unique()))
    flights_with_companions_option = st.select_slider("Numero de voos com acompanhantes:", sorted(df['flights_with_companions'].unique()))
    total_flights_option = st.select_slider("Quantidade de voos totais:", sorted(df['total_flights'].unique()))
    

with col4:
    marital_status_option = st.selectbox("Status Cívil:", df['marital_status'].unique())
    distance_option = st.select_slider("Distancia de voo:", sorted(df['distance'].unique()))
    points_accumulated_option = st.select_slider("Pontos acumulados:", sorted(df['points_accumulated'].unique()))
    clv_option = st.select_slider("CLV (Customer Lifetime Value)", sorted(df['clv'].unique()))
    salary_option = st.select_slider("Renda do cliente:", sorted(df2['salary'].unique()))
enrollment_type_option = st.selectbox("Tipo de pacote", df['enrollment_type'].unique())
# Botão para classificar os dados
if st.button("Teste de probabilidade de adesão"):
    try:
        # Escalar todas as features
        scaled_features = [
            scalers['year'].transform(np.array([[year_option]]))[0, 0],
            scalers['month'].transform(np.array([[month_option]]))[0, 0],
            scalers['flights_booked'].transform(np.array([[flights_booked_option]]))[0, 0],
            scalers['flights_with_companions'].transform(np.array([[flights_with_companions_option]]))[0, 0],
            scalers['total_flights'].transform(np.array([[total_flights_option]]))[0, 0],
            scalers['distance'].transform(np.array([[distance_option]]))[0, 0],
            scalers['points_accumulated'].transform(np.array([[points_accumulated_option]]))[0, 0],
            scalers['salary'].transform(np.array([[salary_option]]))[0, 0],
            scalers['clv'].transform(np.array([[clv_option]]))[0, 0],
        ]

        # Mapeando as variáveis categóricas
        enrollment_type_mapped = 1 if enrollment_type_option == 'Standard' else 2
        marital_status_mapped = {'Divorced': 1, 'Single': 2, 'Married': 3}.get(marital_status_option, 0)

        features = scaled_features + [enrollment_type_mapped, marital_status_mapped]

        # Chamar a função de previsão
        y_prob = prediction(features)

        # Exibir as probabilidades
        rubi_prob, onix_prob, ametista_prob = np.round(y_prob[0] * 100, 2)

        # Determinar a classe majoritária
        classes = ["Rubi", "Onix", "Ametista"]
        probabilities = [rubi_prob, onix_prob, ametista_prob]
        major_class = classes[np.argmax(probabilities)]
        major_prob = np.max(probabilities)

        # Exibir os resultados
        with st.expander("Resultados da Classificação", expanded=True):
            for class_name, probability in zip(classes, probabilities):
                st.progress(probability / 100, text=f"{class_name}: {probability}%")
            st.success(f"O programa de fidelidade **{major_class}** é o mais propenso para o cliente com uma probabilidade de **{major_prob}%** de adesão.")

    except Exception as e:
        st.error(f"Erro ao classificar: {e}")


