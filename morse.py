# morse.py
# python version 2.7.12
# created at 10.10.2016
#
# !/usr/local/bin python
# -*- coding: utf-8 -*-
#
# Morse Code Python Script for encoding or decoding Morse Code
#

import time
from pygame import mixer

code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': '|',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

inverse_code = dict((v, k) for (k, v) in code.items())


def encode(msg):
    encoded_msg = ''
    try:
        for char in msg:
            encoded_msg += code[char.upper()] + ' '
        return encoded_msg
    except Exception as e:
        print('Error, unsupported character: {0}'.format(e))


def decode(msg):
    split_msg = msg.split(' ')
    split_msg = filter(None, split_msg)
    decoded_msg = ''
    try:
        for char in split_msg:
            decoded_msg += inverse_code[char.upper()]
        return decoded_msg
    except Exception as e:
        print('Error, unsupported character: {0}'.format(e))


def play_sound(msg):
    mixer.init()
    short_sound = mixer.Sound("short.wav")
    long_sound = mixer.Sound("long.wav")

    for char in msg:
        if char == '.':
            short_sound.play()
            time.sleep(0.2)
        elif char == '-':
            long_sound.play()
            time.sleep(0.2)
        else:
            time.sleep(0.4)


def main():
    message = raw_input('Type the Message you want to de/encode: ')

    if message.startswith('.') or message.startswith('-'):
        print decode(message)
        play_sound(message)

    else:
        msg = encode(message)
        print msg
        play_sound(msg)

if __name__ == '__main__':
    main()
