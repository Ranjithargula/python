started= False
stop_count=0
while True:
    command=input('> ').lower()
    if command=='start' :
        if started :
            print('car is already started')
        else:
            started = True
            print('car is started')
    elif command == 'stop' :
        if  not started and stop_count==0 :
            print('car not even started once')
        elif not started: 
            print('car is already stopped')
        else:
            started = False
            print('car is stopped')
            stop_count+=1
    elif command=='quit' :
        print('thank you for playing the game')
        break
    elif command=='help' :
        print('''
              start-to start the car
              stop- to stop the car
              quit- to quit the game''')
    else:
        print("i dont understand.please type help for instructions")
    
    
        
    