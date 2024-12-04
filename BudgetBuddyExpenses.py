
from breezypythongui import EasyFrame
from BudgetBuddyReports import ReportsPage


class ExpensesPage(EasyFrame):
    """Displays Expenses page."""
    def __init__(self, parent):
        """Displays Methods for Adding Expenses"""
        super().__init__(title="Enter Expenses", width=800, height=600)
        self.parent = parent

        # Listbox
        self.goal_List_Label = self.addLabel(text="Select Goal:", row=0, column=0)
        self.category_dropdown = self.addListbox(row=0, column=1, listItemSelected=self.update_selection)
        self.selected_category = None
        self.populate_categories()

        # Input for expense amount
        self.expense_Label = self.addLabel(text="Expense Amount:", row=1, column=0)
        self.expense_amount = self.addIntegerField(value=0, row=1, column=1)

        # Buttons
        self.add_Expense_Button = self.addButton(text="Add Expense", row=2, column=1, command=self.add_expense)
        self.generate_Report_Button = self.addButton(text="Generate Report", row=2, column=0,
                                                     command=self.generate_report)

    def populate_categories(self):
        """Populate the Listbox with categories from Goals Data."""
        self.category_dropdown.clear()
        categories = self.parent.data.get("categories", {})
        for category in categories:
            self.category_dropdown.insert("end", category)

    def update_selection(self, category):
        """Update the selected category when the user selects a Goals category."""
        self.selected_category = category

    def add_expense(self):
        """Add an expense to the selected Goals category."""
        category = self.category_dropdown.getSelectedItem()
        amount = self.expense_amount.getNumber()

        # Check if a category is selected and amount is valid
        if category is None:
            self.messageBox(title="Error", message="Please select a category.")
            return

        if amount <= 0:
            self.messageBox(title="Error", message="Please enter a valid expense amount.")
            return

        # Update the expense for the selected category
        self.parent.data["categories"][category]["spent"] += amount
        self.messageBox(title="Success", message=f"Added ${amount} to {category}.")

    def generate_report(self):
        """Generate a report using the Goals and Expenses data."""
        ReportsPage(self.parent)
