class Solution:
    def topKFrequent(self, nums, k: int):
        nums_dict = {}
        for i in nums:
            if i != nums[:-1]:
                if i not in nums_dict:
                    nums_dict[i] = 1
                else:
                    nums_dict.update( {i: (nums_dict.get(i)) + 1})

        sorted_by_values = sorted(nums_dict.items(), key=lambda x:x[1], reverse=True)
        res = []
        for i in range(0,k):
            res.append(sorted_by_values[i][0])
        return res
    
    
def main():
    solution = Solution()
    print(solution.topKFrequent([4,1,-1,2,-1,2,3],k = 2))
main()
