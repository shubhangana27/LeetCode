class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [float('inf')] * len(s)
        last = float('-inf')
        for i in range(len(s)):
            if s[i] == c:
                last = i
            answer[i] = i - last

        last = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                last = i
            answer[i] = min(answer[i], last - i)

        return answer