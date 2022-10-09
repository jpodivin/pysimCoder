from time import time

class TicToc():
    
    def __init__(self):
        self.tic_ = time()

    def tic(self):
        self.tic_ = time()

    def toc(self):
        print(time()-self.tic_)

