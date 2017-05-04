#!/usr/bin/env python
# coding=utf-8

class trigger():
    
    def __init__(self,slot):
        self.cur_time = -1
        self.slot = slot

    def time_trigger(self):
        self.cur_time += 1
        if self.cur_time % self.slot == 0:
            return True
        else:
            return False

