class cirqueue:
    def __init__(self,k):
        self.k=k
        self.q=[None]*k
        self.head=self.tail=-1

    def enqueue(self,d):
        if self.tail==self.k-1:
            return 'queue is full'
        elif self.head==-1:
            self.head=self.head=0
            self.q[self.tail]=d
        else:
            self.tail=self.tail+1
            self.q[self.tail]=d

    def dequeue(self):
        if self.tail==self.head==-1:
            return 'que is empty'
        else:
            pass
