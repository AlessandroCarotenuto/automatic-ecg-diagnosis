import h5py
import csv

def hdf5_to_csv(hdf5_file, csv_file):
    # Apre il file HDF5 in modalità lettura
    with h5py.File(hdf5_file, 'r') as f:
        # Accedi ai dati del tensore 3D (sostituisci 'nome_del_tensore' con il nome effettivo)
        if 'tracings' in f:
            dataset = f['tracings']
            data = dataset[:]  # Ottieni tutti i dati del tensore

            # Scrivi i dati in un file CSV
            with open(csv_file, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)

                # Scorrere i dati del tensore e scriverli nel file CSV
                for i in range(data.shape[0]):
                    for j in range(data.shape[1]):
                        for k in range(data.shape[2]):
                            csvwriter.writerow([i, j, k, data[i, j, k]])

# Esempio di utilizzo
hdf5_file = 'data\ecg_tracings.hdf5'  # Sostituisci con il percorso del file HDF5
csv_file = 'ecg_tracings.csv'    # Sostituisci con il percorso desiderato per il file CSV

hdf5_to_csv(hdf5_file, csv_file)
