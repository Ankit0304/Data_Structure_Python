# Creation of Node class for Doubly Linked List to hold the data, the previous pointer and the next pointer
class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

# creation of Doubly Linked List class
class DoublyLL:
    # creating head or start node
    def __init__(self, start=None):
        self.start = start

    # is_empty method to check if the linked list is empty
    def is_empty(self):
        return self.start is None

    # Insertion at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = new_node
        self.start = new_node

    # Insertion at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(None, data, None)
        if self.is_empty():
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

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
        new_node = Node(temp, data, temp.next)
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node

    # Search for a specific element in the linked list
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                print(f'{data} found in the linked list')
                return
            temp = temp.next
        print(f'{data} not found in the linked list')

    # Deletion at the beginning of the linked list
    def delete_at_beginning(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        self.start = self.start.next
        if self.start is not None:
            self.start.prev = None

    # Deletion at the end of the linked list
    def delete_at_end(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        if temp.prev is not None:
            temp.prev.next = None
        else:
            self.start = None

    # Deletion at a specific position
    def delete_at_position(self, pos):
        if self.is_empty():
            print("Linked list is empty")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.start
        for i in range(pos):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.start = temp.next

    # Traversal of the linked list
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

# Main function to run the program
def main():
    new_ll = DoublyLL()
    while True:
        print("\nChoose an operation:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Insert at position")
        print("4. Search")
        print("5. Delete at the beginning")
        print("6. Delete at the end")
        print("7. Delete at position")
        print("8. Print")
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
            data = int(input("Enter the data to be searched: "))
            new_ll.search(data)
        elif choice == 5:
            new_ll.delete_at_beginning()
        elif choice == 6:
            new_ll.delete_at_end()
        elif choice == 7:
            pos = int(input("Enter the position to delete the data: "))
            new_ll.delete_at_position(pos)
        elif choice == 8:
            new_ll.print_list()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
