cache = OrderedDict()
count = 0
for page in pages:

    if page not in cache:

        count += 1
        if len(cache) == maxCacheSize:  # page fault
            cache.popitem(last=True)
        cache[page] = 1
    cache.move_to_end(page, last=False)
return count