## Table des matières
1. [Projet](#projet)
2. [Data Pipeline](#data-pipeline)
3. [Ad-hoc](#ad-hoc)
4. [Sql Requests](#sql-requests)

## Projet
***
Python est le langage de programmation utiliser pour développer le projet. le fichier requirements.txt liste les dépendances du projet.

## Data Pipeline
***
L'objectif de Ce pipeline est de produire en sortie un fichier JSON qui représente un graphe de liaison entre les différents médicaments et leurs mentions respectives dans les différentes publications PubMed, les différentes publications scientifiques et enfin les journaux avec la date associée à chacune de ces mentions. 
### 📚 Inputs Data
| File | Count | Description |
|:--------------|:-------------:|--------------:|
| data/drugs.csv | 7 | un fichier csv contenant les données des drugs avec deux colonnes : atccode => id de drug, drug => nom de drug |  
|:--------------|:-------------:|--------------:|
| data/clinical_trials.csv | 8 | un fichier csv contenant les données des essais cliniques avec 4 colonnes : id => id de trial, scientific_title => le titre scientifique de trial, data: date de trial, journal: nom de journal de publication de trial |
|:--------------|:-------------:|--------------:|
| data/pubmed.csv | 7 | un fichier csv contenant les données des publications avec 4 colonnes : id => id de publication, title => le titre de la publication, data: date de la publication, journal: nom de journal de publication |
|:--------------|:-------------:|--------------:|
| data/pubmed.json | 5 | un fichier json contenantles données des publications avec 4 colonnes : id => id de publication, title => le titre de la publication, data: date de la publication, journal: nom de journal de publication |

### ⏭ Pipeline
| Workflow | Etapes |
|:--------------|:-------------:|
| All | Reading Inputs → Data Cleaning → Processing → Loading Result |
***
   * 1. Reading Inputs : consiste à lire la config et les données d'entrée en utilisant un connecteur; Dans notre cas, on a un seul type de connecteur :  un connecteur local.
   * 2. Data Cleaning : consiste à : 
       * A. clean_date_column : permet de normaliser les dates afin d'avoir le même format : '%d-%m-%Y'
       * B. clean_words_column : permet de nettoyer les colonnes contenant des mots, d'enlever les caractères non ascii, les espaces et de lower case ces strings.
       * C. deal_with_nan : permet de supprimer les nulls.
   * 3. Processing : permet de calculer les liens entre les differents medicaments et leurs mentions dans les PubMed, 
    les publications scientifiques et les journaux. L'output de cette étape prend la forme suivante : 
    ```
    [{"drug_id": drug_id_value, 
                     "links":[{
                                 "link_type": link_type_1, "journal_name" : journal_name_1, 
                                 "date_mention": date_mention_1},  ....],
                                
                    }]

    ```
    ***
    4. Loading Result: permet d'écrire l'output de la pipeline dans un fichier json en utilisant le laoding. Dans notre cas, on a un seul type de loading : loading_local.

### ⏭ Run Pipeline  :
***
Cette pipeline peut être lancée en utilsant : 
```
main.py 

```
## Ad-Hoc : 
***
Cette feature peut être calculée en utilsant : 
```
main_features.py 

```
## Sql Requests :
*** 
*1.	1ere requête : Calculer le montant total des ventes jour par jour : 
*sql/sales_total_amount_day_by_day
*2.	2eme requête : Calculer le montant des ventes des meubles et deco par client.
*sql/meubles_deco_sales.sql

