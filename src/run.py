#! /usr/bin/env python3

from src.target import Target


def run1():
    target = Target()
    return target.method1(1, 2, 3)


if __name__ == '__main__':
    run1()
