z # x=5

# if x<10 :
#     print ("number is less than 10",x)

# if x<15 :
#     print ("number u less than 15",x)
    
    
    # ternary operator 
    
    
    
# n=5
# print ("odd" if n%2!=0 else "even")



# nested conditionals

# x=5

# if x>0 :
#     if x<10 :
     
#         print("x is a positve single-digit nubmer")
        
#     else:
    
#         print("x is a positive number, but not a single-digit")

# else:
    
#     print("x is not a positive number")






# x=9

# if x>0 and x<10:
#     print("the number is positive and single digit")
    
# elif x>0 and x>=10:
#     print("the number is positive and not single digit")
    
# else:
#     print("the number is not  positive")


# sum=0
# for x in range (10): 
#     sum=sum+x
# print("sum of all number is",sum)
    
    
    
#     # range(begin,end)
    
# for x in range (50,100):
#         print(x)


#range (begin,end,step)

# for x in range (0,10,4):
#     print(x)


# print even numbers between 50-70

# for x in range (50,70,2):
#     print(x)

# # print odd numbers between 60-80

# for x in range (61,80,2):
#     print(x)



# string1 = "abcdef"
# lst1 ={1,2,3,4,5,6}

# tup1 = (1,2,3,4,5)

# for x in string1:
#     print(x)



 #string123 = " aa bbb cccc ddddddddddd eeee ffffff"

# count_a = 0
# for x in string123:
#     if "a" == x:
#         count_a = count_a + 1

# print(count_a)


# string123 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa bbb ccccc ddddddd eeeeeeee ffffffffff"
# count_a=0
# count_b=0
# count_c=0
# count_d=0
# count_e=0
# count_f=0
# for x in string123:
#     if x =="a":
#         count_a += 1 #count-a = count_a +1
        
#     elif x == "b":
#         count_b +=1
        
#     elif x == "c":
#         count_c += 1
        
#     elif x == "d":
#         count_d += 1
    
#     elif x == "e":
#         count_e +=1
        
#     elif x == "f":
#         count_f +=1
        
# if count_a > count_b and count_a > count_c and count_a > count_d and count_a > count_e and count_a > count_f:
#     print("heighest frequently occured character is a",count_a)
    
# elif count_b > count_a and count_b > count_c and count_b > count_d and count_b > count_e and count_b > count_f:
#     print("heighest frequently occured character is b",count_b)
        


# i=0
# while i<10:
#     print(i)
#     i+=1
    

#question1
# get the sum of numbers from 0 to 10 using while

#question2
# get the sum of even numbers form 10 to 20 using while

# question3
# get the sum of odd numbers from 10 to 20 using while


# i = 0
# total = 0

# while i <= 10:
#     total += i
#     i += 1

# print("Sum from 0 to 10 is:", total)




# i = 10
# total = 0

# while i <= 20:
#     total += i
#     i += 2  # increment by 2 to stay on even numbers

# print("Sum of even numbers from 10 to 20 is:", total)



# i = 11  # first odd number after 10
# total = 0

# while i <= 19:  # last odd number before 20
#     total += i
#     i += 2  # increment by 2 to stay on odd numbers

# print("Sum of odd numbers from 10 to 20 is:", total)

# def print_board(board):
#     print("\n")
#     print(" " + board[0] + " | " + board[1] + " | " + board[2])
#     print("---+---+---")
#     print(" " + board[3] + " | " + board[4] + " | " + board[5])
#     print("---+---+---")
#     print(" " + board[6] + " | " + board[7] + " | " + board[8])
#     print("\n")

# def check_winner(board, player):
#     wins = [(0,1,2), (3,4,5), (6,7,8),  # Rows
#             (0,3,6), (1,4,7), (2,5,8),  # Columns
#             (0,4,8), (2,4,6)]           # Diagonals
#     return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

# def is_full(board):
#     return all(cell != " " for cell in board)

# def play_game():
#     board = [" "] * 9
#     current_player = "X"

#     print("Welcome to Tic-Tac-Toe!")
#     print("Positions are 1 to 9 as below:")
#     print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")

#     while True:
#         print_board(board)
#         move = input(f"Player {current_player}, enter your move (1-9): ")

#         if not move.isdigit() or int(move) < 1 or int(move) > 9:
#             print("❌ Invalid input. Please enter a number between 1 and 9.")
#             continue

#         index = int(move) - 1
#         if board[index] != " ":
#             print("❌ That spot is already taken. Try again.")
#             continue

#         board[index] = current_player

#         if check_winner(board, current_player):
#             print_board(board)
#             print(f"🎉 Player {current_player} wins!")
#             break

#         if is_full(board):
#             print_board(board)
#             print("🤝 It's a tie!")
#             break

#         # Switch player
#         current_player = "O" if current_player == "X" else "X"

# play_game()



# s = "Hello, World!"
# print(s.replace("World","Python"))


# s = "hello, world!"
# print(s.lower()) 


# s = "hello, world!"
# print(s.upper())

# s = "hello,world!"
# print(s.lstrip())

# s = "hello , world!"
# print(s.rstrip())

# s = "hello,world"
# print(s.strip())

# s = "###############hello#world######################"
# print(s.lstrip("#"))

# print(s.rstrip("#"))

# print(s.strip("#"))

# # s = "hello,world!"
# # print(s.split())


# # s = ['hello, 'world]
# # print("%",join(s))

# # s = "12345"
# # print(s.isdigit()) #outputs : true

# # s = "HELLO"
# # print(s.isupper())  #ouputs: true

# num1 = int(input("enter the number1:"))
# num2 = int(input("enter the number2:"))
# result = num1 + num2
# print("sum of {} + {} is" .format(num1,num2),result)


# # print(f"sum of {num1} + {num2} is" ,result)


# s = "#################hello world##################"
# print(s.lstrip("#"))

# print(s.rstrip("#"))
# new=s.strip("#")
# print(new)
# print(new.title())
# no_spaces = s.replace("Hello","World")
# print(no_spaces)


























 























