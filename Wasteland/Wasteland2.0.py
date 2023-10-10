import time
import random

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def is_hit_successful():
    return random.randint(1, 100) <= 70


def be_hostile():
    delay_print("\nQual arma você escolhe?")
    delay_print("1 - Você pega a pistola")
    delay_print("2 - Você pega o machado")
    
    choice = input("Digite o número da sua escolha: ")
    
    if choice == "1":
        delay_print("\nVocê erra o primeiro tiro e acerta em uma barraca deles. Eles se assustam e começam a correr para se proteger.")
        time.sleep(1)
        delay_print("Tentar atirar novamente?")
        delay_print("\n1 - Sim")
        delay_print("2 - Não")
        choice = input("Digite o número da sua escolha: ")
        
        if choice == "1":
            if is_hit_successful():
                delay_print("\nVocê acerta o segundo tiro em uma das pessoas e ela cai no chão.")
                time.sleep(1)
                delay_print("Você está com 8 munições restantes.")
                delay_print("Continuar com a pistola ou pegar o machado?.")
                delay_print("1 - Pegar o machado")
                delay_print("2 - Continuar com a pistola")
                choice = input("Digite o número da sua escolha: ")
                
                if choice == "1":
                    delay_print("\nVocê pega o machado e entra em um combate corpo a corpo.")
                    if is_hit_successful():
                        delay_print("Você corre em direção à pessoa da frente e dá 2 golpes rápidos, acertando apenas um deles na barraca dela e fazendo um corte profundo.")
                        delay_print("A pessoa cai no chão e agoniza de dor.")
                        time.sleep(2)
                        if is_hit_successful():
                            delay_print("Você vai em direção à segunda pessoa e acaba levando um soco no rosto sem esperar.")
                            delay_print("Você cai no chão, mas consegue se levantar e começa a lutar no soco com ela.")
                            delay_print("Você consegue vencer a luta e as duas pessoas ficam imobilizadas.")
                            delay_print("Você revista o acampamento e encontra alguns itens:")
                            delay_print("- Botas")
                            delay_print("- Munição para sua pistola (30 balas)")
                            delay_print("- Cantil com água")
                            delay_print("- Algumas latas de comidas")
                            delay_print("- Saco de dormir")
                            delay_print("Você passa a noite no acampamento e parte logo de manhã com a sua camionete.")
                            final_game()
                        else:
                            game_over("Você errou o golpe e a pessoa conseguiu escapar. Eles fogem do acampamento e você não consegue encontrá-los novamente.")
                    else:
                        game_over("Você errou o golpe e não acertou a pessoa. Eles fogem do acampamento e você não consegue encontrá-los novamente.")
                elif choice == "2":
                    delay_print("\nVocê decide continuar com a pistola.")
                    delay_print("Enquanto recarrega sua arma, as duas pessoas fogem e você não consegue encontrá-las novamente.")
                    game_over()
                    
        elif choice == "2":
            delay_print("\nVocê decide não atirar novamente e elas fogem do acampamento. Você não consegue encontrá-las novamente.")
            game_over()
    elif choice == "2":
        delay_print("\nVocê decide não atirar e pega o machado para entrar em um combate corpo a corpo.")
        if is_hit_successful():
            delay_print("Você corre em direção à pessoa da frente e dá 2 golpes rápidos, acertando apenas um deles na barraca dela e fazendo um corte profundo.")
            delay_print("A pessoa cai no chão e agoniza de dor.")
            time.sleep(1)
            if is_hit_successful():
                delay_print("Você vai em direção à segunda pessoa e acaba levando um soco no rosto sem esperar.")
                delay_print("Você cai no chão, mas consegue se levantar e começa a lutar no soco com ela.")
                delay_print("Você consegue vencer a luta e as duas pessoas ficam imobilizadas.")
                delay_print("Você revista o acampamento e encontra alguns itens:")
                delay_print("- Botas")
                delay_print("- Munição para sua pistola (30 balas)")
                delay_print("- Cantil com água")
                delay_print("- Algumas latas de comidas")
                delay_print("- Saco de dormir")
                delay_print("Você passa a noite no acampamento e parte logo de manhã com a sua camionete.")
                final_game()


