import pandas as pd

def conteo_nulos_duplicados (df):

    registros_vacios = df.isna().sum().sum()
    registros_duplicados = df.duplicated().sum()
    
    return ['La cantidad de registros vacios es: '+ str(registros_vacios), 'La cantidad de registros duplicados es: ' + str(registros_duplicados)]

def outliers (df,column):
    # Calcula la media y la desviación estándar de la columna column
    mean_playtime = df[column].mean()
    std_playtime = df[column].std()

    # Define los límites para identificar outliers utilizando el método de 3 sigmas
    lower_limit = mean_playtime - 3 * std_playtime
    upper_limit = mean_playtime + 3 * std_playtime

    # Encuentra outliers
    outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]

    # Imprime los outliers
    if outliers.empty:
        return ['No se encontraron outliers']
    else:
        return outliers