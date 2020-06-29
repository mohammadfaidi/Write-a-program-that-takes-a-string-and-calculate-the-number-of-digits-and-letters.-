

string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      else:
        count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)



'''
list = [4,5,1,2]

max = 0
for i in list:
    if max < i:
        max= i

print(max)
'''


