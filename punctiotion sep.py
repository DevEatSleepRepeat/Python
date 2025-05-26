
input_txt= "The lazy. FoX,,, was lazy...."

newstring0 = input_txt.replace(".", "")
newstring1 = newstring0.replace(",", "")
newstring2 = newstring1.replace("!", "")
newstring3 = newstring2.replace("?", "")

print(newstring3)
