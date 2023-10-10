import time
import random
import tkinter as tk
from tkinter import *
import os
from pygame import mixer
from PIL import Image, ImageTk
from tkinter import font as tkfont
from tkinter import messagebox, Entry, Button


root = tk.Tk()
root.title("Wasteland - Aventura Pós-Apocalíptica")

# Função para imprimir texto com atraso
def delay_print(text, delay=0.03):
    for char in text:
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, char)
        text_widget.see(tk.END)
        text_widget.config(state=tk.DISABLED)
        root.update()
        time.sleep(delay)
    text_widget.config(state=tk.NORMAL)
    text_widget.insert(tk.END, "\n")
    text_widget.see(tk.END)
    text_widget.config(state=tk.DISABLED)
    root.update()

# Função para verificar se o jogador acertou
def is_hit_successful(success_rate=70):
    return random.randint(1, 100) <= success_rate

# Função para lidar com o jogo terminado
def game_over(message="Você perdeu! ☠️"):
    messagebox.showinfo("Game Over", message)
    play_again()

# Função para lidar com a vitória do jogador
def victory():
    messagebox.showinfo("Vitória", "Parabéns, você venceu! 🥳🥳")
    play_again()


def nao():
    delay_print("\nObrigado por jogar. Até a próxima!\n")
    root.destroy()

# Função para reiniciar o jogo
def play_again():
    delay_print("Deseja jogar novamente?")
    choice_button_1.config(text="Sim", command=start_game)
    choice_button_2.config(text="Não", command=nao)

# Função para iniciar o jogo
def start_game():
    play_sound("The_Last_Of_us_Theme_song.mp3")
    global player_name  # Variável para armazenar o nome do jogador

    delay_print("Você está num mundo pós-apocalíptico e encontra uma cabana em uma floresta.")
    time.sleep(1)
    delay_print("Você está totalmente desequipado. O que você decide fazer?")
    time.sleep(1)

    choice_button_1.config(text="1- Entrar na cabana e revistar a procura de equipamentos", command=choose_option1)
    choice_button_2.config(text="2- Decide não entrar na cabana e sair do meio da floresta", command=choose_option2)

    choice_button_1.config(state=tk.NORMAL)
    choice_button_2.config(state=tk.NORMAL)

def choose_option1():
    delay_print("Você revista toda a casa e encontra roupas quentes, uma mochila, um machado e uma pistola sem munição.")
    has_backpack = True
    has_axe = True
    has_pistol = True
    ammo_pistol.set(0)

    delay_print("\nVocê sai da cabana e encontra uma camionete perto dela.")
    choice_button_1.config(text="1- Você força a porta para abrir", command=choose_option3)
    choice_button_2.config(text="2- Você procura a chave", command=choose_option4)

def choose_option2():
    delay_print("Você anda por alguns minutos e é atacado por um zumbi e morre em poucos minutos.")
    game_over()

def choose_option3():
    delay_print("Você não consegue abrir a porta e tenta procurar a chave por perto.")
    delay_print("Você encontra a chave do carro e abre ele.")
    time.sleep(1)

    delay_print("\nVocê vaga pelo caminho e avista fumaça em uma parte da floresta.")
    choice_button_1.config(text="1- Você vai até lá ver o que é aquilo", command=choose_option5)
    choice_button_2.config(text="2- Você decide não arriscar e seguir seu caminho", command=choose_option6)

def choose_option4():
    ammo_pistol.set(ammo_pistol.get() + 10)

    delay_print("Você encontra a chave e abre a camionete. Ao vasculhar o veículo, encontra 10 munições para a sua pistola.")

    delay_print("\nVocê vaga pelo caminho e avista fumaça em uma parte da floresta.")
    choice_button_1.config(text="1- Você vai até lá ver o que é aquilo", command=choose_option5)
    choice_button_2.config(text="2- Você decide não arriscar e seguir seu caminho", command=choose_option6)

def choose_option5():
    delay_print("Você vai até lá e encontra 2 pessoas.")
    time.sleep(1)

    choice_button_1.config(text="1- Você as cumprimenta pacificamente", command=choose_option7)
    choice_button_2.config(text="2- Você as hostiliza e entra em um combate", command=be_hostile)

def choose_option6():
    delay_print("Você encontra uma horda de zumbis e não consegue enfrentar todos sozinho.")
    game_over()

def choose_option7():
    delay_print("\nVocê as cumprimenta pacificamente.")
    name_window = tk.Toplevel(root)
    name_window.title("Digite o seu nome")

    name_label = tk.Label(name_window, text="Digite o seu nome:")
    name_label.pack()

    name_entry = Entry(name_window)
    name_entry.pack()

    confirm_button = Button(name_window, text="Confirmar Nome", command=lambda: get_player_name(name_entry, name_window))
    confirm_button.pack()

