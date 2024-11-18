import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.db_conn = sqlite3.connect("data/climat_france.db")
        self.db_cursor = self.db_conn.cursor()

        self.setup_ui()

    def setup_ui(self):
        labels = [
            "ID Travaux", "Puissance Installee", "Type Panneaux", "Code Region",
            "Code Departement", "Cout Total HT", "Cout Induit HT",
            "Annee Travaux", "Type Logement", "Annee_Cons_L"
        ]

        self.entries = {}
        for i, label_text in enumerate(labels):
            ttk.Label(self, text=label_text).grid(row=i*2, column=0, pady=(5, 0))
            entry = ttk.Entry(self, width=100)
            entry.grid(row=i*2+1, column=0)
            self.entries[label_text] = entry

        btn_ajouter_photovoltaique = ttk.Button(self, text="Ajouter photovoltaique", command=self.ajouter_photovoltaique)
        btn_ajouter_photovoltaique.grid(row=1, column=1, pady=(10, 0))

        btn_ajouter_travaux = ttk.Button(self, text="Ajouter Travaux", command=self.ajouter_travaux)
        btn_ajouter_travaux.grid(row= 2, column=1, pady=(10, 0))

        # Update
        ttk.Label(self, text="Update Query").grid(row=len(labels)*2 + 2, column=0, pady=(10, 0))
        self.entry_update_query = ttk.Entry(self, width=100)
        self.entry_update_query.grid(row=len(labels)*2 + 3, column=0)
        btn_execute_update = ttk.Button(self, text="Execute Update", command=self.execute_update)
        btn_execute_update.grid(row=len(labels)*2 + 3, column=1, pady=(10, 0))

        # Delete
        ttk.Label(self, text="Delete Query").grid(row=len(labels)*2 + 4, column=0, pady=(10, 0))
        self.entry_delete_query = ttk.Entry(self, width=100)
        self.entry_delete_query.grid(row=len(labels)*2 + 5, column=0)
        btn_execute_delete = ttk.Button(self, text="Execute Delete", command=self.execute_delete)
        btn_execute_delete.grid(row=len(labels)*2 + 5, column=1, pady=(10, 0))

    def ajouter_photovoltaique(self):
        try:
            query = f"INSERT INTO Photovoltaiques (puissance_installee, type_panneaux, code_region, code_departement, cout_total_ht, cout_induit_ht, annee_travaux, type_logement, annee_construction_logement) " \
                    f"VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            values = (
                self.entries['Puissance Installee'].get(),
                self.entries['Type Panneaux'].get(),
                self.entries['Code Region'].get(),
                self.entries['Code Departement'].get(),
                self.entries['Cout Total HT'].get(),
                self.entries['Cout Induit HT'].get(),
                self.entries['Annee Travaux'].get(),
                self.entries['Type Logement'].get(),
                self.entries['Annee_Cons_L'].get()
            )
            self.db_cursor.execute(query, values)
            self.db_conn.commit()
            messagebox.showinfo("Success", "Photovoltaique added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def ajouter_travaux(self):
        try:
            query = f"INSERT INTO Travaux (code_departement, code_region, cout_total_ht, cout_induit_ht, annee_travaux, type_logement, annee_construction_logement) " \
                    f"VALUES (?, ?, ?, ?, ?, ?, ?)"
            values = (
                self.entries['Code Departement'].get(),
                self.entries['Code Region'].get(),
                self.entries['Cout Total HT'].get(),
                self.entries['Cout Induit HT'].get(),
                self.entries['Annee Travaux'].get(),
                self.entries['Type Logement'].get(),
                self.entries['Annee_Cons_L'].get()
            )
            self.db_cursor.execute(query, values)
            self.db_conn.commit()
            messagebox.showinfo("Success", "Travaux added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def execute_update(self):
        try:
            query = self.entry_update_query.get()
            self.db_cursor.execute(query)
            self.db_conn.commit()
            messagebox.showinfo("Success", "Update executed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def execute_delete(self):
        try:
            query = self.entry_delete_query.get()
            self.db_cursor.execute(query)
            self.db_conn.commit()
            messagebox.showinfo("Success", "Delete executed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")


