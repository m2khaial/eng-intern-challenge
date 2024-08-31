#Create a translator class to handle the input language
# and the language to translate to
class Translator:
    def __init__(self, input_text):
        #Initialize input text
        self.input_text = input_text
        self.translated_text = ""
#Determine if string is in english or braille 
    def determine_language(self):
        if set(self.input_text).issubset({'O', '.'}):
            return 'braille'
        else:
            return 'english'
    
    def translate(self):
        input_language = self.determine_language()
        # Translate the input text accordingly
        if input_language == 'braille':
             # If the input is Braille, create a BrailleTranslator object
            braille_translator = BrailleTranslator(self.input_text)
            self.translated_text = braille_translator.to_english()
        elif input_language == 'english':
            # If the input is English, create a EnglishTranslator object
            english_translator = EnglishTranslator(self.input_text)
            # Use the object to translate to Braille
            self.translated_text = english_translator.to_braille()
        return self.translated_text

    #Create a class that handles braille to english
class BrailleTranslator:
    BRAILLE_TO_ENGLISH = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
        "O..OOO": "z",
        ".O.OOO": "0", ".OOO..": "1", ".OOO.O": "2", ".OOOO.": "3", ".OOOOO": "4",
        ".O.OO.": "5", "OOO.OO": "6", "OOOOOO": "7", "O.OOOO": "8", "OOO...": "9",
        "......": " ",  # Space
        ".....O": "CAPITAL",  # Capital follows
        ".O.O.O": "NUM"       # Number follows
    }

    def __init__(self, braille_text):
        self.braille_text = braille_text

    def translate_to_english(self):
        english_text = ""
        is_capital = False
        is_number = False
        
        for i in range(0, len(self.braille_text), 6):
            braille_char = self.braille_text[i:i+6]
            english_char = self.BRAILLE_TO_ENGLISH.get(braille_char, "")
            
            if english_char == "CAPITAL":
                is_capital = True
                continue
            elif english_char == "NUM":
                is_number = True
                continue

            if is_capital:
                english_char = english_char.upper()
                is_capital = False

            if is_number:
                is_number = False

            english_text += english_char
            
        return english_text
  
    #Create a class that handles english to braille
class EnglishTranslator:
    # Mapping from English to Braille
    ENGLISH_TO_BRAILLE = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
        "z": "O..OOO",
        "0": ".O.OOO", "1": ".OOO..", "2": ".OOO.O", "3": ".OOOO.", "4": ".OOOOO",
        "5": ".O.OO.", "6": "OOO.OO", "7": "OOOOOO", "8": "O.OOOO", "9": "OOO...",
        " ": "......",  # Space
        "CAPITAL": ".....O",  # Capital follows
        "NUM": ".O.O.O"       # Number follows
    }
    def __init__(self, english_text):
        # Initialize with the English input text
        self.english_text = english_text

    def translate_to_braille(self):
        #Initialize variables
        braille_text = ""
        is_number = False
# Loop through each character in the English input
        for char in self.english_text:
        # For each English character, determine the corresponding Braille character
            if char.isdigit():
                if not is_number:
                    braille_text += self.ENGLISH_TO_BRAILLE["NUM"]
                    is_number = True
                braille_char = self.ENGLISH_TO_BRAILLE[char]
                #Check if the character is uppercase or a number and
        #add the corresponding braille symbol
            elif char.isupper():
                braille_text += self.ENGLISH_TO_BRAILLE["CAPITAL"]
                braille_char = self.ENGLISH_TO_BRAILLE[char.lower()]
                is_number = False  # Reset number flag
            else:
                braille_char = self.ENGLISH_TO_BRAILLE[char]
                is_number = False  # Reset number flag
        # Append the translated Braille character to braille_text
            braille_text += braille_char
        #output translated string into terminal
        return braille_text