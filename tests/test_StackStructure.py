from Structures.Stack import StackS
from Structures.LList import Node


test_stack: StackS = StackS()

for num in range(10):
    test_stack.AtBeggining(Node(num))

print(f"New linked list: {test_stack}")

test_stack.push(Node(-1))
print(f"New head: {test_stack}")
