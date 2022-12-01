def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    answer = 0
    for i in range(1, N + 1):
        x = 1 / i
        answer += x
    return answer