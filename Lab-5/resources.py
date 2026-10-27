resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

def display_resources(items):
    print("\nID    Name            Category        Quantity")
    print("-" * 45)
    for item in items:
        item_id = item[0]
        name = item[1]
        category = item[2]
        quantity = item[3]
        print(f"{item_id:<5} {name:<15} {category:<15} {quantity}")

def search_by_category(items, category):
    print(f"\n--- Resources in '{category}' ---")
    found = False
    for item in items:
        item_id = item[0]
        name = item[1]
        item_category = item[2]
        quantity = item[3]

        if item_category.lower() == category.lower():
            print(f"ID: {item_id}, Name: {name}, Quantity: {quantity}")
            found = True

    if not found:
        print("No resources found in this category.")

def find_unavailable(items):
    print("\n--- Unavailable Resources (Quantity = 0) ---")
    for item in items:
        item_id = item[0]
        name = item[1]
        category = item[2]
        quantity = item[3]

        if quantity == 0:
            print(f"ID: {item_id}, Name: {name} ({category})")

display_resources(resources)
search_by_category(resources, "Electronics")
find_unavailable(resources)
