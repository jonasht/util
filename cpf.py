from validate_docbr import CPF
import sys


try:
    qtd = int(sys.argv[1])
except:
    qtd = 5

def l(qtd:int=18, sth:str='_') -> None:
    print(sth*qtd)

l()
for i in range(qtd):
    print('|',CPF().generate(mask=True), '|')


l(sth='-')
