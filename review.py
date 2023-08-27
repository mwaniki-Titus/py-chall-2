
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
    
# Testing Review class methods
print("All Reviews:")
for review in Review.all():
    print(f"Customer: {review.customer().full_name()}, Restaurant: {review.restaurant().name()}, Rating: {review.rating}")