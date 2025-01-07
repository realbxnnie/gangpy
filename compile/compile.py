from time import sleep
from pathlib import Path

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-file", type=str, help="Path to the file that needs to be compiled.")

path = parser.parse_args().file

toReplace = [
    ("скрытый базар", "#"),
    ("отдельно от", "from"),
    ("из", "for"),
    ("в", "in"),
    ("числе", "range"),
    ("закинуть", "import"),
    ("меняй имя", "as"),
    ("базар", "print"),
    ("буквально все", "*"),
    ("стартуй", "__init__"),
    ("главный", "__main__"),
    ("я думаю", "if"),
    ("ну тогда я думаю", "elif"),
    ("сдаюсь", "else"),
    ("начать думать", "match"),
    ("я сильно думаю", "case"),
    ("энд", ";"),
    ("погоняло", "__name__"),
    ("нум", "int"),
    ("кик", "exit"),
    ("стр", "str"),
    ("хз", "None"),
    ("выполни пока", "while"),
    ("ты", "self"),
    ("выполни", "def"),
    ("потом выполни", "lambda"),
    ("выполняй ", ""),
    ("жди", '__import__("time").sleep'),
    ("введите текст", "input"),
    ("харе", "break"),
    ("продолжай", "continue"),
    ("неопознанный объект", "class"),
    ("суперсила", "super"),
]
with open(path, "r") as f:
    code = f.read()
    compiled = f"""# < THIS FILE WAS AUTOMATICALLY COMPILED BY Gangpy COMPILER. >
# < https://github.com/realbxnnie/gangpy >

{code}
"""
    i1 = None
    for i in toReplace:
        i1 = i[1]
        compiled = compiled.replace(i[0], i1)
        
    pathcompiled = path
    pathcompiled = pathcompiled.replace(".gpy", ".py")
    Path(pathcompiled).touch()
    open(pathcompiled, "w").write(compiled)
    print("=== SUCCESSFULLY COMPILED ===")

    
