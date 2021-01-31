
if __name__ == "__main__":
    print("Singly Link List")
    lst = SinglyLinkedList()
    while True:
        print("\n1. View/print Link List")
        print("2. Insert at begining")
        print("3. Insert at end")
        print("4. Insert at given position")
        print("5. Delete first node")
        print("6. Delete last node")
        print("7. Delete the given node")
        print("8. Delete the data")
        print("9. Delete whole list ")
        print("10. Count Nodes")
        print("0. Exit")
        choice = int(input("Enter Your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            lst.print()
        elif choice == 2:
            data = input("Enter data to insert: ")
            lst.insert_atBegining(data)
        elif choice == 3:
            data = input("Enter data to insert: ")
            lst.insert_atEnd(data)
        elif choice == 4:
            position = int(input("Enter position: "))
            data = input("Enter data to insert: ")
            lst.insert_atPosition(position, data)
        elif choice == 5:
            print(lst.delete_firstNode())
        elif choice == 6:
            print(lst.delete_lastNode())
        elif choice == 7:
            position = int(input("Enter position: "))
            print(lst.delete_byPosition(position))
        elif choice == 8:
            data = input("Enter data to delete: ")
            lst.remove(data)
        elif choice == 9:
            lst.delete()
        elif choice == 10:
            print(lst.length())
        else:
            print("Enter a valid choice: ")
