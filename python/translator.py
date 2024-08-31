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
    def __init__(self, braille_text):
        self.braile_text = braille_text
    
    def translate_to_english(self):
        #initialize empty string to store the translated english text
        english_text = ""
        #split every six characters to get the letter using for loop
        #For each braille letter, determine english letter
        #Check for special symbols
        #Append the translated english letter to english_text
        
        return english_text
    
    #Create a class that handles english to braille
class EnglishTranslator:

    def __init__(self, english_text):
        # Initialize with the English input text
        self.english_text = english_text

    def translate_to_braille(self):
        #initialize empty string to store the translated braille text
        braille_text = ""
# Loop through each character in the English input
        # For each English character, determine the corresponding Braille character
        #Check if the character is uppercase or a number and
        #add the corresponding braille symbol
        # Append the translated Braille character to braille_text
        #output translated string into terminal
        return braille_text