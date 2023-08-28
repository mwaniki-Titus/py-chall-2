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

    
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return [review.restaurant for review in self.reviews]

    def add_review(self, restaurant, rating):
        review = review(self, restaurant, rating)
        self.reviews.append(review)
class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

# Testing Customer class methods
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Doe")
customer3 = Customer("John", "Doe")

print(f"{customer1.full_name()} has authored {len(customer1.add_review)} reviews.")
print(f"{customer2.full_name()} has authored {len(customer2.add_review)} reviews.")
print(f"{customer1.full_name()} has authored {len(customer1.add_review)} reviews.")
   