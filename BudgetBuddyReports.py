# This window displays the budget report based on input data from Goals and Expenses

import customtkinter as ctk
import csv


class ReportsPage(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__()
        self.title("Expense Report")
        self.geometry("800x600")
        self.parent = parent

        # Scrollable Frame
        frame = ctk.CTkScrollableFrame(self)
        frame.pack(fill="both", expand=True)

        # Column headers
        ctk.CTkLabel(frame, text="Category").grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(frame, text="Goal").grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(frame, text="Spent").grid(row=0, column=2, padx=10, pady=5)

        # Data rows
        for i, (category, values) in enumerate(parent.data.get("categories", {}).items(), start=1):
            ctk.CTkLabel(frame, text=category).grid(row=i, column=0, padx=10, pady=5)
            ctk.CTkLabel(frame, text=values["goal"]).grid(row=i, column=1, padx=10, pady=5)
            ctk.CTkLabel(frame, text=values["spent"]).grid(row=i, column=2, padx=10, pady=5)

        export_button = ctk.CTkButton(self, text="Export to CSV File",
                                      command=self.save_report_to_csv(self.parent.data["categories"]))
        export_button.pack(pady=10)

    def save_report_to_csv(self, data, file_name="Report.csv"):
        """Save goals data to a CSV file."""
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write headers
            writer.writerow(["Category", "Goal", "Spent"])
            # Write category data
            for category, values in data.items():
                writer.writerow([category, values["goal"], values.get("spent", 0)])