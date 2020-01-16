import time

class TimeManagement:

    def __init__(self):
        self.secs = self.get_time()
        self.start = time.time()
        self.pause_time = 0
 
    def stop(self):
        self.end = time.time()
        print(self.end-self.start)
        self.get_time_list(self.end - self.start - self.pause_time)

    def get_time(self):
        return time.time()

    def pause(self):
        self.start_pause = time.time()
    
    def unpause(self):
        end_pause = time.time()
        self.pause_time += (end_pause - self.start_pause)


    def get_time_list(self,secs):

        if secs > 60:
            minutes = secs // 60
            if minutes > 60:
                hours = minutes // 60
                rest_minutes = minutes % 60

            rest_secs = secs % 60
            
        else:
            hours = 0
            rest_minutes = 0
            rest_secs = secs

        hundreds = int((rest_secs % 1) * 100)
        millisecs = int((rest_secs % 1) * 1000 - hundreds * 10)        
        microsecs = int((rest_secs % 1) * 1000000 - millisecs * 100 - hundreds*1000)


        print('{}:{}:{}:{}:{}:{}'.format(int(hours),int(rest_minutes),int(rest_secs),hundreds,millisecs,microsecs))



T = TimeManagement()
for i in range(0,1000000):
    j = 1+1

T.stop()