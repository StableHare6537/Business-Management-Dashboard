
def profit_margin(profit, sales):
    """What the function profit_margin do is that is takes the values from profit and sales
       and it divides profit between sales and multiply for 100."""
    if sales == 0:
        return 0

    return profit / sales * 100


def average_sales_per_order(Sales, number_of_orders):
    """ DEF average_sales_per_order do is that takes the value from sales and the number of orders and it says,
if the number of orders  is equal to 0 return 0, if not divide sales between the number of orders."""
    if number_of_orders == 0:
        return 0

    return Sales / number_of_orders


def financial_status(Sales, Expenses):
    """DEF financial_status do is that if the expenses are greater than the sales,
return financial warning because this is not positive for the bussiness.
Meanwhile, if the sales are greater than the expenses, return financial situtation OK."""
    if Expenses > Sales:
        return "Financial warning"

    return "Financial situation OK"


def operational_status(pending_tasks, operational_problems):
    if operational_problems > 0:
        """I added a new function called operatinal_status which use a conditional that says if operational_problems is greater
           than 0 return "operational problems detected".
           Also we do the same for tasks and if there is no operational problem or pending task return all OK."""

        return "Operational problems detected"
    elif pending_tasks > 0:
        return "Pending tasks detected"
    else:
        return "Operations OK"


def show_history(period_names, history):
    """This function shows the information of all the periods saved in the matrix."""

    print("BUSINESS HISTORY")

    for i in range(len(history)):
        print("Period:", period_names[i])
        print("Sales:", history[i][0])
        print("Expenses:", history[i][1])
        print("Orders:", history[i][2])
        print("Profit:", history[i][0] - history[i][1])
        print("--------------------")


def main():

    period_names = []
    history = []

    while True:

        period = input("Period name: ").strip().title()

        Sales = int(input("sales: "))
        Expenses = int(input("expenses: "))
        number_of_orders = int(input("number_of_sales: "))
        pending_tasks = int(input("pending_tasks: "))
        operational_problems = int(input("operational_problems: "))

        profit = Sales - Expenses

        print(profit)
        print(profit_margin(profit, Sales))
        print(average_sales_per_order(Sales, number_of_orders))
        print(financial_status(Sales, Expenses))
        print(operational_status(pending_tasks, operational_problems))

        
        period_names.append(period)

        
        row = [Sales, Expenses, number_of_orders,
               pending_tasks, operational_problems]

        history.append(row)

        again = input("Do you want to analyze another period? yes/no: ")
        again = again.strip().lower()

        if again == "no":
            break

    show_history(period_names, history)


main()
