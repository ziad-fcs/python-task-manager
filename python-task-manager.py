def insert(title, duration, priority):
    task= [title,duration, priority]
    queue.append(task)

def extract(queue,i= 0):
    if is_empty(queue):
        print("The queue is empty, cannot remove anything from it")
        return None
    elif i < 0 or i >= len(queue):
        print("Invalid index")
        return None
    else: return queue.pop(i)

def peek(queue, i=0):
    if is_empty(queue):
        print("The queue is empty")
        return None
    elif i <0 or i>= len(queue):
        print("Invalid Index")
    return queue[i]

def is_empty(queue):
    return len(queue) ==0
        
def complete_next_task(queue):
    if is_empty(queue):
        print("The queue is empty, no tasks to be completed")
        return None
    highest_priority = 0
    for i in range(1, len(queue)):
        if queue[i][2] < queue[highest_priority][2]:  
            highest_priority = i
    task = extract(queue,highest_priority)
    if task != None:
        print("The completed task is: ")
        print("Name: ", task[0])
        print("Duration: ", task[1], "min")
        print("Priority: ", task[2])

def sort_task_by_title(queue):
    n = len(queue)
    for i in range(n-1):
        min_i = i
        for j in range (i + 1, n):
            if queue[j][0].lower() < queue[min_i][0].lower():
                min_i = j
        temp =queue[i]
        queue[i] = queue[min_i]
        queue[min_i] = temp
    return queue

def search_for_task(queue,title):
    sorted_queue = sort_task_by_title(queue)

    low,high = 0, len(sorted_queue)-1

    while low <= high:
        mid = (low + high) // 2
        mid_title = sorted_queue[mid][0].lower()

        if mid_title == title.lower():
            print("Task found")
            return sorted_queue[mid]
        elif mid_title < title.lower():
            low = mid + 1
        else:
            high = mid +1

def sort_task_by_duration(queue):
    n = len(queue)
    for i in range(n-1):
        min_i = i
        for j in range (i + 1, n):
            if queue[j][1] < queue[min_i][1]:
                min_i = j
        temp = queue[i]
        queue[i] = queue[min_i]
        queue[min_i] = temp
    return queue


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

