import math
import random
import time
from mapreduce import *



class Problem:
    def __init__(self, input_file_path, max_map_workers, max_reduce_workers):
        self.path = input_file_path
        self.max_map_workers, self.max_reduce_workers = max_map_workers, max_reduce_workers
        self.state = [random.randint(1, max_map_workers), random.randint(1, max_reduce_workers)]
