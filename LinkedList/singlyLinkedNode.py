class SinglyLinkedNode():
    """Implements a singly-linked node.
    """

    def __init__(self, value, nextNode=None):
        self._value = value
        self._nextNode = nextNode

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, nextNode):
        self._nextNode = nextNode