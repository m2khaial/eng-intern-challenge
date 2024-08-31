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

#Covert to either english or braille based on the input 
# language
    #Create a class that handles braille to english
    #split every sixc characters to get the letter
    #Create a class that handles english to braille
#output translated string into terminal
