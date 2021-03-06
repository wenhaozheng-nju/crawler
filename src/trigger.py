#!/usr/bin/env python
# coding=utf-8


class Trigger():
    
    def __init__(self,slot):
        self.cur_time = -1
        self.slot = slot

    def time_trigger(self):
        self.cur_time += 1
        if self.cur_time % self.slot == 0:
            return True
        else:
            return False

    @staticmethod
    def url_trigger(url_pool):
        if len(url_pool.get_url_queue()) == 0:
            return False
        else:
            return True


