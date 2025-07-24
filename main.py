def palindrome(text: str):
    """
    Checks if the provided text is a palindrome.

    Parameters:
        text (str): The string to be checked.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    if text == text[::-1]:
        return True
    else:
        return False
