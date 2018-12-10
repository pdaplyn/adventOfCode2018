"""
>>> test = read_file("../inputs/input4-test.txt")
Opening file  ../inputs/input4-test.txt
>>> parsed = [parse(x) for x in test]
>>> parsed.sort(key=by_date)
>>> guards = read_messages(parsed)
>>> order_by_sleep(guards)[0][0]
'10'
"""

from advent_util import read_file
from datetime import datetime


def by_date(msg):
    return msg['timestamp']


def parse(input):
    [timestamp,message] = input.replace("[","").split("] ")
    datetime_object = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    return {
        "timestamp": datetime_object,
        "message": message.rstrip()
    }


def read_messages(messages):
    guards = {}
    id = 0
    start_min = 0
    for message in messages:
        text = message['message']
        if text.startswith('Guard'):
            [ignore,post] = text.split('#')
            [id, ignore] = post.split(' ', 1)
            if id not in guards:
                guards[""+id] = [0 for x in range(60)]
        elif text.startswith('falls'):
            start_min = message['timestamp'].minute
        elif text.startswith('wakes'):
            mins = guards[""+id]
            end_min = message['timestamp'].minute
            for min in range(start_min,end_min):
                mins[min] += 1
            guards[""+id] = mins
    return guards


def order_by_sleep(guards):
    sorted_guards = sorted(guards.items(), key=lambda kv: sum(x for x in kv[1]))
    sorted_guards.reverse()
    return sorted_guards


input = read_file("../inputs/input4.txt")
parsed = [parse(x) for x in input]
parsed.sort(key=by_date)
guards = read_messages(parsed)
guards = order_by_sleep(guards)
print("sleepy guard is", guards[0])

for guard in guards:
    print(max(x for x in guard[1]), guard)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
