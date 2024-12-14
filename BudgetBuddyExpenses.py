# This Window allows users to enter expenses based on the Goals created in the Goals window

import customtkinter as ctk
import csv
from BudgetBuddyReports import ReportsPage


class ExpensesPage(ctk.CTkToplevel):
    """Displays Expenses page."""
    def __init__(self, parent):
        """Displays Methods for Adding Expenses"""
        super().__init__()
        self.title("Enter Expenses")
        self.geometry("800x600")
        self.parent = parent

        # Goals Combobox
        self.goal_list_label = ctk.CTkLabel(self, text="Select Goal:")
        self.goal_list_label.grid(row=0, column=0, padx=10, pady=10)
        self.placeholder_text = "Select a Goal"
        self.category_dropdown = ctk.CTkComboBox(self, values=[self.placeholder_text], command=self.update_selection)
        self.category_dropdown.grid(row=0, column=1, padx=10, pady=10)
        self.selected_category = None
        self.populate_categories()

        # Input for Expense Amount
        self.expense_label = ctk.CTkLabel(self, text="Expense Amount:")
        self.expense_label.grid(row=1, column=0, padx=10, pady=10)
        self.expense_amount = ctk.CTkEntry(self, placeholder_text="Enter amount")
        self.expense_amount.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        # Add Expense Button
        self.add_expense_button = ctk.CTkButton(self, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=2, column=1, padx=10, pady=20)
        # Generate Report Button
        self.generate_report_button = ctk.CTkButton(self, text="Generate Report", command=self.generate_report)
        self.generate_report_button.grid(row=2, column=0, padx=10, pady=20)

        # Center Buttons
        self.grid_columnconfigure(1, weight=1)

    def populate_categories(self):
        """Populate the ComboBox with categories from Goals Data."""
        categories = self.parent.data.get("categories", {})
        self.category_dropdown.configure(values=list(categories.keys()))

    def update_selection(self, category):
        """Update the selected category when the user selects a Goals category."""
        self.selected_category = category

    def add_expense(self):
        """Add an expense to the selected Goals category."""
        category = self.selected_category
        amount = self.expense_amount.get().strip()

        # Check if a category is selected
        if not category:
            self.show_message("Error", "Please select a category.")
            return

        # Validate the amount
        if not amount.isdigit() or int(amount) <= 0:
            self.show_message("Error", "Please enter a valid expense amount.")
            return

        amount = int(amount)

        # Update the expense for the selected category
        self.parent.data["categories"][category]["spent"] += amount
        self.show_message("Success", f"Added ${amount} to {category}.")
        self.expense_amount.delete(0, ctk.END)


    def generate_report(self):
        """Generate a report using the Goals and Expenses data."""
        ReportsPage(self.parent)

    def show_message(self, title, message):
        """Displays a message in pop-up window."""
        message_window = ctk.CTkToplevel(self)
        message_window.title(title)
        message_window.geometry("300x150")
        label = ctk.CTkLabel(message_window, text=message, wraplength=250)
        label.pack(pady=20)
        button = ctk.CTkButton(message_window, text="OK", command=message_window.destroy)
        button.pack(pady=10)