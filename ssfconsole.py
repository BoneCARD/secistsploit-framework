#!/usr/bin/env python
# encoding: utf-8
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import CompleteStyle, prompt
import os
from core.Banner import *
animals = ['help', 'exit', 'options', 'use']
animals_family = {
    'use': 'Use module',
    'help': 'Command help',
    'exit': 'Exit SecistSploit',
    'options': 'Settings'
}
family_colors = {
    'Use module': 'ansimagenta',
    'Exit SecistSploit': 'ansired',
    'Command help': 'ansiblue',
    'Settings': 'ansired'
}
meta = {
    'use': HTML('use modules/xxxxxx')
}
class AnimalCompleter(Completer):
    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        for animal in animals:
            if animal.startswith(word):
                if animal in animals_family:
                    family = animals_family[animal]
                    family_color = family_colors.get(family, 'default')
                    display = HTML('%s<b>:</b> <ansired>(<' + family_color + '>%s</' + family_color + '>)</ansired>') % (animal, family)
                else:
                    display = animal
                yield Completion(animal, start_position=-len(word), display=display, display_meta=meta.get(animal))
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    while True:
        cmd = prompt("SSF > ", completer=AnimalCompleter())
        if cmd == 'exit':
            os._exit(0)
        elif cmd == 'help':
            print('''
help: Display this message
use: Use module
            ''')
        else:
            print("Error")
if __name__ == '__main__':
    main()