class Solution:
    def longestConsecutive(self, nums):
        l, nums = len(nums), sorted(nums)
        c, mx = 1, 1
        for i, n in enumerate(nums):
            if i < l-1 and n+1 == nums[i+1]:
                c+=1
            else:
                c, mx = 1, max(c, mx)
        return mx


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    # => 9 => [0-8]
