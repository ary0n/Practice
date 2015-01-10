def main():
    list1 = [2,3,5,7];
    primecount = 4;
    num = 10;
    primesum = 0;
    while(primecount < 1000):
        notprime = False
        for index in range(len(list1)):
            if(num % list1[index] == 0):
                notprime = True;
        if(not notprime):
            list1.append(num)
            primecount +=1;

        num +=1;

    for index in range(len(list1)):
    #    print (list1[index], end = '\n')
        primesum += list1[index];

    print(primesum, end = '\n')
    return


main()