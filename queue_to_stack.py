"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    stack = ArrayStack()
    str_queue = list(str(queue))
    del str_queue[0]
    del str_queue[-1]
    joined = ''.join(str_queue)
    new_lst = [int(i) for i in joined.split(', ')]
    for i in range(len(new_lst)):
        stack.push(new_lst[::-1][i])
    # print(list(str_queue))
    return stack


queue = ArrayQueue()
for i in range(10):
    queue.add(i)

stack = queue_to_stack(queue)
# print(queue)
# print()
# print(stack)
# print()
# print(stack.pop())
# print()
# print(queue.pop())

stack.add(11)
queue.add(11)

print(queue)
print()
print(stack)