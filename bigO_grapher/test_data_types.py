#!/usr/bin/python3
"""Time functions and graph results."""

from bigO_grapher import time_f_on_inputs, generate_inputs
from collections import deque

a = deque()

def append_to_list(N):
    l = []
    for i in range(N):
        l.append(None)

def append_to_dqe(N):
    d = deque()
    for i in range(N):
        d.append(None)

def add_to_set(N):
    d = set()
    for i in range(N):
        d.add(None)

def change_index_in_list(args):
    l, index = args
    l[index] = "a"

def append_to_str(N):
    s = ""
    for i  in range(N):
        s += "a"

def generate_random_string_of_length(length):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))


fs_to_test = (append_to_list, append_to_dqe, add_to_set, append_to_str)
inputs = list(
    generate_inputs(
        generate_input=lambda x: x,
        range_of_input=(0,1000)
    )
)
test_args = ((f, inputs) for f in fs_to_test)
time_f_on_inputs(*test_args, graph=True)