list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
list1 = ["Shogun", "KFC", "Burger King", "KFC1"]
list2 = ["KFC", "Shogun", "Burger King"]
import  collections
d = collections.defaultdict(list)
for i,data in enumerate(list1):
    d[data].append(i)
for i,data in enumerate(list2):
    d[data].append(i)
print(d)

minv = 9999
minVal = collections.defaultdict(list)
for key,value in d.items():
    if len(value) == 2:
        if sum(value) <= minv:
            minv = sum(value)
            minVal[minv].append(key)
print(minVal)
print(minVal[min(minVal.keys())])

initial = {}
for i, el in enumerate(list1):
    initial[el] = i
################################
matches = []
nums = []
for i, el in enumerate(list2):
    if el in initial:
        index_sum = initial[el] + i
        if nums == [] or index_sum < nums[-1]:
            matches = [el]
            nums = [index_sum]
        elif index_sum == nums[-1]:
            matches.append(el)
            nums.append(index_sum)

print(matches)