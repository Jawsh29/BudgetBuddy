# This program allows the user to input expenses and spending goals and generate reports based on data

from breezypythongui import EasyFrame
from BudgetBuddyGoals import GoalsPage
from BudgetBuddyExpenses import ExpensesPage
from BudgetBuddyReports import ReportsPage


class BudgetApp(EasyFrame):
    """Displays Main Menu"""
    def __init__(self):
        """Displays Menu Options"""
        EasyFrame.__init__(self, title="Budget Manager", width=800, height=600)

        # Initialize Data
        self.data = {}

        # Menu Buttons
        self.goalsButton = self.addButton(text="Set Goals", row=0, column=0, command=self.set_goals)
        self.expensesButton = self.addButton(text="Enter Expenses", row=1, column=0, command=self.enter_expenses)
        self.ReportsButton = self.addButton(text="View Past Reports", row=2, column=0, command=self.view_reports)

    def set_goals(self):
        """Opens the Goals page."""
        GoalsPage(self).mainloop()

    def enter_expenses(self):
        """Opens the Expenses page."""
        ExpensesPage(self).mainloop()

    def view_reports(self):
        """Opens the Reports page."""
        ReportsPage(self).mainloop()

def main():
    """Instantiates and opens window."""
    BudgetApp().mainloop()


if __name__ == "__main__":
    main()