from customer import Customer
from coffee import Coffee


def main():
    print("=== Coffee Shop Demo ===")

    # Create customers
    print("\n1. Creating customers:")
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"   - Created customer: {alice.name}")
    print(f"   - Created customer: {bob.name}")

    # Create coffee types
    print("\n2. Creating coffee types:")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    print(f"   - Created coffee: {latte.name}")
    print(f"   - Created coffee: {espresso.name}")

    # Create orders
    print("\n3. Creating orders:")
    # Alice orders a latte
    alice_order = alice.create_order(latte, 4.50)
    print(
        f"   - {alice.name} ordered a {alice_order.coffee.name} for ${alice_order.price}"
    )

    # Bob orders an espresso
    bob_order = bob.create_order(espresso, 3.75)
    print(f"   - {bob.name} ordered a {bob_order.coffee.name} for ${bob_order.price}")

    # Check customer orders
    print("\n4. Checking customer orders:")
    alice_orders = alice.orders()
    print(f"   - {alice.name} has {len(alice_orders)} order(s)")

    bob_orders = bob.orders()
    print(f"   - {bob.name} has {len(bob_orders)} order(s)")

    # Check what coffees each customer ordered
    print("\n5. Checking what coffees each customer ordered:")
    alice_coffees = alice.coffees()
    print(f"   - {alice.name} ordered: {[coffee.name for coffee in alice_coffees]}")

    bob_coffees = bob.coffees()
    print(f"   - {bob.name} ordered: {[coffee.name for coffee in bob_coffees]}")

    # Check coffee orders
    print("\n6. Checking how many times each coffee was ordered:")
    print(f"   - {latte.name} has been ordered {latte.num_orders()} time(s)")
    print(f"   - {espresso.name} has been ordered {espresso.num_orders()} time(s)")

    # Demonstrate error handling
    print("\n7. Demonstrating error handling:")
    try:
        # Try to create an order with an invalid price
        print("   - Trying to create an order with a negative price...")
        invalid_order = alice.create_order(latte, -2.50)
    except ValueError as e:
        print(f"   - Error caught: {e}")


if __name__ == "__main__":
    main()
