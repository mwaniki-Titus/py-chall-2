from review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.customers = []
        Restaurant.all_restaurants.append(self)

    def add_review(self, customer, rating):
        review = Review(customer, self, rating)
        self.reviews.append(review)
        customer.reviews.append(review)
        self.customers.append(customer)

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews





