items = ["Milk", "Bread", "Eggs", "Butter", "Cheese"]
print("Shopping list:")
for item in items:
    print(item)

new_item = input("Add a new item to the list: ")
items.append(new_item)

print("Updated shopping list: ")
for item in items:
    print(item)
