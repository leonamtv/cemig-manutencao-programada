import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Crawler para verificar manutenções programadas da CEMIG',
                                     add_help=False)
    parser.add_argument('city', action='store', help='Nome da cidade para procurar')
    parser.add_argument('-d', '--date', action='store', help='Data para verificar no formato dd/mm/yyyy')
    parser.add_argument('-h', '--help', action='help', help='Mostra essa mensagem e sai.')
    return parser


def parse_args():
    return create_parser().parse_args()
