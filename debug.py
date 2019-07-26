from memory_profiler import profile

@profile
def chg_nums(n):
    n = 20
def chg_list(l):
    l.append(20)
a = 18
chg_nums(a)
b = [1,2]
chg_list(b)
