"""Encryptor & Decryptor"""

import re

# ------------------------------------------------------------------------------


def encode(txt, emoji_list):
    """Encryption"""
    # Uppercase alphabets
    txt = re.sub("A", emoji_list[0], txt)
    txt = re.sub("B", emoji_list[1], txt)
    txt = re.sub("C", emoji_list[2], txt)
    txt = re.sub("D", emoji_list[3], txt)
    txt = re.sub("E", emoji_list[4], txt)

    txt = re.sub("F", emoji_list[5], txt)
    txt = re.sub("G", emoji_list[6], txt)
    txt = re.sub("H", emoji_list[7], txt)
    txt = re.sub("I", emoji_list[8], txt)
    txt = re.sub("J", emoji_list[9], txt)

    txt = re.sub("K", emoji_list[10], txt)
    txt = re.sub("L", emoji_list[11], txt)
    txt = re.sub("M", emoji_list[12], txt)
    txt = re.sub("N", emoji_list[13], txt)
    txt = re.sub("O", emoji_list[14], txt)

    txt = re.sub("P", emoji_list[15], txt)
    txt = re.sub("Q", emoji_list[16], txt)
    txt = re.sub("R", emoji_list[17], txt)
    txt = re.sub("S", emoji_list[18], txt)
    txt = re.sub("T", emoji_list[19], txt)

    txt = re.sub("U", emoji_list[20], txt)
    txt = re.sub("V", emoji_list[21], txt)
    txt = re.sub("W", emoji_list[22], txt)
    txt = re.sub("X", emoji_list[23], txt)
    txt = re.sub("Y", emoji_list[24], txt)

    txt = re.sub("Z", emoji_list[25], txt)

    # Lowercase alphabets
    txt = re.sub("a", emoji_list[26], txt)
    txt = re.sub("b", emoji_list[27], txt)
    txt = re.sub("c", emoji_list[28], txt)
    txt = re.sub("d", emoji_list[29], txt)
    txt = re.sub("e", emoji_list[30], txt)

    txt = re.sub("f", emoji_list[31], txt)
    txt = re.sub("g", emoji_list[32], txt)
    txt = re.sub("h", emoji_list[33], txt)
    txt = re.sub("i", emoji_list[34], txt)
    txt = re.sub("j", emoji_list[35], txt)

    txt = re.sub("k", emoji_list[36], txt)
    txt = re.sub("l", emoji_list[37], txt)
    txt = re.sub("m", emoji_list[38], txt)
    txt = re.sub("n", emoji_list[39], txt)
    txt = re.sub("o", emoji_list[40], txt)

    txt = re.sub("p", emoji_list[41], txt)
    txt = re.sub("q", emoji_list[42], txt)
    txt = re.sub("r", emoji_list[43], txt)
    txt = re.sub("s", emoji_list[44], txt)
    txt = re.sub("t", emoji_list[45], txt)

    txt = re.sub("u", emoji_list[46], txt)
    txt = re.sub("v", emoji_list[47], txt)
    txt = re.sub("w", emoji_list[48], txt)
    txt = re.sub("x", emoji_list[49], txt)
    txt = re.sub("y", emoji_list[50], txt)

    txt = re.sub("z", emoji_list[51], txt)

    # Digits
    txt = re.sub("1", emoji_list[52], txt)
    txt = re.sub("2", emoji_list[53], txt)
    txt = re.sub("3", emoji_list[54], txt)
    txt = re.sub("4", emoji_list[55], txt)
    txt = re.sub("5", emoji_list[56], txt)
    txt = re.sub("6", emoji_list[57], txt)
    txt = re.sub("7", emoji_list[58], txt)
    txt = re.sub("8", emoji_list[59], txt)
    txt = re.sub("9", emoji_list[60], txt)
    txt = re.sub("0", emoji_list[61], txt)

    # Special characters (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    #    txt = re.sub(r"\!",  emoji_list[62], txt)
    #    txt = re.sub(r"\"", emoji_list[63], txt)
    #    txt = re.sub(r"\#",  emoji_list[64], txt)
    #    txt = re.sub(r"\$",  emoji_list[65], txt)
    #    txt = re.sub(r"\%",  emoji_list[66], txt)
    #    txt = re.sub(r"\&",  emoji_list[67], txt)
    #    txt = re.sub(r"\'", emoji_list[68], txt)
    #    txt = re.sub(r"\(",  emoji_list[69], txt)
    #    txt = re.sub(r"\)",  emoji_list[70], txt)
    #    txt = re.sub(r"\*",  emoji_list[71], txt)
    txt = re.sub(r"\+",  emoji_list[72], txt)
