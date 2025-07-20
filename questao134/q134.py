from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Determina o ponto de partida para completar um circuito de postos de gasolina.
        """
        # Se o custo total for maior que a gasolina total, é impossível.
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        start_station = 0
        
        for i in range(len(gas)):
            # Acumula o saldo de gasolina/custo no tanque.
            tank += gas[i] - cost[i]
            
            # Se o tanque fica negativo, este trecho não é viável.
            # O próximo posto se torna o novo candidato a ponto de partida.
            if tank < 0:
                start_station = i + 1
                tank = 0
                
        return start_station