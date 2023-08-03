"""Module to create a GUI for the Hourly Wage Calculator."""
import tkinter as tk
from tkinter import messagebox


class Expense:
    """Class to represent an expense.

    Attributes:
        name (str): The name of the expense.
        value (float): The monetary value of the expense.

    Methods:
        get_name(): Get the name of the expense.
        get_value(): Get the monetary value of the expense.
    """

    def __init__(self, name, value):
        """
        Initialize a new Expense instance.

        Args:
            name (str): The name of the expense.
            value (float): The monetary value of the expense.
        """
        self.name = name
        self.value = value

    def get_name(self):
        """Return the name of the expense."""
        return self.name

    def get_value(self):
        """Return the value of the expense."""
        return self.value


class HourlyWageCalculatorGUI:
    """Class to create the GUI for the Hourly Wage Calculator.

    Attributes:
        root (tk.Tk): The main application window.

    Methods:
        setup_expenses_frame():
            Setup the Expenses Frame.
        add_custom_expense():
            Add a custom expense to the list.
        update_expenses_list():
            Update the expenses list in the GUI.
        setup_delete_expenses_frame():
            Set up the Delete Expenses Frame.
        delete_expense():
            Delete the selected expense from the list.
        setup_working_hours_frame():
            Set up the Working Hours Frame.
        setup_calculation_choice_frame():
            Set up the Calculation Choice Frame.
        setup_calculate_expenses_button():
            Set up the Calculate Expenses Button.
        setup_result_label():
            Set up the Result Label.
        calculate_expenses():
            Calculate the hourly wage needed to cover expenses.
        setup_monthly_earnings_frame():
            Set up the Monthly Earnings Calculation Frame.
        setup_calculate_earnings_button():
            Set up the Calculate Earnings Button.
        setup_earnings_labels():
            Set up the Earnings Labels.
        calculate_earnings():
            Calculate the estimated weekly and monthly earnings based on the user's input.
        setup_remaining_income_label():
            Set up the Remaining Income Label.
        calculate_remaining_income():
            Calculate the remaining income after deducting total expenses from monthly earnings.
    """

    def __init__(self, root_value):
        """
        Initialize the HourlyWageCalculatorGUI instance.

        Args:
            root_value (tk.Tk): The main application window.
        """

        self.yearly_earnings_label = None
        self.monthly_earnings_label = None
        self.weekly_earnings_label = None
        self.hourly_rate_input = None
        self.salary_input = None
        self.remaining_income_label = None
        self.result_label = None
        self.calculation_choice_spinner = None
        self.calculation_choice = None
        self.working_hours_input = None
        self.expenses_list = None
        self.custom_expense_value = None
        self.custom_expense_name = None
        self.root = root_value
        self.root.title("Hourly Wage Calculator")
        self.root.configure(bg="#F0F0F0")

        self.expenses = []

        self.setup_expenses_frame()

        self.setup_delete_expenses_frame()

        self.setup_working_hours_frame()

        self.setup_calculation_choice_frame()

        self.setup_calculate_expenses_button()

        self.setup_result_label()

        self.setup_monthly_earnings_frame()

        self.setup_calculate_earnings_button()

        self.setup_earnings_labels()

        self.setup_remaining_income_label()

    def setup_expenses_frame(self):
        """
        Set up the Expenses Frame.
        This frame allows users to input custom expenses
        and displays the list of expenses.
        """
        expenses_frame = tk.LabelFrame(
            self.root, text="Expenses", font=("Arial", 14, "bold"), bg="#F0F0F0"
        )
        expenses_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        tk.Label(expenses_frame, text="Expense Name", bg="#F0F0F0").grid(
            row=0, column=0, sticky="w"
        )
        self.custom_expense_name = tk.Entry(expenses_frame)
        self.custom_expense_name.grid(row=0, column=1)

        tk.Label(expenses_frame, text="Expense Value", bg="#F0F0F0").grid(
            row=1, column=0, sticky="w"
        )
        self.custom_expense_value = tk.Entry(expenses_frame)
        self.custom_expense_value.grid(row=1, column=1)

        add_button = tk.Button(
            expenses_frame,
            text="Add Expense",
            command=self.add_custom_expense,
            bg="#4CAF50",
            fg="white",
        )
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.expenses_list = tk.Listbox(expenses_frame, width=50)
        self.expenses_list.grid(row=3, column=1, columnspan=2)

    def add_custom_expense(self):
        """Add a custom expense to the list."""
        expense_name = self.custom_expense_name.get()
        expense_value = float(self.custom_expense_value.get())
        self.expenses.append(Expense(expense_name, expense_value))
        self.custom_expense_name.delete(0, tk.END)
        self.custom_expense_value.delete(0, tk.END)
        self.update_expenses_list()

    def update_expenses_list(self):
        """Update the expenses list in the GUI."""
        self.expenses_list.delete(0, tk.END)
        for expense in self.expenses:
            self.expenses_list.insert(tk.END, f"{expense.name}: ${expense.value:.2f}")

    def setup_delete_expenses_frame(self):
        """
        Set up the Delete Expenses Frame.
        This frame allows users to delete selected expenses from the expenses list.
        """
        delete_expenses_frame = tk.LabelFrame(
            self.root, text="Delete Expenses", font=("Arial", 14, "bold"), bg="#F0F0F0"
        )
        delete_expenses_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        delete_button = tk.Button(
            delete_expenses_frame,
            text="Delete Expense",
            command=self.delete_expense,
            bg="#4CAF50",
            fg="white",
        )
        delete_button.grid(row=0, column=2, columnspan=2, pady=10)

    def delete_expense(self):
        """
        Delete the selected expense from the list.
        This method deletes the expense selected in the expenses list.
        """
        try:
            index = self.expenses_list.curselection()[0]
            del self.expenses[index]
            self.update_expenses_list()
        except IndexError:
            messagebox.showerror("Error", "Please select an expense to delete.")

    def setup_working_hours_frame(self):
        """
        Se tup the Working Hours Frame.
        This frame allows users to input the number of working hours per week.
        """
        working_hours_frame = tk.LabelFrame(
            self.root, text="Working Hours", font=("Arial", 14, "bold"), bg="#F0F0F0"
        )
        working_hours_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tk.Label(working_hours_frame, text="Working Hours per Week", bg="#F0F0F0").grid(
            row=0, column=0, sticky="w"
        )
        self.working_hours_input = tk.Entry(working_hours_frame)
        self.working_hours_input.grid(row=0, column=1)

    def setup_calculation_choice_frame(self):
        """
        Set up the Calculation Choice Frame.
        This frame allows users to choose between hourly and salary-based calculations.
        """
        calculation_choice_frame = tk.LabelFrame(
            self.root,
            text="Calculation Method",
            font=("Arial", 14, "bold"),
            bg="#F0F0F0",
        )
        calculation_choice_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.calculation_choice = tk.StringVar(value="Hourly")
        tk.Label(
            calculation_choice_frame, text="Calculation Method", bg="#F0F0F0"
        ).grid(row=0, column=0, sticky="w")
        self.calculation_choice_spinner = tk.OptionMenu(
            calculation_choice_frame, self.calculation_choice, "Hourly", "Salary"
        )
        self.calculation_choice_spinner.grid(row=0, column=1, sticky="w")

    def setup_calculate_expenses_button(self):
        """
        Set up the Calculate Expenses Button.
        This button triggers the calculation of the hourly wage needed to cover expenses.
        """
        calculate_expenses_button = tk.Button(
            self.root,
            text="Calculate Expenses",
            command=self.calculate_expenses,
            bg="#4CAF50",
            fg="white",
        )
        calculate_expenses_button.grid(pady=10)

    def setup_result_label(self):
        """
        Set up the Result Label.
        This label displays the result of the expense calculation.
        """
        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 12, "bold"), bg="#F0F0F0"
        )
        self.result_label.grid(pady=10)

    def calculate_expenses(self):
        """
        Calculate the hourly wage needed to cover expenses and have money for gas and food.
        This method calculates the hourly wage required to cover all expenses entered by the user.
        The result is displayed in the result_label.
        """
        try:
            working_hours_per_week = float(self.working_hours_input.get())

            total_expenses = sum(expense.value for expense in self.expenses)

            working_hours_per_month = working_hours_per_week * 4.33
            hourly_wage = total_expenses / working_hours_per_month

            if self.calculation_choice.get() == "Hourly":
                hourly_rate = float(self.hourly_rate_input.get())
                monthly_earnings = hourly_rate * working_hours_per_month
            else:
                salary = float(self.salary_input.get())
                monthly_earnings = salary / 12

            remaining_income = monthly_earnings - total_expenses
            self.remaining_income_label.config(
                text=f"Your remaining income after expenses is: \n"
                f"${remaining_income:.2f}"
            )

            self.result_label.config(
                text=f"To cover your expenses and have money saved, "
                f"you would need to make ${hourly_wage:.2f} \n"
                f"per hour before taxes."
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Invalid input. Please enter numbers only."
            )

    def setup_monthly_earnings_frame(self):
        """
        Setup the Monthly Earnings Calculation Frame.
        This frame allows users to input their hourly rate or annual salary
        for the calculation of estimated weekly, monthly, and yearly earnings.
        """
        monthly_earnings_frame = tk.LabelFrame(
            self.root,
            text="Monthly Earnings Calculation",
            font=("Arial", 14, "bold"),
            bg="#F0F0F0",
        )
        monthly_earnings_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        tk.Label(monthly_earnings_frame, text="Calculation Choice", bg="#F0F0F0").grid(
            row=0, column=0, sticky="w"
        )
        tk.Label(
            monthly_earnings_frame, textvariable=self.calculation_choice, bg="#F0F0F0"
        ).grid(row=0, column=1, sticky="w")

        tk.Label(monthly_earnings_frame, text="Hourly Rate", bg="#F0F0F0").grid(
            row=1, column=0, sticky="w"
        )
        self.hourly_rate_input = tk.Entry(monthly_earnings_frame)
        self.hourly_rate_input.grid(row=1, column=1)

        tk.Label(monthly_earnings_frame, text="Annual Salary", bg="#F0F0F0").grid(
            row=2, column=0, sticky="w"
        )
        self.salary_input = tk.Entry(monthly_earnings_frame)
        self.salary_input.grid(row=2, column=1)

    def setup_calculate_earnings_button(self):
        """
        Set up the Calculate Earnings Button.
        This button triggers the calculation of estimated weekly, monthly, and yearly earnings.
        """
        calculate_earnings_button = tk.Button(
            self.root,
            text="Calculate Earnings",
            command=self.calculate_earnings,
            bg="#4CAF50",
            fg="white",
        )
        calculate_earnings_button.grid(pady=10)

    def setup_earnings_labels(self):
        """
        Set up the Earnings Labels.
        These labels display the estimated weekly, monthly,
        and yearly earnings based on the user's input.
        """
        self.weekly_earnings_label = tk.Label(
            self.root,
            text="Your estimated weekly earnings are: $0.00",
            font=("Arial", 12, "bold"),
            bg="#F0F0F0",
        )
        self.weekly_earnings_label.grid(pady=10)

        self.monthly_earnings_label = tk.Label(
            self.root,
            text="Your estimated monthly earnings are: $0.00",
            font=("Arial", 12, "bold"),
            bg="#F0F0F0",
        )
        self.monthly_earnings_label.grid(pady=10)

        self.yearly_earnings_label = tk.Label(
            self.root,
            text="Your estimated yearly earnings are: $0.00",
            font=("Arial", 12, "bold"),
            bg="#F0F0F0",
        )
        self.yearly_earnings_label.grid(pady=10)

    def calculate_earnings(self):
        """
        Calculate the estimated weekly, monthly, and yearly earnings based on the user's input.
        This method calculates the earnings based on the user's hourly rate or annual salary,
        and displays the results in the earnings labels.
        """
        try:
            if self.calculation_choice.get() == "Hourly":
                hourly_rate = float(self.hourly_rate_input.get())
                working_hours_per_week = float(self.working_hours_input.get())
                working_hours_per_month = working_hours_per_week * 4.33
                working_hours_per_year = working_hours_per_week * 52

                weekly_earnings = hourly_rate * working_hours_per_week
                monthly_earnings = hourly_rate * working_hours_per_month
                yearly_earnings = hourly_rate * working_hours_per_year

                yearly_earnings = 0.0
            else:
                salary = float(self.salary_input.get())
                weekly_earnings = salary / 52
                monthly_earnings = salary / 12
                yearly_earnings = salary

            self.weekly_earnings_label.config(
                text=f"Your estimated weekly earnings are: \n" f"${weekly_earnings:.2f}"
            )
            self.monthly_earnings_label.config(
                text=f"Your estimated monthly earnings are: \n"
                f"${monthly_earnings:.2f}"
            )

            if self.calculation_choice.get() == "Salary":
                self.yearly_earnings_label.config(
                    text=f"Your estimated yearly earnings are: \n"
                    f"${yearly_earnings:.2f}"
                )

        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Invalid input. Please enter numbers only."
            )

    def setup_remaining_income_label(self):
        """
        Set up the Remaining Income Label.
        This label displays the remaining income
        after deducting total expenses from monthly earnings.
        """
        self.remaining_income_label = tk.Label(
            self.root, text="", font=("Arial", 12, "bold"), bg="#F0F0F0"
        )
        self.remaining_income_label.grid(
            row=1, column=2, padx=10, pady=10, sticky="nsew"
        )

        remaining_income_frame = tk.LabelFrame(
            self.root,
            text="Remaining Income",
            font=("Arial", 14, "bold"),
            bg="#F0F0F0",
        )
        remaining_income_frame.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )

        calculate_remaining_income_button = tk.Button(
            remaining_income_frame,
            text="Calculate Remaining Income",
            command=self.calculate_remaining_income,
            bg="#4CAF50",
            fg="white",
        )
        calculate_remaining_income_button.pack(pady=10)

    def calculate_remaining_income(self):
        """
        Calculate the remaining income after deducting total expenses from monthly earnings.
        This method calculates the remaining income
        after deducting total expenses from the user's
        monthly earnings based on the selected calculation method (hourly/salary).
        The result is displayed in the remaining_income_label.
        """
        try:
            working_hours_per_week = float(self.working_hours_input.get())

            total_expenses = sum(expense.value for expense in self.expenses)

            working_hours_per_month = working_hours_per_week * 4.33

            if self.calculation_choice.get() == "Hourly":
                hourly_rate = float(self.hourly_rate_input.get())
                monthly_earnings = hourly_rate * working_hours_per_month
            else:
                salary = float(self.salary_input.get())
                monthly_earnings = salary / 12

            remaining_income = monthly_earnings - total_expenses
            self.remaining_income_label.config(
                text=f"Your remaining income after expenses is: \n"
                f"${remaining_income:.2f}"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Invalid input. Please enter numbers only."
            )


if __name__ == "__main__":
    root = tk.Tk()
    calculator = HourlyWageCalculatorGUI(root)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    root.mainloop()
