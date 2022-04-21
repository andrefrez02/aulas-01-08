print('Faça um Programa que peça duas temperaturas (inicial e final) em graus Celsius,',
'\bcalcule e mostre a variação de temperatura em graus Celsius e em graus Fahrenheit.\n',
'\bPara tanto considere:\n',
'\t ∆𝑇𝐶 = 𝑇𝑓 − 𝑇𝑖\n',
'\t∆𝑇𝐹 = 1,8 ∗ ∆𝑇C\nEntrada:')
tf, ti = 0, 0
ti = int(input('Digite a temperatura inicial em °C: '))
tf = int(input('Digite a temperatura final em °C: '))
dtc = tf - ti
dtF = 1.8 * dtc
print(f'\nSaída:\nVariação de temperatura em Celsius: {dtc:.0f}°C')
print(f'Variação de temperatura em Fahrenheit: {dtF:.2f}°F')