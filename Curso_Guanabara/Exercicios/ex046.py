from time import sleep
import emoji

for contagem in range(10, -1, -1):
    sleep(1)
    print(contagem)
print(emoji.emojize('BUUUUUUUUUUUUU :boom:', use_aliases=True))