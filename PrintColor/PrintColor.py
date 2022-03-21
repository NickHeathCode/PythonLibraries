class Color:
    WHITE         = "\033[0m"
    BOLD          = "\033[1m"
    ITALIC        = "\033[3m"
    UNDERLINE     = "\033[4m"
    STRIKETHROUGH = "\033[27m"
    BLACK         = "\033[30m"
    RED           = "\033[31m"
    GREEN         = "\033[32m"
    YELLOW        = "\033[33m"
    BLUE          = "\033[34m"
    PURPLE        = "\033[35m"
    CYAN          = "\033[36m"
    GRAY          = "\033[90m"
    BLACK_BACKGROUND  = "\033[40m"
    GRAY_BACKGROUND   = "\033[100m"
    RED_BACKGROUND    = "\033[101m"
    GREEN_BACKGROUND  = "\033[102m"
    YELLOW_BACKGROUND = "\033[103m"
    BLUE_BACKGROUND   = "\033[104m"
    PURPLE_BACKGROUND = "\033[105m"
    CYAN_BACKGROUND   = "\033[106m"

def printColor(color: Color, text, newLine = True):
    print(color + text + Color.WHITE, end="\n" if newLine else "")

def printRainbow(text):
    rainbow_colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE]
    index = 0
    for i in text:
        printColor(rainbow_colors[index % len(rainbow_colors)], i, False)
        if i != ' ':
            index += 1
    print()