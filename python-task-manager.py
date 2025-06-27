def insert(title, duration, priority):
    task= [title,duration, priority]
    queue.append(task)
    
queue = []

#We ask the user to give us the number of tasks
task_number = input("Please input the number of tasks: ")
#We need to verify that the user's input is a positive number (int)


if not task_number.isdigit() or int(task_number) < 0:
    print("Please enter a number greater than zero")
    exit()
elif int(task_number) == 0:
    print("There are not tasks")
else:
    for i in range(int(task_number)):
        task_name = input("Please enter the task name: ")
        task_duration = input("Please input task duration: ")
        if not task_duration.isdigit() or int(task_duration) <=0:
            print("Please enter a number greater than zero for duration")
            exit()
        else:
            task_priority = input("Please input task priority: ")
            if not task_priority.isdigit() or int(task_priority) <0:
                print("Please enter an integer. ")
                exit()
            else: 
                task_duration = int(task_duration)
                task_priority = int(task_priority)
                insert(task_name,task_duration,task_priority)

print(queue)