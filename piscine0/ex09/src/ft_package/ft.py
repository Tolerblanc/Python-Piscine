def ft():
    """
    always return 42

    Args:
        None

    Returns:
        42

    Exception:
        Never Raised.
    """
    return 42


def count_in_list(lst: list, target: any) -> int:
    """
    find the target in list and print the result

    Args:
        :param lst: List Container to find target
        :param target: target to find in `lst`

    Returns:
        the amount of target

    Exception:
        Never Raised.
    """
    count = 0
    for elem in lst:
        if elem == target:
            count += 1
    return count
