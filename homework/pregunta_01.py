# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import os
import glob
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * target: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    # leer los archivos para test
    test_rows = []
    for file in glob.glob("files/input/test/*/*.txt"):
        with open(file, 'r') as f:
            phrase = f.readline().strip()
        target = os.path.basename(os.path.dirname(file))
        test_rows.append((phrase, target))

    train_rows = []
    # leer los archivos para train
    for file in glob.glob("files/input/train/*/*.txt"):
        with open(file, 'r') as f:
            phrase = f.readline().strip()
        target = os.path.basename(os.path.dirname(file))
        train_rows.append((phrase, target))

    # crear dataframes para los csv
    test_dataset = pd.DataFrame(test_rows, columns=["phrase", "target"])
    train_dataset = pd.DataFrame(train_rows, columns=["phrase", "target"])

    # crear el directorio output y guardar los archivos
    if not os.path.exists("files/output/"):
        os.mkdir("files/output")

    test_dataset.to_csv("files/output/test_dataset.csv", index=False)
    train_dataset.to_csv("files/output/train_dataset.csv", index=False)
