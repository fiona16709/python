class Stack:
    def __init__(self):
        """
        初始化使用 list 模擬 Stack 的資料結構行為
        """
        self.stack = []

    def push(self, data):
        """
        透過 append 將元素 append 放入 list 中
        """
        self.stack.append(data)

    def pop(self):
        """
        list 的方法 pop 若沒指定 index 則會移除最後的元素並回傳，符合 stack 後進先出原則
        """
        return self.stack.pop()
    def get_is_empty(self):
      if len(self.stack) == 0:
        return True
      else:
        return False

    def get_size(self):
      return len(self.stack)

stack_1 = Stack()

stack_1.push('Amy')
stack_1.push('Cindy')
stack_1.push('Joe')
stack_1.push('Roy')
stack_1.push('Andy')
stack_1.push('Jame')

pop_item = stack_1.pop()


print('Last in, First out:', pop_item)
print('Empty or not? (True/False)', stack_1.get_is_empty())
print('Rest element amount:', stack_1.get_size())
