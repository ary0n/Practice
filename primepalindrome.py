def main():
    list1 = [2,3,5,7];
    for num in range(10,1000):
        notprime = False
        for index in range(len(list1)):
            if(num % list1[index] == 0):
                notprime = True;
        if(not notprime):
            list1.append(num)

    for index in reversed(range(len(list1))):
        pali = str(list1[index]);
        if(pali[0] == pali[len(pali)-1]):
            print (pali);
            break;
        #primesum += list1[index];

    #print(primesum, end = '\n')
    return


main()