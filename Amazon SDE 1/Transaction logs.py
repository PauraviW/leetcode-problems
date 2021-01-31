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
