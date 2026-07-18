class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        s1=strs[0]
        s3=strs[-1]
        prefix=""
        for i in range(len(s1)):
        
            if i<len(s3) and s1[i]==s3[i]:
                prefix += s1[i]
            else:
                return prefix
        return prefix

        
      