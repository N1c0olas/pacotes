while True:
    try:
        numero = int(input("Entre com um numero: "))
        print(5/numero)
        break
    except ValueError:
        print("Valor Errado.")
    except ZeroDivisionError:
        print("Desculpe. Não posso dividir por zero.")
    except:
        print("Não sei oque fazer...")