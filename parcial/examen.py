list = ["1,2,3,4,7","7,8,9,10,5"]
listA = list[0].split(sep=",")
listB = list[1].split(sep=",")

i=0
count=0

while i < len(listA):
    j=0
    while j < len(listB):
        if listA[i] == listB[j]:
            print(listA[i])
            count+=1
        j+=1
    i+=1
if count == 0:
    print("none")

