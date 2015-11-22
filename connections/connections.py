class Connection:
    def __init__(self, id):
        self.status = 'new'
        self.amount = 0
        self.id = id
    
    def fund(self, amount):
        if self.status == 'new':
            self.amount = amount
            self.status = 'pending'
        else:
            raise RuntimeError('Cannot fund transaction')
    
    def funded(self):
        if self.status == 'pending':
            self.status = 'funded'
        else:
            raise RuntimeError('Cannot have transaction funded')

    def close(self):
        if self.status == 'funded' or self.status == 'pending':
            self.status = 'closed'
        else:
            raise RuntimeError('Cannot close transaction')

    def serialize(self):
        return {'id': self.id, 'status': self.status, 'amount': self.amount}

connections = [
    Connection(1),
    Connection(2)
]
