"""
data structure: set
time: O(m+n), where m is the number of words in s1, and n is the number of words in s2
space: O(m+n)

What I need for this problem are:
      -- know the words that appeared in one and not appeared in the other;
      -- words that have no duplications are potential uncommon words; 
                -- for solving this, I use the set - common - to store the duplicated words.
                -- the difference between the set - common and the set for s1/s2 are the potential uncommon words.
      


"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        unique_set1 = set()
        unique_set2 = set()
        common = set()
        uncommon = []
        for word in re.split(r'\W+', s1):
            if word not in unique_set1:
                unique_set1.add(word)
            else:
                common.add(word)
        for word in re.split(r'\W+', s2):
            if word not in unique_set2:
                unique_set2.add(word)
            else:
                common.add(word)
        for word in unique_set2-unique_set1-common:
            uncommon.append(word)
        for word in unique_set1-unique_set2-common:
            uncommon.append(word)
        return uncommon
