from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    @abstractmethod
    def preparar(self):
        pass

class PratoPrincipal(ItemCardapio):
    def preparar(self, nome, preco):
        return (f"Prato Principal: {nome}, Preço: {preco}")
    
class Sobremesa(ItemCardapio):
    def preparar(self, nome, preco):
        return (f"Sobremesa: {nome}, Preço: {preco}")
    
class Bebida(ItemCardapio):
    def preparar(self, nome, preco):
        return (f"Bebida: {nome}, Preço: {preco}")
    
class CriadorDeItem(ABC):
    @abstractmethod
    def criarItem(self):
        pass

class CriadorDePratoPrincipal(CriadorDeItem):
    def criarItem(self):
        return PratoPrincipal()
    
class CriadorDeSobremesa(CriadorDeItem):
    def criarItem(self):
        return Sobremesa()
    
class CriadorDeBebida(CriadorDeItem):
    def criarItem(self):
        return Bebida()

class Pedido():
    def adicionarItem(self):
        pass

    def resumirPedido(self):
        item1 = CriadorDePratoPrincipal()
        criar1 = item1.criarItem()
        print(criar1.preparar("Misto", "R$100,00"))

        item2 = CriadorDeSobremesa()
        criar2 = item2.criarItem()
        print(criar2.preparar("Brigadeiro", "R$8,00"))

        item3 = CriadorDeBebida()
        criar3 = item3.criarItem()
        print(criar3.preparar("Refrigerante 1L", "R$8,00"))
        return 
    
resumo = Pedido()
exibir = resumo.resumirPedido()
