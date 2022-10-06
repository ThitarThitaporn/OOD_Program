# def isPalindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False 

def isPalindrome(s, fir, las):
    if len(s) <= 1:
        return True
    elif fir != len(s)//2-1:
        return isPalindrome(s, fir+1, las-1)
    elif s[fir] == s[las]:
        return True
    else:
        return False

inp = input('Enter Input : ')
if isPalindrome(inp, 0, -1):
    print(f'\'{inp}\' is palindrome')
else:
    print(f'\'{inp}\' is not palindrome')
