import os
import matplotlib.pyplot as plt
import unicodedata
import pycountry

# Fonction pour sauvegarder une figure en utilisant le titre comme nom de fichier dans le dossier images_v3
def save_figure(title, output_dir):
    # Création du nom de fichier
    if title:
        filename = title.replace(" ", "_") + ".png"
    else:
        filename = "default_image_name.png"  # Nom par défaut si pas de titre

    # Création du chemin complet
    filepath = os.path.join(output_dir, filename)

    # Vérification et création du dossier s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sauvegarde de la figure
    plt.savefig(filepath)
    print(f"Figure sauvegardée dans {filepath}")



#  Fonction pour récuper tous les chemins d'un dossier contenant des fichers csv. 

def path_data(main_directory):
    # Vérifie si le chemin existe
    if not os.path.exists(main_directory):
        raise FileNotFoundError(f"Le répertoire spécifié n'existe pas : {main_directory}")

    # Liste pour stocker les chemins vers chaque fichier CSV
    csv_file_paths = []

    # Boucle pour parcourir tous les sous-dossiers et fichiers
    for root, dirs, files in os.walk(main_directory):
        for file in files:
            # Vérifie si le fichier est un fichier CSV
            if file.endswith('.csv'):
                # Construit le chemin complet et l'ajoute à la liste
                csv_file_paths.append(os.path.join(root, file))
    return csv_file_paths

def supprimer_accents(texte):
    # Supprime les accents en normalisant la chaîne de caractères
    texte_sans_accents = ''.join(c for c in unicodedata.normalize('NFD', texte) if unicodedata.category(c) != 'Mn')
    return texte_sans_accents

def format_chaine(texte):
    # Supprime les accents et met en minuscules
    texte_sans_accents = supprimer_accents(texte)
    return texte_sans_accents.lower()

# Fonction pour rajouter en index d'un dataset, le numéro du pays associé
def add_country(df, country_name):
    # Recherche du pays en utilisant pycountry
    country = next((c for c in pycountry.countries if c.name.lower() == country_name.lower()), None)
    
    # Vérification de la présence du pays dans pycountry
    if not country:
        raise ValueError(f"Erreur : le pays '{country_name}' n'est pas reconnu.")
    
    # Ajout du code numérique ISO du pays dans la colonne 'country_numeric' du DataFrame
    df['country_ISO'] = int(country.numeric)  # Conversion en entier pour éviter le format chaîne
    return df

def get_country_iso_numeric(country_name):
    # Recherche du pays en utilisant pycountry
    country = next((c for c in pycountry.countries if c.name.lower() == country_name.lower()), None)
    
    # Vérification de la présence du pays dans pycountry
    if not country:
        raise ValueError(f"Erreur : le pays '{country_name}' n'est pas reconnu.")
    
    # Retourne le code numérique ISO du pays en entier
    return int(country.numeric)



def add_scale(df, scale):
    # Normaliser le nom du pays
    scale = supprimer_accents(format_chaine(scale))
    
    # Liste des pays autorisés (exemple : France, Norvège)
    echelles_autorises = {'human': 1, 'building': 2, 'neighborhood':3, 'city':4, 'region':5, 'country':6}
    
    # Vérification du pays dans la liste des pays autorisés
    if scale not in echelles_autorises:
        raise ValueError(f"Erreur : l'echelle '{scale}' n'est pas reconnu.")
    
    # Affectation de la valeur spécifique en fonction du pays
    a = echelles_autorises[scale]
    df['scale'] = a  # Vous pouvez ajouter le code correspondant si nécessaire
    return df



#----------------------------------------------------------------
#Features fonction

import pandas as pd
import holidays

def add_holiday_and_day_columns(df, country_code):
    """
    Cette fonction prend en entrée un DataFrame avec une colonne "Date" au format datetime, 
    ainsi qu'un code de pays (ex: 'FR' pour la France).
    Elle ajoute deux colonnes:
      - "holiday": 1 si le jour est férié dans le pays spécifié, 0 sinon
      - "day": un numéro de jour de la semaine (1 pour lundi, 2 pour mardi, ..., 7 pour dimanche)

    Pays disponibles dans la bibliothèque holidays:
    - AR: Argentina
    - AT: Austria
    La liste des autres pays via print(holidays.list_supported_countries())
    Arguments:
    - df (pd.DataFrame): DataFrame contenant la colonne 'Date'
    - country_code (str): Code pays (ex: 'FR' pour la France)

    Retourne:
    - pd.DataFrame: DataFrame avec les colonnes "holiday" et "day" ajoutées.
    """
    # Assure-toi que la colonne "Date" est au format datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Crée un dictionnaire de jours fériés pour le pays spécifié
    country_holidays = holidays.CountryHoliday(country_code)

    # Ajoute la colonne 'holiday' avec 1 si c'est un jour férié, sinon 0
    df['holiday'] = df['Date'].dt.date.apply(lambda x: 1 if x in country_holidays else 0)
    
    # Ajoute la colonne 'day' avec le jour de la semaine (1 pour lundi, ..., 7 pour dimanche)
    df['day'] = df['Date'].dt.dayofweek + 1  # dt.dayofweek donne 0 pour lundi, donc on ajoute 1

    return df

def add_month_and_hours(df):
    # Créer une copie du DataFrame pour ne pas modifier l'original
    df_copy = df.copy()
    
    # S'assurer que la colonne "Date" est de type datetime
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    
    # Ajouter la colonne 'month' avec les mois de 1 à 12
    df_copy['month'] = df_copy['Date'].dt.month
    
    # Ajouter la colonne 'hours' avec les heures de 0 à 23
    df_copy['hours'] = df_copy['Date'].dt.hour
    
    # Supprimer la colonne "Date"
    df_copy = df_copy.drop(columns=['Date'])
    
    return df_copy

def count_nan_rows(df):
    # Compte le nombre de lignes où il y a au moins une valeur NaN
    return df.isna().any(axis=1).sum()

def check_completeness(df):
    missing_count = df.isna().sum()
    total_rows = len(df)
    print("Analyse des valeurs manquantes par colonne :\n", missing_count)
    print("\nNombre total de lignes:", total_rows)
    print("\nLignes contenant des valeurs manquantes:", df.isna().any(axis=1).sum())
    if missing_count.sum() == 0:
        print("\nLe DataFrame est complet (aucune valeur manquante).")
    else:
        print("\nLe DataFrame contient des valeurs manquantes.")


def interpolate_to_hourly(df):
    # Conversion de la colonne de date en format datetime pour faciliter la manipulation
    df['date'] = pd.to_datetime(df['date'])
    
    # Définir la colonne de date comme index pour faciliter la rééchantillonnage
    df = df.set_index('date')
    
    # Rééchantillonnage au pas horaire avec interpolation linéaire pour les valeurs numériques
    df_hourly = df.resample('H').interpolate(method='linear')
    
    # Réinitialiser l'index pour rendre la colonne 'date' disponible à nouveau
    df_hourly = df_hourly.reset_index()
    
    return df_hourly