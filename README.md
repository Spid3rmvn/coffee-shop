# Coffee Shop Challenge

A Python implementation of a coffee shop management system demonstrating object-oriented programming principles and many-to-many relationships through an intermediate class.

## 🎯 Challenge Overview

This project implements a Coffee shop-style domain with three models: **Coffee**, **Customer**, and **Order**. The relationships are:

- A Coffee has many Orders
- A Customer has many Orders
- An Order belongs to a Customer and to a Coffee
- Coffee-Customer is a many-to-many relationship (through Order)

**Single Source of Truth**: The Order class serves as the single source of truth for the relationship between Coffee and Customer.

## ✅ Requirements Implementation

### 1. Models & Initializers

#### **Customer** ✓

- `__init__(self, name)` - Stores a name (must be a string, 1-15 characters)
- **Property** `name` - Getter and setter with validation
  - Enforces string type
  - Enforces 1-15 character length

#### **Coffee** ✓

- `__init__(self, name)` - Stores a name (must be a string, at least 3 characters)
- **Property** `name` - Getter only (immutable after initialization)
  - Enforces string type
  - Enforces minimum 3 character length

#### **Order** ✓

- `__init__(self, customer, coffee, price)` - Accepts Customer instance, Coffee instance, and price
  - Price must be a float between 1.0-10.0
- **Property** `price` - Getter only (immutable)
  - Enforces type and range validation

### 2. Object Relationships ✓

All required relationships are implemented:

- `Order.customer` → Returns the Customer instance (type-checked)
- `Order.coffee` → Returns the Coffee instance (type-checked)
- `Customer.orders()` → All Order instances for that customer
- `Customer.coffees()` → Unique list of Coffee instances they've ordered
- `Coffee.orders()` → All Order instances for that coffee
- `Coffee.customers()` → Unique list of Customer instances who've ordered it

### 3. Aggregates & Associations ✓

- `Customer.create_order(coffee, price)` - Creates a new Order linked to the customer and coffee
- `Coffee.num_orders()` - Returns total count of orders (0 if none)
- `Coffee.average_price()` - Returns mean of all order prices (0 if none)

## 📁 Project Structure

```
coffee-shop-challenge/
├── Pipfile
├── README.md
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
    ├── customer_test.py
    ├── coffee_test.py
    └── order_test.py
```

## 🚀 Getting Started

### Installation

1. Clone the repository:

```bash
git clone git@github.com:<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge
```

2. Initialize your Python environment:

```bash
pipenv install
pipenv shell
```

### Usage Example

```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
alice = Customer("Alice")
latte = Coffee("Latte")

# Create order using Customer.create_order()
order = alice.create_order(latte, 4.50)

# Access relationships
print(alice.orders())       # [<Order instance>]
print(alice.coffees())      # [<Coffee: Latte>]
print(latte.customers())    # [<Customer: Alice>]
print(latte.num_orders())   # 1
print(latte.average_price()) # 4.5
```

## 🧪 Testing

The project includes comprehensive unit tests for all models and their relationships.

Run all tests:

```bash
python -m pytest tests/
```

Run individual test files:

```bash
python tests/customer_test.py
python tests/coffee_test.py
python tests/order_test.py
```

## 💡 Implementation Details

### Validation & Error Handling

- **Customer name**: Must be 1-15 characters

  - `TypeError` if not a string
  - `ValueError` if length is invalid

- **Coffee name**: Must be at least 3 characters

  - `TypeError` if not a string
  - `ValueError` if too short

- **Order price**: Must be between $1.00 and $10.00
  - `TypeError` if not a number
  - `ValueError` if outside range

### Design Patterns

1. **Property Decorators**: Used for controlled access to attributes
2. **Type Checking**: Ensures data integrity across relationships
3. **Immutability**: Coffee names and Order prices cannot be changed after creation
4. **Single Source of Truth**: Order class maintains the relationship data

### Relationship Management

The many-to-many relationship between Customer and Coffee is implemented through the Order class:

- Each Order maintains references to both Customer and Coffee
- Customer and Coffee classes aggregate their orders to provide relationship methods
- Unique lists are maintained to prevent duplicates in `customers()` and `coffees()` methods

## 📝 Additional Features

Beyond the basic requirements, the implementation includes:

- String representation methods (`__str__`) for better debugging
- Comprehensive docstrings for all methods
- Proper encapsulation with private attributes (`_name`, `_orders`, etc.)
- Defensive programming with extensive input validation

## 🏆 Challenge Completion

This implementation successfully meets all requirements of the Coffee Shop Challenge:

- ✅ All three models implemented with proper initializers
- ✅ All required properties with appropriate getters/setters
- ✅ All object relationships properly established
- ✅ All aggregate and association methods implemented
- ✅ Comprehensive test coverage
- ✅ Proper error handling and validation

## License

This project is part of a coding challenge and is for educational purposes.
