"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()
word_definitions['reuse'] = 'use again or more than once'
word_definitions['cost'] = 'an amount that has to be paid or spent to buy or obtain something'
word_definitions['communication'] = 'the imparting or exchanging of information or news'


"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
# print(word_definitions['reuse'])
# print(word_definitions['cost'])



"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for word in word_definitions:
    definition = word_definitions[word]
    print(f"The definition of {word} is {definition} \n")
    
    
    