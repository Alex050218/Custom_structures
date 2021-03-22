from Structures.SQueue import Node, Queue

test_queue: Queue = Queue()

for num in range(10):
    test_queue.enque(Node(num))

print(f"New queue: {test_queue.get_str()}")
print(f"Current length: {test_queue.lenght()}")

print("Iterating through the queue:")
for val in test_queue:
    print(val, end=" ")
print("\n")

removed_val: int = test_queue.deque()

while removed_val is not None:
    print(f"Queue after deque: {test_queue.get_str()}")
    print(f"Removed value: {removed_val}")
    print(f"New lenght: {test_queue.lenght()} \n")

    removed_val = test_queue.deque()
