def palindrome(string, left, right):
    # Base case: crossed pointers → full check done
    if left >= right:
        return True
    
    # If mismatch → not palindrome
    if string[left] != string[right]:
        return False
    
    # Move inward
    return palindrome(string, left + 1, right - 1)


string = "mom1"
left = 0
right = len(string) - 1
print(palindrome(string, left, right))
