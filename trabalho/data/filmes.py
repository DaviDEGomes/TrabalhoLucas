from tkinter import *
from tkinter.scrolledtext import ScrolledText
from collections import deque
import heapq
#lista de todos os filmes e suas categorias
filmes = {
    "Matrix": {"generos":["acao","ficcao"],"diretor":"wachowski","ano":1999,"oscar":True},
    "Matrix Reloaded": {"generos":["acao","ficcao"],"diretor":"wachowski","ano":2003,"oscar":False},
    "Matrix Revolutions": {"generos":["acao","ficcao"],"diretor":"wachowski","ano":2003,"oscar":False},
    "Interestelar": {"generos":["ficcao","drama"],"diretor":"nolan","ano":2014,"oscar":True},
    "Batman O Cavaleiro das Trevas": {"generos":["acao","crime"],"diretor":"nolan","ano":2008,"oscar":True},
    "Tenet": {"generos":["ficcao","acao"],"diretor":"nolan","ano":2020,"oscar":True},
    "A Origem": {"generos":["ficcao","acao"],"diretor":"nolan","ano":2010,"oscar":True},
    "Duna": {"generos":["ficcao","aventura"],"diretor":"villeneuve","ano":2021,"oscar":True},
    "Blade Runner 2049": {"generos":["ficcao"],"diretor":"villeneuve","ano":2017,"oscar":True},
    "Gravidade": {"generos":["ficcao","espaco"],"diretor":"cuaron","ano":2013,"oscar":True},

    "Vingadores": {"generos":["acao","heroi"],"diretor":"russo","ano":2012,"oscar":False},
    "Ultimato": {"generos":["acao","heroi"],"diretor":"russo","ano":2019,"oscar":False},
    "Homem de Ferro": {"generos":["acao","heroi"],"diretor":"favreau","ano":2008,"oscar":False},
    "Pantera Negra": {"generos":["acao","heroi"],"diretor":"coogler","ano":2018,"oscar":True},
    "Coringa": {"generos":["drama","crime"],"diretor":"phillips","ano":2019,"oscar":True},

    "O Poderoso Chefao": {"generos":["crime","drama"],"diretor":"coppola","ano":1972,"oscar":True},
    "O Poderoso Chefao 2": {"generos":["crime","drama"],"diretor":"coppola","ano":1974,"oscar":True},
    "Scarface": {"generos":["crime","drama"],"diretor":"depalma","ano":1983,"oscar":False},
    "Os Bons Companheiros": {"generos":["crime","drama"],"diretor":"scorsese","ano":1990,"oscar":True},
    "Cassino": {"generos":["crime","drama"],"diretor":"scorsese","ano":1995,"oscar":False},
    "O Lobo de Wall Street": {"generos":["drama"],"diretor":"scorsese","ano":2013,"oscar":False},

    "Seven": {"generos":["crime","suspense"],"diretor":"fincher","ano":1995,"oscar":False},
    "Clube da Luta": {"generos":["drama"],"diretor":"fincher","ano":1999,"oscar":False},
    "Garota Exemplar": {"generos":["suspense"],"diretor":"fincher","ano":2014,"oscar":False},

    "Parasita": {"generos":["drama"],"diretor":"bong","ano":2019,"oscar":True},
    "Memorias de um Assassino": {"generos":["crime"],"diretor":"bong","ano":2003,"oscar":False},

    "Titanic": {"generos":["romance","drama"],"diretor":"cameron","ano":1997,"oscar":True},
    "Avatar": {"generos":["ficcao"],"diretor":"cameron","ano":2009,"oscar":True},

    "Gladiador": {"generos":["acao","historico"],"diretor":"scott","ano":2000,"oscar":True},
    "Alien": {"generos":["ficcao","terror"],"diretor":"scott","ano":1979,"oscar":True},

    "O Resgate do Soldado Ryan": {"generos":["guerra"],"diretor":"spielberg","ano":1998,"oscar":True},
    "Jurassic Park": {"generos":["aventura"],"diretor":"spielberg","ano":1993,"oscar":True},
    "E.T.": {"generos":["ficcao"],"diretor":"spielberg","ano":1982,"oscar":True},

    "Harry Potter 1": {"generos":["fantasia"],"diretor":"columbus","ano":2001,"oscar":False},
    "Harry Potter 2": {"generos":["fantasia"],"diretor":"columbus","ano":2002,"oscar":False},
    "Harry Potter 3": {"generos":["fantasia"],"diretor":"cuaron","ano":2004,"oscar":False},

    "Senhor dos Aneis": {"generos":["fantasia"],"diretor":"jackson","ano":2001,"oscar":True},
    "As Duas Torres": {"generos":["fantasia"],"diretor":"jackson","ano":2002,"oscar":True},
    "O Retorno do Rei": {"generos":["fantasia"],"diretor":"jackson","ano":2003,"oscar":True},

    "Toy Story": {"generos":["animacao"],"diretor":"lasseter","ano":1995,"oscar":True},
    "Toy Story 2": {"generos":["animacao"],"diretor":"lasseter","ano":1999,"oscar":True},
    "Toy Story 3": {"generos":["animacao"],"diretor":"lee","ano":2010,"oscar":True},

    "Procurando Nemo": {"generos":["animacao"],"diretor":"stanton","ano":2003,"oscar":True},
    "Wall-E": {"generos":["animacao"],"diretor":"stanton","ano":2008,"oscar":True},

    "Up Altas Aventuras": {"generos":["animacao"],"diretor":"docter","ano":2009,"oscar":True},
    "Divertida Mente": {"generos":["animacao"],"diretor":"docter","ano":2015,"oscar":True},

    "Cisne Negro": {"generos":["drama"],"diretor":"aronofsky","ano":2010,"oscar":True},
    "Requiem para um Sonho": {"generos":["drama"],"diretor":"aronofsky","ano":2000,"oscar":False},

    "1917": {"generos":["guerra"],"diretor":"mendes","ano":2019,"oscar":True},
    "Skyfall": {"generos":["acao"],"diretor":"mendes","ano":2012,"oscar":True},

    "Whiplash": {"generos":["drama"],"diretor":"chazelle","ano":2014,"oscar":True},
    "La La Land": {"generos":["musical"],"diretor":"chazelle","ano":2016,"oscar":True},

    "Ford vs Ferrari": {"generos":["drama"],"diretor":"mangold","ano":2019,"oscar":True},
    "Logan": {"generos":["acao"],"diretor":"mangold","ano":2017,"oscar":False},

    "O Iluminado": {"generos":["terror"],"diretor":"kubrick","ano":1980,"oscar":False},
    "2001 Uma Odisseia": {"generos":["ficcao"],"diretor":"kubrick","ano":1968,"oscar":True},

    "Dunkirk": {"generos":["guerra"],"diretor":"nolan","ano":2017,"oscar":True},
    "Memento": {"generos":["suspense"],"diretor":"nolan","ano":2000,"oscar":False},

    "Zodiaco": {"generos":["crime"],"diretor":"fincher","ano":2007,"oscar":False},
    "O Jogo": {"generos":["suspense"],"diretor":"fincher","ano":1997,"oscar":False},

    "Hereditario": {"generos":["terror"],"diretor":"aster","ano":2018,"oscar":False},
    "Midsommar": {"generos":["terror"],"diretor":"aster","ano":2019,"oscar":False},

    "Corra": {"generos":["terror"],"diretor":"peele","ano":2017,"oscar":True},
    "Nao Nao Olhe": {"generos":["terror"],"diretor":"peele","ano":2022,"oscar":False}
}
grafo = {}

