from datetime import datetime, timedelta
class PlayList:
    def __init__(self, id_playlist: int, nome: str, descricao: str):
        self._id = id_playlist
        self._nome = nome
        self._descricao = descricao
    @property
    def id(self): return self._id
    def Tempo_Total(self, lista_musicas, lista_itens) -> timedelta:
        total = timedelta(0)
        for item in lista_itens:
            if item.id_playlist == self._id:
                for musica in lista_musicas:
                    if musica.id == item.id_musica:
                        total += musica.duracao
        return total
    def __str__(self) -> str:
        return f"Playlist [{self._id}] {self._nome} - {self._descricao}"
class Musica:
    def __init__(self, id_musica: int, titulo: str, artista: str, album: str, duracao: timedelta):
        self._id = id_musica
        self._titulo = titulo
        self._artista = artista
        self._album = album
        self._duracao = duracao
    @property
    def id(self): return self._id
    @property
    def duracao(self): return self._duracao
    @property
    def titulo(self): return self._titulo

    def __str__(self) -> str:
        return f"Música [{self._id}] {self._titulo} - {self._artista} ({self._album}) | {self._duracao}"
class PlayListItem:
    def __init__(self, id_item: int, id_playlist: int, id_musica: int, data_inclusao: datetime, sequencia: int):
        self._id = id_item
        self._id_playlist = id_playlist
        self._id_musica = id_musica
        self._data_inclusao = data_inclusao
        self._sequencia = sequencia
    @property
    def id_playlist(self): return self._id_playlist
    @property
    def id_musica(self): return self._id_musica
    def __str__(self) -> str:
        return f"Item [{self._id}] | Playlist {self._id_playlist} -> Música {self._id_musica} | Seq: {self._sequencia}"
class UI:
    playlists = []
    musicas = []
    itens = []

    @classmethod
    def Main(cls):
        op = -1
        while op != 0:
            print("\n--- APLICAÇÃO PLAYLIST ---")
            print("1 - Gerir Músicas")
            print("2 - Gerir Playlists")
            print("3 - Associar Música A Playlist (Itens)")
            print("4 - Ver Resumo da playlist")
            print("0 - Sair")
            op = int(input("Opção: "))
            
            if op == 1: cls.MenuMusicas()
            elif op == 2: cls.MenuPlaylists()
            elif op == 3: cls.InserirItem()
            elif op == 4: cls.VerResumo()

    @classmethod
    def MenuMusicas(cls):
        print("\n[ Músicas ] 1-Inserir 2-Listar")
        op = int(input("Opção: "))
        if op == 1:
            id_mus = int(input("ID: "))
            tit = input("Título: ")
            art = input("Artista: ")
            alb = input("Álbum: ")
            mins = int(input("Duração (minutos): "))
            segs = int(input("Duração (segundos): "))
            cls.musicas.append(Musica(id_mus, tit, art, alb, timedelta(minutes=mins, seconds=segs)))
        elif op == 2:
            for m in cls.musicas: print(m)

    @classmethod
    def MenuPlaylists(cls):
        print("\n[ Playlists ] 1-Inserir 2-Listar")
        op = int(input("Opção: "))
        if op == 1:
            id_pl = int(input("ID: "))
            nome = input("Nome: ")
            desc = input("Descrição: ")
            cls.playlists.append(PlayList(id_pl, nome, desc))
        elif op == 2:
            for p in cls.playlists: print(p)

    @classmethod
    def InserirItem(cls):
        id_item = int(input("ID do Item: "))
        id_pl = int(input("ID da Playlist: "))
        id_mus = int(input("ID da Música: "))
        seq = int(input("Sequência na lista: "))
        cls.itens.append(PlayListItem(id_item, id_pl, id_mus, datetime.now(), seq))
        print("Música associada com sucesso!")
    @classmethod
    def VerResumo(cls):
        id_pl = int(input("Informe o ID da Playlist para ver o resumo: "))
        for p in cls.playlists:
            if p.id == id_pl:
                print(f"\n--- Resumo: {p} ---")
                tempo = p.Tempo_Total(cls.musicas, cls.itens)
                print(f"Tempo Total: {tempo}")
                print("Faixas:")
                for i in cls.itens:
                    if i.id_playlist == p.id:
                        for m in cls.musicas:
                            if m.id == i.id_musica:
                                print(f" - {m.titulo} ({m.duracao})")
                return
        print("Playlist não encontrada.")

if __name__ == "__main__":
    UI.Main()
