class carro():
    def __init__(self, tipo,  marca, modelo, ano, velocidade = 0, limite = 110):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
        self.velocidade = velocidade 
        self.limite = limite
    
    def acelerar(self, aceleraçao = 10):
        if self.velocidade + aceleraçao > self.limite:
            print(f"{self.tipo} da marca {self.modelo} atingiu o limite de velocidade, REDUZA A VELOCIDADE")
        else:
            self.velocidade += self.limite
            print(f"{self.tipo} da marca {self.modelo} aumentou a velocidade em {aceleraçao}Km/h, velocidade atual: {self.velocidade}Km/h")
    
    def frear(self, freio = 10):
        self.velocidade = max(0, self.velocidade - freio)
       
        print(f"{self.tipo} da marca {self.modelo} diminuiu a velocidade em {freio}Km/h, velocidade atual: {self.velocidade}Km/h")

    def exibir_info(self):
        print(f"{self.tipo} da Marca: {self.marca}; Modelo: {self.modelo}; Ano: {self.ano}; velocidade: {self.velocidade}Km/h")


class moto(carro):
    def __init__(self, marca, modelo, ano, velocidade = 0, limite = 90):
        super().__init__(marca, modelo, ano, velocidade)
    
    def empinar(self):
        if self.velocidade < 30:
            print(f"A moto {self.modelo} está empinando!")
        else:
            print(f"A moto {self.modelo} está muito rápido para empinar")

carro1 = carro("Carro","Fiat", "Uno", "2010")
carro2 = carro("Carro", "Ford", "Fiesta", "2015")
carro3 = carro("Carro", "Chevrolet", "Celta", "2012" )

carro1.exibir_info()
carro2.exibir_info()
carro3.exibir_info()

carro1.acelerar()
carro1.frear()
carro2.acelerar(20)
carro2.frear(15)
carro3.acelerar(5)
carro3.frear(10)

moto1 = moto("Moto", "Honda", "CG", "2018")
moto2 = moto("Moto", "Yamaha", "Factor", "2019")
moto3 = moto("Moto", "Suzuki", "Yes", "2017")
moto1.exibir_info()
moto2.exibir_info()
moto3.exibir_info()

moto1.acelerar()
moto1.frear()
moto3.acelerar(50)
moto2.acelerar(60)
moto1.acelerar(65)
moto2.frear(20)
moto1.frear(80)


