# This program allows the user to input expenses and spending goals and generate reports based on data

import customtkinter as ctk
from BudgetBuddyGoals import GoalsPage
from BudgetBuddyExpenses import ExpensesPage
from BudgetBuddyReports import ReportsPage

# Set Application Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class BudgetBuddy(ctk.CTk):
    """Displays Main Menu"""

    def __init__(self):
        super().__init__()
        """Displays Menu Options"""
        self.title("Budget Buddy")
        self.geometry("800x600")

        # Initialize Data
        self.data = {}

        # Menu Buttons
        # Goals Button
        self.goalsButton = ctk.CTkButton(self, text="Set Goals", command=self.set_goals)
        self.goalsButton.grid(row=1, column=0, padx=20, pady=10)
        # Expenses Button
        self.expensesButton = ctk.CTkButton(self, text="Enter Expenses", command=self.enter_expenses)
        self.expensesButton.grid(row=2, column=0, padx=20, pady=10)
        # Reports Button
        self.reportsButton = ctk.CTkButton(self, text="View Past Reports", command=self.view_reports)
        self.reportsButton.grid(row=3, column=0, padx=20, pady=10)

        # Center Buttons
        self.grid_columnconfigure(0, weight=1)

    def set_goals(self):
        """Opens the Goals page."""
        GoalsPage(self).mainloop()

    def enter_expenses(self):
        """Opens the Expenses page."""
        ExpensesPage(self).mainloop()

    def view_reports(self):
        """Opens the Reports page."""
        ReportsPage(self).mainloop()


if __name__ == "__main__":
    app = BudgetBuddy()
    app.mainloop()
