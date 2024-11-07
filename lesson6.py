#dictionary
#we use curly braces{}
student={'name':'samwel','age':20,'year':3,}
print(student["name"])
print(student)#prints everything
student['weight']='70 kgs' # adds the value weight in the dictionary
print(student)

#set only one existence per item ie cannot print sam twice,mutable,unordered
people={'sam','joji','keiv','larry','mike','malick','Sam'}
print(people)
people.add('janet')
print(people)
print(len(people))#count
people.remove('keiv')
print(people)