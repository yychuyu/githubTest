class Solution(object): 
	def findAndReplacePattern(self, words, pattern): """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
		res=[]
        set_pattern=set(pattern)
        for word in words:
            if len(set(word))!=len(set_pattern):
                continue
            d=dict()
            flag=True
            for i,w in enumerate(word):
                if w in d:
                    if d[w]!=pattern[i]:
                        flag=False
                        break
                d[w]=pattern[i]
            if flag:
                res.append(word)
        return res

        		
        	

