num=[2,7,11,15]
target=int(input("Enter the target: "))

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print([i,j])

