def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    answer = 0
    for i in range(1, N, 2):
        answer += i
    return answer