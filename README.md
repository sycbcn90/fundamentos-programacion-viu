# Exercise 1

## Explanation

In this exercise, we need to calculate whether the budget is enough to pay the real total price. We create different concepts to calculate the total price and then compare it with the budget.

## How my script works

1. **Import the package.** I import the Python package `rich`, and from it `Console` and `Table`. `Console` is used to print with colors, and `Table` is used to create the table.
2. **Define the variables.** I define the different concepts based on the requirements (base price, age, number of tickets and budget).
3. **Define the discount.** I create an `if-elif-else` condition to set the discount percentage depending on the age.
4. **Calculate the total price.** I calculate the real total price based on the previous steps.
5. **Compare with the budget.** I compare the real total price with the budget and get the price difference.
6. **Show the table.** Using the related information, I create a table with `Table` and print it.

## Where I used AI

After finishing the whole script, I used Claude Code to check whether the code met the requirements. I made two improvements with its help:

1. In each `if` branch, after each `porcentaje_descuento`, I wrote `descuento_persona = precio_base * porcentaje_descuento / 100`. Claude Code suggested writing this line only once, after the `if-elif-else` condition, instead of repeating it inside each branch.
2. When the budget was not enough (`dinero_sobra < 0`), I printed `falta {dinero_sobra:.2f}`. Claude Code suggested changing it to `{abs(dinero_sobra):.2f}`, so the missing amount is shown as a positive number instead of a negative one.