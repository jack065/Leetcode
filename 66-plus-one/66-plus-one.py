class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
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