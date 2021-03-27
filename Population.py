from Solution import Solution
from Config import *
from Board import Board


class Population:
    def __init__(self, solutions=[]):
        self.solutions = solutions

    def add(self, solution):
        self.solutions.append(solution)

    def print(self):
        print("Population: (")
        for i in range(len(self.solutions)):
            print("--"+str(i)+"--")
            self.solutions[i].print()
        print(") End Population")