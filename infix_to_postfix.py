class stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        assert self.items, 'No items!'
        return self.items.pop()

    def peek(self):
        assert self.items, 'No items!'
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class infix_to_postfix:
    def __init__(self, infix):
        self.infix = infix
        self.postfix = ""
        self.stack = stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def convert(self):
        for i in self.infix:
            if i.isdigit():
                self.postfix += i
            elif i in self.precedence:
                while (
                    not self.stack.empty()
                    and self.stack.peek() != '('
                    and self.precedence[i] <= self.precedence[self.stack.peek()]
                ):
                    self.postfix += self.stack.pop()
                self.stack.push(i)
            elif i == '(':
                self.stack.push(i)
            elif i == ')':
                while not self.stack.empty() and self.stack.peek() != '(':
                    self.postfix += self.stack.pop()
                self.stack.pop()  # Pop the '(' from the stack

        while not self.stack.empty():
            self.postfix += self.stack.pop()

        return self.postfix


if __name__ == '__main__':
    infix = input('Enter infix expression: ')
    postfix_converter = infix_to_postfix(infix)
    print(postfix_converter.convert())
