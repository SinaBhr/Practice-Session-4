numbers={1,2,3,4,5,6,7,8,9,10}
numbers=list(numbers)
numbers[0:11]=[5,4,6,7,1,2,4,6,7,8]
print(numbers)
print(numbers[3:6])
numbers=set(numbers)
print(numbers)
del numbers

sentence="Happy wife happy life"
sentence=sentence.split()
print(sentence)