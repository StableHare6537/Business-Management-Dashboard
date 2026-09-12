def profit_margin(profit, sales):
    return profit / sales * 100


def average_sales_per_order(Sales, number_of_orders):
    if number_of_orders == 0:
        return 0

    return Sales / number_of_orders


def financial_status(Sales, Expenses):
    if Expenses > Sales:
        return "Financial warning"

    return "Financial situation OK"


def main():
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


main()


"""
What the function profit_margin do is that is takes the values from profit and sales and it divides profit between sales and multiply for 100.
DEF average_sales_per_order do is that takes the value from sales and the number of orders and it says, if the number of orders  is equal to 0 return 0, if not divide sales between the number of orders.
DEF financial_status do is that if the expenses are greater than the sales, return financial warning because this not positive for the bussiness. Meanwhile, if the sales are greater than the expenses, return financial situtation OK.
In the part main we have all the inputs and variables and prints. Also, we have a operantion called profit that it defines the value of the profit by a substraction.
"""
