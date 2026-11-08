if __name__ == '__main__':
    ############################Valor de Rivera #######################
    score_rivera = 0.9126
    precios = [125, 125, 137.3]
    overall = [0.7402, 0.4431, 0.5987]
    valor_rivera = score_rivera * (sum(precios) / sum(overall))

    print(valor_rivera)
