class Mediator:                        # mediator é responsável por coordenar a comunicação entre os colaboradores
    def __init__(self):                # inicializa o Mediator com uma lista vazia de colaboradores
        self.colaboradores = []        # lista que armazenará os colaboradores participantes da comunicação
        
    def adicionar_colaborador(self, colaborador):     # método para adicionar um colaborador ao Mediator
        self.colaboradores.append(colaborador)        # adiciona o colaborador à lista
        colaborador.mediator = self                   # define o Mediator para o colaborador, permitindo que ele envie mensagens através do Mediator
        
    def enviar_mensagem(self, mensagem, remetente):        # método para enviar uma mensagem a todos os colaboradores, exceto o remetente
        for colaborador in self.colaboradores:             # itera sobre todos os colaboradores registrados
            if colaborador != remetente:                   # verifica se o colaborador não é o remetente da mensagem
                colaborador.receber_mensagem(mensagem, remetente)          # envia a mensagem para o colaborador, informando quem é o remetente


class Colaborador:                    # colaborador representa um participante que pode enviar e receber mensagens
    def __init__(self, nome):         # inicializa o colaborador com um nome e um mediador
        self.nome = nome              # nome do colaborador
        self.mediator = None          # mediador que coordena a comunicação entre os colaboradores

    def enviar_mensagem(self, mensagem):                 # método para enviar uma mensagem através do mediador
        print(f"{self.nome} enviou a mensagem: '{mensagem}'")                # imprime a mensagem enviada pelo colaborador
        self.mediator.enviar_mensagem(mensagem, self)          # chama o mediador para enviar a mensagem a todos os outros colaboradores

    def receber_mensagem(self, mensagem, remetente):      # método para receber uma mensagem de outro colaborador
        print(f"{self.nome} recebeu a mensagem: '{mensagem}' de {remetente.nome}")        # imprime a mensagem recebida e o remetente
        
        
# exemplo

mediator = Mediator()           # cria uma instância do Mediator que gerenciará a comunicação entre os colaboradores

# cria três colaboradores que participarão da comunicação

usuario1 = Colaborador("Usuário 1")           
usuario2 = Colaborador("Usuário 2")
usuario3 = Colaborador("Usuário 3")

# adiciona os colaboradores ao Mediator

mediator.adicionar_colaborador(usuario1)      
mediator.adicionar_colaborador(usuario2)
mediator.adicionar_colaborador(usuario3)

# os colaboradores enviam mensagens uns aos outros

usuario1.enviar_mensagem("Olá, galera!!!")    
usuario2.enviar_mensagem("Oi, tudo bem?")
usuario3.enviar_mensagem("Olá, pessoal! Como vão??")     