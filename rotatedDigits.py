class Solution:

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
		"""
        ans = []
        digit_map = {'0': '0', '1': '1', '2': '5',
                     '5': '2', '6': '9', '8': '8', '9': '6'}
        for number in range(1, N + 1):
            numStr = str(number)
            if ('3' in numStr)  or ('4' in numStr) or ('7' in numStr):
                continue
            # revStr是numStr的180°反转字符串,初始化为''
            revStr = ''
            for digit in numStr:
                revStr = revStr + digit_map[digit]
            if revStr != numStr:
                ans.append(numStr)
                # 将该值添加到ans后将revStr重置为''
                revStr = ''
        return len(ans)
