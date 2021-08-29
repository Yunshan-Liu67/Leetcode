def romanToInt(s: str) -> int:
    i = 0
    Result = 0
    Roman_convert = dict({'I': 1, 'V': 5, 'X' : 10 , 'L': 50, 'C': 100, 'D': 500, 'M': 1000})
    Roman_split = [char for char in s]
    if Roman_split[0] == 'I' and Roman_split[-1] == 'V':
        Result = len(Roman_split) - 6
    else:
        while i < len(Roman_split):
            Result += Roman_convert[Roman_split[i]]
            i += 1
    return Result
            
if __name__ == "__main__":
    romanToInt('III')