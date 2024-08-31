#Get input string from the test file
#Determine if string is in english or braille (will 
# determine if you need which translator to use)
    #Create a translator class to handle the input language
    #  and the language to translate to
class Translator:
    def __init__(self, input_text):
        #Initialize input text
        self.input_text = input_text
        self.translated_text = ""
#Determine if string is in english or braille (will 
    def determine_language(self):
        if set(self.input_text).issubset({'O', '.'}):
            return 'braille'
        else:
            return 'english'
    
    def translate(self):
        input_language = self.determine_language()

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
#Covert to either english or braille based on the input 
# language
    #Create a class that handles braille to english
class BrailleTranslator:

    #split every sixc characters to get the letter
    #Create a class that handles english to braille
class EnglishTranslator:
#output translated string into terminal
