import string


def search_in_text(p: string, t: string):
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
                start_index -= t[start_index] == element
                break

    return index_found, total_checks


if __name__ == "__main__":
    p = input("Give pattern to be found (P):")
    t = input("Give text (T):")
    print("Len of t: {}".format(len(t)))
    index, checks = search_in_text(p, t)
    print("Pattern found at index: {}. Total checks done: {}".format(index, checks))
