def sentanceMaker(phrase):
    interrogatives = ("how","what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)  
    else:
         return "{}.".format(capitalized) 

print(sentanceMaker("what the heck"))
print(sentanceMaker("it's a good day"))

sentancelist = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        sentancelist.append(sentanceMaker(user_input))

print(" ".join(sentancelist))