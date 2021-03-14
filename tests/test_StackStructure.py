from Structures.Stack import StackS
from Structures.LList import Node


test_stack: StackS = StackS()

for num in range(10):
    test_stack.AtBeggining(Node(num))

print(f"New linked list: {test_stack}")

test_stack.push(Node(-1))
print(f"New head: {test_stack}")

print(f"Current head: {test_stack.get_top()}")

old_head: int = test_stack.pop()
print(f"Popped value {old_head}")

print(f"Current stack: {test_stack}")
print(f"Current lenght: {test_stack.Lenght()}")
