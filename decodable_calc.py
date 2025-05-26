

import time, os
wait = time.sleep
def load(text):
    print(text)
    wait(0.07)

print('''PDC - Passage Decodability Calculator
Coding done by Samuel B.''')
wait(1)
print('''
***IMPORTENT NOTES***

Do not use CMD+C and CMD+V!!! CMD+C is a stop code.

***END IMPORTANT NOTES***

------------------------------------------------------------
''')
print("Loading Words...")
non_decodable_words = ("ball", "cat", "apple")
wait(2)
input_passage = input("Please Paste Passage Here:\n")

newstring0 = input_passage.replace(".", "")
newstring1 = newstring0.replace(",", "")
newstring2 = newstring1.replace("!", "")
cleaned_passage = newstring2.replace("?", "")

OUT = 0
IN = 1
def countWords(string):
    state = OUT
    wc = 0
    for i in range(len(string)):

        if (string[i] == ' ' or string[i] == '\n' or
            string[i] == '\t'):
            state = OUT

        elif state == OUT:
            state = IN
            wc += 1
    return wc


split_passage = list(cleaned_passage.split(" "))


decodeable = [i for i in split_passage if i not in non_decodable_words]


total_words = countWords(cleaned_passage)



x_decodable = total_words - len(decodeable)
decodable = (total_words - x_decodable)
prec_non_decodeable = (decodable / total_words)*100


prec_decodeable = prec_non_decodeable
print('''------------------------------------------------------------

Your Passage is:''')
print(round(prec_decodeable,1 ),"% Decodable")


#Thx to Geeks for Geeks and W3schools for Code Snippets
# Write your code here :-)
