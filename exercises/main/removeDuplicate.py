class RemoveDuplicates:
    def removeDuplicatesI(self, nums):
        
        if len(nums) < 2:
            return len(nums)
        
        else:
            unique = 1    #number unique elements sorted
            sort = 1      #position looking in the array
            min = nums[0] #registers the smallest biggest number found


            while (sort < len(nums)):          #i think it could be changed for a for loop
                if(min < nums[sort]):         
                    nums[unique] = nums[sort]
                    unique += 1
                    min = nums[sort]
                else:
                    sort += 1

            return unique