# round(var,nºde casas decimais) p/ limitar as casas dps da virgula
# Usei o \ para quebrar apenas a linha do código e \n para quebrar a linha no output
# float() para converter a entrada de dados para type(float)

tempF = float(input('Entre com a temperatura em Fahrenheit que\
 \nvocê deseja converter para Celsius: '))
tempC = (tempF - 32)*5/9
print(f'A temperatura em Celsius é de: {round(tempC,1)}º')
