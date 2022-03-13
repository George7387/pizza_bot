# List to store ordered pizzas
order_list = ['Margherita', 'Hawaiian', 'Vegan', 'BBQ Chicken Deluxe']
# List to store pizza prices
order_cost = [8.50, 8.50, 8.50, 13.50]

cust_details = {'name':'Mark','phone':'0213345656', 'house':'45', 'street':'Harry', 'suburb':'Howick'}


#print("\n",cust_details['name'],"\n",cust_details['phone'], "\n",cust_details['house'], "\n",cust_details['street'], "\n",cust_details['suburb'])

print("\n Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}".format( cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))
 


count = 0
for item in order_list:
    print("Ordered: {}  Cost ${:.2f}".format (item, order_cost[count]))
    count = count+1