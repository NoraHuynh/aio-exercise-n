def max_sliding_window(num_list, k):
    n = len(num_list)
    outpt = []
    for i in range(n - k + 1):
        max_num = max(num_list[i : i + k])
        outpt.append(max_num)
    return outpt


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
assert max_sliding_window(num_list, k) == [5, 5, 5, 5, 10, 12, 33, 33]

# (on-going) deque: https://wiki.vnoi.info/vi/algo/data-structures/deque-min-max
