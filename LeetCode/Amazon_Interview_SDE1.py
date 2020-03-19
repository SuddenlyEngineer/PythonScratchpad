import re

Thread1 = 'Thread 1  start_time: 2:00 end_time: 4:00'
Thread2 = 'Thread 2  start_time: 3:00 end_time: 5:00'
Thread3 = 'Thread 3  start_time: 1:00 end_time: 4:00'
Thread4 = 'Thread 4  start_time: 5:00 end_time: 7:00'

def ThreadComparator(*args): 
    Thread_ranges = []
    for Thread in args:
        Parsed = Thread_Parser(Thread)
        Thread_ranges.append(Thread_Hours(Parsed))
    flat_list = sum(Thread_ranges, [])
    sorted_list = sorted(set(flat_list), key = lambda hour: flat_list.count(hour))
    print(f"Active during {sorted_list[-2]}:00 and {sorted_list[-1]}:00")

def Thread_Hours(Thread):
    return list(range(Thread[0], Thread[1]+1))

def Thread_Parser(str):
    hours_regex = re.compile(r'\d:00')
    [start, end] = hours_regex.findall(str)
    return [int(start[0]), int(end[0])]

ThreadComparator(Thread1, Thread2, Thread3, Thread4)