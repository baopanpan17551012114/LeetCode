class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        number = 0
        tmp_str = ''
        for i in range(len(s)):
            c = s[i]
            if '0' <= c <= '9':
                number = number * 10 + int(c)
                if tmp_str != '':
                    str_stack.append(tmp_str)
                    tmp_str = ''
            elif c == '[':
                if number != 0:
                    num_stack.append(number)
                    number = 0
                if tmp_str != '':
                    str_stack.append(tmp_str)
                    tmp_str = ''
                str_stack.append('[')
            elif c == ']':
                if tmp_str != '':
                    str_stack.append(tmp_str)

                tmp_str = str_stack.pop(-1)
                while str_stack:
                    ttmp_str = str_stack.pop(-1)
                    if ttmp_str == '[':
                        break
                    tmp_str = ttmp_str + tmp_str
                number = num_stack.pop(-1)
                str_stack.append(tmp_str * number)
                number = 0
                tmp_str = ''
            else:
                if number != 0:
                    num_stack.append(number)
                    number = 0
                tmp_str += c
            if i == len(s)-1 and tmp_str != '':
                str_stack.append(tmp_str)
                tmp_str = ''

        return ''.join(str_stack)


if __name__ == '__main__':
    s = "2[abc]3[cd]ef"
    res = Solution().decodeString(s)
    print(res)