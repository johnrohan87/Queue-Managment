import json, os
from DataStructures import Queue
from sms import send
from twilio.rest import Client
import twilio


# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def read_wright_json_file(_Is_Read_or_wright,_Data,_File_Location="/src/"):
    if os.path.exists(_File_Location):
        print("default file found")
    elif os.path.exists(_File_Location) == False:
        print("creating file ")

    if _Is_Read_or_wright == "read":
        with open('data.json', 'w') as outfile:  
            json.dump({}, outfile)
            pass
    elif _Is_Read_or_wright == "wright":
        with open('data.json', 'w') as outfile:  
            json.dump({}, outfile)
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
    pass

def add(guest_to_add):
    queue.enqueue(guest_to_add)
    print("\n" + str(guest_to_add) + " is currently " + str(queue.size()) + " in the Queue line.\n")
    #send(body="Test SMS" + str(guest_to_add),to="+7862174153")
    pass

def dequeue():
    queue.dequeue()
    pass

def save():
    pass

def load():
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
    elif option == 5:
        print("\Importing your Queue from queue.json file.")
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Invalid option "+str(option))
