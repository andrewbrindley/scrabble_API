def partial_permutations(arr, n):

    out = []
    def _permutations(cur, _arr):
        if len(cur) == n: return out.append(cur)
        for i in range(len(_arr)):
            rest = _arr[:i] + _arr[i+1:]
            _permutations([*cur, _arr[i]], rest)
    _permutations([], arr)
    return out


res = partial_permutations([0, 1, 2], 2)
print(res)