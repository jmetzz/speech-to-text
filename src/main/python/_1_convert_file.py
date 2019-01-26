#!/usr/bin/env python3

"""Simple demo application to convert audio to text"""
import argparse
import logging
from os import path

from core.converter import AudioFileToText


def create_argument_parser():
    parser = argparse.ArgumentParser(description='parse incoming')

    parser.add_argument('-f', '--file',
                        help="The input file name",
                        required=True,
                        default=None,
                        type=str)

    parser.add_argument('-p', '--path',
                        help="The path to the input file",
                        required=False,
                        default='.',
                        type=str)

    parser.add_argument('-l', '--lang',
                        help="The language of the audio",
                        default='en-US',
                        type=str)

    parser.add_argument('-c', '--converter',
                        help="The language of the audio",
                        choices=['google', 'sphinx'],
                        type=str)

    parser.add_argument('-v', '--verbose',
                        help="Be verbose. Sets logging level to INFO",
                        action="store_const",
                        dest="loglevel",
                        const=logging.INFO,
                        default=logging.INFO)

    parser.add_argument('-vv', '--debug',
                        help="Print lots of debugging statements. "
                             "Sets logging level to DEBUG",
                        action="store_const",
                        dest="loglevel",
                        const=logging.DEBUG)

    parser.add_argument('-q', '--quiet',
                        help="Be quiet! Sets logging level to WARNING",
                        action="store_const",
                        dest="loglevel",
                        const=logging.WARNING)
    return parser


if __name__ == '__main__':
    cmdline_args = create_argument_parser().parse_args()
    logging.basicConfig(level=cmdline_args.loglevel)

    converter = AudioFileToText(recognizer=cmdline_args.converter,
                                language=cmdline_args.lang)

    audio_file = path.join(cmdline_args.path, cmdline_args.file)

    transcription = converter.convert(audio_file)
    if transcription['success']:
        print("Transcription:")
        print(f">>> '{transcription['text']}'")
    else:
        print(f">>> Error: '{transcription['error']}'")
