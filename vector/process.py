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


    # def event(self):
    #     self.time += 1
    # def send(self,time):
    #     self.time += 1
    # def resive(self,time):
    #     if time > self.time:
    #         self.time = time + 1
    #     else:
    #         self.time += 1

# a=process(0)
# a.event()
# a.send()
# a.resive(5)
# a.resive(3)
# print(a.time)
# b=process(0)
# print(b.id)

