#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    longueur = len(string)

    if longueur %2 == 0:
        return (True)
    else:
        return (False)
    pass


def remove_third_char(string: str) -> str:
    x = string[slice(0,2)]
    y = string[slice(3,len(string))]

    return (x + y)

    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return(string.replace('w','b'))
    pass


def get_number_of_char(string: str, char: str) -> int:
    nb_repet =0
    for n in string:
        if n == char:
            nb_repet+=1

    return nb_repet
    pass


def get_number_of_words(sentence: str, word: str) -> int:
    return(sentence.count(word))
    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")

    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
