# -*- coding: utf8 -*-
"""
Fonctions utilisées dans le fichier app.py
 - trait_fichier() ouvre et extrait les fichiers .xlsx
 - trait_date() récupère le jour de la semaine à partir de la date
 - trait_nan() permet d'attribuer une valeur si la donnée contient un chiffre (ou nombre)
"""

from math import isnan
from datetime import date
from pandas import read_excel

FILETYPE = [
        ('Excel file', '*.xlsx;*.xls'),
]
JOUR_SEMAINE = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")


def trait_fichier(browse_file):
    """
    :param browse_file: str
    :return liste: list
    """
    if browse_file:
        print('fichier chargé.')
        file = read_excel(browse_file)
        liste = file.values.tolist()
    else:
        print('Import annulé')
        exit()
    return liste


def trait_date(annee, mois, jour):
    """
    :param annee: int
    :param mois: int
    :param jour: int
    :return jour_semaine: str
    """
    num_jour = date(annee, mois, jour)
    jour = num_jour.weekday()
    jour_semaine = JOUR_SEMAINE[jour]
    return jour_semaine


def trait_nan(d_male, d_femelle):
    """
    nan = not a number
    :param d_male: float
    :param d_femelle: float
    :return: data float, sexe str
    """
    if isnan(d_male):
        data = d_femelle
        sexe = 'M'
    elif isnan(d_femelle):
        data = d_male
        sexe = 'F'
    else:
        print('error')
    return data, sexe
