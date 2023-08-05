import numpy as np
import pandas as pd

# Specifica il percorso del file .npy
file_path = 'dnn_output.npy'  # Sostituisci con il percorso del tuo file .npy

# Apri il file .npy e leggi i dati
data = np.load(file_path)

# Ora puoi utilizzare la variabile 'data' per accedere ai dati contenuti nel file .npy
# Verifica il tipo di variabile
tipo_variabile = type(data)

# Verifica se la variabile è un array NumPy
if isinstance(data, np.ndarray):
    # Verifica le dimensioni dell'array
    dimensioni = data.shape
    numero_dimensioni = data.ndim
    tipo_dati = data.dtype
else:
    print("La variabile non è un array NumPy.")

print("Tipo di variabile:", tipo_variabile)
if isinstance(data, np.ndarray):
    print("Dimensioni dell'array:", dimensioni)
    print("Numero di dimensioni dell'array:", numero_dimensioni)
    print("Tipo di dati dell'array:", tipo_dati)

# Creazione di un DataFrame da array bidimensionale
df = pd.DataFrame(data)

# Visualizzazione dei dati
print(df)