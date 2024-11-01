import gdown
import sqlite3
import pandas as pd
import numpy as np

def data_cleaning(data):

    df = data.loc[:, ~data.columns.duplicated()]

    df = df.drop(columns = ['cancellation_year', 'cancellation_month'])

        #Filtrando dados
    df_na = df[['education', 'salary']]
    df_filter = df_na.loc[df_na['education'] != 'College']
    df_calc_na = df_filter.loc[df_filter['education'] == 'Bachelor']

    #calculando as medidas
    mean_salary = df_calc_na['salary'].mean()
    median_salary = df_calc_na['salary'].median()

    #calculando a quantidade de NAN
    total_na = df['salary'].isna().sum()

    #definindo limites minimos e maximos
    lower_limit = min(mean_salary, median_salary)
    upper_limit = max(mean_salary, median_salary)

    #Gerando os valores dentro do range de NA com base nos limites
    fill_values = np.random.uniform(lower_limit, upper_limit, size = total_na)

    #Prenchendo os valores
    df.loc[df['salary'].isna(), 'salary'] = fill_values

    df['salary'] = df['salary'].apply(lambda x: np.abs(x) if x <= 0 else x)

    df['loyalty_card'] = df['loyalty_card'].replace({'Star':'Ametista', 'Nova': 'Onix', 'Aurora':'Rubi'})

    df['year'] = df['year'].astype(int)

    feature_selected = ['year', 'month', 'flights_booked','flights_with_companions', 'total_flights','distance', 
    'points_accumulated', 'salary','clv', 'loyalty_card','enrollment_type', 'marital_status']

    df = df[feature_selected]

    return df

