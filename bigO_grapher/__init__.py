#!/usr/bin/python3
"""Time functions and graph results."""

import timeit
import matplotlib.pyplot as pyplot
from numpy import zeros
from collections import deque
import string
import os, sys
import random


class MuteablePrints:
    def __init__(self, mute):
        self.mute = mute

    def __enter__(self):
        self._original_stdout = sys.stdout
        if self.mute:
            sys.stdout = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._original_stdout


def muteable_prints(f):

    def wrapper(*args, mute=False, **kwargs):
        with MuteablePrints(mute):
            r = f(*args, **kwargs)
        return r
    return wrapper

def graph_times(times_to_graph):
    for t, label in times_to_graph:
        pyplot.plot(t, label=label)
    pyplot.legend(loc="upper left")
    pyplot.show()

def time_f_on_inputs(*args, **kwargs):
    """Run f on inputs, record results, graph."""
    number = kwargs.get("number")
    if number is None:
        number = 1000
    times_to_graph = deque()
    max_times = deque()
    for f, inputs in args:
        max_time = -1
        max_input = None
        times = []
        #print("FUNCTION", f)
        for i in inputs:
            #print("INPUT", i)
            s = lambda: f(i)
            t = timeit.timeit(s, number=number)
            #print("TIME", t)
            if t > max_time:
                max_time = t
                max_input = i
            times.append(t)
        times_to_graph.append((times, f.__name__))
        max_times.append((max_time, max_input))


    graph = kwargs.get("graph")
    if graph:
        graph_times(times_to_graph)

    time_averages = []
    for t, label in times_to_graph:
        time_averages.append(sum(times) / len(times))

    return max_times, time_averages


max_size = 10 ** 6


def generate_inputs(
    range_of_input = (0, 1000, 1),
    generate_input=None
):
    """Generate inputs for timing test."""
    if generate_input is None:
        generate_input = lambda x: zeros((x,))

    return (generate_input(i) for i in range(*range_of_input))


def time_f_on_growing_inputs(f, *args, **kwargs):
    """Time f on inputs of size initial size to max size."""
    inputs = generate_inputs(*args, **kwargs)
    time_f_on_inputs(f, inputs, **kwargs)


def graph_avg_times(*args, range_of_sizes=(0, 1000), num_of_size=1000):
        times_to_graph = deque()
        for f, generate_input in args:
            maxes = avgs = []
            for i in range(*range_of_sizes):
                inputs = generate_inputs(
                    generate_input=lambda x: generate_input(i),
                    range_of_input=(num_of_size,)
                )
                time_maxs, time_avgs = time_f_on_inputs((f, inputs), mute=True)
                print("timed size", i)
                for max_time, max_input in time_maxs:
                    maxes.append(max_time)
                for at in time_avgs:
                    avgs.append(at)

            times_to_graph.append((maxes, f.__name__ + " max"))
            times_to_graph.append((avgs, f.__name__ + " avg"))

        graph_times(times_to_graph)


def gen_random_str(length):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))


def generate_random_string_and_permutation(length):
    s = gen_random_str(length)
    return (s, s.shuffle())

