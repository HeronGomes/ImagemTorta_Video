# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

imagem = cv.imread("Quadro5.jpg")
imagem = cv.resize(imagem,(400,600))

imagemOriginal = imagem.copy()


filme = cv.VideoWriter('./arte10.mp4',cv.VideoWriter.fourcc(*'mp4v'),15,(800,600))


cv.putText(imagemOriginal,
           'Original',
           (0,25),
           cv.FONT_HERSHEY_PLAIN,
           2,
           (0,127,0),
           2,
           cv.LINE_AA )


linha,coluna,canais = imagem.shape


back = np.full((linha,coluna,3),(0,0,0),np.uint8)  




for l in range(linha):
    for c in range(coluna):
        
        x = int(35 * np.sin(1.5*np.pi*l/180))
        
        if( x+c < coluna):
            back[l,c] = imagem[l,(x+c)]
        else:
            back[l,c] = imagem[l,c]
    
    resultado = cv.hconcat([imagemOriginal,back])
    
    cv.putText(resultado,
           'Algoritmo em funcionamento',
           (405,25),
           cv.FONT_HERSHEY_PLAIN,
           1.5,
           (0,127,0),
           2,
           cv.LINE_AA )
    
    
    
    cv.imshow("Quadro",resultado)
    cv.waitKey(25)
    filme.write(resultado)
           





cv.imshow("Quadro",resultado)

cv.waitKey()
cv.destroyAllWindows()
filme.release()









