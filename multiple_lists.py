__author__ = 'Ashton'

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    list = []
    list1 = []
    list2 = []
    list3 = []
    list = test.split()
    for i in list:
        if(i != "|" and i != " " and i!= "\n"):
            var = int(i)
            list1.append(var)
    half = (len(list1)+1)/2
    list2 = list1[:int(half)]
    list3 = list1[int(half):]
    i =0
    while(i < len(list2)):
        mult = list2[i] * list3[i]
        print(mult, end = " ")
        i+=1
    print()
test_cases.close()