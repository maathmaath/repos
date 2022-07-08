import re


class Eval(object):
    def __init__(self, string):
        self.string = string
        self.alpha_regex = r"([a-zA-Z]+)"
        self.number_regex = r"([0-9]+)"
        self.op_regex = r"([+-^%*/])"
        self.list_ = []

    def peek(self):
        if self.string:
            return self.string[0]
        else:
            return None

    def get(self):
        if self.string:
            x = self.string[0]
            self.string = self.string[1:]
            return x
        print("Return None")
        return None

    def number(self):
        result = int(self.get()) - 0
        if self.string:
            while self.peek() >= '0' and self.peek() <= '9':
                result = 10*result + self.get() - 0
        return result

    def factor(self):
        if self.string:
            if self.peek() >= '0' and self.peek() <= '9':
                return self.number()
            elif self.peek() == '(':
                self.get()
                result = self.expr()
                self.get()
                return result
            elif self.peek() == '-':
                return -self.factor()
        return 0

    def term(self):
        result = self.factor()
        if self.string:
            while self.peek() == '*' or self.peek() == '/':
                if self.get() == '*':
                    result *= self.factor()
                elif self.get() == '/':
                    result /= self.factor()
                else:
                    return result
        return result

    def expr(self):
        result = self.term()
        if self.string:
            while self.peek() == '+' or self.peek() == '-':
                if self.get() == '+':
                    result += self.term()
                elif self.get() == '-':
                    result -= self.term()
                else:
                    return result
        return result

    def compute(self):
        if self.string == "":
            return None
        elif re.findall(self.alpha_regex, self.string.lower()):
            print("[*] Invalid string.")
            return None
        else:
            result = self.expr()
            print(f"[*] The value of the expression is {result}.")
            return


_expr = "5*3*2+4*1+(4+9)*6"
c = Eval(_expr)
c.compute()
