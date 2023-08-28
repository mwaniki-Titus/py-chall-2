
from restaurant import Restaurant
from review import Review
from customer import Customer

# Creating instances of Restaurant
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Creating instances of Customer
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Adding reviews using the add_review method
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Testing Review class methods
print("All Reviews:")
for r in Review.all():
    print(f"Customer: {r.customer.full_name()}, Restaurant: {r.restaurant.name}, Rating: {r.rating}")

# Testing Restaurant class methods
print(f"\nAverage rating for {restaurant1.name}: {restaurant1.average_star_rating()}")

# Testing Customer class methods
print(f"\n{customer1.full_name()} has authored {customer1.num_reviews()} reviews.")
found_customer = Customer.find_by_name("John Doe")
if found_customer:
    print(f"Found customer: {found_customer.full_name()}")
else:
    print("Customer not found.")

all_johns = Customer.find_all_by_given_name("John")
print("\nCustomers with the given name 'John':")
for john in all_johns:
    print(john.full_name())
