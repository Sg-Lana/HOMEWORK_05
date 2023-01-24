#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Привет! абв, ауы окю, абвот"
text = text.split() 
print(text)
new_text = []
for i in range(len(text)):
    if "абв" not in text[i]:
        new_text.append(text[i])
print(new_text)


