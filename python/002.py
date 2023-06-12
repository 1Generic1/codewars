""" Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway ! 

sample test

test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay') """
def pig_it(text):
    result = []
    aystr ="ay"
    #first we convert the string to list 
    new_list = text.split()
    
    #we iterate using a for loop to remove the first character of each word and concantenate
    for word in new_list:
    #check if the word contains only alphabetic characters
        if word.isalpha():
            if len(word) > 1:
            #here we use string slicing to start from the index 1 and concantenate to index 0
                sliced_list = word[1:] + word[0] + aystr

            else:
                sliced_list = word + aystr
            result.append(sliced_list)
        else:
            result.append(word) #Append the word as it is if it contains non-alphabetic characters
    #we convert the list back to string
    str_result = " ".join(result)
    return (str_result)

