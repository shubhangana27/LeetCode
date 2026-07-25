class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero_count=0
        for i in nums:
            if i!=0:
                prod=prod*i
            else:
                zero_count+=1
        answer=[]
        for i in nums:
            if zero_count<1:
                answer.append(prod//i)
            elif zero_count==1:
                answer.append(prod if i ==0 else 0)
            else:
                answer.append(0)
        return(answer)