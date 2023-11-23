import numpy as np

def generate_invertible_matrix(dim: int):
    m = np.random.randint(0, 20, size=(dim, dim))
    mx = np.sum(np.abs(m), axis=1)
    # make this matrix diagonal dominance which is the sufficient condition of invertible
    np.fill_diagonal(m, mx)
    return m

def cofactor(matrix, row, col):
    submatrix = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
    return ((-1) ** (row + col) * np.linalg.det(submatrix))


class Hill:
    Z26 = {
        1: 1,
        3: 9,
        5: 21,
        7: 15,
        9: 3,
        11: 19,
        15: 7,
        17: 23,
        19: 11,
        21: 5,
        23: 17,
    }


    def cipher(self, text: str):
        n = 3
        while True:
            K = generate_invertible_matrix(n)
            if np.linalg.det(K) % 26 in self.Z26:
                break
        text = text.upper()
        ord_A = ord('A')
        self.n = n
        self.K = K
        ans = []
        for i in range(0, len(text), n):
            chunk = [ord(c) - ord_A for c in text[i:i+n]]
            while len(chunk) < n:
                chunk.append(ord_A)
            tmp = [chr(ord_A + c % 26) for c in np.dot(chunk, K)]
            ans.extend(tmp)
        return "".join(ans)

    
    def decipher(self, text: str):
        n = self.n
        det = np.linalg.det(self.K) % 26
        det_inv = self.Z26[det]
        K = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                K[i][j] = det_inv * cofactor(self.K, j, i) % 26
        K = np.round(np.array(K)).astype(int)
        ord_A = ord('A')
        ans = []
        text = text.upper()
        for i in range(0, len(text), n):
            chunk = [ord(c) - ord_A for c in text[i:i+n]]
            while len(chunk) < n:
                chunk.append(ord_A)
            tmp = [chr(ord_A + c % 26) for c in np.dot(chunk, K)]
            ans.extend(tmp)
        return "".join(ans)


            





