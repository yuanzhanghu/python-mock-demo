#! /usr/bin/env python3

def func1():
    return 'original func1'

class Target:
    """test target"""
    def __int__(self):
        print("initialized.")

    def method1(self, a, b, c):
        """mothod 1"""
        return [a, b, c]

    def method2(self):
        """mothod 2"""
        return func1()
