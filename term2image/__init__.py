import argparse
import sys
from array import array

import TermEmulator as te

_COLORS = {
    1: (0, 0, 0),
    2: (255, 0, 0),
    3: (0, 255, 0),
    4: (255, 255, 0),
    5: (0, 0, 255),
    6: (255, 0, 255),
    7: (0, 255, 255),
    8: (255, 255, 255),
}


def find_end(screen):
    width = len(screen[0])
    blank = array('c', ' ' * width)

    for row, line in reversed(list(enumerate(screen))):
        if line != blank:
            return row


def main(opts):
    buf = opts.infile.read()
    opts.infile.close()

    cols = 120
    rows = 10000
    term = te.V102Terminal(rows=rows, cols=cols)

    term.ProcessInput(buf)
    screen = term.GetRawScreen()
    last_row = find_end(screen)
    for row, line in enumerate(screen):
        for col, c in enumerate(line):
            style, fgcolor, bgcolor = term.GetRendition(row, col)
            if style & term.RENDITION_STYLE_BOLD:
                pass

            if style & term.RENDITION_STYLE_UNDERLINE:
                pass

            sys.stdout.write(c)

        sys.stdout.write('\n')
        if row == last_row:
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Receive term")
    parser.add_argument('-i', '--infile', type=argparse.FileType('r'), default='-')
    opts = parser.parse_args()
    main(opts)
