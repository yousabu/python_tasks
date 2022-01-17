# f = open('sample.txt', 'r')
# print(f.mode)
# f.close()

# call my context manager


with open('sample.txt', 'r') as f:
    with open('copy.txt', 'w') as wf:
        for line in f:
            wf.write(line)


