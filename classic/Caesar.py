def Caesar(text: str, k: int = 3):
    ans = ''
    for c in text:
        if c.isalpha():
            ans += offset(c, k) 
        else:
            ans += c
    return ans

def offset(c: str, k: int):
    a_ord = ord('A')
    c = c.capitalize()
    return chr(a_ord + (ord(c) - a_ord + k) % 26).capitalize()

def decipher(text: str):
    word_set = set()
    ans = "FAILED"
    max_confidence = 0
    with open("word-lists/20k.txt", "r") as file:
        for line in file:
            word_set.add(line.strip())
    words = text.split()
    for i in range(0, 26):
        ans_list = []
        confidence = 0
        for word in words:
            tmp = Caesar(word, i).lower()
            # print("[debug]", tmp, word)
            if tmp not in word_set:
                continue
            confidence += 1
            ans_list.append(tmp)
        if confidence > max_confidence:
            ans = " ".join(ans_list)
            max_confidence = confidence
    return ans
        


        