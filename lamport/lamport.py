from process import *
    
class lamports(object):
    def __init__(self,time,no_of_p,init_time):
        self.prossess_ = {}
        self.time = time
        self.no=no_of_p
        for i in range(self.no):
            x=process(init_time)
            print("ls = ",x.id)
            self.prossess_[x.id]=x

    def event(self,pid):
        p = self.prossess_[pid]
        p_time = p.get_clock()
        p.set_clock(p_time + 1)

    def send(self,sender_pid,resiver_pid):
        s = self.prossess_[sender_pid]
        s.set_clock(s.get_clock() + 1)
        
        r=self.prossess_[resiver_pid]
        self.resive(s.get_clock(),resiver_pid)
    def resive(self,time,resiver_pid):
        r=self.prossess_[resiver_pid]
        t=max(time,r.get_clock())
        r.set_clock(t+1)
        



