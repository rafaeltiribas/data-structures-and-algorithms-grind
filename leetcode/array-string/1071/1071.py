class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        
        a = len(str1)
        b = len(str2)

        while b != 0:
            resto = a % b
            a = b
            b = resto
        mdc = a

        for i in range(0, len(str1), mdc):
            if str1[i:i+mdc] != str2 [0:mdc]:
                return ""
            if i+mdc-1 < len(str2) and str2[i:i+mdc] != str1[0:mdc]:
                return ""
        
        return str1[:mdc]
