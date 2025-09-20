tasks = []

def menu ():
  print(40*"=")
  print("             TO-DO LIST                ")
  print(40*"=")
  print(" 1 - ADD tasks")
  print(" 2 - REMOVE taks already done")
  print(" 3 - SHOW the To-Do list ")
  print(" 4 - Exit")


def adding ():
   while True:
        add = input("Enter a task (or type 'out' to stop): ")
        if add.lower() == "out":
            break  
        else:
            tasks.append(add)
  


def remove ():
  remove = input("What do you alreaady did: ")
  if remove in tasks:
    tasks.remove(remove)
    print(f"I´m proud of you! the item {remove}´s done!")
  else:
    print("item did not find in it!")  


def show ():
  if not tasks:
    print("Your list is empty!")
  else:
        print("\n" + 40 * "=")
        print("             T A S K S")
        print(40 * "=")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print(40 * "=")

 
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        adding()
    elif choice == "2":
        remove()
    elif choice == "3":
        show()
    elif choice == "4":
        print(" SEE YOU NEXT TIME!")
        break
    else:
        print(" Invalid choice! Please enter 1, 2, 3, or 4.")
