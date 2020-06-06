rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
    print(False)

if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
    print(False)

print(True)
