def ft_tqdm(lst: range) -> None:
    while lst:
        lst = next(lst)
        yield lst
