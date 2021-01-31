
if __name__ == "__main__":
    s = Stack()
    while True:
        print("\n1. View Stack")
        print("2. Push")
        print("3. Pop")
        print("4. Peek")
        print("5. Size of Stack")
        print("0. Exit")
        ch = int(input("Enter your choice"))
        if ch == 0:
            break
        elif ch == 1:
            print(s)
        elif ch == 2:
            value = input("Enter a value to push: ")
            s.push(value)
        elif ch == 3:
            print(s.pop())
        elif ch == 4:
            print(s.peek())
        elif ch == 5:
            print(s.length())
        else:
            print("Please Enter valid choice")
