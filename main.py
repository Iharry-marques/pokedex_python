from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# cores

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

# criando janelas
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

# Nome
pok_nome = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

# Categoria
pok_tipo = Label(frame_pokemon, text='Eletrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

# ID
pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

# Imagem do pokemon
imagem_pokemon = Image.open('images/pikachu.png')
imagem_pokemon = imagem_pokemon.resize((238,238))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=co1, fg=co0)
pok_imagem.place(x=60, y=50)

pok_tipo.lift()

# Status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

# HP
pok_hp = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

# ATAQUE
pok_atack = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15, y=385)

# DEFESA
pok_defesa = Label(janela, text='Defesa', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

# VELOCIDADE
pok_velocidade = Label(janela, text='Velocidade', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

# TOTAL
pok_total = Label(janela, text='Total', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)

# HABILIDADES
pok_habilidade = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidade.place(x=180, y=310)

pok_hb1 = Label(janela, text='Choque do Trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb1.place(x=195, y=360)

pok_hb2 = Label(janela, text='Ataque Rapido', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb2.place(x=195, y=385)

# Criando Botões





janela.mainloop()

