#!/usr/bin/env python3
# encoding: utf-8
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt = {}
        for i,m in enumerate(nums):
            n = target - m
            if n in dt:
                return dt.get(n),i
            dt[m] = i
        return [None,None]

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[k] != nums[i]:
                k = k +1
                nums[k] = nums[i]
            print(nums)

        del nums[k+1:]
        print(nums)
        return len(nums)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        cul = 0
        tlist = []
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = cul + x + y
            cul = s // 10
            l = s % 10
            r.next = ListNode(l)
            r = r.next
            tlist.append(l)
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if cul != 0:
            # re.next = ListNode(cul)
            tlist.append(cul)
        # tmp = re.next
        # while tmp:
        #     tlist.append(tmp.val)
        #     tmp = tmp.next
        print(tlist)
        return tlist

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        dt = {}
        maxLength = 0
        now = 0
        for i in range(len(s)):
            if dt.get(s[i]) is not None:
                now = max(dt.get(s[i])+1,now)
                if (i - now +1) > maxLength:
                    maxLength = i - now + 1
            else:
                if (i - now +1) > maxLength:
                    maxLength = i - now + 1
            dt[s[i]] = i

        print(maxLength)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "#" + '#'.join(s) +"#"
        RL = [0] * len(s)
        mr = 0
        pos = 0
        mx = 0
        rtn = ""
        for i in range(len(s)):
            if i < mx:
                RL[i] = min(RL[2*pos-i],mr-i)
            else:
                RL[i] = 1
            while i - RL[i] >=0 and i+RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
                RL[i] += 1
            if RL[i]+i -1 > mr:
                mr = RL[i] +i -1
                pos = i
            if mx < RL[i]:
                mx = RL[i]
                n = RL[i]-1
                print(mx,RL,i,RL[i],s[i-n:i+n])
                rtn = ''.join([x for x in s[i-n:i+n] if (x !='#' and x != '%')])
        print(rtn)
        return rtn

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                result.append(nums1.pop(0))
            else:
                result.append(nums2.pop(0))
        if nums1:
            result += nums1
        if nums2:
            result += nums2

        n = len(result)
        if n %2 == 0: #偶数
            p = (result[n//2-1] + result[n//2])/2
        else: #奇数
            p = result[n//2]
        print(result,n,p)
        return p

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        f = False
        if x < 0:
            f = True
        x = abs(x)
        while x != 0:
            result = result * 10 + x %10
            x = x // 10
        if result > 2**31-1 or result < -2**31:
            result = 0
        if f:
            result = 0 - result
        print(result)
        return result

    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        import re
        strings =  re.search(r'^([+|-]?\d+)', string.lstrip())
        if strings is None:
            strings = 0
        else:
            strings = int(strings.group(1))

        if strings < -2**31:
            strings = -2**31
        if strings > 2**31 -1:
            strings = 2**31 -1
        return strings

    def signleNumber(self,nums):
        i = 0
        for x in nums:
            i = i ^x
        print(i)
        return i

def main():
    s = Solution()
    s.signleNumber([4,1,2,1,2,1])
    # i1 = ListNode(5)
    # j1 = ListNode(5)
    # print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    # s.addTwoNumbers(i1,j1)
    # s.lengthOfLongestSubstring("abcabcbb")
    # s.longestPalindrome("aba")
    # s.findMedianSortedArrays([1,3],[2])
    # s.reverse(-123)
    # s.myAtoi("-91283472332")

if __name__ == '__main__':
    main()
