
fruits = ["pear","apple","orange","banana","kiwi"]
fruit = "apple"
vegs = ["peas","carrots"]

fruits.append(fruits)
print(fruits)

fruits.extend(vegs)
print(fruits)

fruits.insert(2, fruit)
print(fruits)

fruits.pop()
print(fruits)

fruits.remove(fruit)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

print(fruits.index(fruit))
print(fruits.count(fruit))
