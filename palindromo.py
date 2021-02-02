def palindromo(palabra):
    palabra=palabra.replace(' ','')#reemplazar los espacios en blanco por espacios vacios
    palabra=palabra.lower()#pasar a minuscula
    palabra_invertida=palabra[::-1]# escribirlo al reves
    if palabra==palabra_invertida:
        return True
    else:
        return False


def run():#funcion principal puede tener el nombre que nostros queramos
    palabra=input('escribe una palabra:')
    es_palindromo= palindromo(palabra)
    if es_palindromo==True:
        print('es palindromo')
    else:
        print('no es palindromo')


if __name__=='__main__':  #punto de entrada de un programa de py 
    run()
          
    
