
line_0 = '12'
line_1 = 'insert 0 5'
line_2 = 'insert 1 10'
line_3 = 'insert 0 6'
line_4 = 'print'
line_5 = 'remove 6'
line_6 = 'append 9'
line_7 = 'append 1'
line_8 = 'sort'
line_9 = 'print'
line_10 = 'pop'
line_11 = 'reverse'
line_12 = 'print'

n = int(line_0)
out_list = []

for i in range(1, n+1):
    command = eval("line_" + str(i)).split()
    if command[0] != "print":
        eval('out_list.{0}{1}'.format(command[0], tuple(map(int, command[1:]))))
    else:
        print(out_list)

