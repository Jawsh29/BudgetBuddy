# This window lets the user define and set Goals for Budget

from breezypythongui import EasyFrame


class GoalsPage(EasyFrame):
    """Displays Goals Page"""
    def __init__(self, parent):
        """Displays Methods for Creating Goals and Entering Amounts"""
        super().__init__(title="Set Goals",  width=800, height=600)
        self.parent = parent

        # Widgets
        self.category_Label = self.addLabel(text="Category Name:", row=0, column=0)
        self.category_Name = self.addTextField(text="", row=0, column=1)
        self.goal_Label = self.addLabel(text="Goal Amount:", row=1, column=0)
        self.goal_Amount = self.addIntegerField(value=0, row=1, column=1)
        self.goal_Button = self.addButton(text="Add Goal", row=2, column=0, columnspan=2, command=self.add_goal)

    def add_goal(self):
        """Creates Goal Category and Goal Amount"""
        # Get input values
        category = self.category_Name.getText()
        goal = self.goal_Amount.getNumber()

        # Validate inputs
        if category == "":
            self.messageBox(title="Error", message="Category name cannot be empty!")
            return
        if goal <= 0:
            self.messageBox(title="Error", message="Goal amount must be greater than 0!")
            return

        # Add or update the category in the data dictionary
        if "categories" not in self.parent.data:
            self.parent.data["categories"] = {}

        self.parent.data["categories"][category] = {
            "goal": goal,
            "spent": self.parent.data["categories"].get(category, {}).get("spent", 0)
        }

        # Confirm Entry
        self.messageBox(title="Success", message=f"Goal of ${goal} set for '{category}'!")
        self.category_Name.setText("")
        self.goal_Amount.setNumber(0)
