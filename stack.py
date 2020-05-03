class Stack:
    def __init__(self, list_list):
        self.list_stack = list_list

    def isEmpty(self):
        if self.list_stack == []:
            return True
        else:
            return False

    def push(self, item):
        self.list_stack.append(item)

    def pop(self):
        return self.list_stack.pop()

    def peek(self):
        last_item = self.list_stack[len(self.list_stack) - 1]
        return last_item

    def size(self):
        return len(self.list_stack)

    def show(self):
        print(self.list_stack)

def main():
    while True:
        list_brackets = input('Введите скобки слитно: \n')
        dict_brackets = {'(': ')',
                         '{': '}',
                         '[': ']'
                         }
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        stack = Stack([])
        for bracket in list_brackets:
            stack.push(bracket)
        if stack.size() % 2 != 0 or stack.peek() in open_brackets:
            print('Неcбалансированно')
            continue
        ex_close_brackets = []
        ex_open_brackets = []
        k = 0
        while stack.isEmpty() == False:
            part_close_brackets = []
            part_open_brackets = []
            while stack.peek() in close_brackets:
                part_close_brackets.append(stack.pop())
                if stack.isEmpty() == True:
                    break
            while stack.peek() in open_brackets:
                part_open_brackets.append(stack.pop())
                if stack.isEmpty() == True:
                    break
            part_close_brackets.reverse()
            if len(part_close_brackets) > len(part_open_brackets):
                delta = len(part_close_brackets) - len(part_open_brackets)
                for i in reversed(range(len(part_close_brackets)-delta, len(part_close_brackets))):
                    ex_close_brackets.append(part_close_brackets[i])
                    part_close_brackets.pop(i)
            if len(part_close_brackets) < len(part_open_brackets):
                delta = len(part_open_brackets) - len(part_close_brackets)
                for i in reversed(range(len(part_open_brackets) - delta, len(part_open_brackets))):
                    ex_open_brackets.append(part_open_brackets[i])
                    part_open_brackets.pop(i)
            for i in range(len(part_close_brackets)):
                if dict_brackets[part_open_brackets[i]] == part_close_brackets[i]:
                    continue
                else:
                    k += 1
        if k != 0:
            print('Неcбалансированно')
            continue
        else:
            # ex_close_brackets.reverse()
            if len(ex_close_brackets) != len(ex_open_brackets):
                k += 1
            else:
                for j in range(len(ex_close_brackets)):
                    if dict_brackets[ex_open_brackets[j]] == ex_close_brackets[j]:
                        continue
                    else:
                        k += 1
        if k == 0:
            print('Сбалансированно')
        else:
            print('Неcбалансированно')

main()
