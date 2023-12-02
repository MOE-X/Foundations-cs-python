from anytree import Node, RenderTree, PreOrderIter
from datetime import datetime

class FamilyMember:
    def __init__(self, name, family_name, birthdate):
        self.name = name
        self.family_name = family_name
        self.birthdate = birthdate
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def add_family_member():
    name = input("Enter the name: ")
    family_name = input("Enter the family name: ")
    birthdate_str = input("Enter the birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

    # Assume root as the starting point, you can modify this as needed
    root = Node("Root")
    new_member = FamilyMember(name, family_name, birthdate)
    
    parent_name = input("Enter the parent's name (or 'Root' for the first generation): ")
    parent = find_member(root, parent_name)

    if parent:
        parent_node = Node(parent_name, parent)
        parent.data.add_child(new_member)
        print(f"{name} {family_name} added to the family tree.")
    else:
        print(f"Parent {parent_name} not found.")

def display_sorted_birthdays(root):
    birthdays = []

    for node in PreOrderIter(root):
        if hasattr(node, 'data') and hasattr(node.data, 'birthdate'):
            birthdays.append((node.data.name, node.data.family_name, node.data.birthdate))

    sorted_birthdays = sorted(birthdays, key=lambda x: x[2])
    
    print("\nSorted Birthdays:")
    for birthday in sorted_birthdays:
        print(f"{birthday[0]} {birthday[1]}: {birthday[2].strftime('%Y-%m-%d')}")

def find_relationship(root, member1_name, member2_name):
    member1 = find_member(root, member1_name)
    member2 = find_member(root, member2_name)

    if member1 and member2:
        relationship = get_relationship(member1, member2)
        print(f"The relationship between {member1_name} and {member2_name} is: {relationship}")
    else:
        print("One or both family members not found.")

def visualize_family_tree(root):
    for pre, _, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

def count_same_first_names(root, first_name):
    count = 0

    for node in PreOrderIter(root):
        if hasattr(node, 'data') and hasattr(node.data, 'name') and node.data.name.split()[0] == first_name:
            count += 1

    print(f"There are {count} family members with the first name {first_name}.")

def find_member(root, name):
    for node in PreOrderIter(root):
        if hasattr(node, 'data') and hasattr(node.data, 'name') and node.data.name == name:
            return node.data
    return None

def get_relationship(member1, member2):
    # You need to define your logic for determining the relationship
    # This is a placeholder, and you should customize it based on your family tree structure
    return "Relationship logic not implemented."

if __name__ == "__main__":
    root = Node("Root")  # Initial family tree with the root node

    while True:
        print("\n- - - - - - - - - - - - - - -")
        print("1. Add Family Member")
        print("2. Display Sorted Birthdays")
        print("3. Find Relationship")
        print("4. Visualize Family Tree")
        print("5. Count Same First Names")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_family_member()
        elif choice == "2":
            display_sorted_birthdays(root)
        elif choice == "3":
            member1_name = input("Enter the name of the first family member: ")
            member2_name = input("Enter the name of the second family member: ")
            find_relationship(root, member1_name, member2_name)
        elif choice == "4":
            visualize_family_tree(root)
        elif choice == "5":
            first_name = input("Enter the first name to count: ")
            count_same_first_names(root, first_name)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
