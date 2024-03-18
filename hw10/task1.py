from pulp import LpProblem, LpMaximize, LpVariable

# Create the 'production' LP problem
production = LpProblem("Production", LpMaximize)

# Create the 'lemonade' and 'fruit_juice' variables
lemonade = LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = LpVariable('Fruit Juice', lowBound=0, cat='Integer')

# Add the objective function to the LP problem
production += lemonade + fruit_juice, "Total Production"

# Add the constraints to the LP problem
production += 2 * lemonade + fruit_juice <= 100, "Water"
production += lemonade <= 50, "Sugar"
production += lemonade <= 30, "Lemon Juice"
production += 2 * fruit_juice <= 40, "Fruit Puree"

# Solve the LP problem
production.solve()

# Print the results
print(f"Production of Lemonade: {lemonade.varValue}")
print(f"Production of Fruit Juice: {fruit_juice.varValue}")

