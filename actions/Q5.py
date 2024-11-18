import tkinter as tk
from tkinter import ttk
from utils import display
from utils import db
import time

class Window(tk.Toplevel):

    treeview = False
    timelabel = False

    def __init__(self, parent):
        super().__init__(parent)

        display.centerWindow(900, 600, self)
        self.title('Q5 : températures par département et par année (version optimisée)')
        display.defineGridDisplay(self, 4, 2)
        self.grid_rowconfigure(3, weight=10)
        ttk.Label(self, text="On a repris le code de F3. Modifier le code pour optimiser l'algorithme à la fois en terme de temps d'exécution mais aussi de nombre de requêtes exécutées (éco-conception).",
                  wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0, columnspan=2)

        ttk.Label(self, text="Lancer l'extraction des données :", anchor="center").grid(row=1, column=0)
        ttk.Button(self, text='Go !', command=self.extract_data).grid(column=1, row=1)
        self.timelabel = ttk.Label(self, anchor="center")
        self.timelabel.grid(row=2, columnspan=2)
        columns = ('code_departement', 'nom_departement', 'annee_mesure', 'moyenne', 'minimum', 'maximum')
        self.treeview = display.createTreeViewDisplay(self, columns, [], 150)
        self.treeview.grid(row=3, columnspan=2, sticky="nswe")

    def extract_data(self):
        self.treeview.delete(*self.treeview.get_children())

        start = time.time()
        nbquery = 0

        try:
            cursor = db.data.cursor()

            query = """
                    SELECT
                        Departements.code_departement,
                        Departements.nom_departement,
                        STRFTIME('%Y', Mesures.date_mesure) as annee,
                        ROUND(AVG(Mesures.temperature_moy_mesure), 2) AS moyenne,
                        MIN(Mesures.temperature_min_mesure) AS minimum,
                        MAX(Mesures.temperature_min_mesure) AS maximum
                    FROM
                        Mesures
                    LEFT JOIN
                        Departements USING (code_departement)
                    GROUP BY
                        Departements.code_departement, annee
                    ORDER BY
                        Departements.code_departement, annee;

            """

            result = cursor.execute(query)
            nbquery += 1

            for row in result.fetchall():
                self.treeview.insert('', tk.END, values=row)

        except Exception as e:
            print("Erreur : " + repr(e))

        end = time.time()
        self.timelabel.configure(text="Le calcul a pris " + str(round(end - start, 3)) + " secondes et exécuté " + str(nbquery) + " requêtes.")

