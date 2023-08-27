class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        self.__class__.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return [review.restaurant for review in self.reviews]

    def add_review(self, restaurant, rating):
        review = review(self, restaurant, rating)
        self.reviews.append(review)
# Testing Customer class methods
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Doe")
customer3 = Customer("John", "Doe")

print(f"\n{customer1.full_name()} has authored {customer1.num_reviews()} reviews.")
print(f"\n{customer2.full_name()} has authored {customer2.num_reviews()} reviews.")
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