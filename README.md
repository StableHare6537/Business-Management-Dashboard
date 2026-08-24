Project Context

My idea is to create a program for the management of restaurants and small businesses. What I am looking for is for them to be able to visualize their finances, progress, pending tasks, and problems in a simple way, similar to a dashboard.

I am interested in this project because I have noticed that in some businesses, important data can go unnoticed or is not reviewed with enough attention. This can cause problems to not be detected on time or opportunities to improve and become more efficient to be missed.

The main idea is for the program to show the information in a visual and easy-to-understand way, so that when someone reviews it, they can quickly understand how the business is doing without having to analyze too much text or a large amount of numbers.

With this information, better decisions could be made based on data, mainly in areas such as sales, expenses, profits, pending tasks, and problems that may be affecting the business.

AI helped me improve my idea and algorithm. I explained my idea about a dashboard for restaurants. This program would allow the personnel to make correct decisions based on data. I read the information that the AI proposed to me and I considered it solid. It helped me give a structure to the idea.

Algorithm

1. Start the program.

2. Display the main menu.

3. Ask the user what action they want to perform:

   * Register sales.
   * Register expenses.
   * Register number of orders.
   * Register a pending task.
   * Register an operational problem.
   * View dashboard.
   * Exit the program.

4. If the user selects **Register sales**:

   * Ask for the sales amount.
   * Validate that the value is positive.
   * Save the information.

5. If the user selects **Register expenses**:

   * Ask for the expense amount.
   * Ask for the expense category.
   * Validate the information.
   * Save the expense.

6. If the user selects **Register number of orders**:

   * Ask for the number of completed orders.
   * Validate that the value is a positive integer.
   * Save the information.

7. If the user selects **Register a pending task**:

   * Ask for a short description of the task.
   * Ask for its priority.
   * Save the task.

8. If the user selects **Register an operational problem**:

   * Ask for a description of the problem.
   * Ask for its level of importance.
   * Save the problem.

9. If the user selects **View dashboard**:

   * Calculate total sales.
   * Calculate total expenses.
   * Calculate profit:

   **Profit = Total sales - Total expenses**

   * Calculate profit margin:

   **Profit margin = Profit / Total sales × 100**

   * Calculate the average sale per order:

   **Average sale per order = Total sales / Number of orders**

   * Count pending tasks.
   * Count operational problems.

10. Display the results in a simple dashboard.

11. Show warnings when necessary:

* If expenses are greater than sales, show a financial warning.
* If the profit margin is low, show a profitability warning.
* If there are high-priority pending tasks, show an operational warning.
* If there are important unresolved problems, highlight them.

12. Return to the main menu.

13. Repeat the process until the user selects **Exit**.

14. End the program.

