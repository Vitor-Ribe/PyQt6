import sys
# QApplication = aplicação
# QWidgets = Organiza os componentes dentro da aplicação
# QPushButton = cria botões
# QLabel = Textos
# QLineEdit = caixas de texto do usuario
# QComboBox = caixas de opções
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox


def funcao1():
    label.setText("Botão 1 apertado!")
    label.adjustSize()  # Ajusta o texto para aparecer completo


def funcao3():
    valor_Lido = le.text()  # salva a string que o usuário digitou
    label.setText("Olá " + valor_Lido + ", Seja bem vindo!")  # Altera o texto
    label.adjustSize()  # Ajusta o texto para aparecer completo


def lerComboBox():
    valor = combo.currentText()  # Salva o texto lido
    print(valor)


# Criação do objeto da aplicação
app = QApplication(sys.argv)
# Criação do objeto da janela
janela = QWidget()
janela.resize(800, 600)  # Redefinindo tamanho da janela
janela.setWindowTitle("Primeira Janela")  # Definição do título da janela

# Criação de um botão
btn = QPushButton("Botao 1", janela)  # (texto do botão, janela que ele aparecerá)
btn.setGeometry(100, 100, 150, 80)  # Definição de onde ele ficará (eixoX, eixoY, largura, altura)
btn.setStyleSheet('background-color:gray; color:white')  # Definição de estilo do botão através de CSS
btn.clicked.connect(funcao1)  # Atribui uma ação ao botão

btn2 = QPushButton("Botao 2", janela) # (texto do botão, janela que ele aparecerá)
btn2.setGeometry(100, 200, 150, 80)  # Definição de onde ele ficará (eixoX, eixoY, largura, altura)
btn2.setStyleSheet('background-color:gray; color:white')  # Definição de estilo do botão através de CSS
btn2.clicked.connect(lerComboBox)  # Atribui uma ação ao botão

btn3 = QPushButton("Botao 3", janela) # (texto do botão, janela que ele aparecerá)
btn3.setGeometry(100, 300, 150, 80)  # Definição de onde ele ficará (eixoX, eixoY, largura, altura)
btn3.setStyleSheet('background-color:gray; color:white')  # Definição de estilo do botão através de CSS
btn3.clicked.connect(funcao3)  # Atribui uma ação ao botão

# Exibição de texto
label = QLabel("Texto", janela)  # (texto que será exibido, janela que ele aparecerá)
label.move(300, 130)  # Define onde ele ficará (eixoX, eixoY)
label.setStyleSheet('font-size:30px')  # Define tamanho da fonte

# Criação da line edit
le = QLineEdit("", janela)   # (texto da caixa de texto, janela que ele aparecerá)
le.setGeometry(500, 300, 150, 40)  # definição de onde ele ficará

# Criação da combo box
combo = QComboBox(janela) # (janela que ele aparecerá)
# itens da caixa
combo.addItem("Selecione uma linguagem de programação")
combo.addItem("Java")
combo.addItem("Python")
combo.addItem("C")
combo.addItem("C#")
combo.move(10, 10)  # onde ficará (eixoX, eixoY)

janela.show()  # exibição da janela
app.exec()  # Execução do aplicativo
