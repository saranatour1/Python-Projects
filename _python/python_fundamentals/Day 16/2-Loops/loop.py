for x in range (1  , 151 ,1): 
    print (x)

for i in range (5 , 1001 , 5):
    print(i)

for a in range (1 ,100 ,1):
    if a%5==0 :
        print("coding")
    if a%10==0 :
        print("coding dojo")
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for i in range (0 , 5001,1):
        if i%2 !=0:
                sum+= i
print (sum)                

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range (2018 ,0 ,-4):
    print(x)
"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
 print only the integers that are a multiple of mult.
 For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines) 
 for x in range( highNum ):
    if x%mult == 0 :
        print(x)
"""
lowNum = 2
highNum = 9
mult = 3

while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum += 1

