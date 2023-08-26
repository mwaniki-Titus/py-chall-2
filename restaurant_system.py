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
        review = Review(self, restaurant, rating)
        self.reviews.append(review)


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


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.__class__.all_reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant


# Create instances and test methods
if __name__ == "__main__":
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Jane", "Smith")
    restaurant1 = Restaurant("Pizza Place")
    restaurant2 = Restaurant("Burger Joint")

    customer1.add_review(restaurant1, 4)
    customer1.add_review(restaurant2, 5)
    customer2.add_review(restaurant1, 3)
    customer2.add_review(restaurant2, 2)

    print(customer1.full_name())  # Output: John Doe
    print(restaurant1.name())  # Output: Pizza Place
    print(customer1.restaurants())  # Output: [Pizza Place, Burger Joint]
    print(restaurant1.customers())  # Output: [John Doe, Jane Smith]
    print(restaurant1.average_star_rating())  # Output: 3.5
