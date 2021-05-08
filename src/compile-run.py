import parac_compiler
import logging

logger = logging.getLogger("parac_compiler")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='parac-compile.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

if __name__ == '__main__':
    parac_compiler.init()
