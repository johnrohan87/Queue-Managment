class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        #print("Self = " + str(self) + " item " + str(item) )
        self._queue.insert(0,item)
        pass
    def dequeue(self):
        return self._queue.pop()
    def get_queue(self):
        return self._queue
    def size(self):
        return len(self._queue)