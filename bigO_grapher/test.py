#!/usr/bin/python3
"""Time functions and graph results."""

from bigO_grapher import time_f_on_inputs, generate_inputs
from collections import deque
import math

max_arg = 20

def log_time(N):
    for i in range(math.floor(math.log(N + 1))):
        pass

def linear_time(N):
    for i in range(N):
        pass


def constant_time(N):
    for i in range(max_arg):
        pass


def n_logn_time(N):
    for i in range(N * math.floor(math.log(N + 1))):
        pass


def n_squared_time(N):
    for i in range(N * N):
        pass


def generate_random_string_of_length(length):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))


fs_to_test = (
    log_time,
    linear_time,
    constant_time,
    n_logn_time,
    #n_squared_time   
)


test_args = ((f, generate_inputs(
    generate_input=lambda x: x,
    range_of_input=(0, max_arg)
)) for f in fs_to_test)

time_f_on_inputs(*test_args, graph=True, number=1000)
