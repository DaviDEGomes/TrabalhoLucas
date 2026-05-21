from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pandas as pd

def carregar_filmes ():
    return  pd.read_excel(
         r"trabalho\data\filmes.xlsx",
        sheet_name="Filmes", 
        skiprows=1 
)

def mostrar_filmes():
    df = carregar_filmes()

    texto_filmes.delete(1.0, END)
    texto_filmes.insert(END, df.to_string())
 
def limpar_texto():
    texto_filmes.delete(1.0, END)
    texto_busca.delete(0,END)

janela = Tk()

janela.configure(bg="#0F0518")
janela.title ("FILMES NEXUS")
janela.geometry("1080x720")

titulo = Label(janela, text= "Filmes Nexus IA", font=("Segoe UI",30, "bold"),fg="white", bg= "#0F0518")
titulo.pack(pady=10)

painel = Frame (janela, bg = "#281446",  bd=2, padx=10,pady=10)
painel.pack(pady=20)

text_chat = Label(painel, text="Chat",font=("Segoe UI",15, "bold"),bg="#281446",fg="white")
text_chat.pack(pady=(0,10))

texto_filmes = ScrolledText(painel, width=80, height=20, bg="#3C1E64",fg="white",  insertbackground="white",relief="flat")
texto_filmes.pack(pady=10)

text_bsc = Label(painel, text="Digite sua busca abaixo.",font=("Segoe UI",15, "bold"),bg="#281446", fg="white")
text_bsc.pack(pady=5)

texto_busca = Entry(painel,width=50,bg="#502882",font=("Segoe UI",10, "bold"),fg="white",insertbackground="white",relief="flat")
texto_busca.pack(fill=X, ipadx=10,pady=10)

btn_buscar = Button(painel,text="Buscar",command=mostrar_filmes,bg="#783CC8",fg="white",relief="flat", width=15,height=2,cursor="hand2")
btn_buscar.pack(side=LEFT, expand=TRUE,fill=X,padx=5)

btn_limpar = Button(painel,text="Limpar",command=limpar_texto, bg="#783CC8",fg="white",relief="flat", width=15,height=2, cursor="hand2")
btn_limpar.pack(side=LEFT, expand=TRUE, fill=X,padx=5)

janela.mainloop()
