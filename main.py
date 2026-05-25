todos = []
 
print("=== Todo App ===")
 
while True:
    print("\n1. Add todo")
    print("2. Complete todo")
    print("3. Exit")
 
    if todos:
        print("\nYour todos:")
        for i, todo in enumerate(todos, 1):
            status = "✓" if todo["done"] else "○"
            print(f"  {i}. [{status}] {todo['text']}")
 
    choice = input("\nChoose option: ").strip()
 
    if choice == "1":
        text = input("Enter todo: ").strip()
        if text:
            todos.append({"text": text, "done": False})
            print(f"Added: {text}")
        else:
            print("Todo cannot be empty.")
 
    elif choice == "2":
        if not todos:
            print("No todos yet!")
        else:
            num = input("Enter todo number to complete: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(todos):
                todo = todos[int(num) - 1]
                todo["done"] = True
                print(f"Completed: {todo['text']}")
            else:
                print("Invalid number.")
 
    elif choice == "3":
        print("Bye!")
        break
 
    else:
        print("Invalid option. Enter 1, 2 or 3.")
        
print("To jest testowy plik")