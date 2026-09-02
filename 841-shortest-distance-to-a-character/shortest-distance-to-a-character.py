class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        position = [] 
        for i in range(len(s)): 
            if s[i] == c: 
                position.append(i) 
                answer = [] 
                for j in range(len(s)): 
                    smallest = float('inf') 
                    for x in position: 
                        res=abs(j-x) 
                        smallest=min(smallest,res) 
                    answer.append(smallest)
        return answer