def final_game():
    while True:
        delay_print("Depois de sair do acampamento você pega a sua camionte e segue ate uma rua bifurcada")
        delay_print("Qual rua você segue?")
        choice = input("1- Direita\n2- Esquerda\nEscolha sua opção: ").strip()

        if choice == '1':
            delay_print("Você segue por 50 km sem nenhum sinal de vida. Na frente, você observa 5 motos vindo em sua direção e eles sacam suas armas e atiram em seu carro.")
            time.sleep(1)
            delay_print("Você é acertado pelos tiros e acaba morrendo.")
            game_over()
        elif choice == '2':
            delay_print("Você segue pelo caminho a esquerda e acaba de cruzar a ponte de sua cidade, assim viajando por todo o estado.")
            time.sleep(1)
            delay_print("Finalmente, você consegue avisar as autoridades sobre a situação da cidade onde eles conseguem fazer pesquisas sobre como tudo aquilo começou, onde cientistas começam a estudar os zumbis e começar a desenvolver uma cura.")
            victory()
        else:
            delay_print("Opção inválida. Escolha novamente.")

def game_over():
    delay_print("\nGame Over ☠️\n")
    play_again()

def victory():
    delay_print("\nVocê venceu! 🥳🥳\n")
    play_again()

def play_again():
    choice = input("Deseja tentar novamente? [Sim/Não]: ").strip().lower()
    if choice == 'sim':
        start_game()
    else:
        delay_print("\nObrigado por jogar. Até a próxima!\n")

def start_game():
    delay_print("Wasteland - Aventura pós-apocalíptica\n")
    time.sleep(1)

    delay_print("Você está num mundo pós-apocalíptico e encontra uma cabana em uma floresta.")
    time.sleep(1)
    delay_print("Você está totalmente desequipado. O que você decide fazer?")
    time.sleep(1)

    while True:
        choice = input("1- Entrar na cabana e revistar a procura de equipamentos\n2- Decide não entrar na cabana e sair do meio da floresta\nEscolha sua opção: ").strip()

        if choice == '1':
            delay_print("Você revista toda a casa e encontra roupas quentes, uma mochila, um machado e uma pistola sem munição.")
            has_backpack = True
            has_axe = True
            has_pistol = True
            ammo_pistol = 0
            break
        elif choice == '2':
            delay_print("Você anda por alguns minutos e é atacado por um zumbi e morre em poucos minutos.")
            game_over()
        else:
            delay_print("Opção inválida. Escolha novamente.")

    delay_print("\nVocê sai da cabana e encontra uma camionete perto dela.")
    while True:
        choice = input("1- Você força a porta para abrir\n2- Você procura a chave\nEscolha sua opção: ").strip()

        if choice == '1':
            delay_print("Você não consegue abrir a porta e tenta procurar a chave por perto.")
            time.sleep(1)
        elif choice == '2':
            delay_print("Você encontra a chave e abre a camionete. Ao vasculhar o veículo, encontra 10 munições para a sua pistola.")
            ammo_pistol += 10
            break
        else:
            delay_print("Opção inválida. Escolha novamente.")

    delay_print("\nVocê vaga pelo caminho e avista fumaça em uma parte da floresta.")
    while True:
        choice = input("1- Você vai até lá ver o que é aquilo\n2- Você decide não arriscar e seguir seu caminho\nEscolha sua opção: ").strip()

        if choice == '1':
            delay_print("Você vai até lá e encontra 2 pessoas.")
            time.sleep(1)
            break
        elif choice == '2':
            delay_print("Você encontra uma horda de zumbis e não consegue enfrentar todos sozinho.")
            game_over()
        else:
            delay_print("Opção inválida. Escolha novamente.")

    while True:
        choice = input("1- Você as cumprimeta pacificamente\n2- Você as hostiliza e entra em um combate\nEscolha sua opção: ")

        if choice == '1':
            delay_print("\nVocê as cumprimenta pacificamente.")
            name = input("Elas perguntam o seu nome: ")
            delay_print("Você fala o nome e elas se apresentam para você como Antônio e Matheus, pai e filho respectivamente.")
            while True:
                choice = input("Elas te oferecem comida e abrigo por uma noite, deseja aceitar? [Sim/Não]: ").strip().lower()
                if choice == 'sim':
                    delay_print("Você descansa por uma noite e fica bem alimentado. De manhã cedo, você parte.")
                    time.sleep(1)
                    final_game()
                elif choice == 'não':
                    delay_print("Você volta para o carro e depois de poucos minutos é atacado por uma horda de zumbis.")
                    game_over()
                break
            break
        elif choice == '2':
            be_hostile()

if __name__ == "__main__":
    start_game()