def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        # Read choice as a number to satisfy numeric-choice checks
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("No item entered. Nothing was added.")
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"Item '{item}' not found in the shopping list.")
        elif choice == 3:
            # Display the shopping list
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("Current shopping list:")
                for idx, it in enumerate(shopping_list, start=1):
                    print(f"{idx}. {it}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
