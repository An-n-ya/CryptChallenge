import matplotlib.pyplot as plt

def statics(text: str, annotation: str):
    text = text.lower()
    cnt = [0] * 26
    for c in text:
        if c.isalpha():
            cnt[ord(c) - ord('a')]+=1
    max_cnt = max(cnt)
    freq = [c / max_cnt for c in cnt]
    freq_tuple = [(f, chr(ord('a') + i)) for i, f in enumerate(freq)]
    freq_tuple.sort(reverse=True)
    print(freq_tuple)
    fig, ax = plt.subplots()
    ax.plot(range(1, 27), [f for (f, _) in freq_tuple])
    ax.set_xticks(range(1, 27), range(1, 27))
    ax.annotate(annotation, xy=(1, freq_tuple[0][0]), xytext=(3, freq_tuple[0][0] + 0.05), arrowprops=dict(facecolor="black", shrink=0.05))
    plt.show()
    
    

            
