class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        end = m + n -1
        m -= 1
        n -= 1
        while end >=0 and m >=0 and n >=0:
            if nums1[m] >= nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
            else:
                nums1[end] = nums2[n]
                n -=1
            end -= 1
        
        while n >= 0:
            nums1[end] = nums2[n]
            end -= 1
            n -= 1
        print(nums1)

def CountLength(string,curpos,count,maxlength):
    if curpos == len(string):
        return maxlength
    if string[curpos] == string[curpos-1]:
        count += 1
        if count > maxlength:
            maxlength = count
    else:
        count = 1
    return CountLength(string,curpos+1,count,maxlength)


if __name__ == '__main__':
    # s = Solution()
    # s.merge([1,2,3,0,0,0],3,[2,5,6],3)
    s = CountLength("aaabbcc",1,1,1)
    print(s)
