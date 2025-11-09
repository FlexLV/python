def write_lines(filename, list):
    with open(filename,'w') as f:
        for i in list:
            f.write(i+'\n')