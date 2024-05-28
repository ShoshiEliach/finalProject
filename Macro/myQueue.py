from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def insert_sons(self,G,item_father):
        list_sons = list(G.successors(int(item_father)))
        for i in list_sons:
            self.enqueue(i)

# Example usage
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
#
# print(queue.dequeue())  # Output: 1
# print(queue.dequeue())  # Output: 2
# print(queue.dequeue())  # Output: 3
# print(queue.dequeue())  # Output: Queue is empty
