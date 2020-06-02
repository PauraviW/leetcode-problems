def canConstruct(ransomNote: str, magazine: str) -> bool:

    for  i in ransomNote:
        if i in magazine:
            magazine = magazine.replace(i, '', 1)
            print(magazine)
        else:
            return False
    return True


# ransomNote = "fffbfg"
# magazine = "effjfggbffjdgbjjhhdegh"
ransomNote = "aa"
magazine = "ab"

print(canConstruct(ransomNote, magazine))
