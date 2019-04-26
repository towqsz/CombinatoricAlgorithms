import itertools
# itertools.combinations_with_replacement(iterable, r)


def get_combinations(nominals, m):
    if m == 1:
        nominals = [1]
    combinations = [combination for combination in itertools.combinations_with_replacement(nominals, m)]
    return get_combinations(nominals, m-1) + combinations if m != 1 else combinations


def get_all_combinations(nominals, m):
    combs = get_combinations(nominals, m)
    for i, element in enumerate(nominals):
        if element != 1:
            combs.insert(i, (element,))
    return combs


def get_all_nominals_comb(n, m):
    possible_nominals = [[1]]
    prev_best_nominal = 1

    for i in range(n-1):
        curr_best_nominal = prev_best_nominal * m + 1
        new_elements = []
        for element in possible_nominals:
            for l in range(element[-1], curr_best_nominal+1):
                new_element = element[:]
                new_element.append(l)
                new_elements.append(new_element)
        possible_nominals += new_elements
        prev_best_nominal = curr_best_nominal
    return possible_nominals


def get_best_nom_combs(n, m):
    combinations = get_all_nominals_comb(n, m)
    combinations = [c for c in combinations if len(c)==n]
    best_score = 0
    for combination in combinations:
        score = get_payment_score(combination, m)
        if score > best_score:
            best_score = score
    return [combination for combination in combinations if get_payment_score(combination, m) == best_score]


def get_payments(nominals, m):
    sums = []
    for combination in get_all_combinations(nominals, m):
        sums.append(sum(combination))
    payments = []
    i = 1
    while True:
        if i in sums:
            payments.append(i)
            i += 1
        else:
            break
    return payments


def get_payment_score(nominals, m):
    return max(get_payments(nominals, m))


def get_next_best_nominal(nominals, m):
    score = get_payment_score(nominals, m)
    new_nominal = score + 1
    best_nominal = new_nominal
    best_score = 0

    while new_nominal > nominals[-1]:
        new_nominals = nominals[:]
        new_nominals.append(new_nominal)
        new_score = get_payment_score(new_nominals, m)
        if new_score > best_score:
            best_nominal = new_nominal
            best_score = new_score
        else:
            new_nominal -= 1
    return best_nominal


def get_best_nominals_set(n, m):
    nominals = [1]

    for i in range(n-1):
        nominals.append(get_next_best_nominal(nominals, m))

    return nominals


if __name__ == "__main__":
    n = int(input("Give n:"))
    m = int(input("Give m:"))
    best_combs = get_best_nom_combs(n, m)
    for comb in best_combs:
        print("{} : {}".format(comb, get_payment_score(comb, m)))
