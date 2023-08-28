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


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.__class__.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def customers(self):
        return [review.customer for review in self.reviews]

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)
  # Testing Restaurant class methods
print("All Restaurants:")
for restaurant in Restaurant.all():
    print(f"Name: {restaurant.name}, Rating: {restaurant.average_star_rating()}")

restaurant1 = Restaurant("Pizza Place")
print(f"\nAverage rating for {restaurant1.name}: {restaurant1.average_star_rating()}")  
print(f"\nAverage rating for {restaurant1.name}: {restaurant1.average_star_rating()}")




