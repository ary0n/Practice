__author__ = 'Ashton'

import sys
test_cases = open(sys.argv[1], 'r')
list = []
for test in test_cases:
    list = test.split()
    #list.reverse()
    while(len(list) !=0):
        print(list.pop(), end =" ")
        if(len(list) !=0):
            list.pop()
    print();
test_cases.close()
