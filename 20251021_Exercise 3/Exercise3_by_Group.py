# All tasks in separate files you can find here - https://github.com/FlexLV/python/tree/main/20251021_Exercise%203

# Task 1

five_integers = [1,2,3,4,5]
last_element = len(five_integers) - 1
print(five_integers[0], five_integers[last_element])

# Task 2 

colors = ("red", "green", "blue")
print(colors[1])
# colors[1] = "yellow"  # can't change because tuple is immutable (unlike list, set, or dict)

# Task 3

person = ("Alice", "25", "Berlin")
name = person[0]
age = person[1]
city = person[2]

print(name + " is " + age + " years old and lives in " + city)

# Task 4

A = {1,2,3,4}
B = {3,4,5,6}

union_set = A | B
intersection_set = A & B
difference_set = A - B

print("Union: " , union_set)
print("Intersection: " , intersection_set)
print("Difference: " , difference_set)

# Task 5

numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers) # duplicates getting removed sets only store unique items

# Task 6

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print("Bob's score: ", students["Bob"])
students["David"] = 92
students["Alice"] = 88
 
 # Task 7

capitals = {
    "Germany": "Berlin",
    "France": "Paris",
    "Italy": "Rome"
}

for country in capitals:
    print("The capital of", country, "is", capitals[country])

# Task 9

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22}
]

for student in students:
    print(student["name"])

# Task 10

sentence = "Lists are ordered and Sets are not"
words = sentence.split()
unique_words = set(words)
word_lengths = {}

for word in unique_words:
    word_lengths[word] = len(word)

print(word_lengths)


# Task 11

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    print(num)       
    total += num     

print("Total sum is: ", total)