def criar_grafo():
    for f1 in filmes:
        grafo[f1] = []
        for f2 in filmes:
            if f1 != f2:
                g1 = set(filmes[f1]["generos"])
                g2 = set(filmes[f2]["generos"])

                # conecta se tiver gênero igual OU mesmo diretor
                if g1 & g2 or filmes[f1]["diretor"] == filmes[f2]["diretor"]:
                    grafo[f1].append(f2)


def heuristica(filme, busca):
    score = 0

    if busca in filmes[filme]["diretor"]:
        score += 3

    if busca in filmes[filme]["generos"]:
        score += 2

    if busca in filme.lower():
        score += 1

    return score
def bfs(busca):

    fila = deque(filmes.keys())
    visitado = set()
    resultado = []
    nos = 0

    while fila:
        atual = fila.popleft()
        nos += 1

        if atual not in visitado:
            visitado.add(atual)

            score = heuristica(atual, busca)
            if score > 0:
                resultado.append((atual, score))

            for vizinho in grafo[atual]:
                if vizinho not in visitado:
                    fila.append(vizinho)

    return sorted(resultado, key=lambda x: x[1], reverse=True), nos
def dfs(busca):
    pilha = list(filmes.keys())
    visitado = set()
    resultado = []
    nos = 0

    while pilha:
        atual = pilha.pop()
        nos += 1

        if atual not in visitado:
            visitado.add(atual)

            score = heuristica(atual, busca)
            if score > 0:
                resultado.append((atual, score))

            for vizinho in grafo[atual]:
                if vizinho not in visitado:
                    pilha.append(vizinho)

    return sorted(resultado, key=lambda x: x[1], reverse=True), nos
