class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotations = {
            "0":"0",
            '1':'1',
            '6':'9',
            '8':'8',
            '9':'6'
        }
        reverseS= ""

        for char in str(n):
            if char not in rotations:
                print(type(char))
                return False
            reverseS += rotations[char]
        
        return reverseS[::-1] != str(n)