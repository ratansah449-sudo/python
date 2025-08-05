# # class person:
# #     def __init__(self,name,age):
# #         self.name=NameError
# #         self.age=age
# #         def greet(self):
# #             return f"Hello,my name is {self.name}and I am {self.age}years old"
# #         person1=person("Alice",30)
# #         person2=person("ratan",25)
        
# try:        
#     a=int(input("enter the number1"))
#     b=int(input("enter the number2:"))

#     result =a/b
#     print(result)

# except ZeroDivisionError as e:
#     print(e)
#     print("you have deivided by zero")
#     a=int(input("enter the number1"))
#     b=int(input("enter the number2:"))
#     result = a/b
#     print(result)
    
# except ValueError as e:
#     print(e)
        
#     print("you have entered the character")
#     a=int(input("enter the number1:"))
#     b=int(input("enter the number2:"))
         
#     result = a/b
#     print(result)
# with open("C:/Users/NITRO V15/OneDrive/Desktop/python.py/demofile.txt",mode="r")as file:
#       content = file.read()
#     print(content)
# import csv        
# file_path="C:/Users/NITRO V15/OneDrive/Desktop/python.py/file.csv"

# with open(file_path,mode='r')as file:
#   csv_reader = csv.reader(file)
#   header = next(csv_reader)
#   for row in csv_reader:
#     print(row)
# import csv
# file_path='data.csv'
# with open(file_path,mode='r')as file:
#   csv_reader = csv.reader(file)
#   header = next(csv_reader)
#   for row in csv_reader:
#     print(row)
    
    
# import csv
# file_path='file.csv'
# with open(file_path,mode='r')as file:
#   csv_reader = csv.DictReader(file)
#   for row in csv_reader:
#     # print(row['Name'],row['Age'],row['City'])
#      print (row)    

data=[{'Name':'Alice','Age':30,'City':'London'},
{'Name':'Bob','Age':25,'City':'paris'},
{'Name':'Charlie','Age':35,'City':'Berlin'}]


import csv
file_path = 'output1.csv'
fieldnames = ['Name','Age','City']
with open(file_path,mode='w',newline='')as file:
  writer = csv.DictWriter(file,fieldnames=fieldnames)
  writer.writeheader()
  for row in data:
    writer.writerow(row)




         
         
         
         
         