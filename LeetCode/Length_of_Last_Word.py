"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # The regex approach: ~96ms runtime, 11.9MB memory
        
        #regex = re.compile(r"(\w*)\Z")
        #match = re.search(regex,s.strip())
        #return len(match.group()) if match else len(strip(s))
        
        # The iterative approach: ~20ms runtime, 12MB memory
        
        #s = s.strip() # Get rid of trailing and preceding whitespace
        #s = s[::-1] # Reverse the string
        
        #counter = 0
        #for char in s:
        #    if char == " ":
        #        break
        #    counter += 1
        #return counter
        
        # The Pythonic approach: ~16ms, 12.9MB memory
        
        s = s.strip()
        if s:
            return len(s.split()[-1])
        else:
            return 0