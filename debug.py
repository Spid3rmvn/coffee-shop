#!/usr/bin/env python3
"""
Debug script to test the coffee shop functionality.
"""

from customer import Customer
from coffee import Coffee


def main():
    print("=== Coffee Shop Demo ===")

    # Create customers
    print("\n--- Creating Customers ---")
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"Created customer: {alice.name}")
    print(f"Created customer: {bob.name}")

    # Create coffees
    print("\n--- Creating Coffees ---")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    mocha = Coffee("Mocha")
    print(f"Created coffee: {latte.name}")
    print(f"Created coffee: {espresso.name}")
    print(f"Created coffee: {mocha.name}")

    # Create orders
    print("\n--- Creating Orders ---")
    alice_latte = alice.create_order(latte, 4.50)
    print(
        f"Order created: {alice.name} ordered a {alice_latte.coffee.name} for ${alice_latte.price}"
    )

    alice_mocha = alice.create_order(mocha, 5.75)
    print(
        f"Order created: {alice.name} ordered a {alice_mocha.coffee.name} for ${alice_mocha.price}"
    )

    bob_latte = bob.create_order(latte, 4.25)
    print(
        f"Order created: {bob.name} ordered a {bob_latte.coffee.name} for ${bob_latte.price}"
    )

    # Test Customer.orders()
    print("\n--- Customer.orders() ---")
    alice_orders = alice.orders()
    print(f"{alice.name} has {len(alice_orders)} order(s)")

    bob_orders = bob.orders()
    print(f"{bob.name} has {len(bob_orders)} order(s)")

    # Test Customer.coffees()
    print("\n--- Customer.coffees() ---")
    alice_coffees = alice.coffees()
    print(f"{alice.name} ordered these coffees: {[coffee.name for coffee in alice_coffees]}")

    bob_coffees = bob.coffees()
    print(f"{bob.name} ordered these coffees: {[coffee.name for coffee in bob_coffees]}")

    # Test Coffee.orders()
    print("\n--- Coffee.orders() ---")
    latte_orders = latte.orders()
    print(f"{latte.name} has {len(latte_orders)} order(s)")

    # Test Coffee.customers()
    print("\n--- Coffee.customers() ---")
    latte_customers = latte.customers()
    print(f"{latte.name} was ordered by: {[customer.name for customer in latte_customers]}")

    # Test Coffee.num_orders()
    print("\n--- Coffee.num_orders() ---")
    print(f"{latte.name} has been ordered {latte.num_orders()} time(s)")
    print(f"{mocha.name} has been ordered {mocha.num_orders()} time(s)")
    print(f"{espresso.name} has been ordered {espresso.num_orders()} time(s)")

    # Test Coffee.average_price()
    print("\n--- Coffee.average_price() ---")
    print(f"{latte.name} average price: ${latte.average_price():.2f}")
    print(f"{mocha.name} average price: ${mocha.average_price():.2f}")

    # Test validation
    print("\n--- Validation Examples ---")
    
    # Try to create a customer with a too-long name
    print("Trying to create a customer with a too-long name...")
    try:
        invalid_customer = Customer("ThisNameIsTooLongForTheSystem")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Try to create a coffee with a too-short name
    print("\nTrying to create a coffee with a too-short name...")
    try:
        invalid_coffee = Coffee("XY")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Try to create an order with an invalid price
    print("\nTrying to create an order with a negative price...")
    try:
        invalid_order = alice.create_order(latte, -2.50)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print("\nTrying to create an order with a price that's too high...")
    try:
        expensive_order = alice.create_order(espresso, 15.0)
    except ValueError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
