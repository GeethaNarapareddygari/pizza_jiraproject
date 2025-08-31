import matplotlib.pyplot as plt

customers_data = {
    'Alice': [25, 30, 22],
    'Bob': [15, 18],
    'Charlie': [35, 40, 30, 50],
    'Diana': [10, 12, 18, 20],
    'Eve': [25, 28, 26],
    'Frank': [60, 75, 55, 80, 120],
    'Grace': [12, 15, 10, 14, 11, 18],
    'Heidi': [26, 27, 25],
    'Ivan': [15, 30, 20, 45, 22, 18],
    'Judy': [50, 10, 40, 5, 30],
    'Kevin': [],
    'Leo': [100, 15, 50]
}
def find_eligible_customers(customers, min_orders, min_price):
    """
    Finds customers who have a minimum number of orders, each above a minimum price.
    
    Args:
        customers (dict): A dictionary with customer names as keys and a list of order prices as values.
        min_orders (int): The minimum number of orders a customer must have.
        min_price (int): The minimum price for each of those orders.
        
    Returns:
        list: A list of names of eligible customers.
    """
    eligible_list = []
    for customer, orders in customers.items():
        # Filter orders to find those that meet the minimum price
        qualifying_orders = [order for order in orders if order >= min_price]
        
        # Check if the number of qualifying orders meets the minimum requirement
        if len(qualifying_orders) >= min_orders:
            eligible_list.append(customer)
            
    return eligible_list

def visualize_sales(customers):
    """
    Visualizes total sales and income per customer.
    """
    customer_names = list(customers.keys())
    total_sales = [sum(orders) for orders in customers.values()]
    
    # Visualization 1: Total Sales per Customer (Bar Chart)
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.bar(customer_names, total_sales, color='skyblue')
    plt.xlabel('Customer')
    plt.ylabel('Total Sales ($)')
    plt.title('Total Sales per Customer')
    plt.xticks(rotation=45)
    
    # Visualization 2: Income Contribution (Pie Chart)
    total_income = sum(total_sales)
    
    plt.subplot(1, 2, 2)
    if total_income > 0:
        plt.pie(total_sales, labels=customer_names, autopct='%1.1f%%', startangle=140)
        plt.title('Customer Income Contribution')
    else:
        plt.text(0.5, 0.5, 'No sales data to display', horizontalalignment='center', verticalalignment='center')

    plt.tight_layout()
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    # Define the criteria for a free pizza
    minimum_orders = 3
    minimum_price_per_order = 25
    
    # Find and print the list of eligible customers
    eligible = find_eligible_customers(customers_data, minimum_orders, minimum_price_per_order)
    print(f"Customers eligible for a free pizza: {eligible}")
    
    # Visualize the sales data
    visualize_sales(customers_data)