class process(object):
    i=0
    def __init__(self,time):
        self.id = process.i
        process.i += 1
        self.__time = time

    def set_clock(self,time):
        self.__time = time

    def get_clock(self):
        return self.__time


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

