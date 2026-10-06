class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights
        right=len(heights)-1
        left=0
        width= right-left
        maxi= min(heights[left],heights[right])*(width)

        while (left<right):
            if (right - left) * min(heights[right], heights[left])<maxi:
                if(heights[left]<heights[right]):
                    left+=1
                else:
                    right-=1
            if (right - left) * min(heights[right], heights[left])>=maxi:
                maxi=max(maxi, (right - left) * min(heights[right], heights[left]))
                if (heights[left]<heights[right]):
                    left+=1
                else:
                    right-=1
        return maxi

             
            

