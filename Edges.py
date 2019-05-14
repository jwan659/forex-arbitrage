class Edge():
    
    def __init__(self, start, target, weight):
        self.start = start
        self.target = target
        self.weight = weight
    
    def get_weight(self):
        return self.weight
    
    def set_weight(self, weight):
        self.weight = weight
    
    def get_start(self):
        return self.start

    def set_start(self, start):
        self.start = start
    
    def get_target(self):
        return self.target
    
    def set_target(self, target):
        self.target = target