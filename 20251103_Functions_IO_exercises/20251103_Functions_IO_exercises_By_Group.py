

# TASK 1

def greet_user(first_name,last_name):
    if len(last_name)!=0:
        return f"fHello,{first_name} {last_name}! Welcome back!"[1:]
    return f"fHello,{first_name}! Welcome back! "[1:]

# TASK 2

def max(a,b,c):
    if a<=b and c<=b:
        return b
    elif a<=c and b<=c:
        return c
    elif b<=a and c<=a:
        return a
    
# TASK 3

def average(list):
    if len(list)==0:
        return 0
    return sum(list)/len(list)

# TASK 4

def filter_even(list):
    return [i for i in list if i%2==0]

# TASK 5

def factorial(n):
    if n<0:
        return "Invalid Input"
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

# TASK 6

def write_lines(filename, list):
    with open(filename,'w') as f:
        for i in list:
            f.write(i+'\n')

# TASK 7

def count_words(filename):
    return len([i for i in filename.open().split()])

# TASK 8

def longest_length(filename):
    m=0
    with open(filename,'w') as f:
        for i in f:
            m=max(m,len(i))
    return m

# TASK 9

def reverse_file(input_file, output_file):
    with open(input_file,'w') as f:
        list=[i for i in f].reverse()
    with open(output_file,'w') as g:
        for i in list:
            g.write(i+'\n')

# TASK 10

def word_frequency(filename):
    with open(filename, 'r') as f:
        t = f.read().lower()  
    words = t.split()           
    freq = {}                  

    for i in words:
        i = ''.join(ch for ch in i if ch.isalnum())  
        if i:
            freq[i] = freq.get(i, 0) + 1

    for w, c in freq.items():
        print(w, ':', c)