from process import *
    
class logical_vector(object):
    def __init__(self,time,no_of_p,init_time):
        self.prossess_ = {}
        self.time = time
        self.no=no_of_p
        for i in range(self.no):
            x=process(init_time)
            print("id = ",x.id)
            self.prossess_[x.id]=x
            for j in range(self.no):
                x.time_vector[j]=0

    def event(self,pid):
        p = self.prossess_[pid]
        p_time = p.get_clock()
        p.set_clock(p_time + 1)

    def send(self,sender_pid,resiver_pid):
        s = self.prossess_[sender_pid]
        self.event(sender_pid)
        self.resive(s.time_vector,resiver_pid)
    def resive(self,v,resiver_pid):
        r=self.prossess_[resiver_pid]
        t=r.get_clock()
        for i in v:
            r.time_vector[i]=v[i]
        r.set_clock(t+1)
        