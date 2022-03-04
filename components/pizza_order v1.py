# list of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
               'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']
# List of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]


def menu ():
    number_pizza = 12

    for count in range (number_pizza):
        print("{} {} ${:.2f}" .format(count+1,pizza_names[count],pizza_prices[count])) 

menu()

# ask for total number of pizzas for order
num_pizzas = 0

num_pizzas = input("How many pizzas do you want to order?  ")

print(num_pizzas)

# Choose pizza from menu 



# Count down until all pizzas are ordered



# Pizza order