def is_palindrome(input_data: str) -> bool:
    new_data = ''
    for element in input_data:
        if element.isalnum():
            new_data += element.lower()
    if new_data == new_data[::-1]:
        return True
    return False


print(is_palindrome(input()))