def get_player_name(name_entry, name_window):
    global player_name  # Variável para armazenar o nome do jogador
    player_name = name_entry.get()
    name_window.destroy()  # Fecha a janela de entrada de nome
    delay_print(f"Você se apresenta como {player_name}.")
    choose_option8()

def choose_option8():
    delay_print("Você descansa por uma noite e fica bem alimentado. De manhã cedo, você parte.")
    time.sleep(1)
    final_game()

def be_hostile():
    delay_print("\nQual arma você escolhe?")
    
    # Criar botões para as opções do jogador
    choice_button_1.config(text="1 - Você pega a pistola", command=choose_pistol)
    choice_button_2.config(text="2 - Você pega o machado", command=choose_axe)

# Função para escolher a pistola
def choose_pistol():
    delay_print("\nVocê erra o primeiro tiro e acerta em uma barraca deles. Eles se assustam e começam a correr para se proteger.")
    time.sleep(1)
    delay_print("Tentar atirar novamente?")
    
    # Criar botões para as opções do jogador
    choice_button_1.config(text="1 - Sim", command=choose_second_shot)
    choice_button_2.config(text="2 - Não", command=choose_no_second_shot)
    

# Função para escolher o machado
def choose_axe():
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

def choose_second_shot():
    if is_hit_successful():
        delay_print("\nVocê acerta o segundo tiro em uma das pessoas e ela cai no chão.")
        time.sleep(1)
        delay_print("Você está com 8 munições restantes.")
        delay_print("Continuar com a pistola ou pegar o machado?.")
        
        # Criar botões para as opções do jogador
        choice_button_1.config(text="1 - Pegar o machado", command=choose_axe)
        choice_button_2.config(text="2 - Continuar com a pistola", command=continue_with_pistol)
        
    else:
        delay_print("Você errou o golpe e a pessoa conseguiu escapar. Eles fogem do acampamento e você não consegue encontrá-los novamente.")
        game_over()

def choose_no_second_shot():
    delay_print("Você decide não atirar novamente e elas fogem do acampamento. Você não consegue encontrá-las novamente.")
    game_over()

def continue_with_pistol():
    delay_print("\nVocê decide continuar com a pistola.")
    delay_print("Enquanto recarrega sua arma, as duas pessoas fogem e você não consegue encontrá-las novamente.")
    game_over()

def final_game():
    delay_print("Depois de sair do acampamento você pega a sua camionete e segue até uma rua bifurcada")
    delay_print("Qual rua você segue?")
    choice_button_1.config(text="1- Direita", command=choose_option15)
    choice_button_2.config(text="2- Esquerda", command=choose_option16)

def choose_option15():
    delay_print("Você segue por 50 km sem nenhum sinal de vida. Na frente, você observa 5 motos vindo em sua direção e eles sacam suas armas e atiram em seu carro.")
    time.sleep(1)
    delay_print("Você é acertado pelos tiros e acaba morrendo.")
    game_over()

def choose_option16():
    delay_print("Você segue pelo caminho a esquerda e acaba de cruzar a ponte de sua cidade, assim viajando por todo o estado.")
    time.sleep(1)
    delay_print("Finalmente, você consegue avisar as autoridades sobre a situação da cidade onde eles conseguem fazer pesquisas sobre como tudo aquilo começou, onde cientistas começam a estudar os zumbis e começar a desenvolver uma cura.")
    victory()

# Inicializa variáveis de estado do jogo
has_backpack = False
has_axe = False
has_pistol = False
ammo_pistol = tk.IntVar()
player_name = ""

# Cria uma área de texto para exibir o texto do jogo
text_widget = tk.Text(root, wrap=tk.WORD, height=15, width=60, fg="white", bg="black", font=tkfont.Font)
text_widget.config(state=tk.DISABLED)
text_widget.pack()

# Estilização
root.configure(bg="black")
font = tkfont.Font(family="Arial" , size="10" , weight="bold")
button_font = tkfont.Font(family="Arial", size=12, slant="italic")

icon = tk.PhotoImage(file='pistol.png')
root.iconphoto(True, icon)


def play_sound(audio_filename):
    try:
        mixer.init()
        audio_path = os.path.join(audio_filename)
        mixer.music.load(audio_path)
        mixer.music.play()
    except Exception as e:
        print(f"Erro ao reproduzir áudio: {str(e)}") 

# Cria botões para escolhas do jogador
choice_button_1 = tk.Button(root, text="1 - Escolher opção 1", bg="red", fg="black", font=button_font)
choice_button_2 = tk.Button(root, text="2 - Escolher opção 2", bg="red", fg="black", font=button_font)
choice_button_1.config(state=tk.DISABLED)
choice_button_2.config(state=tk.DISABLED)
choice_button_1.pack(padx=10, pady=10)
choice_button_2.pack(padx=10, pady=10)

# Inicializa o jogo
start_game()

root.mainloop()