
path = 'button.css'

# f = open(path,'r')
# print(f.mode)
#     print(f.name)
#     f.close
# with open(path,'r') as f:
    # print(f.mode)
    # print(f.name)
    # f_contents = f.read()
    # print(f_contents)
    # f_contents = f.readlines()
    # print(f_contents)
    # for line in f:
    #     print(line, end='')


# with open(path,'r') as f:
#
#     size_to_read = 10
#
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#
#     f.seek(0)
#
#     f_contents = f.read(size_to_read)
#     print(f_contents)

# with open('button2.css', 'w') as f:
#     f.write('BUTTON')
#     f.seek(0)
#     f.write('R')

with open('button.css', 'r') as rf:
    with open('button_copy.css', 'w') as wf:
        f_contents = rf.read()
        wf.write(f_contents)