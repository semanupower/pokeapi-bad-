#!/usr/bin/env python
# -*- coding: utf-8 -*-

from funciones import main
         
if __name__ == '__main__':
    main()

    while True:
        try:
            opc = int(input("Quiere buscar otro pokémon? S - 1/N - 2: "))
        
        except ValueError:
            print("Por favor escriba una opción correcta.")

        else:
            if opc == 1:
                main()
            elif opc == 2:
                print("Cerrando...")
                break
            else:
                print("Por favor escriba una opción correcta.")
            
            