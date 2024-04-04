from expense import Expense

def main():
    print(f"- - - - - Running Expense Tracker! - - - - -")

    # Get User input for expense
    expense = get_user_expense()
    # print(expense) debugging line to check whether get_user_expense is working correctly or not
    expense_file_path = "expense.csv"

    # write their expense to a file 
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expense(expense_file_path) 


def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name  =input("Enter expense name: ")
    expense_amount  =float(input("Enter expense amount: "))
    #print(f"You've Entered {expense_name}, {expense_amount}")
    expense_categories = [
        "🍕 Food", "🏠 Home", "💼 Work", "🥳 Fun", "✨ Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"    {i + 1}.{category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        
        else:
            print("Invalid category. Please try again")
 

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding='utf-8') as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def summarize_expense(expense_file_path):
    print(f"🎯 Summarizing User Expense")
    expenses = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines =f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(expense_name, expense_amount, expense_category)


# to make sure this main function runs only when we run this file , not as part of another file 
# we put it into a condition 
# this "__name__" is a special variable in python
if __name__ == "__main__":
    main()