def main(list1 : list[str]):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    answer = []
    for i in list1:
        answer.append(i.capitalize(i))
    return answer