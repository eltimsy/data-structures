class Queue:
  def __init__(self, k):
    self.queue = ['' for i in range(k)]
    self.maxSize = k
    self.head = 0
    self.tail = 0

  def enqueue(self, data):
    if '' not in self.queue:
      return ("Queue Full")
    if self.tail == self.maxSize:
      self.tail = 0
      self.queue[self.tail] = (data)
    else:
      self.queue[self.tail] = (data)
      self.tail += 1
    return True

  def dequeue(self):
    if self.size() <= 0:
      self.resetQueue()
      return ("Queue Empty")
    data = self.queue[self.head]
    self.queue[self.head] = ''
    if self.head == self.maxSize:
      self.head = 0
    else:
      self.head += 1
    return data

  def size(self):
    return self.tail - self.head

  def resetQueue(self):
    self.tail = 0
    self.head = 0
    self.queue = ['' for i in range(self.maxSize)]