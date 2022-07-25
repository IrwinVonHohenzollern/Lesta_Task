# На языке Python реализовать минимум 2 класса, реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
from typing import Any


class UserQueue:
    """This class realises FIFO with Python tuples. It checks the type of data, 
    allowing to append only the similar types."""
    def __init__(self):
        self._queue = tuple()
        self._dtype = None
        self._first = True

    def __str__(self):
        return str(self._queue)

    def put(self, value):
        if self._first:
            self._first = False
            self._queue += (value, )
            self._dtype = type(value)
        else:
            if type(value) == int and self._dtype == float:
                value = float(value)
            if isinstance(value, self._dtype):
                self._queue += (value, )
            else:
                raise TypeError("Your type is incorrect.")

    def get(self):
        if len(self._queue) > 0:
            value = self._queue[0]
            self._queue = self._queue[1:]
            return value
        else:
            raise IndexError('Your queue is empty.')
    
    def size(self):
        return len(self._queue)

    def isEmpty(self):
        return self.size() == 0



queue = UserQueue()
print(queue.isEmpty())
queue.put(18.1)
queue.put(-123.4)
queue.put(14)
queue.put(24)
queue.put(-34.2)
print(queue.isEmpty())
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.isEmpty())
print(queue)