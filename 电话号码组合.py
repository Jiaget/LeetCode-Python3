from typing import List

if __name__ == '__main__':
    def letterCombinations(digits: str) -> List[str]:
        dic = {'2': "abc",
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz"}
        res = []

        def backtracking(string, digits):
            if not digits:
                res.append(string)
            else:
                for letter in dic[digits[0]]:
                    backtracking(string + letter, digits[1:])

        backtracking('', digits)
        return res


    print(letterCombinations("23"))
