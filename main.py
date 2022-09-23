#créé par Philippe Coutu
#15 septembre 2022
phrase = "mon code est original frong."


def count_words(sentence):
    nombre = len(sentence.split())
    return nombre


print("---------------------------------------------")
print("| phrase : ", phrase, "       |")
print("---------------------------------------------")
print("| nombre de mot dans la phrase : ", count_words(phrase),"|")
print("---------------------------------------------")