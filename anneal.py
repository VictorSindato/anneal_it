import math
import random
import time
from mapreduce import *



class Problem:
    def __init__(self, input_file_path, max_map_workers, max_reduce_workers):
        self.path = input_file_path
        self.max_map_workers, self.max_reduce_workers = max_map_workers, max_reduce_workers
        self.state = [random.randint(1, max_map_workers), random.randint(1, max_reduce_workers)]

    def evaluate(self, state):
        map_workers, reduce_workers = state
        wc = WordCount(map_workers, reduce_workers, self.path)
        start_time = time.time()
        wc.run()
        out = wc.Merge()
        return time.time() - start_time

    def generate_random_state(self):
        return [random.randint(1, self.max_map_workers), random.randint(1, self.max_reduce_workers)]


def schedule(t):
    return 10-t

def anneal(problem):
    current = problem.state
    t = 1
    while True:
        print("t=",t)
        T = schedule(t)
        if T == 0:
            return "map workers:{}, reduce workers:{}".format(current[0], current[1])
        # Select a random next state
        next = problem.generate_random_state()
        delta = problem.evaluate(current) - problem.evaluate(next) # shorter time means better performance
        if delta > 0:
            current = next
        else:
            if random.random() < pow(math.e, delta/T):
                current = next
        t += 1
