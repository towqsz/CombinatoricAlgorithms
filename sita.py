import threading
index = 0
lock_i = 0
lock = threading.Lock()
b = threading.Barrier(2)


def inc():
    global lock_i
    with lock:
        lock_i += 1


def dec():
    global lock_i
    with lock:
        lock_i -= 1


def count_sums(sum, sum_elements_list):
    sum_counter = 0
    for i, element in enumerate(sum_elements_list):
        for other_element in sum_elements_list[i+1:]:
            if sum == element + other_element:
                sum_counter += 1
    return sum_counter


def filter_not_sum(some_list):
    for element in some_list[:]:
        if (not count_sums(element, some_list)) and element > 2:
            some_list.remove(element)
        b.wait()


def filter_more_sums(some_list):
    for element in some_list[:]:
        if count_sums(element, some_list) > 1 and element > 2:
            some_list.remove(element)
        b.wait()


if __name__ == "__main__":
    n = int(input("Give n:"))
    list_to_filter = [i for i in range(1, n+1)]
    not_sum_th = threading.Thread(target=filter_not_sum, args=(list_to_filter,))
    more_sums_th = threading.Thread(target=filter_more_sums, args=(list_to_filter,))
    threads = [not_sum_th, more_sums_th]
    [th.start() for th in threads]
    [th.join() for th in threads]
    print(list_to_filter)
