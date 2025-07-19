class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        resposta = [-1] * n
        pilha1, pilha2 = [], []
        for i, v in enumerate(nums):
            while pilha2 and v > nums[pilha2[-1]]:
                idx = pilha2.pop()
                resposta[idx] = v
            indices_movidos = []
            while pilha1 and v > nums[pilha1[-1]]:
                indices_movidos.append(pilha1.pop())
            for idx in reversed(indices_movidos):
                pilha2.append(idx)
            pilha1.append(i)
        return resposta