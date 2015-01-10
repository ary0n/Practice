import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    list = []
    list[:0] = test
    list.reverse();
    #list2 = list[:]
    #print(list2)
    count = 0
    var = 0
    sum =0
    for i in (list):
        if(i == "a"):
            var = 10
        elif (i == "b"):
            var = 11
        elif (i == "c"):
            var = 12
        elif (i == "d"):
            var = 13
        elif (i == "e"):
            var = 14
        elif (i == "f"):
            var = 15
        else:
            var = int(i)
        sum += var* 16**count
        count+=1
    print(sum)

test_cases.close()