# txt = re.sub(r"\,",  emoji_list[73], txt)
# txt = re.sub(r"\-",  emoji_list[74], txt)
# txt = re.sub(r"\.",  emoji_list[75], txt)
    txt = re.sub(r"\/",  emoji_list[76], txt)
# txt = re.sub(r"\:",  emoji_list[77], txt)
# txt = re.sub(r"\;",  emoji_list[78], txt)
# txt = re.sub(r"\<",  emoji_list[79], txt)
    txt = re.sub(r"\=",  emoji_list[80], txt)
# txt = re.sub(r"\>",  emoji_list[81], txt)
# txt = re.sub(r"\?",  emoji_list[82], txt)
# txt = re.sub(r"\@",  emoji_list[83], txt)
# txt = re.sub(r"\[",  emoji_list[84], txt)
# txt = re.sub(r"\]",  emoji_list[85], txt)
# txt = re.sub(r"\^",  emoji_list[86], txt)
# txt = re.sub(r"\_",  emoji_list[87], txt)
# txt = re.sub(r"\`",  emoji_list[88], txt)
# txt = re.sub(r"\{",  emoji_list[89], txt)
# txt = re.sub(r"\|",  emoji_list[90], txt)
# txt = re.sub(r"\}",  emoji_list[91], txt)
# txt = re.sub(r"\~",  emoji_list[92], txt)

    return txt

# ------------------------------------------------------------------------------


