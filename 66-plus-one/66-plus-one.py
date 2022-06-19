class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Alternative method which iterates through the whole list without reversing the order
        # Time Complexity : O(n), Space Complexity : O(1), since it is a fixed size array hence O(1)
        one, i = 1, (len(digits) - 1)
        while one:
            if i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
                    return digits
            else:
                digits.insert(0, 1)
                one = 0
            i -= 1
        return digits