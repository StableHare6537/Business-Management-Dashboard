
def profit_margin(profit, sales):
    """What the function profit_margin do is that it takes the values from profit and sales
    and divides profit between sales and multiplies by 100."""
    if sales == 0:
        return 0

    return profit / sales * 100


def average_sales_per_order(Sales, number_of_orders):
    """DEF average_sales_per_order takes the value from sales and the number of orders.
    If the number of orders is equal to 0 return 0, if not divide sales between the number of orders."""
    if number_of_orders == 0:
        return 0

    return Sales / number_of_orders


def financial_status(Sales, Expenses):
    """DEF financial_status do is that if the expenses are greater than the sales,
    return financial warning because this is not positive for the business.
    Meanwhile, if the sales are greater than the expenses, return financial situation OK."""
    if Expenses > Sales:
        return "Financial warning"

    return "Financial situation OK"


def operational_status(pending_tasks, operational_problems):
    """I added a new function called operational_status which uses a conditional that says
    if operational_problems is greater than 0 return operational problems detected.
    Also we do the same for tasks and if there is no operational problem or pending task return all OK."""

    if operational_problems > 0:
        return "Operational problems detected"
    elif pending_tasks > 0:
        return "Pending tasks detected"
    else:
        return "Operations OK"


def main():

    while True:

        Sales = int(input("sales: "))
        Expenses = int(input("expenses: "))
        number_of_orders = int(input("number_of_sales: "))
        pending_tasks = int(input("pending_tasks: "))
        operational_problems = int(input("operational_problems: "))

        if Sales < 0 or Expenses < 0 or number_of_orders < 0 or pending_tasks < 0 or operational_problems < 0:
            print("Values cannot be negative")
            continue

        profit = Sales - Expenses

        print(profit)
        print(profit_margin(profit, Sales))
        print(average_sales_per_order(Sales, number_of_orders))
        print(financial_status(Sales, Expenses))
        print(operational_status(pending_tasks, operational_problems))

        again = input("Do you want to analyze another period? yes/no: ").lower()

        if again == "no":
            break


main()
