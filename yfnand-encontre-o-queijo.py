print("vamos caçar o queijo!!")
encontrou=False
tentativas=0
lugares("armairio","gaveta","geladeira","mesa","pote")
#preoparando a busca
while not encontrou:
    tentativas += 1
    print("{}".format(tentativas))
    for lugar in lugares:
        print("procurando no{}" .format(lugar))
    if lugar =="pote":
       print("achei o queijo!!!")
       encontrou=True
    break
print("consegui achar o queijo em{} ")
