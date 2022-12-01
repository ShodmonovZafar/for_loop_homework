def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int = 3
    Returns:
        string: return  answer = "0,1,2,3"
    """
    answer = ""
    for i in range(n):
        if i == n - 1:
            answer += str(i)
        else:
            answer += str(i) + ","
    return answer