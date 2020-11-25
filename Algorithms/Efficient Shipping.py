# Long[] boxArr = new Long[boxes.size()];
#         boxArr = boxes.toArray(boxArr);
#         Long[] uPB = new Long[unitsPerBox.size()];
#         uPB = unitsPerBox.toArray(uPB);
#
#         long result =0;
#         PriorityQueue<Long[]> q = new PriorityQueue<Long[]>((a,b)->{return Long.compare(b[0],a[0]);});
#         for (int i =0; i<boxArr.length; ++i)
#         {
#             q.offer(new Long[]{uPB[i], boxArr[i]});
#         }
#         while(truckSize > 0 && q.size() > 0)
#         {
#             Long[] info = q.poll();
#             result = result + info[0] * (truckSize > info[1] ? info[1] : truckSize);
#             truckSize = truckSize - info[1];
#         }
#         return result;
import heapq

boxArr = [1,2,3]
uPB = [3,2,1]
trucksize = 3
queue = []

for i in range(len(boxArr)):
    heapq.heappush(queue, (-uPB[i], boxArr[i]))
result = 0
while trucksize and queue:
    units , noBox = heapq.heappop(queue)
    if noBox > trucksize:
        result += -units * (trucksize)
        trucksize  = 0
    else:
        result += -units * noBox
        trucksize -= noBox
print(result)
