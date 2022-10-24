import os
import sys
# print(sys.path)

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# print(PROJECT_ROOT)

sys.path.append(PROJECT_ROOT)
# print(sys.path)

from utils.decorators import do_twice

@do_twice
def pew():
    print("pew pew pew")

if __name__=='__main__':
    pew()
