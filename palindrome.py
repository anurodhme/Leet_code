def palindrome(n):
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False
        
print(palindrome(122))