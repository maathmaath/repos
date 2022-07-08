switcher = {
    'vowels' : ['a', 'e', 'i', 'o', 'u'],
    'consonants': ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']    
    }
    
def char(char):
    if char in switcher.get('vowels'):
        return 'Alice'
    elif char in switcher.get('consonants'):
        return 'Bob'
    else:
        return 'nobody'
    
def solution():
    n = int(input())
    if not n<=300:
        exit()
    for i in range(n):
        name = input()
        print(f"Case #{i+1}: {name} is ruled by {char(name[-1])}.")

solution()
