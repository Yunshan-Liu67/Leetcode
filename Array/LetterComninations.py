def letterCombinations(digits):
        letter = [['a','b','c'],
        ['d','e','f'],
        ['g','h','i'],
        ['j','k','l'],
        ['m','n','o'],
        ['p','q','r','s'],
        ['t','u','v'],
        ['w','x','y','z']]
        digit = ['2','3','4','5','6','7','8','9']
        mapping = dict(zip(digit,letter))
        digits_split = [i for i in digits]
        if digits_split != []:
            store = mapping[digits_split[0]]
            used_length = 1
            while used_length < len(digits_split):
                store = [i + j for i in store for j in mapping[digits_split[used_length]]]
                used_length += 1
            return store
        else:
            return []
if __name__ == "__main__":
    print(letterCombinations("2"))