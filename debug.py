#!/usr/bin/env python3
"""
Debug script to test the coffee shop functionality.
"""

from customer import Customer
from coffee import Coffee


def main():
    print("=== Coffee Shop Demo ===")

    print("\n--- Creating Customers ---")
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"Created customer: {alice.name}")
    print(f"Created customer: {bob.name}")

    print("\n--- Creating Coffees ---")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    print(f"Created coffee: {latte.name}")
    print(f"Created coffee: {espresso.name}")

    print("\n--- Creating Orders ---")
    alice_order = alice.create_order(latte, 4.50)
    print(
        f"Order created: {alice.name} ordered a {alice_order.coffee.name} for ${alice_order.price}"
    )

    bob_order = bob.create_order(espresso, 3.75)
    print(
        f"Order created: {bob.name} ordered a {bob_order.coffee.name} for ${bob_order.price}"
    )

    print("\n--- Customer Orders ---")
    alice_orders = alice.orders()
    print(f"{alice.name} has {len(alice_orders)} order(s)")

    bob_orders = bob.orders()
    print(f"{bob.name} has {len(bob_orders)} order(s)")

    print("\n--- Customer Coffees ---")
    alice_coffees = alice.coffees()
    print(f"{alice.name} ordered: {[coffee.name for coffee in alice_coffees]}")

    bob_coffees = bob.coffees()
    print(f"{bob.name} ordered: {[coffee.name for coffee in bob_coffees]}")

    print("\n--- Coffee Orders ---")
    print(f"{latte.name} has been ordered {latte.num_orders()} time(s)")
    print(f"{espresso.name} has been ordered {espresso.num_orders()} time(s)")

    print("\n--- Validation Example ---")
    try:
        print("Trying to create an order with a negative price...")
        invalid_order = alice.create_order(latte, -2.50)
    except ValueError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
