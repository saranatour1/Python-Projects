# #1: Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. 
# # Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# def change_x():
#     for i in range(len(x)):
#         for j in range(len(x[i])):
#             if(x[i][j]==10):
#                 x[i][j]=15
#     return x
# print(change_x())
# #Change the last_name of the first student from 'Jordan' to 'Bryant'
# def change_lastname(students, old_last_name, new_last_name):
#     for student in students:
#         if student['last_name'] == old_last_name:
#             student['last_name'] = new_last_name
#     return students
# students = change_lastname(students, 'Jordan', 'Bryant')
# print(students)
# #In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][sports_directory['soccer'].index('Messi')] = 'Ronaldo'
# print(sports_directory)
# # Change the value 20 in z to 30
# z[0]['y']=30
# print(z)

#2 Iterate Through a List of Dictionaries
# students = [
#       {'first_name':  'Michael', 'last_name' : 'Jordan'},
#       {'first_name' : 'John', 'last_name' : 'Rosales'},
#       {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#       {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# # def iterateDictionary(some_list):
# #     for dictionary in some_list:
# #         for key, val in dictionary.items():
# #             print(f"{key} - {val}", end=", ")

# # print(iterateDictionary(students))  # add a new line after each dictionary

# # Get Values From a List of Dictionaries

# def iterateDictionary2(key_name, some_list):
#     for val in some_list:
#         print(val[key_name])
# iterateDictionary2('last_name',students)

#4 Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key in some_dict:
        length=len(some_dict[key])
        print(key, length)
        for val in some_dict[key]:
          print(val)
  
dojo = {
  'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


    #sports_directory['soccer'][sports_directory['soccer'].index('Messi')] = 'Ronaldo'