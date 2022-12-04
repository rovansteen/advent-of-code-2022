import os 

def solution(input):
    return len(list(filter(None, iterate(input))))

def iterate(input: str):
    for line in input.splitlines():
        i, j = (range(* (int(x) for x in x.split('-'))) for x in line.split(','))
        yield (i.start >= j.start and i.stop <= j.stop) or (j.start >= i.start and j.stop <= i.stop) 


if __name__ == '__main__':
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    print(solution(input))