import tkinter as tk
from utils import display
from utils import db
from tkinter import ttk
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q6 : Graphique correlation temperatures minimales - coût de travaux (Isère / 2022)')
        display.defineGridDisplay(self, 2, 1)
        ttk.Label(self, text="""Pour l’Isère et l'année 2022, donner deux courbes sur le même graphique  :
   - par mois, l’évolution de la moyenne des températures minimales
   - par mois, l’évolution des totaux de coûts de travaux tout type confondu""",
                  wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)

        # Requête pour récupérer les données de température minimale par mois en 2022
        temp_query = """
            SELECT STRFTIME('%m', date_mesure) as month, AVG(temperature_min_mesure) as avg_min_temperature
            FROM Mesures
            WHERE code_departement = 38 AND STRFTIME('%Y', date_mesure) = '2022'
            GROUP BY month
        """

        # Requête pour récupérer les totaux de coûts de travaux par mois en 2022
        cost_query = """
            SELECT STRFTIME('%m', annee_travaux) as month, SUM(cout_total_ht) as total_cost
            FROM Travaux
            WHERE code_departement = 38 AND STRFTIME('%Y', annee_travaux) = '2022'
            GROUP BY month
        """

        # Extraction des données de température
        temp_result = []
        try:
            cursor_temp = db.data.cursor()
            temp_result = cursor_temp.execute(temp_query)

        except Exception as e:
            print("Erreur température : " + repr(e))

        # Extraction des données de coûts de travaux
        cost_result = []
        try:
            cursor_cost = db.data.cursor()
            cost_result = cursor_cost.execute(cost_query)

        except Exception as e:
            print("Erreur coûts de travaux : " + repr(e))

        # Préparation des données pour le graphique
        temp_data = {row[0]: row[1] for row in temp_result}
        cost_data = {row[0]: row[1] for row in cost_result}

        # Création de la figure et du subplot pour le graphique
        fig = Figure(figsize=(10, 6), dpi=100)
        plot1 = fig.add_subplot(111)

        # Affichage de la courbe de température minimale
        plot1.plot(list(temp_data.keys()), list(temp_data.values()), color='g', label='Température Minimale')

        # Création d'un deuxième axe y pour les coûts de travaux
        plot2 = plot1.twinx()
        plot2.plot(list(cost_data.keys()), list(cost_data.values()), color='b', label='Coûts de Travaux', linestyle='dashed')

        # Configuration de l'axe x
        plot1.set_xlabel('Mois')
        plot1.set_ylabel('Température Minimale (°C)')
        plot2.set_ylabel('Coûts de Travaux')
        plot1.legend(loc='upper left')
        plot2.legend(loc='upper right')

        # Affichage du graphique
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)


