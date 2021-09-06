def main(): 
    arquivo = open("newton_saida.txt", "w")
    arquivo.write("Método de Newton:\n")

    k = 0
    xk = -1
    xr = 0
    mod = abs(xk - xr)
    erro = 1./7.

    arquivo.write("No intervalo [-1, 0]\n")
    arquivo.write("\tk\t     xk\t\t   f(xk)\t   f'(xk)\t   erro\n")

    while(mod > 0.000001 and k <= 50):
        fx = funcao(xk)
        dx = derivada(xk)

        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fx) + "\t")
        arquivo.write(str(dx) + "\t")
        arquivo.write(str(abs(xk-erro)) + "\n")

        xr = xk 
        xk = xk - (fx / dx)
        k += 1
        mod = abs(xk - xr)
    
    arquivo.write("\t" + str(k) + "\t")
    arquivo.write(str(xk) + "\t")
    arquivo.write(str(fx) + "\t")
    arquivo.write(str(dx) + "\t")
    arquivo.write(str(abs(xk-erro)) + "\n")

    arquivo.close()

def funcao(x): 
    fx = 3*x*x*x*x*x - 9*x*x*x*x + 2*x*x*x - 6*x*x - x + 3
    return fx

def derivada(x): 
    dx = 15*x*x*x*x - 36*x*x*x + 6*x*x - 12*x -1 
    return dx

if __name__ == "__main__":
    main()

