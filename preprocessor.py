# coding: utf-8
import os
import sys
import re

class FileNotFoundException(Exception):
    """
    Exceção para marcar que o arquivo não foi encontrado.
    """
    pass

INCLUDE_TOKEN = "\\include"
INCLUDE_REGEX = re.compile("^\\include\{.+\}")

def preprocess_include(index_file):
    new_lines = []

    open_braces = 0
    close_braces = 0

    with open(index_file) as current_file:
        for i, line in enumerate(current_file):
            print line

            if line.startswith(r"\include{"):
                open_braces = line.find("{")
                close_braces = line.find("}")

                new_path = line[open_braces + 1: close_braces]

                new_path = os.path.join(os.path.dirname(index_file), new_path)

                print new_path

                if not os.path.exists(new_path):
                    raise FileNotFoundException(u"%s ñ foi encontrado." % new_path)

                new_lines.extend(preprocess_include(new_path))

            else:
                new_lines.append(line)

    return new_lines


def run_preprocess(index_file, new_file="acumulado.md"):
    if not os.path.exists(index_file):
        print "arquivo escolhido não existe"
        return

    try:
        new_lines = preprocess_include(index_file)
    except Exception as ex:
        print ex.message
        return

    with open(new_file, "w") as write_file:

        for line in new_lines:
            write_file.write("%s" % line)

        write_file.flush()

if __name__ == "__main__":
    original_file = sys.argv[1]
    try:
        write_file = sys.argv[2]
    except IndexError as idxError:
        basedir = os.path.dirname(original_file)
        write_file = os.path.join(basedir, "acumulado.md")

    print "arquivo original", original_file
    print "novo", write_file

    run_preprocess(original_file, write_file)