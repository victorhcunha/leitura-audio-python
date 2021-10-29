import gtts

with open('text.txt','r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('texto.mp3')
