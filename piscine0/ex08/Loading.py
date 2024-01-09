import sys
import time


def ft_tqdm(lst: range) -> None:
    """
    Simplified Reproduction of tqdm with yield keyword

    Args:
        :param lst: range

    Returns:
        None

    Exception:
        Never Raised.

    TODO: Iteration speed and Expected time
    """
    total = len(lst)
    start_time = time.time()

    def print_progress_bar(iteration):
        percent = f'{int(100 * (iteration / float(total)))}'
        filled_length = int(50 * iteration // total)
        bar = '█' * filled_length + ' ' * (50 - filled_length)
        current_time = time.time() - start_time
        current_minute = int(current_time // 60)
        current_second = int(current_time % 60)
        sys.stdout.write(
            f'\r{percent}%|{bar}| {iteration}/{total} '
            f'[{current_minute:02}:{current_second:02}]')
        sys.stdout.flush()

    for i, item in enumerate(lst):
        yield item
        print_progress_bar(i + 1)
    sys.stdout.write('\n')
    sys.stdout.flush()
