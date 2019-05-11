import string


def compare_elements(list1, list2):
    found = True
    shift = 0
    if list1:
        for i, el in enumerate(list1):
            if el != list2[i]:
                found = False
                shift = i + 1
    return found, shift


def simple_search(p: string, t: string):
    start_index = 0
    total_checks = 0
    p = [c for c in p]
    index_found = None

    while start_index < len(t) - (len(p)-1) and not index_found:
        index_found = start_index
        for i, element in enumerate(p):
            start_index += 1
            total_checks += 1
            if element != t[start_index-1]:
                index_found = None
                break

    return index_found, total_checks


if __name__ == "__main__":
    p = input("Give pattern to be found (P):")
    t = input("Give text (T):")
    print("Len of t: {}".format(len(t)))
    index, checks = simple_search(p, t)
    print("Pattern found at index: {}. Total checks done: {}".format(index, checks))



