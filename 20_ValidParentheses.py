class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        elif len(s) % 2 == 1 or s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        else:
            d = {"(": ")", "[": "]", "{": "}"}
            tmp = s[0]
            for parenthese in s[1:]:
                tmp = tmp + parenthese
                # if parenthese != d[tmp[-1]] or parenthese != "(" or parenthese != "[" or parenthese != "{":
                #	return False
								#len(tmp)>=2是为了防止诸如()[]的情况,{}消除后第一个tmp长度只有1,程序中断
                if len(tmp) >= 2 and parenthese == d[tmp[-2]]:
                    tmp = tmp[:-2]
                elif parenthese != "(" and parenthese != "[" and parenthese != "{":
                    return False
            if len(tmp) == 0:
                return True
            else:
                return False
