class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            
            match ops:
                case '+':
                    stack.append(stack[-1]+stack[-2])
                case 'C':
                    stack.pop()
                case 'D':
                    stack.append(stack[-1]*2)
                case _:
                    stack.append(int(ops))
        return sum(stack)
        