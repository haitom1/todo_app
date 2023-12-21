todos = []



while True:
    user_action = input("Type add or show: ")
    user_action.strip(" ")


    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        
        case "show":
            for item in todos:
                item = item.title()
                print(item)

        case "exit":
            break

        case whatever:
            print("Type again")