#!/usr/bin/env python
"""
Demonstration of all the ANSI colors.
"""
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML, FormattedText
from prompt_toolkit.output import ColorDepth

print = print_formatted_text


def color():
    for template in [
            'bg:#{0:02x}00{0:02x}', # Magenta.
            'bg:#00{0:02x}{0:02x}', # Cyan.
            'bg:#{0:02x}{0:02x}{0:02x}', # Gray.
            ]:
        fragments = []
        for i in range(0, 256, 4):
            fragments.append((template.format(i), ' '))
        space= '              '
        print(space,FormattedText(fragments), color_depth=ColorDepth.DEPTH_4_BIT)
        print(space,FormattedText(fragments), color_depth=ColorDepth.DEPTH_8_BIT)
        print(space,FormattedText(fragments), color_depth=ColorDepth.DEPTH_24_BIT)
        
