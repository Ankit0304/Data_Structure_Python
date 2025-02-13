# creation of Node class for Singly Linked List to hold the data and the next pointer
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

# creation of Singly Linked List class
class Singly_LL:
    # creating head or start node
    def __init__(self, start=None):
        self.start = start

    # is_empty method to check if the linked list is empty
    def is_empty(self):
        return self.start is None

    # Insertion at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    # Insertion at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        else:
            self.start = new_node

    # Insertion at a specific position
    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        temp = self.start
        for i in range(pos - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node = Node(data, temp.next)
        temp.next = new_node

    # Search for a specific element in the linked list
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                print(f'{data} found in the linked list')
                return
            temp = temp.next
        print(f'{data} not found in the linked list')

    # Traversal of the linked list
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    # Deletion at the beginning of the linked list
    def delete_at_beginning(self):
        if not self.is_empty():
            temp = self.start
            self.start = self.start.next
            del temp
        else:
            print("Linked list is empty")

    # Deletion at the end of the linked list
    def delete_at_end(self):
        if not self.is_empty():
            temp = self.start
            if temp.next is None:
                self.start = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            print("Linked list is empty")

    # Deletion at a specific position of the linked list
    def delete_at_position(self, pos):
        if self.is_empty():
            print("Linked list is empty")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.start
        for i in range(pos - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp.next is None:
            print("Position out of bounds")
            return
        temp.next = temp.next.next

# Main function to provide a menu for user interaction
def main():
    new_ll = Singly_LL()
    while True:
        print("\nMenu:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete at beginning")
        print("5. Delete at end")
        print("6. Delete at position")
        print("7. Search")
        print("8. Print list")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the data to be inserted at the beginning: "))
            new_ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter the data to be inserted at the end: "))
            new_ll.insert_at_end(data)
        elif choice == 3:
            pos = int(input("Enter the position to insert the data: "))
            data = int(input("Enter the data to be inserted: "))
            new_ll.insert_at_position(pos, data)
        elif choice == 4:
            new_ll.delete_at_beginning()
        elif choice == 5:
            new_ll.delete_at_end()
        elif choice == 6:
            pos = int(input("Enter the position to delete the data: "))
            new_ll.delete_at_position(pos)
        elif choice == 7:
            data = int(input("Enter the data to be searched: "))
            new_ll.search(data)
        elif choice == 8:
            new_ll.print_list()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()