class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        class UnionFind:
            """Estrutura Union-Find otimizada: união por tamanho e compressão de caminho."""
            def __init__(self, n: int):
                self.parent = list(range(n))
                self.size = [1] * n
                self.num_components = n

            def find(self, i: int) -> int:
                if self.parent[i] == i:
                    return i
                self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i: int, j: int) -> bool:
                root_i = self.find(i)
                root_j = self.find(j)
                if root_i != root_j:
                    if self.size[root_i] < self.size[root_j]:
                        root_i, root_j = root_j, root_i
                    self.parent[root_j] = root_i
                    self.size[root_i] += self.size[root_j]
                    self.num_components -= 1
                    return True
                return False

        n = len(nums)
        if n == 1:
            return True

        # Descobre o maior valor em nums para definir o limite da peneira de primos.
        max_val = max(nums)

        # Se houver algum número igual a 1, não é possível conectar todos (exceto caso único).
        if 1 in nums:
            return False

        # Pré-calcula o Menor Fator Primo (SPF) para cada número até max_val usando a peneira de Eratóstenes.
        spf = list(range(max_val + 1))
        i = 2
        while i * i <= max_val:
            if spf[i] == i:  # i é primo
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        def get_prime_factors(num: int) -> List[int]:
            """Retorna todos os fatores primos de num usando o SPF pré-calculado."""
            factors = set()
            while num > 1:
                factors.add(spf[num])
                num //= spf[num]
            return list(factors)

        uf = UnionFind(n)
        prime_to_index = {}  # Associa cada fator primo ao primeiro índice que o possui.

        # Para cada número, une conjuntos de índices que compartilham fatores primos.
        for i, num in enumerate(nums):
            factors = get_prime_factors(num)
            for p in factors:
                if p in prime_to_index:
                    uf.union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i

        # Só é possível atravessar todos se houver apenas um componente conectado.
        return uf.num_components == 1