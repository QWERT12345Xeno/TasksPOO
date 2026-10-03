from datetime import datetime, timedelta 
class Treino:
    def __init__(self, id_treino: int, data: datetime, distancia: float, tempo: timedelta):
        self._id = id_treino
        self._data = data
        self._distancia = distancia
        self._tempo = tempo
    @property
    def id(self): return self._id
    @id.setter
    def id(self, valor): self._id = valor
    @property
    def data(self): return self._data
    @data.setter
    def data(self, valor): self._data = valor
    @property
    def distancia(self): return self._distancia
    @distancia.setter
    def distancia(self, valor): self._distancia = valor
    @property
    def tempo(self): return self._tempo
    @tempo.setter
    def tempo(self, valor): self._tempo = valor

    def Pace(self) -> timedelta:
        if self._distancia > 0:
            segundos_totais = self._tempo.total_seconds()
            segundos_por_km = segundos_totais / self._distancia
            return timedelta(seconds=segundos_por_km)
        return timedelta(0)

    def __str__(self) -> str:
        return f"ID: {self._id} | Data: {self._data.strftime('%d/%m/%Y')} | Dist: {self._distancia}km | Tempo: {self._tempo} | Pace: {self.Pace()}/km"


class TreinoUI:
    treinos = []

    @classmethod
    def Main(cls):
        op = -1
        while op != 0:
            op = cls.Menu()
            if op == 1: cls.Inserir()
            elif op == 2: cls.Listar()
            elif op == 3: cls.Listar_Id()
            elif op == 4: cls.Atualizar()
            elif op == 5: cls.Excluir()
            elif op == 6: cls.MaisRapido()
            elif op == 0: print("A encerrar...")
            else: print("Opção inválida.")

    @classmethod
    def Menu(cls):
        print("\n--- APLICAÇÃO TREINO ---")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Listar por ID")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Mais Rápido (Menor Pace)")
        print("0 - Sair")
        return int(input("Escolha uma opção: "))
    @classmethod
    def Inserir(cls):
        try:
            id_treino = int(input("ID do Treino: "))
            data_str = input("Data (DD/MM/AAAA): ")
            data = datetime.strptime(data_str, "%d/%m/%Y")
            distancia = float(input("Distância (km): "))
            minutos = int(input("Duração (minutos): "))
            segundos = int(input("Duração (segundos): "))
            
            novo_treino = Treino(id_treino, data, distancia, timedelta(minutes=minutos, seconds=segundos))
            cls.treinos.append(novo_treino)
            print("Treino inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir: {e}")
    @classmethod
    def Listar(cls):
        if not cls.treinos:
            print("Nenhum treino registado.")
            return
        for t in cls.treinos:
            print(t)
    @classmethod
    def Listar_Id(cls):
        id_busca = int(input("Informe o ID para procurar: "))
        for t in cls.treinos:
            if t.id == id_busca:
                print(t)
                return
        print("Treino não encontrado.")

    @classmethod
    def Atualizar(cls):
        id_busca = int(input("Informe o ID a atualizar: "))
        for t in cls.treinos:
            if t.id == id_busca:
                try:
                    t.distancia = float(input("Nova Distância (km): "))
                    minutos = int(input("Nova Duração (minutos): "))
                    segundos = int(input("Nova Duração (segundos): "))
                    t.tempo = timedelta(minutes=minutos, seconds=segundos)
                    print("Treino atualizado!")
                except Exception as e:
                    print(f"Erro: {e}")
                return
        print("Treino não encontrado.")
    @classmethod
    def Excluir(cls):
        id_busca = int(input("Informe o ID a excluir: "))
        for i, t in enumerate(cls.treinos):
            if t.id == id_busca:
                cls.treinos.pop(i)
                print("Treino excluído.")
                return
        print("Treino não encontrado.")

    @classmethod
    def MaisRapido(cls):
        if not cls.treinos:
            print("Nenhum treino registado.")
            return
        mais_rapido = min(cls.treinos, key=lambda t: t.Pace())
        print("Treino mais rápido:")
        print(mais_rapido)

if __name__ == "__main__":
    TreinoUI.Main()
