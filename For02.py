def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    answer = ""
    for i in range(n):
        answer += str(i)
    return answer