#When user at the windy room
def step4():
    user_command4=''
    while user_command4.upper()!="D":
        print("You are now at a cozy room that you feel windy and cool.")
        user_command4=input("Press W,S,D OR A:")
        if  user_command4.upper()=="D":
            print('You reach the exit! You win the game!')
        elif user_command4.upper()=='S':
            print("Here's a wall! You can't move further in this direction.Try again.")
        elif (user_command4.upper()=='W'or user_command4.upper()=='A'):
            print ('You fell down from the cliff. Game over!')
            break
        else:
            print("Your input can't be recognised. Try again.")

#When user at the cozy room without danger
def step3():
    user_command3=''
    while user_command3.upper()!='W':
        print('You are now at a cozy room with dry air. Try to move to next step.')
        user_command3= input("Press W,S,D OR A:")
        step4()
        if user_command3.upper()=='W':
            print('You have moved to the next room! You are now at room you can feel windy and cool.')
        elif (user_command3.upper()=="A"or user_command3.upper()=="S"or user_command3.upper()=="D"):
            print("Here's a wall! You can't move further in this direction.Try again.")
        else:
            print("Your input can't be recognised. Try again.")

#when user at the humid room
def step2():
    user_command2=''
    while user_command2.upper()!='D':
        print('You are now at a room with humid air. Try to move to next step.')
        user_command2=input("Press W,S,D OR A:")
        if user_command2.upper()=='D':
            print('You have moved to the next room! You are now at a cozy room without danger')
            step3()
        elif user_command2.upper()=='A':
            password=''
            while password!='125':
                print('You stepped into jail accidentlly. You can be released only when you input the right password:______.(hint:What is the cube between 100 and 164?)')  
                password=input('Please enter the password:')
                if password=='125':
                    print('You are released back to the room with humid air.')
                else:
                    print('Incorrect password. Please guess again.')
        elif ( user_command2.upper()=='W'or user_command2.upper()=='S'):
            print( "Here's a wall! You can't move further in this direction.Try again.")
        else:
            print("Your input can't be recognised. Try again.")

#when user at the start room
def step1():
    user_command1=''
    print("You wake up at midnight, at a strange place your never been and  surounded by darkness. Try to find a way to escape and input your first step.")
    while user_command1.upper()!='W':
        user_command1=input(" Press W,S,D OR A:")
        if user_command1.upper()== 'W':
            print('You have moved to the next room! You are now at a room with humid air. ')
            step2()
        elif (user_command1.upper()=='A'or user_command1.upper()=='D'or user_command1.upper()=='S'):
            print( "Here's a wall! You can't move further in this direction.Try again.")
        else:
            print("Your input can't be recognised. Try again.")

print("Starting Game")
print("Game instruction: You can control your direction to move by input:'W' to go up one step; 'S' to go down one step; 'A' to go left one step; 'D' to go right one step. ",
      "Please notice, when you come to a new room, a new wall would rise between this room and the old room you came from, which means you can never go back.",
      "Try to find the exit and avoid dangers on your way!")
step1()
print("Game Ended")