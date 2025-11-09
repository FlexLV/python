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