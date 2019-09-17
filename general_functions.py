from datetime import datetime, time


# Convert str to time
def str_to_time(strtime):
    temp_time = [int(i) for i in strtime.split(':')]
    return time(*temp_time)


# Get current time
def get_cur_time():
    return datetime.now().time()