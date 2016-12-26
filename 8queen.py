# coding:utf8

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '十' * (pos) + '龘' + '十' * (length-pos-1)
    for pos in solution:
        print(line(pos))

from random import choice
prettyprint(choice(list(queens(8))))

# print(list(queens(4, (1,3,0))))