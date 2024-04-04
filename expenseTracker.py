def main():
    print(f"🎯 Running Expense Tracker!")

    # Get User input for expense
    get_user_expense()

    # write their expense to a file 
    save_expense_to_file()

    # Read file and summarize expense
    summarize_expense()

    

def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name  =input("Enter expense name: ")
    expense_amount  =float(input("Enter expense amount: "))
    print(f"You've Entered {expense_name}, {expense_amount}")

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
            break
        else:
            print("Invalid category. Please try again")
 

def save_expense_to_file():
    print(f"🎯 Saving User Expense")
    

def summarize_expense():
    print(f"🎯 Summarizing User Expense")
    

# to make sure this main function runs only when we run this file , not as part of another file 
# we put it into a condition 
# this "__name__" is a special variable in python

if __name__ == "__main__":
    main()