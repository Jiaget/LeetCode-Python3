if __name__ == '__main__':
    # 递归是一步一步寻找上一个状态，只要知道第一个状态或者前几个状态，即可一步一步推导最终状态
    def countAndSay(n: int) -> str:
        if n == 1:
            return '1'
        remain = countAndSay(n - 1)
        left = 0
        res = ''
        for right in range(len(remain)):
            if remain[left] != remain[right]:
                res = res + str(right - left) + remain[left]
                left = right
        res += str(len(remain) - left) + remain[left]
        return res

    print(countAndSay(5))