class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic={}
        for i in strs:
            joint_i = "".join(sorted(i))
            if joint_i not in dic:
                dic[joint_i]=[]
            dic[joint_i].append(i)
            
        return list(dic.values())


















            


