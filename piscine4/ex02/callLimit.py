def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwargs):
            nonlocal count, limit
            count += 1
            if count <= limit:
                return function(*args, **kwargs)
            else:
                print(f'Error: {function} call too many times')
                return None
        return limit_function

    return callLimiter
