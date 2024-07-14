from tabulate import tabulate

def total_task():
    task = int(input("Enter total task you want to add :"))
    task_list = []
    for i in range(1,task+1):
        task_input = input(f"Enter Task {i}: ")
        task_list.append(task_input)
        
    while(True):
        header=['S.No.','Operation']
        data=[
            ['1','Add'],['2','Update'],['3','Delete'],['4','View'],['5','Exit']
        ]
        
        print(tabulate(data,headers=header,tablefmt="fancy_grid"))
        choice = int(input("Enter the choice(1,2,3,4,5) :"))
        if choice == 1:
            add = input("Enter Your task :")
            task_list.append(add)
            
        elif choice == 2:
            change = input("Enter your task you want to change :")
            if change in task_list:
                index = task_list.index(change)
                new_task = input("Enter your new task :")
                task_list[index] = new_task
                
        elif choice == 3:
            change = input("Enter your task you want to delete :")
            if change in task_list:
                task_list.remove(change)
                print(f"'{change}' deleted from your To-Do List...")
                
                
                
        elif choice == 4:
            if len(task_list)==0:
                print("\nTo-Do List is Empty\n")
            else:
                print("="*20)
                newheader=['S.No.','To-Do List']
                l=[]
                newdata=[]
                for work in range(0,len(task_list)):
                  
                    l=[f"{work+1}", f"{task_list[work]}"]
                    newdata.append(l)
                    l=[]
            print(tabulate(newdata, headers=newheader, tablefmt="fancy_grid"))
            print("="*20)
        elif choice == 5:
            print("\nExit Successfully....")
            break
        else:
            print("\nInvald input....")  
         
total_task()
