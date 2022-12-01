def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    answer = 0
    for i in range(A, B):
        answer += i
    return answer