class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1: return [[strs[0]]]

        def get_key(s: str):
            char_arr=[0]*26
            for i in s:
                char_arr[ord(i)-ord('a')]+=1
            
            return char_arr

        groups=defaultdict(list)
        for s in strs:
            groups[tuple(get_key(s))].append(s)
        
        return list(groups.values())
            
