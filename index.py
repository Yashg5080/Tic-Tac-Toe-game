def game():
    
 
  print('1.To play player1 vs player2 game press 1')
  print('2.To play player vs computer game press 2')
  print('3.If you want to see demo game press 3')
  print('4.Press any other key to exit game')
  choice_1=input('Enter your choice')
  list=[1,2,3,4,5,6,7,8,9]
  #defining structure of program
  def struct():
     print('                               ','-'*37)
     print('                               ','|','         ','|','         ','|','         ','|')
     print('                               ','|','   %s     '%(list[0]),'|','    %s    '%list[1],'|','    %s    '%list[2],'|')
     print('                               ','|','         ','|','         ','|','         ','|')
    
     print('                               ','-'*37)
     print('                               ','|','         ','|','         ','|','         ','|')
     print('                               ','|','   %s     '%(list[3]),'|','    %s    '%list[4],'|','    %s    '%list[5],'|')
     print('                               ','|','         ','|','         ','|','         ','|')
    
     print('                               ','-'*37)
     print('                               ','|','         ','|','         ','|','         ','|')
     print('                               ','|','   %s     '%(list[6]),'|','    %s    '%list[7],'|','    %s    '%list[8],'|')
     print('                               ','|','         ','|','         ','|','         ','|')
     print('                               ','-'*37)
  #code for player 1 vs player 2   
  if(choice_1=='1'):
    print('Player 1 will break')
    player1=input('Enter the name of first player')
    player2=input('Enter the name of second player')
    
    print('%s will have X and %s will have 0'%(player1,player2))
    print('%s will break'%(player1))
    print('Choose the place from 1 to 9 as shown in below box where you want to place X or 0')
    struct()
    c=0
    while(c<9):
        if(c%2==0):
            print('%s turn'%(player1))
            choice=int(input('Enter the place number'))
            if(choice<1 or choice>9):
              print('Invalid choice.enter again')
              continue
            if(list[choice-1]=='X'):
                list[choice-1]='X'
                print('You cannot enter same choice again.Choose again')
                continue
            elif(list[choice-1]=='0'):
                list[choice-1]='0'
                print('You cannot enter same choice again.Choose again')
                continue     
            if(choice<1 or choice>9):
              print('Invalid choice.enter again')
              continue
            else: 
             list[choice-1]='X' 
             c=c+1
             struct()
             if(list[0]==list[1]==list[2] or list[1]==list[4]==list[7] or list[2]==list[5]==list[8] or list[0]==list[3]==list[6] or list[3]==list[4]==list[5] or list[6]==list[7]==list[8] or list[0]==list[4]==list[8] or list[2]==list[4]==list[6]):
               print('%s wins'%player1)
               break
        elif(c%2!=0):
            print('%s turn'%(player2))
            choice=int(input('Enter the place number'))
            if(choice<1 or choice>9):
              print('Invalid choice.enter again')
              continue
            if(list[choice-1]=='X'):
                list[choice-1]='X'
                print('You cannot enter same choice again.Choose again')
                continue
            elif(list[choice-1]=='0'):
                list[choice-1]='0'
                print('You cannot enter same choice again.Choose again')
                continue
   
            if(choice<1 or choice>9):
             print('Invalid Choice')
            else: 
             list[choice-1]='0'
             c=c+1
             struct()
            if(list[0]==list[1]==list[2] or list[1]==list[4]==list[7] or list[2]==list[5]==list[8] or list[0]==list[3]==list[6] or list[3]==list[4]==list[5] or list[6]==list[7]==list[8] or list[0]==list[4]==list[8] or list[2]==list[4]==list[6]):
                print('%s wins'%(player2))
                break
    else:
      print('Match draw')
    print('If you want to replay press 1.Press any other key to exit')
    replay=input('Enter your choice')
    if(replay=='1'):
          game()
    else:
          print('Thanks dor playing')
  #code for player vs computer         
  elif(choice_1=='2'):
    
    print('You will break')
    player1=input('Enter your name')
    
    print('%s will have X and computer will have 0'%(player1))
    print('%s will break'%(player1))
    print('Choose the place from 1 to 9 as shown in below box where you want to place X or 0')
    struct()
    c=0
    while(c<9):
        if(c%2==0):
            print('%s turn'%(player1))
            choice=int(input('Enter the place number'))
            if(choice<1 or choice>9):
              print('Invalid choice.enter again')
              continue
            if(list[choice-1]=='X'):
                list[choice-1]='X'
                print('You cannot enter same choice again.Choose again')
                continue
            elif(list[choice-1]=='0'):
                list[choice-1]='0'
                print('You cannot enter same choice again.Choose again')
                continue
   
            if(choice<1 or choice>9):
              print('Invalid choice.enter again')
              continue
            else: 
             list[choice-1]='X' 
             c=c+1
             struct()
             if(list[0]==list[1]==list[2] or list[1]==list[4]==list[7] or list[2]==list[5]==list[8] or list[0]==list[3]==list[6] or list[3]==list[4]==list[5] or list[6]==list[7]==list[8] or list[0]==list[4]==list[8] or list[2]==list[4]==list[6]):
               print('Hurray!You have won this game')
               break
            print('Computer turn')    
        elif(c%2!=0):
            import time as t
            t.sleep(1)
            import random as r
            p=r.choice([1,2,3,4,5,6,7,8,9])
            if(list[p-1]=='X'):
                list[p-1]='X'
                continue
            elif(list[p-1]=='0'):
                list[p-1]='0'
                continue

            else: 
             list[p-1]='0' 
             c=c+1
             struct()
             if(list[0]==list[1]==list[2] or list[1]==list[4]==list[7] or list[2]==list[5]==list[8] or list[0]==list[3]==list[6] or list[3]==list[4]==list[5] or list[6]==list[7]==list[8] or list[0]==list[4]==list[8] or list[2]==list[4]==list[6]):
               print('You Lose')
               break
    else:
               print('Match draw')
    print('If you want to replay press 1.Press any other key to exit')
    replay=input('Enter your choice')
    if(replay=='1'):
          game()
          
    else:
          print('Thanks for playing')
 #code for computer vs computer           
  elif(choice_1=='3'):
    import time as t
    
    print('Now you see the game computer1 vs computer2')
    print('This is a3X3 grid where you have to place "X" or "0" as shown by our computer')
    struct()
    t.sleep(10)      
    c=0
    print('Computer 1 turn')
    while(c<9):
        
     if(c%2==0):
            
            
            import random as r
            p=r.choice([1,2,3,4,5,6,7,8,9])
            if(list[p-1]=='X'):
                list[p-1]='X'
                continue
            elif(list[p-1]=='0'):
                list[p-1]='0'
                continue
            

            else: 
             list[p-1]='X' 
             c=c+1
             struct()
             if(list[0]==list[1]==list[2] or list[1]==list[4]==list[7] or list[2]==list[5]==list[8] or list[0]==list[3]==list[6] or list[3]==list[4]==list[5] or list[6]==list[7]==list[8] or list[0]==list[4]==list[8] or list[2]==list[4]==list[6]):
               print('computer 1 wins')
               break
            print('Computer 2 turn')
            t.sleep(3)
     elif(c%2!=0):
            
            import random as r
            p=r.choice([1,2,3,4,5,6,7,8,9])
            if(list[p-1]=='X'):
                list[p-1]='X'
                continue
            elif(list[p-1]=='0'):
                list[p-1]='0'
                continue

            else: 
             list[p-1]='0' 
             c=c+1
             struct()
             if(list[0]==list[1]==list[2] or list[1]==list[4]==list[7] or list[2]==list[5]==list[8] or list[0]==list[3]==list[6] or list[3]==list[4]==list[5] or list[6]==list[7]==list[8] or list[0]==list[4]==list[8] or list[2]==list[4]==list[6]):
               print('Computer 2 wins')
               break
            print('Computer 1 turn')
            t.sleep(3)
    else:
               print('Match draw')
    print('If you want to play press 1.Press any other key to exit')
    replay=input('Enter your choice')
    if(replay=='1'):
          game()
          
    else:
          print('Thanks for playing')
            
     
              
  else:
     print('You have came out of the game')
 



game()

    

