import tkinter as tk
from utils import display
from tkinter import ttk

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q2 : département le plus froid par région')
        display.defineGridDisplay(self, 2, 1)
        # ttk.Label(self, text="Modifier cette fonction en s'inspirant du code de F1, pour qu'elle affiche le(s) département(s) avec la température moyenne (c.a.d. moyenne des moyennes de toutes les mesures) la plus basse. \nSchéma attendu : (nom_region, nom_departement, temperature_moy_min)",
        #           wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)

        # On définit les colonnes que l'on souhaite afficher dans la fenêtre
        columns = ('nom_region', 'nom_departement', 'temperature_moy_min')

        # On définit la requête SQL

        query = """WITH Moyenne_departement AS (
    SELECT code_departement, AVG(temperature_moy_mesure) AS temperature_moy
    FROM Mesures
    GROUP BY code_departement       
),
Minimum_region AS (
    SELECT code_region, MIN(temperature_moy) AS temperature_moy
    FROM Regions
    JOIN Departements USING (code_region)
    JOIN Moyenne_departement USING (code_departement)   
    GROUP BY code_region    
)
SELECT nom_region, nom_departement, temperature_moy
FROM Departements
JOIN Regions USING (code_region)
JOIN Moyenne_departement USING (code_departement)
JOIN Minimum_region USING (temperature_moy)
where (Minimum_region.code_region,Departements.code_departement) in 
    (select code_region,code_departement
    FROM Departements
     )
ORDER BY temperature_moy
"""

        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
        tree = display.createTreeViewDisplayQuery(self, columns, query, 200)
        tree.grid(row=1, sticky="nswe")
