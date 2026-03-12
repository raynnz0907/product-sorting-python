# START
# Create a list of products with name, price, and popularity

# DISPLAY menu
# 1. Sort by Price
# 2. Sort by Popularity
# 3. Sort Alphabetically

# INPUT user choice

# IF choice = 1
#     Sort products by price using Bubble Sort
# ELSE IF choice = 2
#     Sort products by popularity
# ELSE IF choice = 3
#     Sort products by name
# END IF

# DISPLAY sorted list of products

# END


products = [
    {"name": "Laptop", "price": 70000, "popularity": 90},
    {"name": "Headphones", "price": 2000, "popularity": 85},
    {"name": "Smartphone", "price": 50000, "popularity": 95},
    {"name": "Keyboard", "price": 1500, "popularity": 70}
]

def bubble_sort(products, key):
    n = len(products)

    for i in range(n):
        for j in range(0, n-i-1):
            if products[j][key] > products[j+1][key]:
                products[j], products[j+1] = products[j+1], products[j]

print("1. Sort by Price")
print("2. Sort by Popularity")
print("3. Sort Alphabetically")

choice = int(input("Enter your choice: "))

if choice == 1:
    bubble_sort(products, "price")

elif choice == 2:
    bubble_sort(products, "popularity")

elif choice == 3:
    bubble_sort(products, "name")

print("\nSorted Products:")
for p in products:
    print(p["name"], "- Price:", p["price"], "- Popularity:", p["popularity"])