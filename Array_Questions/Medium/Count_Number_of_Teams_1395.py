#rating = [2,5,3,4,1]
# rating = [2,1,3]
# rating = [1,1,1]
# rating = [1,2,3,4]
rating = [4,3,2,1]
# count = 0
#
# for i in range(len(rating)-2):
#     for j in range(i+1, len(rating) - 1):
#         for k in range(j+1, len(rating)):
#             if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
#                 count += 1

# print(count)

l = len(rating)
count = 0
greater = [0] * l
less = [0] * l
for i in range(l):
    for j in range(i):
        if (rating[i] < rating[j]):
            count += greater[j]
            greater[i] += 1
        else:
            count += less[j]
            less[i] += 1
print(count)