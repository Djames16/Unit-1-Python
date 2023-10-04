Todo=["get cash", "spend cash", "cry"]

while True:
    User=input("Would you like to add or remove a todo?")
    print(User)
    if User == "add": 
        print(Todo)

        Add=input("Enter an item:")

        Todo.append(Add)

        print(Todo)
    else:
        print(Todo)

        Delete=input("Select an item:")

        Todo.remove(Delete)
        
        print(Todo)