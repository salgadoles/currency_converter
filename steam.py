# janela -> 500x500
#titulo - conversor de moedas
# campos de selecionar moedas de origem e destino (campos de listas)
#botao de converter
#lista de exibcao com os nomes das moedas

import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela = customtkinter.CTk()
janela.geometry("500x500")

#criar os botoes, textos e outros elementos
titulo = customtkinter.CTkLabel(janela)

textoMoedaOrigem = customtkinter.CTkLabel(janela)
# colocar todos os elementos na tela

# rodar a janela
janela.mainloop()