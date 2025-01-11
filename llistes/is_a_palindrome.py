def is_palindrome(s: str) -> bool:
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l - i - 1]:
            return False
    return True