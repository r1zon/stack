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
        list_brackets = list(list_brackets)
        stack = Stack([])
        k = 0
        for i in range(len(list_brackets)):
            if list_brackets[k] in open_brackets:
                stack.push(list_brackets[k])
                k += 1
            elif list_brackets[k] in close_brackets:
                if len(list_brackets) == 1 or k == 0:
                    stack.push(list_brackets[k])
                elif dict_brackets[list_brackets[k-1]] == list_brackets[k]:
                    stack.push(list_brackets[k])
                    stack.pop()
                    stack.pop()
                    list_brackets.pop(k)
                    list_brackets.pop(k-1)
                    k -= 1
        if stack.size() == 0:
            print('Сбалансированно')
        else:
            print('Несбалансированно')

main()
