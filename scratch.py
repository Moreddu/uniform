elenco_nomi={'maschile':[], 'femminile':[]}
while True:
    nome= raw_input("Inserisci un nome: ")
    print(nome)

    if(nome == "fine"):
        print("ciclo finito")
        break
    elif(nome in elenco_nomi['maschile']):
        print("E' un nome maschile")
    elif(nome in elenco_nomi['femminile']):
        print("E' un nome femminile")
    else:
        genere= raw_input("non conosco questo nome, dimmi se e' maschile o femminile: ")
        if(genere== "maschile"):
            elenco_nomi['maschile']=nome
            print("nome inserito")
        elif(genere== "femminile"):
            elenco_nomi['femminile']=nome
            print("nome inserito")
        else:
            print("valore non corretto, inserisci un nuovo nome")




