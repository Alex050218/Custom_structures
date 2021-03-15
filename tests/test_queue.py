from Structures.SQueue import Node, Queue

test_queue: Queue = Queue()

for num in range(10):
    test_queue.enque(Node(num))

print(f"New queue: {test_queue.get_str()}")
