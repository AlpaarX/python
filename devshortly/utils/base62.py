import string
# Remove the `_@` below for base62, now it has 64 characters
# For Python 2 use `string.letters` instead of `string.ascii_letters
BASE_LIST = string.digits + string.ascii_letters + '_@'
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def base_decode(string, reverse_base=BASE_DICT):
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(string[::-1]):
        ret += (length ** i) * reverse_base[c]

    return ret

def base_encode(integer, base=BASE_LIST):
    if integer == 0:
        return base[0]

    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        # For Python 2 use /= instead of //=:
        # integer /= length
        integer //= length

    return ret