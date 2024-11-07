#list
scores=[98,45,34,22,24,78,88,67]
#acess a value
# in lists we use square braces[] but not curly braces{}
print(scores[3])#starts counting from zero
scores.append(55)#adds 55 in your list
print(scores)
scores.sort(reverse=True)#arranges from largest to smallest
print(scores)
scores.pop(3)#removes index number 3 that is 67
print(scores)