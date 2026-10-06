class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count={}
        t_count={}

        if len(t)!=len(s):
            return False

        for i in s:
            if i in s_count:
                s_count[i]+=1
            if i not in s_count:
                s_count[i]=1
        for i in t:
            if i in t_count:
                t_count[i]+=1
            if i not in t_count:
                t_count[i]=1

        if s_count!=t_count:
            return False
        else:
            return True