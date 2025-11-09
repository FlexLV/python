def longest_length(filename):
    m=0
    with open(filename,'w') as f:
        for i in f:
            m=max(m,len(i))
    return m