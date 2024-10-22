Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
Traceback (most recent call last):
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 28, in dispersion_plot
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/text.py", line 561, in dispersion_plot
    dispersion_plot(self, words)
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 30, in dispersion_plot
    raise ImportError(
ImportError: The plot function requires matplotlib to be installed. See https://matplotlib.org/
