import random
import argparse
import textwrap
cur_pass = ''
symbols10 = ('0','1','2','3','4','5','6','7','8','9')
symbols52 = ('Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M','A','S','D','F','G','H','J','K','L'
             ,'z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p')
symbols62 = symbols52 + symbols10
symbols70 = symbols62 + ('!','@','#','$','%','*','-','+')
symbols80 = symbols70 + ('&','_','|','?','~','[',']','(',')','.')
symbols94 = symbols80 + (',', '/', '\\', '`', '"', '<', '>', '=', '^', ':', '\'', ';', '{', '}')
parser = argparse.ArgumentParser(
    description='Random Password Generator мать его ети',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''Example: 
        genpass.py -n 10 -l 20 -s 80 # сгeнeрировать 10 паролей по 20 символов алфавит 80 печатаемых символов
        genpass.py без параметров сгенерирует 16 паролей по 24 символа из алфавита 62 печатаемых символа
        Ограничения на параметры: -n < 128, -l < 64, -s [0-5]
    '''))
parser.add_argument('-n', '--number', type=int, default=16, help='passwords number')
parser.add_argument('-l', '--length', type=int, default=24, help='password length')
parser.add_argument('-s', '--symbols', type=int, default=3, help='set of symbols: 0-digits, 1-52 symbosl,2-62 symbols,3-70 symbols,4-80 symbols, 5-94 symbols')
args = parser.parse_args()
if args.length > 63:
    args.length = 32
if args.number > 127:
    args.number = 32
if args.symbols == 0:
    symbols = symbols10
elif args.symbols == 1:
    symbols = symbols52
elif args.symbols == 2:
    symbols = symbols62
elif args.symbols == 3:
    symbols = symbols70
elif args.symbols == 4:
    symbols = symbols80
elif args.symbols == 5:
    symbols = symbols94
else:
    symbols = symbols62


for i in range(1,args.number):
    for j in range(1,args.length):
#        ptr = int((random(len(symbols))+random(len(symbols))+random(len(symbols))) % len(symbols))
        ptr = random.choice(symbols)
        cur_pass = cur_pass + ptr
    print(str(cur_pass))
    cur_pass = ''
