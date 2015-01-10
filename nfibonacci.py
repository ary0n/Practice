def main():
    n = 12;
    list = [1, 1];
    for num in range(2,n):
      temp = list[num -1] + list[num-2];
      list.append(temp);

    print (list[n-1]);

    return


main();