#
def a_star(busca):

    fila = []

    visitado = set()

    resultado = []

    nos = 0

    for filme in filmes:

        score = -heuristica(filme, busca)

        heapq.heappush(fila, (score, filme))

    while fila:

        score, atual = heapq.heappop(fila)

        nos += 1

        if atual not in visitado:

            visitado.add(atual)

            if -score > 0:

                resultado.append((atual, -score))

    return resultado, nos
def buscar_filmes():

    criar_grafo()

    texto_filmes.delete(1.0, END)

    busca = texto_busca.get().lower().strip()

    if busca == "":

        texto_filmes.insert(
            END,
            "Digite algo para pesquisar."
        )

        return

    resultado, nos = a_star(busca)

    texto_filmes.insert(
        END,
        "===== FILMES ENCONTRADOS =====\n\n"
    )

    if resultado:

        for filme, score in resultado[:10]:

            dados = filmes[filme]

            texto_filmes.insert(
                END,
                f"""
Filme: {filme}
Diretor: {dados['diretor']}
Ano: {dados['ano']}
Gêneros: {", ".join(dados['generos'])}
Oscar: {dados['oscar']}
Score: {score}

-------------------------------

"""
            )

    else:

        texto_filmes.insert(
            END,
            "Nenhum filme encontrado."
        )

    texto_filmes.insert(
        END,
        f"\nNós visitados: {nos}"
    )
 #davi
def limpar_texto():
    texto_filmes.delete(1.0, END)
    texto_busca.delete(0,END)

#criação da interface gráfica
janela = Tk()

janela.configure(bg="#0F0518")
janela.title ("FILMES NEXUS")
janela.geometry("1080x720")
#titulo do porgrama 
titulo = Label(janela, text= "Filmes Nexus IA", font=("Segoe UI",30, "bold"),fg="white", bg= "#0F0518")
titulo.pack(pady=10)
#criando painel onde vai ficar os conteúdos
painel = Frame (janela, bg = "#281446",  bd=2, padx=10,pady=10)
painel.pack(pady=20)

text_chat = Label(painel, text="Chat",font=("Segoe UI",15, "bold"),bg="#281446",fg="white")
text_chat.pack(pady=(0,10))

texto_filmes = ScrolledText(painel, width=80, height=20, bg="#3C1E64",fg="white",  insertbackground="white",relief="flat")
texto_filmes.pack(pady=10)
# campo onde os usuarios irão fazer sua busca por filmes
text_bsc = Label(painel, text="Digite sua busca abaixo.",font=("Segoe UI",15, "bold"),bg="#281446", fg="white")
text_bsc.pack(pady=5)

texto_busca = Entry(painel,width=50,bg="#502882",font=("Segoe UI",10, "bold"),fg="white",insertbackground="white",relief="flat")
texto_busca.pack(fill=X, ipadx=10,pady=10)
#botão buscar, onde o usuario ira efetuar a busca
btn_buscar = Button(painel,text="Buscar",command=buscar_filmes,bg="#783CC8",fg="white",relief="flat", width=15,height=2,cursor="hand2")
btn_buscar.pack(side=LEFT, expand=TRUE,fill=X,padx=6)
#botao de limpar, irá limpar as buscar já feitas
btn_limpar = Button(painel,text="Limpar",command=limpar_texto, bg="#783CC8",fg="white",relief="flat", width=15,height=2, cursor="hand2")
btn_limpar.pack(side=LEFT, expand=TRUE, fill=X,padx=6)

janela.mainloop()