def decode(txt, emoji_list):
    """Decryption"""
    # Uppercase alphabets
    txt = re.sub(emoji_list[0], "A", txt)
    txt = re.sub(emoji_list[1], "B", txt)
    txt = re.sub(emoji_list[2], "C", txt)
    txt = re.sub(emoji_list[3], "D", txt)
    txt = re.sub(emoji_list[4], "E", txt)

    txt = re.sub(emoji_list[5], "F", txt)
    txt = re.sub(emoji_list[6], "G", txt)
    txt = re.sub(emoji_list[7], "H", txt)
    txt = re.sub(emoji_list[8], "I", txt)
    txt = re.sub(emoji_list[9], "J", txt)

    txt = re.sub(emoji_list[10], "K", txt)
    txt = re.sub(emoji_list[11], "L", txt)
    txt = re.sub(emoji_list[12], "M", txt)
    txt = re.sub(emoji_list[13], "N", txt)
    txt = re.sub(emoji_list[14], "O", txt)

    txt = re.sub(emoji_list[15], "P", txt)
    txt = re.sub(emoji_list[16], "Q", txt)
    txt = re.sub(emoji_list[17], "R", txt)
    txt = re.sub(emoji_list[18], "S", txt)
    txt = re.sub(emoji_list[19], "T", txt)

    txt = re.sub(emoji_list[20], "U", txt)
    txt = re.sub(emoji_list[21], "V", txt)
    txt = re.sub(emoji_list[22], "W", txt)
    txt = re.sub(emoji_list[23], "X", txt)
    txt = re.sub(emoji_list[24], "Y", txt)

    txt = re.sub(emoji_list[25], "Z", txt)

    # Lowercase alphabets
    txt = re.sub(emoji_list[26], "a", txt)
    txt = re.sub(emoji_list[27], "b", txt)
    txt = re.sub(emoji_list[28], "c", txt)
    txt = re.sub(emoji_list[29], "d", txt)
    txt = re.sub(emoji_list[30], "e", txt)

    txt = re.sub(emoji_list[31], "f", txt)
    txt = re.sub(emoji_list[32], "g", txt)
    txt = re.sub(emoji_list[33], "h", txt)
    txt = re.sub(emoji_list[34], "i", txt)
    txt = re.sub(emoji_list[35], "j", txt)

    txt = re.sub(emoji_list[36], "k", txt)
    txt = re.sub(emoji_list[37], "l", txt)
    txt = re.sub(emoji_list[38], "m", txt)
    txt = re.sub(emoji_list[39], "n", txt)
    txt = re.sub(emoji_list[40], "o", txt)

    txt = re.sub(emoji_list[41], "p", txt)
    txt = re.sub(emoji_list[42], "q", txt)
    txt = re.sub(emoji_list[43], "r", txt)
    txt = re.sub(emoji_list[44], "s", txt)
    txt = re.sub(emoji_list[45], "t", txt)

    txt = re.sub(emoji_list[46], "u", txt)
    txt = re.sub(emoji_list[47], "v", txt)
    txt = re.sub(emoji_list[48], "w", txt)
    txt = re.sub(emoji_list[49], "x", txt)
    txt = re.sub(emoji_list[50], "y", txt)

    txt = re.sub(emoji_list[51], "z", txt)

    # Digits
    txt = re.sub(emoji_list[52], "1", txt)
    txt = re.sub(emoji_list[53], "2", txt)
    txt = re.sub(emoji_list[54], "3", txt)
    txt = re.sub(emoji_list[55], "4", txt)
    txt = re.sub(emoji_list[56], "5", txt)
    txt = re.sub(emoji_list[57], "6", txt)
    txt = re.sub(emoji_list[58], "7", txt)
    txt = re.sub(emoji_list[59], "8", txt)
    txt = re.sub(emoji_list[60], "9", txt)
    txt = re.sub(emoji_list[61], "0", txt)

    # Special characters (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    # txt = re.sub(emoji_list[62], "!", txt)
    # txt = re.sub(emoji_list[63], "\"", txt)
    # txt = re.sub(emoji_list[64], "#", txt)
    # txt = re.sub(emoji_list[65], "$", txt)
    # txt = re.sub(emoji_list[66], "%", txt)
    # txt = re.sub(emoji_list[67], "&", txt)
    # txt = re.sub(emoji_list[68], "'", txt)
    # txt = re.sub(emoji_list[69], "(", txt)
    # txt = re.sub(emoji_list[70], ")", txt)
    # txt = re.sub(emoji_list[71], "*", txt)
    txt = re.sub(emoji_list[72], "+", txt)
    # txt = re.sub(emoji_list[73], ",", txt)
    # txt = re.sub(emoji_list[74], "-", txt)
    # txt = re.sub(emoji_list[75], ".", txt)
    txt = re.sub(emoji_list[76], "/", txt)
    # txt = re.sub(emoji_list[77], ":", txt)
    # txt = re.sub(emoji_list[78], ";", txt)
    # txt = re.sub(emoji_list[79], "<", txt)
    txt = re.sub(emoji_list[80], "=", txt)
    # txt = re.sub(emoji_list[81], ">", txt)
    # txt = re.sub(emoji_list[82], "?", txt)
    # txt = re.sub(emoji_list[83], "@", txt)
    # txt = re.sub(emoji_list[84], "[", txt)
    # txt = re.sub(emoji_list[85], "]", txt)
    # txt = re.sub(emoji_list[86], "^", txt)
    # txt = re.sub(emoji_list[87], "_", txt)
    # txt = re.sub(emoji_list[88], "`", txt)
    # txt = re.sub(emoji_list[89], "{", txt)
    # txt = re.sub(emoji_list[90], "|", txt)
    # txt = re.sub(emoji_list[91], "}", txt)
    # txt = re.sub(emoji_list[92], "~", txt)

    return txt
# ------------------------------------------------------------------------------
