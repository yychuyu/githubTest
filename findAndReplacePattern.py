class Solution(object): 
	def findAndReplacePattern(self, words, pattern): """
        :type pattern: str
        :rtype: List[str]
		res=[]
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

        		
        	

