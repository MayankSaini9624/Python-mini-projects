tasks=[]
discription=[]
to_do_list=[tasks,discription]
while True:
        print("""
        1. ADD A TASK
        2. REMOVE A TASK
        3. ADD A DISCRIPTION
        4. view tasks and discription
        5. EXIT """)
        choice=int(input("ENTER YOUR CHOICE:"))
        if choice==1:
            task=input("ENTER YOUR TASK:")
            tasks.append(task)
        elif choice==2:
            anothertask=input("ENTER YOUR TASK:")
            if anothertask in tasks:
                tasks.remove(anothertask)
            else:
                print("INVALID COMMAND")
        elif choice==3:
            print("add disciption OR type 0 for no discription ")
            dis=input("ENTER THE DISCRIPTION:")
            discription.append(dis)
        elif choice==4:
             print("THAT IS THE TASK MANNUAL",tasks)
             print("THIS THE LIST OF DICRIPTON",discription)
             print(to_do_list)
             exit()
        elif choice==5:
             exit()
        else:
            print("INVALID CHOICE")
