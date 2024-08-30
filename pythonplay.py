from emoji import emojize
import wikipedia
import random
page_title = '3069677'
monkey = wikipedia.page(pageid = page_title)
monkey_article_words = [i for i in monkey.content.split()]

monkeylist = ['ape', 'apes', 'monkey', 'monkeys', 'gorilla', 'orangutan', 'chimpanzee', 'baboon', 'gorillas', 'orangutans', 'chimpanzees', 'chimps', 'chimp', 'baboons']
monkey_emojis = [
    ":monkey_face:",  # 🐵
    ":monkey:",       # 🐒
    ":see_no_evil:",  # 🙈
    ":hear_no_evil:", # 🙉
    ":speak_no_evil:",# 🙊
    ":gorilla:",      # 🦍
    ":orangutan:"     # 🦧
]
# print(monkey.content, monkey.url)

for i in monkey_article_words:
    if i.lower() in monkeylist:
        print(emojize(monkey_emojis[random.randint(0, len(monkey_emojis)-1)]), end = " ")
    else:
        print(i, end = " ")