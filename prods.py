def names():
    popular = ["tomatoes", "oranges", "pineapples", "coffee", "strawberries"]

    print(popular)
    print(popular[0])
    #for loop
    for object in popular:
        print(object)

def prices():
    popular_prices = [12.99, 34.76, 11.95, 39.00, 23, 46.90, 12.34]
    total = 0
    for price in popular_prices:
        total = total + price

        if price > 20:
            print(price)

    print(total)


def manager():
    products = [
        {
            "_id": "1a2b3c4d5e6f7g8h9i0j",
            "title": "Wireless Headphones",
            "price": 79.99,
            "image": "https://example.com/images/headphones.jpg",
            "category": "Electronics"
        },
        {
            "_id": "2b3c4d5e6f7g8h9i0j1a",
            "title": "Gaming Mouse",
            "price": 39.99,
            "image": "https://example.com/images/mouse.jpg",
            "category": "Electronics"
        },
        {
            "_id": "3c4d5e6f7g8h9i0j1a2b",
            "title": "Running Shoes",
            "price": 59.99,
            "image": "https://example.com/images/shoes.jpg",
            "category": "Footwear"
        },
        {
            "_id": "4d5e6f7g8h9i0j1a2b3c",
            "title": "Coffee Maker",
            "price": 99.95,
            "image": "https://example.com/images/coffeemaker.jpg",
            "category": "Home Appliances"
        },
        {
            "_id": "5e6f7g8h9i0j1a2b3c4d",
            "title": "Yoga Mat",
            "price": 25.00,
            "image": "https://example.com/images/yogamat.jpg",
            "category": "Fitness"
        }
    ]

    #for loop to print each product's title
    for product in products:
        price = product["price"]
        if price > 50:
            print(product["title"]) 





#call fns
names()
prices()
manager()