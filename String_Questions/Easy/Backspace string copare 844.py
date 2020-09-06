class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        s_stack = []
        i = 0
        while i < len(S):
            while i < len(S) and S[i] != '#' :
                s_stack.append(S[i])
                i += 1

            if i < len(S) and  S[i] == '#':
                if s_stack:
                    s_stack.pop()
                i += 1
        t_stack = []
        i = 0
        while i < len(T):
            while i < len(T) and T[i] != '#':
                t_stack.append(T[i])
                i += 1

            if i < len(T) and T[i] == '#':
                if t_stack:
                    t_stack.pop()
                i += 1
        print(t_stack)
        return ''.join(s_stack) == ''.join(t_stack)

S = "ab#c"
T = "ad#c"
# S = "ab##"
# T = "c#d#"
S = "a#c"
T = "b"
S = "a##c"
T = "#a#c"
print(Solution().backspaceCompare(S, T))