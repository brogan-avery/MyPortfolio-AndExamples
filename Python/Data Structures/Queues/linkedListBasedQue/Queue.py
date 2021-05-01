"""
***************************************************************
* Class Name: Queue
* Author: Brogan Avery
* Created: 2021-02-13
***************************************************************
"""

# List Bases Queue, Not Array Based

from QueueEmptyException import QueueEmptyException

class Queue:
    def __init__(self):
        self.head = 0 # the next item to come out of queue
        self.tail = -1 # last item put in and last to come out
        self.size = 0 # how many memory boxes are currently in use
        self.items = [] # the queue list

    def is_empty(self):
        return self.size == 0 #  if the size of the queue is 0 it means that none of the boxes in the list are being occupied

    def enqueue(self, item): # puts an item in the line (end of queue)
            if self.is_empty(): # adding to the line when the queue is empty
                self.head = 0      # the first three just make sure it is initialized back to the values for an empty queue
                self.tail = -1
                self.size = 0
                self.tail += 1 # says the tail is now the last (but also the first here) element in the queue by pointing to the index that comes right  after the current index of tail
                self.size += 1 # also keeps track that the queue just grew by one size
                self.items.append(item)  # puts what ever value we want to add to end of line by putting it in the index of the new tail that was just changed
            else:
                self.tail += 1   # same as if the queue was empty only the tail just keeps getting tacked onto end
                self.size += 1
                self.items.append(item)  # puts what ever value we want to add to end of line by putting it in the index of the new tail that was just changed

    def dequeue(self):    # this is very much like the opposite of enqueue
        if not self.is_empty(): # in the case the queue is not empty
            item_str = self.items[self.head]
            self.items.pop(self.head)  # removes first value in the queue
            self.size -= 1   # reflects an element has been pushed through and out of the queue so the size shrinks by one
        else:
            raise QueueEmptyException()
        return item_str

    def peek(self):
        item_str = ""     # string var to capture the value in the head index
        if not self.is_empty():
            item_str = self.items[self.head]  # captures the value in the head index if there is something there
        else:
            # Raises exception.
            raise QueueEmptyException()

        # Return statement.
        return item_str

    def get_size(self):
        return self.size   # returns the current size of the queue

    def print_queue(self):
        for i in self.items:
            print(i)

    def __str__(self):
        return str(self.items)
