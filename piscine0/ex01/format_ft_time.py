import time
import datetime

current_time = time.time()
print(f'Seconds since January 1, 1970: {current_time:,.4f} or \
{current_time:.2e} in scientific notation')

current_date = datetime.datetime.now().date()
print(f'{current_date.strftime("%b")} {current_date.day} {current_date.year}')
