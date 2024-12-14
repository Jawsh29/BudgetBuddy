# This window lets the user define and set Goals for Budget

import customtkinter as ctk
import csv


class GoalsPage(ctk.CTkToplevel):
    """Displays Goals Page"""
    def __init__(self, parent):
        """Displays Methods for Creating Goals and Entering Amounts"""
        super().__init__()
        self.title("Set Goals")
        self.geometry("800x600")
        self.parent = parent

        # Widgets
        # Category Label
        self.category_Label = ctk.CTkLabel(self, text="Category Name:")
        self.category_Label.grid(row=0, column=0, padx=10, pady=10)
        # Category Entry Field
        self.category_Name = ctk.CTkEntry(self, placeholder_text="Enter Category Name")
        self.category_Name.grid(row=0, column=1, padx=10, pady=10)
        # Goal Label
        self.goal_Label = ctk.CTkLabel(self, text="Goal Amount:")
        self.goal_Label.grid(row=1, column=0, padx=10, pady=10)
        # Goal Entry Field
        self.goal_Amount = ctk.CTkEntry(self, placeholder_text="Enter Goal Amount")
        self.goal_Amount.grid(row=1, column=1, padx=10, pady=10)
        # Add Goal Button
        self.goal_Button = ctk.CTkButton(self, text="Add Goal", command=self.add_goal)
        self.goal_Button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Center Buttons
        self.grid_columnconfigure(1, weight=1)

    def add_goal(self):
        """Creates Goal Category and Goal Amount"""
        # Get input values
        category = self.category_Name.get().strip()
        goal = self.goal_Amount.get().strip()

        # Validate inputs
        if category == "":
            self.show_message("Error", "Category name cannot be empty!")
            return
        if not goal.isdigit() or int(goal) <= 0:
            self.show_message(title="Error", message="Goal amount must be greater than 0!")
            return

        goal = int(goal)

        # Add or update the category in the data dictionary
        if "categories" not in self.parent.data:
            self.parent.data["categories"] = {}

        self.parent.data["categories"][category] = {
            "goal": goal,
            "spent": self.parent.data["categories"].get(category, {}).get("spent", 0)
        }

        # Confirm Entry
        self.show_message("Success", f"Goal of ${goal} set for '{category}'!")
        self.category_Name.delete(0, ctk.END)
        self.goal_Amount.delete(0, ctk.END)

    def show_message(self, title, message):
        """Displays a message in pop-up window"""
        message_window = ctk.CTkToplevel(self)
        message_window.title(title)
        message_window.geometry("300x150")
        label = ctk.CTkLabel(message_window, text=message, wraplength=250)
        label.pack(pady=20)
        button = ctk.CTkButton(message_window, text="OK", command=message_window.destroy)
        button.pack(pady=10)
