from typing import List

if __name__ == '__main__':


    def characterReplacement(s: str, k: int) -> int:
        n = len(s)
        dic = {}
        left = res = 0
        for right in range(n):
            # 统计字母出现次数
            # dic.get(s[right], 0) 当dic中没有对应建，赋默认值0
            dic[s[right]] = dic.get(s[right], 0) + 1
            # 获取字典最值对应键 方法二： max(dic, key= dic.get)
            maxLetter = max(dic, key=lambda x: dic[x])
            # 将出现次数最大字母作为目标字幕，其余为待替换字母。
            # 待替换字母数大于k时，左边界右缩,原左边界字母出现次数减一，更新最大出现次数字母
            while right - left + 1 - dic[maxLetter] > k:
                dic[s[left]] -= 1
                left += 1
                maxLetter = max(dic, key=lambda x: dic[x])
            res = max(res, right - left + 1)
        return res


    s = "ABAA"
    k = 0
    print(characterReplacement(s, k))
