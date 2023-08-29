class BusStop:
    def __init__(self, name):

        self.name = name
        self.queue = []


    def add_to_queue(self, input_person):

        self.queue.append(input_person)

        
    def clear(self):

        self.queue = []


    def queue_length(self):

        return len(self.queue)