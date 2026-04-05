class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = re.findall('[a-zA-Z0-9]', s.lower())
        reverse = newString[::-1]
        for i in range (len(newString)):
            if newString[i] != reverse[i]:
                return False
        return True
        
       

