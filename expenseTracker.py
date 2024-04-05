from expense import Expense
import datetime
import calendar

def main():
    print(f"- - - - - Running Expense Tracker! - - - - -")

    # Get User input for expense
    #expense = get_user_expense()
    # print(expense) debugging line to check whether get_user_expense is working correctly or not
    expense_file_path = "expense.csv"
    budget = 2000

    #write their expense to a file 
    #save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expense(expense_file_path, budget) 


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

def summarize_expense(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    expense_list : list[Expense]= []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines =f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expense_list.append(line_expense)

    amount_by_category = {}
    for expense in expense_list:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount  
        else:
            amount_by_category[key] = expense.amount
    
        
    print("Expense By Category")
    for key, amount in amount_by_category.items():
        print(f"    {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expense_list])
    print(f"🪙  You've spent ${total_spent:.2f} this month")


    # showing the budget
    remaining_budget = budget - total_spent
    if remaining_budget < 0:  
        new_remaining_budget = abs(remaining_budget)
        print(f"😟 Hey you are got over budget by ${new_remaining_budget:.2f}")
    else:
        print(f"💵 Your remaining budget ${remaining_budget:.2f}")

    # Get the current date
    now =datetime.datetime.now() 

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year,now.month)[1]       
    
    # Calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day

    print(f"Remaining days in the current month: {remaining_days}")


# to make sure this main function runs only when we run this file , not as part of another file we put it into a condition 
if __name__ == "__main__":      # this "__name__" is a special variable in python
    main()