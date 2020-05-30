flowerbed = [1,0,0,0,1,0,0]

n = 2
i = 0
L = len(flowerbed)
while i <= L - 1:
    print(i)
    if  i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
        n = n - 1
        i = i + 2
    elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
        n = n - 1
        break
    elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
        n = n - 1
        i = i + 2
    else:
        i = i+1




# if flowerbed.index(0)
if n > 0:
    print("False")
else:
    print("True")


###########################33Alternate solutions#########################

if n==0:
    print (0==0)
i=0
while(n>0 and i<len(flowerbed)):
    if flowerbed[i]==1:
        i=i+2
        continue
    else:  # flowerbed[i]==0
        if i+1==len(flowerbed) or flowerbed[i+1]==0:
            flowerbed[i]=1
            n=n-1
            i=i+2
            continue
        else:
            i=i+1
print (n==0)

