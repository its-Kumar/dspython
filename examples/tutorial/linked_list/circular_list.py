
if __name__ == "__main__":
    print("Singly Link List")
    lst = CircularLinkedList()
    while True:
        print("\n1. View/print Link List")
        print("2. Insert at begining")
        print("3. Insert at end")
        print("4. Delete first node")
        print("5. Delete last node")
        print("6. Count Nodes")
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
            print(lst.delete_firstNode())
        elif choice == 5:
            print(lst.delete_lastNode())
        elif choice == 6:
            print(lst.length())
        else:
            print("Enter a valid choice: ")
