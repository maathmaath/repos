import copy

# outputs new string which has no same adj letter, else abort with upto newstring.

# var = "aaabbc"
# var = "aaab"
var = ["aaabbc", "aaab", "aaab", "asbjdfhwgfjfjafwf",
       "lskadlskdadksadkaksddskdadsdk", "klsklklklklklklllalslslalllll"]


def get_str(dict_):
    # Keymax = max(Tv, key= lambda x: Tv[x])
    keymax = max(zip(dict_.values(), dict_.keys()))[1]
    return keymax


def check(newstr, keymax, dict_):
    dict_copy = copy.deepcopy(dict_)
    del dict_copy[keymax]
    if dict_copy:
        keymax = get_str(dict_copy)
        return 1, dict_, keymax
    else:
        return 0, None, None


def loop(dict_, index):
    newstr = ''
    while True:
        if not dict_:
            print(f"[A{index}] String incorporated- {newstr}.")
            break
        keymax = get_str(dict_)
        if newstr:
            if newstr[-1] == keymax:
                bool, dict_, keymax = check(newstr, keymax, dict_)
                if not bool:
                    print(f"[*] Formed upto {newstr}.")
                    print(
                        "[*] string incorporation not possible, formation Aborted.")
                    break
        dict_[keymax] -= 1
        if dict_[keymax] == 0:
            del dict_[keymax]
        newstr += keymax


def iter_list(list_):
    for index, strg in enumerate(list_):
        dict_ = {}
        for i in strg:
            if i in dict_.keys():
                dict_[i] += 1
            else:
                dict_[i] = 1
        print(f"[Q{index+1}] Input string- {strg}.")
        loop(dict_, index+1)
        print("\n")


def main(var):
    if type(var) == list:
        iter_list(var)
    else:
        loop(var)


if __name__ == '__main__':
    main(var)
