# 也许编程编的是逻辑思维能力和逻辑思考
# 思路顺畅了 编程又有什么难得
# 练习性的项目，永远记不住
# 练手神经网络可能更适合我 用的多 敲把 别内耗了
# 32个保留关键字和四则运算
# 敲李航 李沐那两本书
import random

def update_clue(gueessed_letter,secret_word,clue):
    index=0
    while index<len(secret_word):
        if gueessed_letter == secret_word[index]:
            clue[index]=gueessed_letter
        index = index+1

lives=3

words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
print("待选词列表：",words)
secret_word = random.choice(words)

print(secret_word)

clue = list("?????")
print(clue)
heart_symbol = u'\u2764'
print(heart_symbol)

guessed_word_correctly = False


while lives>0:
    print(clue)
    print('剩余生命次数：'+ heart_symbol * lives)
    guess = input('猜测字母或是整个单词：\n')

    if guess == secret_word:
        guessed_word_correctly = True
        break
    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print("错误。你丢了一条性命\n")
        lives = lives-1

if guessed_word_correctly:
    print('你赢了，秘密单词是'+ secret_word)
else:
    print('你输了，秘密单词是'+secret_word)