from collections import defaultdict


def processLogFile(logs, threshold):
    """
    :type logs: List[str]
    :type threshold: int
    :rtype: List[str]
    """

    logDict = defaultdict(int)
    ans = set()
    for i in range(len(logs)):
        fro, to, _ = logs[i].split(' ')
        if fro != to:
            logDict[to] += 1
            if logDict[to] >= threshold:
                ans.add(to)
        logDict[fro] += 1
        if logDict[fro] >= threshold:
            ans.add(fro)
    return sorted(ans)

print(processLogFile(["88 99 200", "88 99 300", "99 32 100", "12 12 15"], 2))
print(processLogFile(['88 99 200', '88 99 300', '99 32 100', '12 12 15'], 1))
"""
Time Complexity: O(n) - iterating through the list once
Space Complexity: O(n) - because of the dictionary that can contain at most 2n ids

I iterate through the list and check for transactions where both the sender and receiver are same. In such cases, I add an instnce of only one of them and for the next i check if the in
"""