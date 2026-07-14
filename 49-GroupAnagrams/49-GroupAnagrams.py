# Last updated: 7/14/2026, 3:20:24 PM
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map=defaultdict(list)

        for word in strs:
            sorted_word=''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())        