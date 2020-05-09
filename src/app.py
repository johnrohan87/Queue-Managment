import json, os
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def read_wright_json_file(_Is_Read_or_wright,_File_Location="src/data_file.json",_Data=""):
    
    #Check if file exists 
    if os.path.exists(_File_Location):
        print("default file found")
    elif os.path.exists(_File_Location) == False:
        print(f"Creating file in {_File_Location}")
        with open(_File_Location, 'w+') as outfile:  
            json.dump(None, outfile)

    #Perform Read or Wright
    if _Is_Read_or_wright == "read":
        with open(_File_Location, 'r') as read_file:  
            
            #Read
            print(f"Reading from file {_File_Location}")
            contents = read_file.read()
            #print(f"This is your file contents -{str(contents)}")
            if contents != "null":
                print("Converting file to .json")
                data = json(read_file)
                read_file.close()
                return data
            else:
                print("File is empty")
                pass
            
    elif _Is_Read_or_wright == "wright":
        with open(_File_Location, 'w') as wright_file:

            #Wright
            print(f"Wrighting to file {_File_Location}") 
            json.dump(_Data, wright_file)
            wright_file.close()
            pass
    else:
        print(f"please specify read or wright --{_Is_Read_or_wright}")
        pass

def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    tmp_queue = queue.get_queue()
    if tmp_queue == []:
        print("The Queue is empty")
        pass
    count = 1
    for item in range(len(tmp_queue),0,-1):
        print(str(count) + ") " + str(tmp_queue[item-1]))
        count +=1
    return tmp_queue

def add(guest_to_add):
    queue.enqueue(guest_to_add)
    print("\n" + str(guest_to_add) + " is currently " + str(queue.size()) + " in the Queue line.\n")
    #send(body="This is a text from the Queue messager. -"+ str(guest_to_add) + "- is " + str(queue.size()) + " in line",to="7862174153")
    pass

def dequeue():
    queue.dequeue()
    pass

def save():
    current_queue = print_queue()
    read_wright_json_file(_Is_Read_or_wright="wright", _Data=current_queue)
    print("Done")
    pass

def load():
    tmp_data = (read_wright_json_file("read"))
    print(tmp_data)
    pass 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        print("\nPlease enter the guest phone number you would like to add to the Queue.")
        user_input = str(input(""))
        add(user_input)
    elif option == 2:
        print("\nRemoving the first guest in line\n")
        if queue.size() > 0:
            queue.dequeue()
        else:
            print("The Queue is empty")
        print_queue()
    elif option == 3:
        print_queue()
    elif option == 4:
        print("\nExporting your Queue to .json file.")
        save()
    elif option == 5:
        print("\nImporting your Queue from queue.json file.")
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Invalid option "+str(option))
