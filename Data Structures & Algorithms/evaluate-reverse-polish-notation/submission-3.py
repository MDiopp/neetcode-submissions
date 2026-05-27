class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operand1 = None
        operand2 = None
        result = None
        intToken = None
        if not tokens:
            return 0
        for token in tokens:
            if token == "+":
                operand2 = numStack.pop()
                operand1 = numStack.pop()
                result = operand1 + operand2
                numStack.append(result)
            elif token == "-":
                operand2 = numStack.pop()
                operand1 = numStack.pop()
                result = operand1 - operand2
                numStack.append(result)
            elif token == "*":
                operand2 = numStack.pop()
                operand1 = numStack.pop()
                result = operand1 * operand2
                numStack.append(result)
            elif token == "/":
                operand2 = numStack.pop()
                operand1 = numStack.pop()
                result = int(operand1 / operand2)
                numStack.append(result)
            else:
                numToken = int(token)
                numStack.append(numToken)
        result = numStack.pop()
        return int(result)    



        