class Stack:
    def __init__(self):
        self.bracket_list = []

    def is_empty(self):
        if self.bracket_list:
            return False
        else:
            return True

    def push(self, brackets):
        self.bracket_list.append(str(brackets))

    def pop(self):
        if self.is_empty() == False:
            return self.bracket_list.pop()

    def peek(self):
        if self.is_empty() == False:
            return self.bracket_list[-1]

    def size(self):
        return len(self.bracket_list)

    def is_balanced(self):
        s = input('Ввод:\n')
        balanced = True
        for i in s:
            if i in "([{":
                self.push(i)
            elif i in ")]}":
                open_brackets = self.pop()
                if open_brackets == "(" and i == ")":
                    continue
                if open_brackets == "[" and i == "]":
                    continue
                if open_brackets == "{" and i == "}":
                    continue
                print('Несбалансированно')
                balanced = False
                return balanced
                # break
        print('Сбалансированно')
        return balanced
