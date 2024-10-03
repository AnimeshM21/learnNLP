Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from nltk.corpus import brown
brown.words()
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
from nltk.book import *
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
text1
<Text: Moby Dick by Herman Melville 1851>
text1.concordance("monstrous")
Displaying 11 of 11 matches:
ong the former , one was of a most monstrous size . ... This came towards us , 
ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
ll over with a heathenish array of monstrous clubs and spears . Some were thick
d as you gazed , and wondered what monstrous cannibal and savage could ever hav
that has survived the flood ; most monstrous and most mountainous ! That Himmal
they might scout at Moby Dick as a monstrous fable , or still worse and more de
th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
ere to enter upon those still more monstrous stories of them which are to be fo
ght have been rummaged out of this monstrous cabinet there is no telling . But 
of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u
text1.concordance("rummaged")
Displaying 1 of 1 matches:
What other marvels might have been rummaged out of this monstrous cabinet ther
text1.concordance("whales")
Displaying 25 of 268 matches:
ing up whatever random allusions to whales he could anyways find in any book w
 EXTRACTS . " And God created great whales ." -- GENESIS . " Leviathan maketh 
t fishes that are : among which the Whales and Whirlpooles called Balaene , ta
a , when about sunrise a great many Whales and other monsters of the sea , app
lso with a view of catching horse - whales , which had bones of very great val
ght some to the king . ... The best whales were catched in his own country , o
 -- THE FAERIE QUEEN . " Immense as whales , the motion of whose vast bodies c
out a sea ." -- IBID . " The mighty whales which swim in a sea of water , and 
CHAS . " In their way they saw many whales sporting in the ocean , and in want
" Here they saw such huge troops of whales , that they were forced to proceed 
 . D . 1671 HARRIS COLL . " Several whales have come in upon this coast ( Fife
S . PHIL . TRANS . A . D . 1668 . " Whales in the sea God ' s voice obey ." --
 . " We saw also abundance of large whales , there being more in those souther
 -- COOK ' S VOYAGES . " The larger whales , they seldom venture to attack . T
 degrees south , we saw Spermacetti Whales , but did not take any till the fir
de Assaulted by voracious enemies , Whales , sharks , and monsters , arm ' d i
s were on a high hill observing the whales spouting and sporting with each oth
d we saw in the Berlin Gazette that whales had been introduced on the stage th
?" " Ay ay , sir ! A shoal of Sperm Whales ! There she blows ! There she breac
en told that these were the ribs of whales ." -- TALES OF A WHALE VOYAGER TO T
 returned from the pursuit of these whales , that the whites saw their ship in
asion I saw two of these monsters ( whales ) probably male and female , slowly
o goes the story -- to throw at the whales , in order to discover when they we
s ago did Nathan Swain kill fifteen whales between a sunrise and a sunset . An
htest bashfulness had boarded great whales on the high seas -- entire stranger
text1.similar("monstrous")
true contemptible christian abundant few part mean careful puzzled
mystifying passing curious loving wise doleful gamesome singular
delightfully perilous fearless
text1.similar("a")
the his that this one their some my any its in so no your those
another these her our not
text1.concordance("a")
Displaying 25 of 4736 matches:
ville 1851 ] ETYMOLOGY . ( Supplied by a Late Consumptive Usher to a Grammar Sc
upplied by a Late Consumptive Usher to a Grammar School ) The pale Usher -- thr
g his old lexicons and grammars , with a queer handkerchief , mockingly embelli
thers , and to teach them by what name a whale - fish is to be called in our to
tely from the Dut . and Ger . WALLEN ; A . S . WALW - IAN , to roll , to wallow
, ERROMANGOAN . EXTRACTS ( Supplied by a Sub - Sub - Librarian ). It will be se
ainstaking burrower and grub - worm of a poor devil of a Sub - Sub appears to h
wer and grub - worm of a poor devil of a Sub - Sub appears to have gone through
aluable or entertaining , as affording a glancing bird ' s eye view of what has
wn . So fare thee well , poor devil of a Sub - Sub , whose commentator I am . T
les ." -- GENESIS . " Leviathan maketh a path to shine after him ; One would th
" -- JOB . " Now the Lord had prepared a great fish to swallow up Jonah ." -- J
o days on the sea , when about sunrise a great many Whales and other monsters o
peared . Among the former , one was of a most monstrous size . ... This came to
 , and beating the sea before him into a foam ." -- TOOKE ' S LUCIAN . " THE TR
." " He visited this country also with a view of catching horse - whales , whic
N DOWN FROM HIS MOUTH BY KING ALFRED , A . D . 890 . " And whereas all the othe
 bruise ." -- KING HENRY . " Very like a whale ." -- HAMLET . " Which to secure
the motion of whose vast bodies can in a peaceful calm trouble the ocean til it
in his side he wears , And on his back a grove of pikes appears ." -- WALLER ' 
 created that great Leviathan , called a Commonwealth or State --( in Latin , C
it without chewing , as if it had been a sprat in the mouth of a whale ." -- PI
if it had been a sprat in the mouth of a whale ." -- PILGRIM ' S PROGRESS . " T
creatures , in the deep Stretched like a promontory sleeps or swims , And seems
promontory sleeps or swims , And seems a moving land ; and at his gills Draws i
text4.dispersion_plot(["democracy")
                      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
text4.dispersion_plot(["democracy"])
                      
Traceback (most recent call last):
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 28, in dispersion_plot
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    text4.dispersion_plot(["democracy"])
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/text.py", line 561, in dispersion_plot
    dispersion_plot(self, words)
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 30, in dispersion_plot
    raise ImportError(
ImportError: The plot function requires matplotlib to be installed. See https://matplotlib.org/
>>> text4.dispersion_plot(["democracy"])
Traceback (most recent call last):
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 28, in dispersion_plot
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    text4.dispersion_plot(["democracy"])
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/text.py", line 561, in dispersion_plot
    dispersion_plot(self, words)
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 30, in dispersion_plot
    raise ImportError(
ImportError: The plot function requires matplotlib to be installed. See https://matplotlib.org/
