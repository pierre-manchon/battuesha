# -*- coding: utf8 -*-
"""
Fichier principal de traitement des données battues
    - Remises en forme des champs
    - Remise en forme des données
    - Ajout à la suite du fichier précédent

Commande utilisée pour la compilation :
    pyinstaller --clean -D -n battuesha battuesha/app.py
Commande utilisée pour la création d'un executable :
    python setup.py bdist_msi
"""

# init des var de base
from tkinter import Tk, filedialog
from flask import Flask
from pandas import DataFrame
from battuesha.data import trait_fichier, trait_date, trait_nan, FILETYPE

# root vars
APP = Flask(__name__)
ROOT = Tk()
ROOT.withdraw()

# Récupération des chemins d'accès vers les fichiers excel bdd
print('Sélectionnez le fichier exporté depuis retriever.')
LISTE_IE_RETRIEVER = trait_fichier(filedialog.askopenfilename(filetypes=FILETYPE))
print('Sélectionnez le fichier à mettre à jour (battues des années précédentes).')
LISTE_I_BDD_BATTUES = trait_fichier(filedialog.askopenfilename(filetypes=FILETYPE))

# Ici il y a les calculs pour changer les valeurs/ordre des champs du excel
LISTE_CALC = []
for SAISON, UG_CODE, EQU_LIBELLE, EQU_RESP, TERR_INTITULE, COM_INSEE,\
    COM_LIBELLE, BATTUE_DATE, NBR_CHASS, POIDS_M, POIDS_F, GESTANTE in LISTE_IE_RETRIEVER:

    # Calculs dates
    DATE = BATTUE_DATE.strftime('%d/%m/%y')
    DATE_SPLIT = DATE.split('/')
    JM = DATE_SPLIT[0] + "/" + DATE_SPLIT[1]
    MJ = DATE_SPLIT[1] + "/" + DATE_SPLIT[0]
    M = DATE_SPLIT[1]
    J_SEM = trait_date(int(DATE_SPLIT[2]), int(DATE_SPLIT[1]), int(DATE_SPLIT[0]))

    # Remplacememnt des 0 et des 1 aveec oui/non
    if GESTANTE == 1:
        GESTANTE_ON = 'oui'
    elif GESTANTE == 2:
        GESTANTE_ON = 'Indetermine'
    else:
        GESTANTE_ON = 'non'

    # Nettoyage des données poids
    POIDS_CLEAN, SEXE = trait_nan(POIDS_M, POIDS_F)

    # Calcul poids et classe poids
    POIDS_CLASSE = None
    if POIDS_CLEAN <= 40:
        POIDS_CLASSE = 'Jeune'
    elif POIDS_CLEAN >= 60:
        POIDS_CLASSE = 'Adulte'
    else:
        POIDS_CLASSE = 'Subadulte'

    # Append liste_calculs
    LISTE_CALC.append([COM_LIBELLE, COM_INSEE, UG_CODE, EQU_RESP, EQU_LIBELLE,
                       TERR_INTITULE, SAISON, DATE, J_SEM, JM, MJ, M,
                       NBR_CHASS, '1', SEXE, POIDS_CLEAN, POIDS_CLASSE, GESTANTE_ON])
# Ajout à la var bd battues
LISTE_I_BDD_BATTUES.extend(LISTE_CALC)

# choix d'un export ou non
print('Terminé')
GOTO_EXP = 0
while GOTO_EXP == 0:
    PARSER_OP = input('Créer un nouveau fichier ? Y/N :')
    try:
        CAP = str(PARSER_OP).capitalize()
        if "Y" in CAP:
            GOTO_EXP = 1
            # L'export en xlsx
            DF = DataFrame(LISTE_I_BDD_BATTUES)
            DF.to_excel('bdd_battues.xlsx', sheet_name='bdd_battues', header=False, startcol=-1)
            break
        elif "N" in CAP:
            GOTO_EXP = 1
            # pas export
            break
        else:
            print('Mauvaise valeur')
    except ValueError:
        # raise des erreurs
        print(ValueError)
