# This window displays the budget report based on input data from Goals and Expenses

from breezypythongui import EasyFrame
import matplotlib.pyplot as plt


class ReportsPage(EasyFrame):
    """Displays Reports Page"""
    def __init__(self, parent):
        """Creates Report Charts"""
        super().__init__(title="Expense Report", width=800, height=600)
        self.parent = parent

        categories = self.parent.data.get("categories", {})
        if categories == "":
            self.messageBox(title="Error", message="No data to generate report.")
            return

        # Pie chart
        labels = list(categories.keys())
        sizes = [cat["spent"] for cat in categories.values()]
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.pie(sizes, labels=labels)
        plt.title("Spending by Category")

        # Bar chart
        goals = [cat["goal"] for cat in categories.values()]
        plt.subplot(1, 2, 2)
        plt.bar(labels, sizes, label="Spent")
        plt.bar(labels, goals, label="Goal", alpha=0.7)
        plt.legend()
        plt.title("Goals vs. Spending")

        # Show plots
        plt.tight_layout()
        plt.show()
