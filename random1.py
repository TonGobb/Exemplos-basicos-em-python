import random
num = int(input('O computador pensou em um numero entre 1 e 10, você é capaz de advinhar?'))
sorteio = random.randint(1, 11)

if num == sorteio:
    print('Parabens, o numero pensando pelo computador foi {}, o mesmo do seu!!!'.format(sorteio))
else:
    print('Que pena, você errou!!')
