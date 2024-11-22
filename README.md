# Description des données

## Label
- **Consommation** : exprimée en mégawatts (MW).

## Features
Les caractéristiques utilisées sont les suivantes : 

1. **Température** : exprimée en degrés Celsius (°C).  
2. **Humidité** : exprimée en pourcentage (%).  
3. **Force du vent** : exprimée en mètres par seconde (m/s).  
4. **Numéro du pays** : selon la norme ISO des codes pays.  
5. **Échelle** : valeur entière comprise entre 1 et 6.  
6. **Jour férié** : indicateur binaire (0 = jour normal, 1 = jour férié).  
7. **Jour de la semaine** : valeur entière de 1 à 7 (1 = lundi, 7 = dimanche).  
8. **Mois** : valeur entière de 1 à 12 (1 = janvier, 12 = décembre).  

---

## Sources des données

### 1. **Données de consommation d'électricité**

Les données relatives à la consommation d'électricité par pays proviennent de :

- **Source :** [Nom de la source de données](lien_vers_la_source)
- **Fréquence :** [quotidienne, hebdomadaire, mensuelle, etc.]
- **Période :** [dates de début et fin]
- **Format :** [CSV, API, Base de données, etc.]

**Exemple de données :**
- [Exemple de valeur : Pays, Consommation (MW), Date]

---

### 2. **Données météorologiques**

Les données météorologiques (température, humidité, force du vent) proviennent de :

- **Source :** [Nom de la source de données](lien_vers_la_source)
- **Fréquence :** [quotidienne, horaire, etc.]
- **Période :** [dates de début et fin]
- **Format :** [API, CSV, etc.]

**Exemple de données :**
- [Exemple de valeur : Pays, Température (°C), Humidité (%), Vent (m/s), Date]

---

### 3. **Données sur les jours fériés**

Les informations sur les jours fériés sont récupérées depuis :

- **Source :** [Nom de la source de données](lien_vers_la_source)
- **Fréquence :** [annuelle, spécifique, etc.]
- **Période :** [dates de début et fin]
- **Format :** [API, fichier CSV, etc.]

**Exemple de données :**
- [Exemple de valeur : Pays, Jour férié (0/1), Date]

---

### 4. **Autres données (par exemple, code du pays, jour de la semaine, mois)**

- **Code du pays** : Les codes pays sont fournis par la norme ISO 3166-1 alpha-2.
- **Jour de la semaine** : Ces données sont extraites directement à partir des dates.
- **Mois** : De même, les mois sont extraits à partir des dates associées aux autres données.