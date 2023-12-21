FILEPATH = "data.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return  todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")



# while True:
#     user_action = input("Type add or show: ")
#     user_action.strip(" ")
#
#
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#
#         case "show":
#             for item in todos:
#                 item = item.title()
#                 print(item)
#
#         case "exit":
#             break
#
#         case whatever:
#             print("Type again")