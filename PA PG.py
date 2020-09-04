p_a = []
p_g = []
inicial = 0
opcao = 0
seq = 0

sequencia = 1


def primeiraCond(re):
    sim_nao = input("Você quer saber um termo específico?(S/N): ").lower()
    if sim_nao == "n":
        re = "n"
        return re
    else:
        re = "s"
        return re


def segundaCond(re):
    sim_nao = input("Você quer sabe a posição de um valor específico?(S/N): ").lower()
    if sim_nao == "n":
        re = "n"
        return re
    else:
        re = "s"
        return re


def razao():
    if len(p_a) == 1:
        r = float(input("Qual a razão? "))
        return r
    else:
        r = p_a[1] - p_a[0]
        return r


def equacoes_pa():
    sorted(p_a)
    n_ezimo = sequencia - 1
    tm = (p_a[-1] + p_a[0]) / 2
    sn = ((p_a[-1] + p_a[0]) * len(p_a)) / 2
    print("—" * 50)
    print(" Sua P.A. tem {} termos.".format(len(p_a)))
    print(" A razão é:", r)
    print(" A soma de termos da sua P.A. é:", sn)
    print(" O termo médio é:", tm)
    print("—" * 50)


def printlista():
    print("—" * 50)
    print("\033[1:52m\033[1:36m", sorted(p_a), "\033[0:0m")


# def opcaof(opc):
#     print("[1] Progressão Aritmética.\n"
#           "[2] Progressão Geométrica.\n"
#           "[3] Sair.\n")
#     opc = int(input("Escolha uma das opções: "))
#     return opc
#
#
# opcaof(opcao)

while opcao != 3:
    print("[1] Progressão Aritmética.\n"
          "[2] Progressão Geométrica.\n"
          "[3] Sair.\n")
    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        p_a_criacao = int(input("[1] Já tenho uma P.A.\n"
                                "[2] Quero criar uma P.A.\n"))
        if p_a_criacao == 1:
            fim = "fim"
            while not fim == True:
                print("\033[1;31m""Digite \"fim\" a qualquer momento para encerrar a progressão.""\033[0;0m")
                termo = input("Digite o {}º termo: ".format(sequencia))
                if termo != fim:
                    p_a.append(int(termo))
                    sequencia += 1
                else:
                    fim = True
            if len(p_a) == 0:
                inicial = 0
            else:
                sorted(p_a)
                resp = "n"
                termo_usuario = True
                n = len(p_a)
                if primeiraCond(resp) == "s":
                    while termo_usuario:
                        sorted(p_a)
                        termo_e = float(input("Qual o termo? "))
                        r = razao()
                        an = p_a[0] + (((termo_e) - 1) * r)
                        print("O termo {} é: {} e a razão é {}.".format(int(termo_e), an, r))
                        encerramento = input("Quer saber mais algum? (S/N) ").lower()
                        if encerramento == "s":
                            continue
                        else:
                            # equacoes_pa()
                            # printlista()
                            termo_usuario = False
                termo_usuario = True
                if segundaCond(resp) == "s":
                    while termo_usuario:
                        sorted(p_a)
                        valor = float(input("Qual o valor a ser encontrado? "))
                        r = razao()
                        n = (-p_a[0] + r + valor) / r
                        print("O valor {} ocupa o {}º termo.".format(valor, int(n)))
                        encerramento = input("Quer saber mais algum? (S/N) ").lower()
                        if encerramento == "s":
                            continue
                        else:
                            # equacoes_pa()
                            # printlista()
                            termo_usuario = False
                else:
                    sorted(p_a)
                    r = p_a[1] - p_a[0]
                    # printlista()
                    # equacoes_pa()
        elif p_a_criacao == 2:
            a1 = float(input("Digite o 1º termo: "))
            n_ezimo = int(input("Quantidade de termos: "))
            r = float(input("Razão: "))
            n = 1
            for a in range(n_ezimo):
                an = a1 + ((n - 1) * r)
                p_a.append(an)
                n += 1


            # printlista()
            # equacoes_pa()
        printlista()
        equacoes_pa()

    inicial = 1
    p_a.clear()
    p_g.clear()
