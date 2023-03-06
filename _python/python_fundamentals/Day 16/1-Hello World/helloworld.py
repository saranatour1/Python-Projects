# 1. TASK: print "Hello World"
print("Hello World!")
# # 2. print "Hello Noelle!" with the name in a variable
name = "Sara"
print("My name is:",name)	# with a comma
print("My name is"+name)	# with a +
# # 3. print "Hello 42!" with the number in a variable
name = 28
print("Hello",name,"!")	# with a comma
print("Hello"+ str(name))	# with a +	-- this one should give us an error!
# # 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "chicken"
print('I Love {fave_food1} and {fave_food2}'.format(fave_food1=fave_food1,fave_food2=fave_food2)) # with .format()
print(f'I love {fave_food1} and {fave_food2}') # with an f string

