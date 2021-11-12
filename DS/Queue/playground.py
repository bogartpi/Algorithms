from queue import Queue

mqueue = Queue(432)
mqueue.enqueue(22)
mqueue.enqueue(33)

mqueue.dequeue()

mqueue.print_queue()