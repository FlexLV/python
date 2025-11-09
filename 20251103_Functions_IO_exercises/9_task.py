def reverse_file(input_file, output_file):
    with open(input_file,'w') as f:
        list=[i for i in f].reverse()
    with open(output_file,'w') as g:
        for i in list:
            g.write(i+'\n')