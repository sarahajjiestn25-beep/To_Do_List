Tasks=[]
print("📝 Welcome to the To-Do List App!")
while True:
    print("-----------------------")
    print("choose an option :")
    print("1:Add task ")
    print("2:View Tasks ")
    print("3:Delete Task " )
    print("4:Exit ")
    print("-----------------------")
    choice = input("Enter your choice (1-4):")
    #add tasks
    if choice == "1":
        value=input("Enter a task :")
        Tasks.append(value)
        print("✅ Task added")
    #view tasks
    elif choice == "2":
        if not Tasks:
            print("No tasks yet")
        else:
            print("your tasks 📝:")
            i=1
            for data in Tasks:
                print(i,data)
                i+=1
    #delete tasks            
    elif choice =="3":
        if not Tasks:
            print("No tasks to delete !")
        else:
            i=1
            print("Your Tasks:")
            for data in Tasks:
                print(i,data)
                i+=1
            task_number=input("Enter Task number to delete:") 
            task_number=int(task_number)
            if task_number>=1 and task_number<=len(Tasks):
                deleted= Tasks.pop(task_number-1)
                print(f"deleted tasks is :{deleted}")
            else :
                print("Invailid value")  
    elif choice =="4":
        print("Goodbye 🖐️!")   
        break
    else:
        print("invalid choice")         



