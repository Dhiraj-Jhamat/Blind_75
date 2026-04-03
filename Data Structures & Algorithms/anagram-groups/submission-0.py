class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word in hm.keys():
                hm[s_word].append(word)
            else:
                hm[s_word]=[word]
        return list(hm.values())
