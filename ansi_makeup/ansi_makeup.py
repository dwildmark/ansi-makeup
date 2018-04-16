class ansiseq:
    RESET = '0'
    BOLD = '1'
    FAINT = '2'
    ITALIC = '3'
    UNDERLINE = '4'
    SLOW_BLINK = '5'
    RAPID_BLINK = '6'
    REVERSE_COLORS = '7'
    CONCEAL = '8'

    def disable(self):
        RESET = ''
        BOLD = ''
        FAINT = ''
        ITALIC = ''
        UNDERLINE = ''
        SLOW_BLINK = ''
        RAPID_BLINK = ''
        REVERSE_COLORS = ''
        CONCEAL = ''


def startcmd(cmd):
    return '\033[' + cmd + 'm'


def endcmd():
    return '\033[0m'


def bold(text):
    return startcmd(ansiseq.BOLD) + text + endcmd()


def faint(text):
    return startcmd(ansiseq.FAINT) + text + endcmd()
