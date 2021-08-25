ValorRosa = 2.8
ValorTulipa = 4.20

QuantRosa = int(input("Rosas: "))
QuantTulipa = int(input("Tulipa: "))

TotalRosa = ValorRosa * QuantRosa
TotalTulipa = ValorTulipa * QuantTulipa
TotalValor = TotalRosa + TotalTulipa

print(f"Vai prescisar de R${TotalValor:.2f}")