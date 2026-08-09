class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for anagram in strs:
            if "".join(sorted(anagram)) in hashmap:
                hashmap["".join(sorted(anagram))].append(anagram)
            else:
                hashmap["".join(sorted(anagram))] = [anagram]

        return list(hashmap.values())
        