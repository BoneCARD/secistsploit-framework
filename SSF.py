#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Demonstration of a custom completer class and the possibility of styling
completions independently by passing formatted text objects to the "display"
and "display_meta" arguments of "Completion".
"""
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import CompleteStyle, prompt
import os
from core.Banner import *

#from core.completer import *
animals = [
    'help','exit','options','use'
]

animal_family = {
    'use': '使用模块',
    'help': '帮助参数',
    'exit': '退出',
    'options': '选项',
    'use': '使用模块',
}

family_colors = {
     '使用模块': 'ansimagenta',
     '退出': 'ansigreen',
     '帮助参数': 'ansired',
     '选项': 'ansiyellow',
#    'mammal': 'ansimagenta',
#    'insect': 'ansigreen',
#    'reptile': 'ansired',
#    'bird': 'ansiyellow',
}

meta = {
    'use': HTML('use  modules/xxxxxx'),
}


class AnimalCompleter(Completer):
    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        for animal in animals:
            if animal.startswith(word):
                if animal in animal_family:
                    family = animal_family[animal]
                    family_color = family_colors.get(family, 'default')

                    display = HTML(
                        '%s<b>:</b> <ansired>(<' + family_color + '>%s</' + family_color + '>)</ansired>'
                        ) % (animal, family)
                else:
                    display = animal

                yield Completion(
                    animal,
                    start_position=-len(word),
                    display=display,
                    display_meta=meta.get(animal)
                )


def main():
     os.system('cls' if os.name == 'nt' else 'clear')
     banner()

     while True:

            cmd = prompt('SSF >>', completer=AnimalCompleter())
            if   cmd == 'exit':
                os._exit(0)
            elif cmd=='help':
                print('''
                    help  帮助参数
                    use  使用模块
                ''')
            else :
                print ("error")

if __name__ == '__main__':
    main()
