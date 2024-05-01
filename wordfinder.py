"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, file):
        """reads text file and tells how many items read"""

        text_file = open(file)

        self.words = self.count(text_file)

        print(f"{len(self.words)} words read")

        def count(self, text_file):
            """collect all the words from text file"""
            return [word.strip() for word in text_file]
        
        def random_word(self):
            """return random word from text file"""
            
            return random.choice(self.words)
class SpecialWordFinder(WordFinder):

    def count(self, text_file):
        """returns list without blank spaces and comments"""

        return [word.strip() for word in text_file if word.strip() and not word.startswith("#")]