# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'Штирлиц самозабвевнно любовался горяшим штабом абвера'
new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)

