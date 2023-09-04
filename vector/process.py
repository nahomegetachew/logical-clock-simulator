class process(object):
    i=0
    def __init__(self,time):
        self.id = process.i
        process.i += 1
        self.time_vector = {}
        self.sml_pt = 0

    def set_clock(self,time):
        self.time_vector[self.id] = time

    def get_clock(self):
        return self.time_vector[self.id]
    def larger_clock(self):
            # print(max(self.time_vector.values()),"hjk")
            return max(self.time_vector.values())

