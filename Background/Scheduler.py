import datetime as dt

from scheduler import Scheduler
from scheduler.trigger import Monday, Tuesday

def foo():
    print("foo")

schedule = Scheduler()

#schedule.cyclic(dt.timedelta(minutes=10), foo)

#schedule.minutely(dt.time(second=15), foo)
#schedule.hourly(dt.time(minute=30, second=15), foo)
schedule.daily(dt.time(hour=2, minute=0), foo)
#schedule.weekly(Monday(), foo)
#schedule.weekly(Monday(dt.time(hour=16, minute=30)), foo)

#schedule.once(dt.timedelta(minutes=10), foo)
#schedule.once(Tuesday(), foo)
#schedule.once(dt.datetime(year=2022, month=2, day=15, minute=45), foo)