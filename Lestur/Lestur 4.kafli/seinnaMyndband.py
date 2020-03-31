def foo_recur(lis):

    if len(lis) == 0:
        return

    # prentum stökin í öfugri röð
    print(lis[-1])

    # styttum listann um einn, stak -1 updateast 
    # alltaf því það er bara síðasta stakið
    foo_recur(lis[:-1])

    #prentum stökin í réttri röð
    print(lis[-1])


foo_recur([1,23,4,5])


def foo_recur2(lis, index):

    # ef maður vill gera í öfugri röð eins og í foo recur 1
    # þá er hægt að gera < 0 og svo index-1 
    # þegar kallað í foo recur 2 niðri
    if len(lis) == index:
        return

    # prentum stökin í öfugri röð
    print(lis[index])

    # styttum listann um einn, stak -1 updateast 
    # alltaf því það er bara síðasta stakið
    foo_recur2(lis, index+1)

    #prentum stökin í réttri röð
    print(lis[index])


foo_recur2([1,23,4,5],4)