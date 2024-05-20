import cv2
import pytesseract

def reconhecer(imagem):
    #chamando o executavel de reconhecimento de caracteres (biblioteca)
    pytesseract.pytesseract.tesseract_cmd=r""
    
    #leitura de uma imagem que contem textos
    placa = cv2.imread(imagem, 0)
    
    # converter/capturar textos de imagem
    meusTextos =pytesseract.image_to_string(placa, config="1 eng --oem 3 --psm 12")
    
    #print(meusTextos)
    return meusTextos

#enviar uma imagem para a função e exibir os textos reconhecidos
imagem = "livros.jpg"

textosReconhecidos = reconhecer(imagem)
print(textosReconhecidos)