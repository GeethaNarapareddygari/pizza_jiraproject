import matplotlib.pyplot as plt
import seaborn as sns

def find_eligible_customers(customers, min_orders, min_price):
    eligible_customers = []
    for customer, orders in customers.items():
        # Check if the customer meets the minimum number of orders
        if len(orders) >= min_orders:
            # Check if all of their orders are at or above the minimum price
            if all(order >= min_price for order in orders):
                eligible_customers.append(customer)
    return eligible_customers

def visualize_sales(customers):
    # Calculate the total income from each customer
    customer_income = {name: sum(orders) for name, orders in customers.items()}
    
    if not customer_income:
        print("No customer data to visualize.")
        return

    # Sort customers by income for a cleaner chart
    sorted_customers = sorted(customer_income.items(), key=lambda item: item[1], reverse=True)
    names = [item[0] for item in sorted_customers]
    income = [item[1] for item in sorted_customers]

    # --- Create the Visualization ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bars with a color palette
    bars = ax.bar(names, income, color=sns.color_palette("viridis", len(names)))

    # Add labels and a title for clarity
    ax.set_title('Total Income per Customer', fontsize=16, fontweight='bold')
    ax.set_xlabel('Customer', fontsize=12)
    ax.set_ylabel('Total Income ($)', fontsize=12)
    
    # Add data labels on top of each bar
    ax.bar_label(bars, fmt='$%.2f')

    # Rotate x-axis labels for better readability and adjust layout
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    # Sample customer data to test the functions
    customer_data = {
        'Alice': [25.50, 30.00, 22.75],
        'Bob': [40.00, 45.50],
        'Charlie': [18.00, 20.50, 25.00],
        'Diana': [35.00, 38.20, 32.50, 40.00],
        'Eve': [15.00, 19.50],
        'Frank': [30.00, 31.00, 33.00]
    }

    MINIMUM_ORDERS = 3
    MINIMUM_ORDER_PRICE = 30.00

    eligible = find_eligible_customers(customer_data, MINIMUM_ORDERS, MINIMUM_ORDER_PRICE)
    
    print(f"--- Pizza Promotion Eligibility ---")
    print(f"Criteria: At least {MINIMUM_ORDERS} orders, each over ${MINIMUM_ORDER_PRICE:.2f}")
    print(f"Eligible Customers: {eligible}")
    print("---------------------------------")

    visualize_sales(customer_data)