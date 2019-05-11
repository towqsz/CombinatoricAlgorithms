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


def search_in_text(p: string, t: string):
    start_index = 1
    total_checks = 0
    p = [c for c in p]
    index_found = None
    if len(p) < 3:
        return simple_search(p, t)

    while (start_index < (len(t) - (len(p)-2))) and index_found is None:
        index_found = start_index - 1
        total_checks += 1

        if t[start_index] == p[1]:
            total_checks += 2
            if t[start_index+1] == p[2] and t[start_index-1] == p[0]:
                list1 = p[3:]
                total_checks += len(list1)
                c = compare_elements(list1, t[start_index + 2:start_index + 2 + len(list1)])
                if not c[0]:
                    index_found = None
                    start_index += 2 + c[1]
            else:
                index_found = None
                start_index += 2
        else:
            index_found = None
            start_index += 1

    return index_found, total_checks


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
    simple = input("")
    print("Len of t: {}".format(len(t)))
    if simple:
        index, checks = simple_search(p, t)
    else:
        index, checks = search_in_text(p, t)
    print("Pattern found at index: {}. Total checks done: {}".format(index, checks))



