# -*- coding: utf-8 -*-

from random import randint

def Generator():
    for i in range(numbers):
        num = randint(num_from, num_endp)
        
        text = 'BEGIN:VCARD\n'
        text += 'VERSION:2.1\n'
        text += 'N:{}{};{};;;\n'.format("Deanon", i, "Telegram")
        text += 'FN:{} {}{}\n'.format("Telegram", "Deanon", i)
        text += 'TEL;CELL:{}\n'.format(num)
        text += 'END:VCARD\n\n'

        card_file.write(text)
        text_file.write('{}\n'.format(num))
            
        print('Generated: {} of {}'.format(i, numbers) , end='\r')

if __name__ == '__main__':
    numbers = int(input('Count of number to generate: ') or 500)
    num_from = int(input('Numbers from (ex. 138000000000): ') or 138000000000)
    num_endp = int(input('Numbers to (ex. 138999999999): ') or 138999999999)

    print('\n')

    card_file = open("card.vcf", "a")
    text_file = open("nums.txt", "a")

    Generator()

    card_file.close()
    text_file.close()