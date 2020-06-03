# products = ["mobile","mouse","moneypot","monitor","mousepad"]
# searchWord= "mouse"
# products = ['havana']
# searchWord= 'havana'
products = ["bags", "baggage", "banner", "box", "cloths"]
searchWord = "bags"
# products = ["havana"]
# searchWord = "tatiana"
products.sort()
l = []

# j = 1
# while j<=len(searchWord):
#     patt = searchWord[0:j]
#     print(patt)
#     l1 = []
#     for i in products:
#         if len(l1) < 3:
#             if i.startswith(patt):
#                 l1.append(i)
#         else:
#             break
#     l.append(l1)
#     j+=1
# print(l)
#
import  bisect

res = []
for i in range(1, len(searchWord) + 1):
    l = bisect.bisect_left(products, searchWord[:i])
    print('l',l,searchWord[:i])
    r = bisect.bisect_right(products, searchWord[:i] + '~')
    print('r',r,searchWord[:i],searchWord[:i] + '~')
    # print(l,r,searchWord[:i],products)
    res.append(products[l:min(l + 3, r)])
print(res)