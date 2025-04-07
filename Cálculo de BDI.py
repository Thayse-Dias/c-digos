def calcular_bdi():
    print("Calculadora de BDI\n")
    
    # Entrada de dados
    custos_diretos = float(input("Digite o valor dos custos diretos (R$): "))
    despesas_administrativas = float(input("Percentual de despesas administrativas (%): "))
    tributos = float(input("Percentual de tributos (%): "))
    seguros = float(input("Percentual de seguros (%): "))
    garantias = float(input("Percentual de garantias (%): "))
    custos_financeiros = float(input("Percentual de custos financeiros (%): "))
    lucro = float(input("Percentual de lucro desejado (%): "))
    
    # Cálculo do BDI
    bdi = (
        (1 + 
        (despesas_administrativas/100) +
        (tributos/100) +
        (seguros/100) +
        (garantias/100) +
        (custos_financeiros/100)) 
        * (1 + (lucro/100)) 
        - 1
    ) * 100
    
    # Cálculo do preço de venda
    preco_venda = custos_diretos * (1 + bdi/100)
    
    # Exibição dos resultados
    print("\nResultados:")
    print(f"BDI Calculado: {bdi:.2f}%")
    print(f"Custos Diretos: R$ {custos_diretos:,.2f}".replace(",", "v").replace(".", ",").replace("v", "."))
    print(f"Preço de Venda: R$ {preco_venda:,.2f}".replace(",", "v").replace(".", ",").replace("v", "."))

if __name__ == "__main__":
    try:
        calcular_bdi()
    except ValueError:
        print("\nErro: Insira apenas valores numéricos válidos!")