class Solution:
    def trap(self, height: List[int]) -> int:
        
        '''max_left = []
        m_l = 0
        for i in range(len(height)) :
            if height[i] > m_l:
                max_left.append(m_l)
                m_l = height[i]   
            else:
                max_left.append(m_l)
         
        max_right = [0 for i in range(len(height))]
        m_r = height[-1]
        
        for i in range(len(height)-2,-1,-1):
            if height[i] > m_r:
                max_right[i] = m_r
                m_r = height[i]   
            else:
                max_right[i] = m_r
        print(max_left)
        print(max_right)
        
        count = 0
        for i in range(len(height)):
            val = min(max_left[i],max_right[i]) - height[i]
            if val > 0 :
                count+=val
            
        return count'''
        l = 0
        m_l = 0
        m_r = 0
        r = len(height)-1
        
        count = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] > m_l:
                    m_l = height[l]  
                val = m_l - height[l]
                if val > 0:
                    count += val
                l += 1
                
            else:
                if height[r] > m_r:
                    m_r = height[r]
                val = m_r - height[r]
                if val > 0:
                    count += val
                r -= 1

                
        return count
            
            
        
            
            
                
            
                
        