#only in english

import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Seja bem-vindo a Ilha do Tesouro.")
print("Sua missão, se você aceitar, é achar o tesouro.\n")

accept = input("Você aceita? Y ou N.\n> ").lower()

if accept == "y":
  entrada = input("\nVocê está entrando na mata, por qual lado deseja ir? ESQUERDA ou DIREITA\n> ").lower()
  if entrada != "direita":
    print("\nPor ai não tem nada, você foi pela direita.\n")
    print("Continuando...")
    time.sleep(2)
  if 0 == 0:
    print('''\n



                  _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'
 ___.'       '.       /               '-._
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-'

 ''')
    fugir = input("\nVocê encontrou um lago sombrio e nebuloso, parece haver alguem a frente, você suspeita... Deseja esperar esta pessoa, ou fugir?\n> ")
    if fugir == "fugir":
      print("")
      insultar = input("\nVocê foge, e então encontra 4 magos, 1 cego, 1 mudo, 1 surdo e o outro é cotoco. Você deseja insultar eles? Y ou N\n> ").lower()
      if insultar == "y":
        print('''
              _,._
  .||,       /_ _\\
 \.`',/      |'L'| |
 = ,. =      | - | L
 / || \    ,-'\"/,'`.
   ||     ,'   `,,. `.
   ,|____,' , ,;' \| |
  (3|\    _/|/'   _| |
   ||/,-''  | >-'' _,\\
   ||'      ==\ ,-'  ,'
   ||       |  V \ ,|
   ||       |    |` |
   ||       |    |   \
   ||       |    \    \
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/
   ||                ''')
        input("\nVocê insulta eles, eles se juntam e se transformam num só mago (de patins). Deseja implorar por perdâo?\n> ")
        print("\nVocê morreu.")
      else:
          print('''
              _,._
  .||,       /_ _\\
 \.`',/      |'L'| |
 = ,. =      | - | L
 / || \    ,-'\"/,'`.
   ||     ,'   `,,. `.
   ,|____,' , ,;' \| |
  (3|\    _/|/'   _| |
   ||/,-''  | >-'' _,\\
   ||'      ==\ ,-'  ,'
   ||       |  V \ ,|
   ||       |    |` |
   ||       |    |   \
   ||       |    \    \
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/
   ||                ''')
          input("\nSeu espirito preconceituoso faz com que você insulte-os do mesmo jeito. Eles se juntam e se transformam num só mago (de patinete). Deseja implorar por perdâo?\n> ")
          print("Você morreu.")
    else:
        print("\nVocê espera, e então descobre que era o Kratos e o GAROTO. Eles estão procurando pelo mesmo tesouro que você. Você descobre que, na verdade, o tesouro está em outra ilha, vocês decidem se ajudar e seguir para a Temível Ilha Fortnite.\n")
        mata = input("\nChegando lá você encontra uma criança. Deseja mata-la, ou seguir seu caminho?\n> ")
        if mata != "matar" or mata != "mata" or mata != "mata-la":
          print("\nEla te mata pelas costas. Kratos e o GAROTO acham o tesouro e vão embora.\n")
          print("FIM DE JOGO!")
        else:
          print("\nEla te mata primeiro. Kratos e o GAROTO, acham o tesouro e vão embora.\n")
          print("FIM DE JOGO!")
else:
  print("\nComo qualquer outro desertor, Irá morrer enforcado!")
  print("Você morreu.")
