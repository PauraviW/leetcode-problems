import heapq
from collections import defaultdict


class MostFrequentPage:
    def combinations(self, weblist):
        res = []
        for i in range(len(weblist)):
            for j in range(i+1, len(weblist)):
                for k in range(j + 1, len(weblist)):
                    res.append((weblist[i], weblist[j],weblist[k]))
        return  res
    def mostfreq(self, timestamps, username, websites):

        heap = []
        for tstamp, website, uname in zip(timestamps, websites, username):
            heapq.heappush(heap, (tstamp, uname, website))


        userWebsiteDictionary = defaultdict(list)

        while heap:
            _, uname, website = heapq.heappop(heap)
            userWebsiteDictionary[uname].append(website)

        seq_counts = defaultdict(int)
        max_count = 0
        res = None
        for uname, webList in userWebsiteDictionary.items():
            combinations = self.combinations(webList)
            for c in combinations:
                seq_counts[c] += 1
                if seq_counts[c] > max_count:
                    res = c
                elif seq_counts[c] == max_count:
                    if res > c:
                        res = c
        return res


username = ['joe','joe','joe', 'joe', 'jill','jill','jill','james','james','james', 'james']
websites = ['home', 'career', 'about', 'about', 'career', 'home','career', 'career','home', 'about','home']
timestamps = [2,3,4,1,9,6,7,8,10,11]

print(MostFrequentPage().mostfreq(timestamps,username, websites))