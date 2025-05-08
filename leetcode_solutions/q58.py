"""
58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, sentence: str) -> int:
        """Returns the length of the final word in an input string, where a word is defined as a maximal substring containing no spaces.
            Uses Python built in string methods.
        Args:
            sentence (str): input string

        Returns:
            int: Length of final word in string.
        """

        sentence = sentence.rstrip()                #remove trailing whitespace
        sentence = sentence.split()                 #Split the string into a list of words

        return len(sentence[-1])

    # def solution_2(self, sentence: str) -> int:
        
    #     i = len(sentence) -1

    #     while i >= 0 and sentence[i] == ' ':
    #         i -= 1                              #Skipping any trailing whitespace
        
    #     length = 0
    #     while i >= 0 and sentence[i] != ' ':    #Counting the letters in the word
    #         length += 1
    #     return length

    """ Solution 2 seems to break pytest? come back"""
