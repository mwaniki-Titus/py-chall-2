# py-chall-2
##Restaurant Class:

The Restaurant class represents a restaurant. It has a class attribute all_restaurants to keep track of all restaurant instances.
The __init__ method initializes a restaurant with a name. It also initializes empty lists for reviews and customers.
The add_review method takes a customer and a rating, creates a new Review instance, and adds it to the restaurant's reviews list, as well as to the customer's reviews list. It also adds the customer to the restaurant's customers list.
The average_star_rating method calculates the average rating for the restaurant based on its reviews.

##Customer Class:

The Customer class represents a customer. It has a class attribute all_customers to keep track of all customer instances.
The __init__ method initializes a customer with given_name and family_name. It also initializes an empty list for reviews.
The add_review method is a shortcut to add a review for a specific restaurant with a rating.
The num_reviews method returns the total number of reviews authored by the customer.
The find_by_name class method takes a full name as input and returns the first customer whose full name matches.
The find_all_by_given_name class method takes a given name as input and returns a list of all customers with that given name.

##Review Class:

The Review class represents a review. It has a class attribute all_reviews to keep track of all review instances.
The __init__ method initializes a review with a customer, restaurant, and a rating.
The customer and restaurant methods are used to retrieve the associated customer and restaurant for a review.
The all class method returns a list of all review instances.