import io
import sys

def foo():
    orig_out = sys.stdout
    print('give me input: ')
    sys.stdout = io.StringIO()
    a = input()
    sys.stdout = orig_out

if __name__ == '__main__':
    foo()
