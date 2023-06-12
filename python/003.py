""" Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized. In python """

def to_camel_case(text):
    # Replace dashes with underscores and split the string into a list of words
    words = text.replace('-', '_').split('_')
    camel_case = words[0]
    for word in words[1:]:
        # Capitalize each word and append it to camel_case
        camel_case += word.title()
        return (camel_case)

print (to_camel_case("hello-world"))
