Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
len(text3)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    len(text3)
NameError: name 'text3' is not defined. Did you mean: 'next'?
import nltk
nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
len(text1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    len(text1)
NameError: name 'text1' is not defined. Did you mean: 'next'?
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
len(text3)
44764
text2.similar("Monstrous")
very so exceedingly heartily a as good great extremely remarkably
sweet vast amazingly
text2.common_contexts(["monstrous","very"])
am_glad a_pretty a_lucky is_pretty be_glad
text4.dispersion_plot(["citizens","democracy"])
Traceback (most recent call last):
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 28, in dispersion_plot
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    text4.dispersion_plot(["citizens","democracy"])
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/text.py", line 561, in dispersion_plot
    dispersion_plot(self, words)
  File "/Users/animeshmishra/Library/Python/3.12/lib/python/site-packages/nltk/draw/dispersion.py", line 30, in dispersion_plot
    raise ImportError(
ImportError: The plot function requires matplotlib to be installed. See https://matplotlib.org/
text3.generate()
Building ngram index...
laid by her , and said unto Cain , Where art thou , and said , Go to ,
I will not do it for ten ' s sons ; we dreamed each man according to
their generatio the firstborn said unto Laban , Because I said , Nay ,
but Sarah shall her name be . , duke Elah , duke Shobal , and Akan .
and looked upon my affliction . Bashemath Ishmael ' s blood , but Isra
for as a prince hast thou found of all the cattle in the valley , and
the wo The
"laid by her , and said unto Cain , Where art thou , and said , Go to ,\nI will not do it for ten ' s sons ; we dreamed each man according to\ntheir generatio the firstborn said unto Laban , Because I said , Nay ,\nbut Sarah shall her name be . , duke Elah , duke Shobal , and Akan .\nand looked upon my affliction . Bashemath Ishmael ' s blood , but Isra\nfor as a prince hast thou found of all the cattle in the valley , and\nthe wo The"
text3.generate()
laid by her , and said unto Cain , Where art thou , and said , Go to ,
I will not do it for ten ' s sons ; we dreamed each man according to
their generatio the firstborn said unto Laban , Because I said , Nay ,
but Sarah shall her name be . , duke Elah , duke Shobal , and Akan .
and looked upon my affliction . Bashemath Ishmael ' s blood , but Isra
for as a prince hast thou found of all the cattle in the valley , and
the wo The
"laid by her , and said unto Cain , Where art thou , and said , Go to ,\nI will not do it for ten ' s sons ; we dreamed each man according to\ntheir generatio the firstborn said unto Laban , Because I said , Nay ,\nbut Sarah shall her name be . , duke Elah , duke Shobal , and Akan .\nand looked upon my affliction . Bashemath Ishmael ' s blood , but Isra\nfor as a prince hast thou found of all the cattle in the valley , and\nthe wo The"
set(text3)
{'heir', 'book', 'generatio', 'led', 'strangers', 'washed', 'Have', 'maiden', 'sell', 'Saul', 'shouldest', 'Mizraim', 'Gomorrah', 'dark', 'soul', 'Hittites', 'couching', 'perform', 'rained', 'if', 'strove', 'presence', 'Arise', 'shut', 'dearth', 'weighed', 'dwelling', 'state', 'fame', 'Eldaah', 'Eber', 'Uz', 'mocking', 'ships', 'quickly', 'overtook', 'ha', 'changed', 'harm', 'wroth', 'Phara', 'make', 'awaked', 'prison', 'Ur', 'stand', 'moreover', 'Jetur', 'he', 'whosoever', 'man', 'other', 'shoulders', 'Dothan', 'Yet', 'hired', 'devoured', 'Abr', 'loose', 'shew', 'Edar', ',)', 'Thahash', 'ass', 'nought', 'clear', 'Enoch', 'exceedingly', 'content', 'Methuselah', 'Beor', 'uppermost', 'sat', 'Shaul', 'hith', 'sa', 'Jebusite', 'sweat', 'Peleg', 'you', 'northward', 'me', 'understood', 'flood', 'Drink', 'Jac', 'souls', 'Nimrod', 'able', 'appeared', 'lay', 'Ammon', 'fine', 'hearth', 'beheld', 'instead', 'withheld', 'began', 'assigned', 'mercies', 'Kadesh', 'poplar', 'Abimelech', 'vow', 'follow', 'ought', 'present', 'another', 'ri', 'Lehabim', 'Padanaram', 'm', 'proved', 'Erech', 'dost', 'wounding', 'his', 'dim', 'maid', 'entered', 'guiltiness', 'almon', 'basket', 'seed', 'be', 'Anah', 'draw', 'camest', 'fish', 'arms', 'distressed', 'rebelled', 'subtil', 'feel', 'asses', 'Shelah', 'sceptre', 'trade', 'behind', 'Cursed', 'arose', 'clothed', 'upon', 'force', 'blood', 'say', 'beari', 'pledge', 'commanding', 'dreams', 'vine', 'Muppim', 'possessi', 'pillar', 'bosom', 'yonder', 'ewes', 'jud', 'Peradventure', 'large', 'took', 'tent', 'Sojourn', 'magnified', 'continued', 'hanged', 'healed', 'stood', 'gold', 'Abide', 'Reu', 'Tubalcain', 'abide', 'lad', 'reproved', 'sod', 'clusters', 'angel', 'quite', 'deceitfully', 'thee', 'punishment', 'your', 'sojourned', 'precious', 'planted', 'Phut', 'seedtime', 'smote', 'out', 'angels', 'It', 'offered', 'after', 'Happy', 'tim', 'fig', 'afar', 'asswaged', 'enlarge', 'ruler', 'royal', 'sand', 'Tebah', 'Ask', 'adder', 'space', 'numbering', 'Hiddekel', 'ill', 'path', 'wherefore', 'report', 'drink', 'prepared', 'lodged', 'crown', 'Chaldees', 'Hebron', 'Abelmizraim', 'journey', 'comforted', 'troubled', 'Cheran', 'yearn', 'My', 'wives', 'windows', 'doest', 'pass', 'signs', 'sou', 'spices', 'wrapped', 'lands', 'Beerlahairoi', 'hear', 'ste', 'escaped', 'armed', 'chief', 'knead', 'seven', 'Husham', 'Eshcol', 'yoke', 'fetcht', 'anger', 'Elam', 'cakes', 'Gather', 'Egypt', 'living', 'upward', 'interpretations', 'lights', 'drinking', 'Sell', 'messenger', 'chode', 'cometh', 'moon', 'deliver', 'prayed', 'within', 'onyx', 'communed', 'justice', 'Jabal', 'Mash', 'sheepshearers', 'natio', 'alive', 'Zarah', 'faileth', 'wot', 'seasons', 'coats', 'See', 'Milcah', 'gate', '?)', 'talked', 'proceedeth', 'wickedness', 'oath', 'How', 'ours', 'Jaalam', 'burning', 'intreat', 'interpreted', 'eighteen', 'Omar', 'loud', 'Ezbon', 'sepulchres', 'bre', 'fifty', 'kingdom', 'heels', 'rolled', 'roughly', 'done', 'life', 'Here', 'couch', 'bones', 'heel', 'da', 'wombs', 'togeth', 'excel', 'sheaves', 'become', 'bowed', 'Adah', 'overcome', 'scarce', 'lives', 'watch', 'neck', 'Fifteen', 'Lie', 'driven', 'Philistines', 'delivered', 'Siddim', 'frost', 'stooped', 'merchantmen', 'had', 'Kemuel', 'Mesopotamia', 'himself', 'great', 'breach', 'lower', 'goodly', 'Magdiel', 'lesser', 'dead', 'parted', '?', 'sh', 'En', 'month', 'birthday', 'Pathrusim', 'give', 'Heber', 'never', 'only', 'anointedst', 'an', 'Abrah', 'wind', 'troop', 'saw', 'crieth', 'Return', 'Which', 'families', 'Riphath', 'law', 'firmament', 'people', 'harvest', 'droves', 'imagined', 'Buz', 'Male', 'Cush', 'ey', 'Hazo', 'findeth', 'Jehovahjireh', 'pulled', 'Let', 'sole', 'mocked', 'caught', 'over', 'grew', 'bearing', 'standest', 'knowing', 'goats', 'dew', 'names', 'Ellasar', 'image', 'gopher', 'wandered', 'mistress', 'following', 'feeding', 'gods', 'sworn', 'shoelatchet', 'spirit', 'ready', 'Naaman', 'discern', 'offeri', 'except', 'magicians', 'dread', 'Sichem', 'barr', 'cause', 'destroy', 'five', 'sack', 'forty', 'knife', 'yet', 'see', 'Alvan', 'Now', 'knowest', 'deliverance', 'raiment', 'battle', 'Hadar', 'prosperous', 'Hadad', 'raise', 'dried', 'innocency', 'fruits', 'kind', 'wrestlings', 'hou', 'ones', 'Whose', 'Rachel', 'vision', 'Javan', 'I', 'because', 'fair', 'ring', 'direct', ',', 'Abram', 'Serug', 'Pharez', 'supplanted', 'han', 'distress', 'Jachin', 'now', 'Togarmah', 'brass', 'leanfleshed', 'Unstable', 'find', 'giving', 'Lasha', 'iniquity', 'prosper', 'even', 'seek', 'confederate', 'dea', 'friends', 'lien', 'Salem', 'speech', 'waxen', 'winter', 'Of', 'regard', 'discreet', 'pray', 'slept', 'save', 'persons', 'Ebal', 'window', 'hunting', 'tell', 'left', 'judgment', 'rid', 'bare', 'nativity', 'ground', 'look', 'open', 'grove', 'protest', 'weapons', 'Shillem', 'war', 'sister', 'twenty', 'bought', 'rulers', 'Who', 'd', 'run', 'laughed', 'strife', 'Israel', 'belly', 'too', 'withered', 'fir', 'mouth', 'abroad', 'poured', 'bou', 'troughs', 'Ishbak', 'Perizzites', 'let', 'longeth', 'pleasant', 'raven', 'till', 'clothes', 'finding', 'begotten', 'gro', 'damsel', 'Phallu', 'Can', 'flock', 'Beersheba', 'tabret', 'knoweth', 'riv', 'ride', 'gather', 'smoking', 'break', 'doeth', 'judged', 'seventy', 'marry', 'mirth', 'Canaan', 'mules', 'came', 'espied', 'king', 'Eri', 'Samlah', 'trembled', 'Reumah', 'inherit', 'friend', 'Asenath', 'teeth', 'Dan', 'Cause', 'fourth', 'observed', 'meeteth', 'gone', 'multiplied', 'Abel', 'walked', 'seventeen', 'far', ':', 'custom', 'Es', 'floor', 'Sephar', 'they', 'As', 'unawares', 'nourished', 'tongues', 'together', 'Leah', 'dreamer', 'increase', 'Should', 'handfuls', 'kept', 'Come', 'rightly', 'answer', 'Job', 'Zeboim', 'overdrive', 'defiledst', 'been', 'stead', 'womenservan', 'Feed', 'breaketh', 'embalmed', 'also', 'Pison', 'bracelets', 'Upon', 'inn', 'giveth', 'beneath', 'Gera', 'Seth', 'hated', 'embalm', 'hither', 'kindness', 'while', 'commanded', 'dry', 'Whereas', 'linen', 'tenth', 'womb', 'Bashemath', 'refrained', 'bakers', 'springing', 'thus', 'Bera', 'Amalekites', 'pow', 'fugitive', 'require', 'pit', 'feet', 'Isra', 'boys', 'thin', 'Wilt', 'sort', 'afflict', 'born', 'firmame', 'Neither', 'Zillah', 'Sarai', 'speed', 'flee', 'aileth', 'wandering', 'bury', 'dowry', 'shield', 'Jobab', 'perceived', 'Becher', 'Amorites', 'saving', 'Pharaoh', 'increased', 'thoughts', 'nourish', 'Shalem', 'bowels', 'current', 'parcel', 'Alvah', 'Thorns', 'itself', 'Terah', 'Esek', 'commandments', 'host', 'sowed', 'mead', 'desire', 'Oh', 'Tell', 'excellency', 'Se', 'children', 'young', 'Eliphaz', 'come', 'thence', 'slay', 'men', 'cloud', 'Deborah', 'endued', 'last', 'yielding', 'sanctified', 'floc', 'Heaven', 'signet', 'bless', 'spi', 'Be', 'things', 'bade', 'female', 'perish', 'Euphrat', 'Zilpah', 'interpreter', 'He', 'spies', 'captive', 'do', 'dealt', 'Moreover', 'Jemuel', 'sinners', 'openly', 'Pau', 'Said', 'thousands', 'pottage', 'Spake', 'wo', 'brethren', 'clave', 'suffered', 'spare', 'sheaf', 'renown', 'respect', 'Twelve', 'sight', 'gat', 'dwelt', 'bowing', 'Hinder', 'Shinab', 'purposing', 'fle', 'have', 'Tidal', 'artificer', 'head', 'ninety', 'commune', 'husbandman', 'Haste', 'journeyed', 'beast', 'Rehoboth', 'Jamin', 'four', 'dressed', 'Mizpah', 'urged', 'hand', 'Japhe', 'pitch', 'wherewith', 'business', 'laded', 'Save', 'thousand', 'fruitful', 'lead', 'held', 'Abimael', 'secret', 'perfect', 'or', 'Ishmael', 'younge', 'Hast', 'about', 'smoke', 'Discern', 'think', 'back', 'summer', 'Midian', 'pluckt', 'hastily', 'nineteen', 'Zoar', 'as', 'comi', 'laugh', 'possessions', 'poverty', 'findest', 'daughter', 'captives', 'stuff', 'booths', 'kinds', 'birds', 'merchant', 'Jahzeel', 'lads', 'chose', 'speaking', 'hil', 'hurt', 'found', 'gathered', 'voi', 'Tiras', 'reign', 'fallen', 'treasure', 'wittingly', 'enquire', 'loins', 'sevenfold', 'mi', 'fifteen', 'rain', 'lion', 'milk', 'coming', 'exchange', 'spent', 'divine', 'Rosh', 'until', 'vessels', 'failed', 'set', 'forbid', 'Kedemah', 'stricken', 'possessor', 'sojourner', 'Edomites', 'desired', 'stronger', 'reigned', 'activity', 'pressed', 'pleasure', 'fulfilled', 'vestures', 'touch', 'hundredfo', 'Nebajoth', 'whereon', 'everlasting', 'Lot', 'tak', 'Shepho', 'trough', 'from', 'sword', 'deceiver', 'right', 'watered', 'know', 'wit', 'provision', 'biteth', 'rider', 'LORD', 'womenservants', 'Where', 'day', 'Thy', 'under', 'thing', 'shed', 'males', 'Yea', 'soon', 'bundles', 'Shall', 'dipped', 'built', 'ungirded', 'Sodom', 'Gatam', 'Pinon', 'tree', 'In', 'anything', 'own', 'sad', 'honour', 'visited', 'Sered', 'strakes', 'salvation', 'tithes', 'Eden', 'Avith', 'profit', 'th', 'emptied', 'rested', 'Bedad', 'surely', 'westwa', 'sought', 'fill', 'Uzal', 'ir', 'Forasmuch', 'when', 'vowed', 'bodies', 'but', 'harlot', 'pla', 'Zaavan', 'hairy', 'Naamah', 'whelp', 'purchased', 'G', 'Dishan', 'butler', 'liveth', 'walking', 'Fill', 'counted', 'Shechem', 'Jimnah', 'should', 'command', 'Our', 'breed', 'breath', 'keep', 'Lift', 'Beriah', 'inhabitants', 'ewe', 'upright', 'surety', 'selfwill', 'are', 'loved', 'leave', 'solemnly', 'possession', 'establish', 'taken', 'sawest', 'true', 'Arphaxad', 'bitter', 'sustained', 'person', 'Man', 'carried', 'Eno', 'get', 'yea', 'south', 'After', 'hastened', 'Gad', 'doer', 'haven', 'requite', 'mess', 'hold', 'messengers', 'bow', 'bed', 'Machpelah', 'amongst', 'Surely', 'bake', 'sake', 'Hitti', 'For', 'manner', 'Phichol', 'Hebrew', 'bank', 'walketh', 'Kadmonites', 'towns', 'strengthened', 'peop', 'blessings', 'tarried', 'dukes', 'commandment', 'lived', 'Syrian', 'burdens', 'widow', 'canst', 'assembly', 'worship', 'sir', 'Pildash', 'Magog', 'Kenizzites', 'dwelled', 'Medan', 'Mehetabel', 'fie', 'bird', 'Obal', 'lovest', 'badest', 'age', 'departing', 'ears', 'Sheba', 'unleavened', 'smelled', 'seas', 'grace', 'sweet', 'touching', 'fatfleshed', 'tender', 'truly', 'While', 'gift', 'earth', 'heap', 'Serah', 'quart', 'Kedar', 'ear', 'clo', 'Amal', 'ark', 'forgotten', 'sakes', 'concerning', 'Epher', 'rods', 'Hamathite', 'knowledge', 'cannot', 'lambs', 'On', 'therein', 'where', 'Look', 'between', 'Jidlaph', 'beside', 'remained', 'six', 'Reuben', 'storehouses', 'elders', 'Jabbok', 'arrayed', 'two', 'sixteen', 'Hirah', 'tidings', 'restrained', 'Bela', 'silv', 'rent', 'What', 'thither', 'Potiphar', 'younger', 'white', 'deceived', 'befell', 'learned', 'vineyard', 'firstborn', 'buryingplace', 'citi', 'getting', 'hairs', 'shot', 'no', 'scattered', 'communing', 'must', 'kissed', 'These', 'dungeon', 'flo', 'whose', 'curse', 'formed', 'hide', 'saith', 'Diklah', 'liest', 'sorrow', 'Shem', 'having', 'Meshech', 'grown', 'long', 'piece', 'kids', 'this', 'reason', 'roll', 'declare', 'attained', 'obeisance', 'beginning', 'gotten', 'verily', 'nig', 'thoroughly', 'finish', 'many', 'ruled', 'Hear', 'shewed', 'thine', 'wept', 'weep', 'go', 'stars', 'gutters', 'secretly', 'Zar', 'subdue', 'willing', 'place', 'smell', 'looked', 'Lay', 'Jacob', '.)', 'with', 'hotly', 'our', 'marvelled', 'Irad', 'river', 'comest', 'labour', 'jewels', 'cold', 'order', 'A', 'strive', 'married', 'travailed', 'land', 'Zebul', 'flocks', 'oxen', 'bakemeats', 'roof', 'Horites', 'Mishma', 'Then', 'Jegarsahadutha', 'prevail', 'noon', 'Hemdan', 'instruments', 'am', 'Lud', 'mean', 'multiply', 'down', 'anguish', 'fast', 'Asshurim', 'Enos', 'Bilhah', 'garments', 'Lest', 'Tamar', 'Huz', 'Isui', 'charge', 'Up', 'overthrew', 'strange', 'former', 'Shuah', 'mark', 'Zeboiim', 'waxed', 'interpret', 'Iram', 'Zemarite', 'killed', 'Jeush', 'water', 'brook', 'Nahath', 'feeble', 'Haggi', 'made', 'fear', 'asked', 'sixth', 'played', 'horse', 'second', 'opened', 'childless', 'Shobal', 'hire', 'bak', 'priests', 'wander', 'vagabond', 'Jetheth', 'sevens', 'seeing', 'help', 'Elah', 'Egyptian', 'appointed', 'removing', 'thicket', 'Hereby', 'time', 'blossoms', 'fatness', 'Unto', 'laden', 'lingered', 'ourselves', 'Babel', 'Enmishpat', 'weig', 'Aner', 'nati', 'didst', 'broth', 'lan', 'inheritance', 'devour', 'sorely', 'rebuked', 'forget', 'nine', 'wick', 'bruise', 'rank', 'meat', 'Bethuel', 'decreased', 'fo', 'His', 'sent', 'continually', 'deprived', 'that', 'Manass', 'beget', 'matter', 'couched', 'moveth', 'Methusa', 'Esau', 'Earth', 'ea', 'Eve', 'earing', 'Naphish', 'wild', 'heads', 'Ephraim', 'Zuzims', 'daught', 'Eshban', 'Set', 'without', 'skins', 'Hivite', 'ne', 'fourteenth', 'strong', 'Er', 'wi', 'prospered', 'loss', 'nigh', 'Forgive', 'none', 'exceeding', 'hazel', 'Speak', 'carcases', 'Dinah', 'reproa', 'co', 'searched', 'Ludim', 'thread', 'Timna', 'abode', 'despised', 'servant', 'thy', 'fetch', 'Potipherah', 'buy', 'descending', 'plant', 'first', 'hunter', 'still', 'tar', 'provide', 'spee', 'al', 'Lahairoi', 'sojourn', 'uncovered', 'Peniel', 'sackcloth', 'haste', 'fa', 'part', 'colours', 'Joktan', 'beasts', 'guilty', 'loveth', 'God', 'anoth', 'daughte', 'seekest', 'dunge', 'Sabtech', 'occasion', 'Sarah', 'just', 'Ararat', 'Penuel', 'entreated', 'laws', 'affliction', 'year', 'utmost', 'fled', 'oil', 'Onan', 'likene', 'quiver', 'instructor', 'Nod', 'youth', 'An', 'Mahalaleel', 'goa', 'hast', 'ash', 'blameless', 'north', 'process', 'wrong', 'scarlet', 'goat', 'Egy', 'physicians', 'altogether', 'blessed', 'Euphrates', 'Ephah', 'overseer', 'childr', 'Elbethel', 'greatly', 'kiss', 'Shuni', 'afraid', 'Anamim', 'child', 'Emins', 'Spirit', 'kneel', 'weight', 'slayeth', 'Asher', 'Baalhanan', 'evening', 'mountains', 'Aholibamah', 'plagues', 'here', 'hardly', 'Until', 'preserved', 'these', 'mine', 'drank', 'elder', 'handmaids', 'peaceable', 'saved', 'pigeon', 'why', 'breadth', 'pursued', 'grief', 'brick', 'cattle', 'We', 'travail', 'Zimran', 'Gershon', 'Eliezer', 'Tubal', 'stalk', 'They', 'door', 'Angel', 'tongue', 'meal', 'behold', 'dreadful', 'issue', 'vale', 'reward', 'creeping', 'field', 'rib', 'Duke', 'dreamed', 'wherein', 'shaved', 'Karnaim', 'forgive', 'isles', 'forward', 'sheddeth', 'delight', 'Beware', 'eastward', 'Out', 'spoken', 'foals', 'removed', 'nights', 'displease', 'halted', 'wheat', 'food', 'circumcis', 'blessi', 'reached', 'watering', 'throne', 'plagued', 'overtake', 'Whoso', 'worth', 'Birsha', 'sacrifice', 'spotted', 'Laban', 'nothing', 'Judge', 'ways', 'hence', 'herb', 'waited', 'By', 'eventide', 'void', 'youngest', 'Dumah', 'grieved', 'Midianites', 'savoury', 'silver', 'near', 'Dodanim', 'Moab', 'butlers', 'enmity', 'Arbah', 'Shaveh', 'thyself', 'stript', 'doth', 'Sitnah', 'worthy', 'served', 'length', 'Tola', 'in', 'Ohad', 'their', 'voice', 'trees', 'east', 'torn', 'accept', 'concubine', 'Get', 'substance', 'truth', 'pitched', 'perpetual', 'Elishah', 'lawgiver', 'conspired', 'Deliver', 'whether', 'rise', 'wine', 'buried', 'add', 'thigh', 'foolishly', 'Canaanite', 'n', 'thirty', 'of', 'goods', 'least', 'followed', 'Temani', 'Gaham', 'women', 'inhabited', 'army', 'fou', 'sold', 'At', 'wearied', 'Damascus', 'mouths', 'Machir', 'duke', 'always', 'Every', 'winged', 'blindness', 'above', 'like', 'shall', 'coffin', 'prophet', 'Lo', 'gray', 'Melchizedek', 'presented', 'fountain', 'Woman', 'ripe', 'restore', 'trained', 'morter', 'again', 'abundantly', 'little', 'reviv', 'conceal', 'curseth', 'grass', 'afterward', 'wrought', 'herein', 'favour', 'mourned', 'h', 'years', 'Hazezontamar', 'number', 'known', 'Nahor', 'selfsame', 'besought', 'firstlings', 'plain', 'west', 'bough', 'fed', 'repenteth', 'certainly', 'pitcher', 'Dedan', 'hearkened', 'bondman', 'Zibeon', 'whom', 'depart', 'belong', 'poor', 'Judith', 'stolen', 'twelve', 'Zerah', 'Send', 'She', 'denied', 'So', 'eaten', 'art', 'fierce', 'spoil', 'kine', 'Nay', 'aga', 'high', 'hath', 'birthright', 'nuts', 'spilled', 'kid', 'enemies', 'prey', 'woman', 'wilderness', 'Shel', 'hands', 'on', 'whole', 'Japheth', 'mandrakes', 'chariot', 'cleave', 'heard', 'w', 'saddled', 'committed', 'Atad', '!', 'kn', 'health', 'hundred', 'grievous', 'to', 'more', 'sewed', 'purchase', 'la', 'remove', 'Matred', 'whence', 'intreated', 'appoint', 'mighty', 'named', 'visit', 'may', 'errand', 'straitly', 'Massa', 'captain', 'hous', 'themselves', 'stink', 'li', 'Amalek', 'hearken', 'valley', 'darkne', 'enough', 'vowedst', 'slimepits', 'Edom', 'sin', 'wiv', 'aloud', 'drought', 's', 'Calneh', 'violently', 'Seeing', 'Resen', 'stopped', 'each', 'home', 'Ehi', 'filled', 'hunt', 'got', 'doubled', 'sepulchre', 'sadly', 'Slay', 'fetched', 'city', 'Arkite', 'mention', ';)', 'imagination', 'na', 'drunken', 'company', 'darkness', 'begat', 'store', 'blesseth', 'form', 'Almodad', 'drew', 'cru', 'slain', 'cursed', 'them', 'Akan', 'gr', 'Goshen', 'kings', 'Appoint', 'Manahath', 'heav', 'begettest', 'henceforth', 'ask', 'very', 'likeness', 'height', 'putting', 'up', 'blasted', 'face', 'kindred', 'daughers', 'messes', 'fellow', 'angry', 'son', 'given', 'places', 'heavens', 'Accad', 'dove', 'Adullamite', 'Shebah', 'she', 'mind', 'knees', 'the', 'foot', 'Elon', 'Hori', 'Moriah', 'vail', 'bulls', 'mercy', 'Mehujael', 'Philistim', 'Kiriathaim', 'Raamah', 'Timnah', 'Lamech', 'reproach', 'most', 'Bow', 'lamentati', 'Moabites', 'Shammah', 'wealth', 'creature', 'Mizz', 'salt', 'will', 'blessing', 'Dinhabah', 'reserved', 'household', 'cunning', 'uncircumcised', 'merry', 'sons', 'can', 'Haran', 'end', 'cry', 'eldest', 'Succoth', 'Jahleel', 'lighted', 'sprung', 'traffick', 'steal', 'Swear', 'Fulfil', 'Shimron', 'restored', 'closed', 'Kittim', 'Zo', 'dust', 'worshipped', 'gifts', 'Almighty', 'thereby', 'cubits', 'If', 'ceased', 'LO', 'Sidon', 'fruit', 'seventh', 'fifth', 'heart', 'balm', 'could', 'serva', 'eleven', 'deep', 'fishes', 'fowls', 'returned', 'Because', 'speckled', 'waters', 'Beno', 'themselv', 'fat', 'replenish', 'dainties', 'Put', 'garden', 'cut', 'pea', 'hollow', 'room', 'Know', 'past', 'Girgasite', 'gave', 'take', 'olive', 'sun', 'Therefore', 'service', 'grapes', 'sacks', 'Gerar', 'Havilah', 'Stand', 'brink', 'yield', 'away', 'a', 'stories', 'nation', 'one', 'fly', 'pleased', 'concubi', 'Beeri', 'shekels', 'put', 'Bring', 'Hamul', 'needeth', 'therefore', 'side', 'integrity', 'thi', 'Mibsam', 'shalt', 'favoured', 'Tema', 'mou', 'commended', 'When', 'Hobah', 'morning', 'backward', 'Reub', 'creepeth', 'ringstraked', 'welfare', 'toward', 'faults', 'lightly', 'Except', 'naked', 'avenged', 'feebler', 'stole', 'bring', 'goeth', 'feed', 'Bered', 'Me', 'Cast', 'lentiles', 'brought', 'stretched', 'redeemed', 'horses', 'portion', 'flaming', 'Zepho', 'good', 'Timnath', 'righteous', 'struggled', 'Amorite', 'brother', 'Ye', 'builded', 'ladder', 'serpent', 'Take', 'chi', 'tents', 'lade', 'Zaphnathpaaneah', 'fathers', 'fire', 'send', 'changes', 'Canaanites', 'meadow', 'keeper', 'Ophir', 'countenance', 'fashion', 'Keturah', 'chesnut', 'Asshur', 'Cherubims', 'needs', 'Rameses', 'mother', 'herds', 'Rebek', 'deal', 'morsel', 'catt', 'Egyptia', 'garmen', 'bundle', 'Naphtuhim', 'sinew', 'beyond', 'terror', 'concubines', 'speak', 'Arvadite', 'foal', 'breathed', 'Cain', 'handle', 'some', 'compasseth', 'endure', 'Tarshish', 'Isa', 'accepted', 'else', 'Hittite', 'cease', 'songs', 'ye', 'grave', 'tribute', 'is', 'oth', 'occupation', 'Why', 'eatest', 'unit', 'Gilead', 'Teman', 'spread', 'ribs', 'lifted', 'speckl', 'smite', 'wentest', 'stay', 'light', 'sacrifices', 'country', 'hearts', 'princes', 'Paran', 'begin', 'doing', 'rewarded', 'Leummim', 'since', 'dine', 'rest', 'Sheleph', 'for', 'against', 'Rephaims', 'rode', 'Do', 'wells', 'ward', 'bread', 'Reuel', 'fleddest', 'garment', 'ravin', 'Gentiles', 'edge', 'bone', 'change', 'obtain', 'famine', 'doubt', 'milch', 'trespass', 'strength', 'Canaanitish', 'officers', 'branches', 'saying', 'nostrils', 'Maachah', 'oa', 'burn', 'thought', 'eyes', 'offering', 'Assyria', 'grisl', 'tenor', 'died', 'chariots', 'millions', 'shear', 'Simeon', 'feast', 'weaned', 'Ephra', 'live', 'choice', 'before', 'either', 'it', 'whither', 'multitude', 'forgat', 'gavest', ')', 'Ishmeelites', 'midst', 'sixty', 'tower', 'threescore', 'Bilhan', 'wa', 'heat', 'ev', 'wages', 'Hamor', 'experience', 'Also', 'withhold', 'Abraham', 'shrank', 'merciful', 'dwe', 'early', 'Chesed', 'office', 'Zebulun', 'hills', 'Mesha', 'destitute', 'Shiloh', 'earring', 'That', 'Allonbachuth', 'Perizzit', 'might', 'aprons', 'befall', 'round', 'Calah', 'afterwards', 'shepherds', 'From', 'meanest', 'Hebrews', 'thou', 'peaceably', 'Am', 'envied', 'bad', 'than', 'maidservants', 'pilled', 'Hanoch', 'sist', 'flesh', 'servan', 'thereof', 'heifer', 'Kohath', 'brimstone', 'Areli', 'Some', 'But', 'progenitors', 'leaves', 'covered', 'Say', 'Jared', 'arise', 'Masrekah', '.', 'Letushim', 'Ham', 'submit', 'months', 'Is', 'meant', 'cool', 'generation', 'Ashkenaz', 'unto', 'house', 'token', 'Elparan', 'consume', 'felt', 'lest', 'wise', 'brown', 'Isaac', 'bereaved', 'sheep', 'o', 'covenant', 'love', 'stone', 'tiller', 'golden', 'corn', 'Zidon', 'Go', 'Chezib', 'believed', 'overspread', 'sea', 'furnace', 'badne', 'conceived', 'sore', 'stranger', 'borders', 'si', 'wicked', 'Hemam', 'slaughter', 'Levi', 'Girgashites', 'answered', 'virgin', 'Methusael', 'seeth', 'hor', 'Luz', 'overthrow', 'erected', 'prisoners', 'divineth', 'week', 'air', 'oak', 'lean', 'southward', 'well', 'All', 'camels', 'dream', 'faces', 'Padan', 'This', 'went', 'straw', 'all', 'Mezahab', 'among', 'tribes', 'drove', 'days', 'not', 'furniture', 'build', 'laid', 'leaf', 'mist', 'Not', 'Are', 'Ajah', 'going', 'Sinite', 'Rebekah', 'shepherd', 'dale', 'lying', 'meditate', 'bondmen', 'thereon', 'mountain', 'finished', 'reach', 'separated', 'through', 'bondwoman', 'serve', 'chain', 'sit', 'Night', 'myself', 'Seba', 'provender', 'lords', 'touched', "'", 'ou', 'mount', 'shadow', 'Sabtah', 'Aram', 'carry', 'consumed', 'Judah', 'old', 'Nineveh', 'nor', 'audience', 'hind', 'spe', 'drinketh', 'would', 'yesternight', 'appease', 'work', 'spoiled', 'horsemen', 'Joseph', 'Shinar', 'numbered', 'visions', 'Jokshan', 'empty', 'tr', 'grap', 'beguiled', 'sure', 'created', 'beautiful', 'covering', 'victuals', 'whensoever', 'much', 'stones', 'point', 'Heth', 'there', 'cruelty', 'departed', 'both', 'hate', 'To', 'righteousness', 'Thou', 'camel', 'enter', 'ascending', 'Bless', 'power', 'images', 'fell', 'Arodi', 'witness', 'binding', 'divide', 'staff', 'Ashbel', 'escape', 'told', 'mock', 'tempt', 'Madai', 'next', 'servants', 'And', 'mayest', 'Ithran', 'habitations', 'circumcise', 'calf', 'Art', 'asketh', 'Bethlehem', 'so', 'male', '(', 'threshingfloor', 'Ephrath', 'wife', 'mischief', 'burnt', 'betwixt', 'separate', 'green', 'sto', 'pasture', 'Only', 'her', 'plains', 'walk', 'grisled', 'circumcised', 'hang', 'lodge', 'offended', 'twins', 'plenty', 'Whence', 'feared', 'rooms', 'was', 'fury', 'butlership', 'digged', 'night', 'pursue', 'boldly', 'wast', 'way', 'words', 'fainted', 'ghost', 'Horite', 'ashamed', 'Binding', 'subtilty', 'hard', 'wolf', 'longedst', 'yourselves', 'Jezer', 'Mahalath', 'fema', 'Gihon', 'received', 'wotteth', 'said', 'guiding', 'Hai', 'displeased', 'With', 'fro', 'Blessed', 'sware', 'shekel', 'season', 'parts', 'leaped', 'rule', 'few', 'whoredom', 'toil', 'Shemeber', 'shrubs', 'pilgrimage', 'lord', 'indeed', 'Mahanaim', 'and', 'Thirty', 'Aran', 'established', 'though', 'gracious', 'Ezer', 'Kor', 'sinning', 'whereby', 'off', 'besides', 'Phuvah', 'butter', 'which', 'venison', 'journeys', 'into', 'Noah', 'obey', 'Cainan', 'destroyed', 'we', 'pleaseth', 'statutes', 'offer', 'what', 'ever', 'EleloheIsrael', 'yielded', 'Zohar', 'wood', 'honourable', 'twice', 'moved', 'sheweth', 'spicery', 'wrath', 'defiled', 'Carmi', 'compassed', 'Amraphel', 'desolate', 'any', 'seem', 'ten', 'charged', 'Hul', 'Casluhim', 'best', 'call', 'who', 'appe', 'Arioch', 'ram', 'marriages', 'conceive', 'Benjamin', 'dress', 'coat', 'Belah', 'Huppim', 'measures', 'Thus', 'Kirjatharba', 'Bozrah', 'Jubal', 'us', 'colt', 'abated', 'consent', 'verified', 'breasts', ';', 'twel', 'husba', 'guard', 'O', 'speaketh', 'street', 'archers', 'breaking', 'language', 'master', 'speedily', 'fall', 'ma', 'understand', 'lift', 'preserve', 'death', 'at', 'priest', 'name', 'Iscah', 'tillest', 'joined', 'archer', 'morever', 'shamed', 'altar', 'half', 'lieth', 'Gomer', 'corrupted', 'Peace', 'lamp', 'Ard', 'lo', 'Give', 'forth', 'hid', 'did', 'cities', 'Jebusites', 'Ziphion', 'seemed', 'became', 'my', 'word', 'Mamre', 'comfort', 'falsely', 'wagons', 'then', 'discerned', 'lack', 'worse', 'cast', 'better', 'alone', 'Naphtali', 'chamber', 'bands', 'hadst', 'sow', 'lamb', 'abomination', 'passed', 'handmaidens', 'rose', 'whatsoever', 'wickedly', 'oversig', 'Day', 'generations', 'cup', 'whales', 'Jordan', 'Assyr', 'alo', 'cried', 'cave', 'daughters', 'lie', 'Perizzite', 'officer', 'mourning', 'deed', 'conception', 'aw', 'Admah', 'were', 'Escape', 'Hagar', 'fail', 'rul', 'placed', 'Seir', 'remaineth', 'throughout', 'sle', 'fai', 'shoulder', 'wash', 'Kenaz', 'double', 'ended', 'midwife', 'every', 'ki', 'neither', 'slime', 'Abidah', 'fearest', 'peace', 'fourscore', 'kindled', 'Salah', 'joint', 'scatter', 'wouldest', 'pris', 'bear', 'mast', 'colts', 'sleep', 'absent', 'goest', 'seen', 'households', 'foreskin', 'bound', 'bottle', 'menservants', 'Both', 'such', 'pillows', 'stayed', 'offerings', 'possess', 'tops', 'Gaza', 'baskets', 'met', 'multiplying', 'Make', 'myrrh', 'remember', 'Ashteroth', 'Guni', 'whereof', 'called', 'damsels', 'blame', 'rich', 'those', 'thirteenth', 'Sod', 'hindermost', 'Malchiel', 'tru', 'fath', 'dwell', 'Fear', 'posterity', 'receive', 'risen', 'heaven', 'greater', 'herself', 'rams', 'Merari', 'whomsoever', 'vengeance', 'knew', 'being', 'Hadoram', 'glory', 'Hazarmaveth', 'Moreh', 'refrain', 'nurse', 'wilt', 'praise', 'Korah', 'pieces', 'Two', 'Mam', 'budded', 'savour', 'Bethel', 'foremost', 'bdellium', 'wrestled', 'nations', 'father', 'him', 'ran', 'Behold', 'Benam', 'Shalt', 'deferred', 'Gether', 'remembered', 'according', 'appear', 'ford', 'harp', 'twentieth', 'shortly', 'turn', 'leap', 'governor', 'castles', 'rouse', 'divided', 'eighty', 'tarry', 'third', 'graciously', 'certain', 'famished', 'Issachar', 'confound', 'Ephron', 'judge', 'embraced', 'clean', 'heed', 'honey', 'Din', 'prince', 'Remain', 'times', 'Kenites', 'deeds', 'slew', 'mightier', 'Lotan', 'plenteousness', 'red', 'sac', 'Even', 'swear', 'folly', 'how', 'evil', 'handmaid', 'money', 'Hushim', 'wor', 'top', 'die', 'Adam', 'herdmen', 'obeyed', 'kindly', 'fourteen', 'Achbor', 'Pass', 'toucheth', 'caused', 'turned', 'horror', 'gard', 'prevailed', 'sporting', 'wondering', 'weary', 'shore', 'Manasseh', 'required', 'Jerah', 'countries', 'gre', 'fathe', 'boug', 'corrupt', 'mourn', 'earrings', 'moving', 'Caphtorim', 'interpretation', 'giants', 'dominion', 'Chedorlaomer', 'The', 'hundredth', 'Shed', 'seventeenth', 'herd', 'meet', 'husband', 'baker', 'plenteous', 'steward', 'Adbeel', 'wall', 'doe', 'gathering', 'grow', 'barren', 'return', 'seest', 'betimes', 'softly', 'same', 'y', 'freely', 'fountains', 'Onam', 'Ishuah', 'three', 'turtledove', 'talking', 'morrow', 'Dishon', 'broken', 'Ahuzzath', 'Ethiopia', 'thistles', 'riches', 'Egyptians', 'small', 'spake', 'Hezron', 'kill', 'full', 'There', 'Galeed', 'awoke', 'Cana', 'nakedness', 'dignity', 'repented', 'acknowledged', 'wat', 'border', 'folk', 'by', 'widowhood', 'eyed', 'peradventure', 'Wherefore', 'organ', 'saidst', 'hasted', 'suck', 'fowl', 'eight', 'eat', 'Mibzar', 'e', 'refused', 'Shur', 'violence', 'thirteen', 'smooth', 'cubit'}
clear
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
sorted(set(text3))
['!', "'", '(', ')', ',', ',)', '.', '.)', ':', ';', ';)', '?', '?)', 'A', 'Abel', 'Abelmizraim', 'Abidah', 'Abide', 'Abimael', 'Abimelech', 'Abr', 'Abrah', 'Abraham', 'Abram', 'Accad', 'Achbor', 'Adah', 'Adam', 'Adbeel', 'Admah', 'Adullamite', 'After', 'Aholibamah', 'Ahuzzath', 'Ajah', 'Akan', 'All', 'Allonbachuth', 'Almighty', 'Almodad', 'Also', 'Alvah', 'Alvan', 'Am', 'Amal', 'Amalek', 'Amalekites', 'Ammon', 'Amorite', 'Amorites', 'Amraphel', 'An', 'Anah', 'Anamim', 'And', 'Aner', 'Angel', 'Appoint', 'Aram', 'Aran', 'Ararat', 'Arbah', 'Ard', 'Are', 'Areli', 'Arioch', 'Arise', 'Arkite', 'Arodi', 'Arphaxad', 'Art', 'Arvadite', 'As', 'Asenath', 'Ashbel', 'Asher', 'Ashkenaz', 'Ashteroth', 'Ask', 'Asshur', 'Asshurim', 'Assyr', 'Assyria', 'At', 'Atad', 'Avith', 'Baalhanan', 'Babel', 'Bashemath', 'Be', 'Because', 'Becher', 'Bedad', 'Beeri', 'Beerlahairoi', 'Beersheba', 'Behold', 'Bela', 'Belah', 'Benam', 'Benjamin', 'Beno', 'Beor', 'Bera', 'Bered', 'Beriah', 'Bethel', 'Bethlehem', 'Bethuel', 'Beware', 'Bilhah', 'Bilhan', 'Binding', 'Birsha', 'Bless', 'Blessed', 'Both', 'Bow', 'Bozrah', 'Bring', 'But', 'Buz', 'By', 'Cain', 'Cainan', 'Calah', 'Calneh', 'Can', 'Cana', 'Canaan', 'Canaanite', 'Canaanites', 'Canaanitish', 'Caphtorim', 'Carmi', 'Casluhim', 'Cast', 'Cause', 'Chaldees', 'Chedorlaomer', 'Cheran', 'Cherubims', 'Chesed', 'Chezib', 'Come', 'Cursed', 'Cush', 'Damascus', 'Dan', 'Day', 'Deborah', 'Dedan', 'Deliver', 'Diklah', 'Din', 'Dinah', 'Dinhabah', 'Discern', 'Dishan', 'Dishon', 'Do', 'Dodanim', 'Dothan', 'Drink', 'Duke', 'Dumah', 'Earth', 'Ebal', 'Eber', 'Edar', 'Eden', 'Edom', 'Edomites', 'Egy', 'Egypt', 'Egyptia', 'Egyptian', 'Egyptians', 'Ehi', 'Elah', 'Elam', 'Elbethel', 'Eldaah', 'EleloheIsrael', 'Eliezer', 'Eliphaz', 'Elishah', 'Ellasar', 'Elon', 'Elparan', 'Emins', 'En', 'Enmishpat', 'Eno', 'Enoch', 'Enos', 'Ephah', 'Epher', 'Ephra', 'Ephraim', 'Ephrath', 'Ephron', 'Er', 'Erech', 'Eri', 'Es', 'Esau', 'Escape', 'Esek', 'Eshban', 'Eshcol', 'Ethiopia', 'Euphrat', 'Euphrates', 'Eve', 'Even', 'Every', 'Except', 'Ezbon', 'Ezer', 'Fear', 'Feed', 'Fifteen', 'Fill', 'For', 'Forasmuch', 'Forgive', 'From', 'Fulfil', 'G', 'Gad', 'Gaham', 'Galeed', 'Gatam', 'Gather', 'Gaza', 'Gentiles', 'Gera', 'Gerar', 'Gershon', 'Get', 'Gether', 'Gihon', 'Gilead', 'Girgashites', 'Girgasite', 'Give', 'Go', 'God', 'Gomer', 'Gomorrah', 'Goshen', 'Guni', 'Hadad', 'Hadar', 'Hadoram', 'Hagar', 'Haggi', 'Hai', 'Ham', 'Hamathite', 'Hamor', 'Hamul', 'Hanoch', 'Happy', 'Haran', 'Hast', 'Haste', 'Have', 'Havilah', 'Hazarmaveth', 'Hazezontamar', 'Hazo', 'He', 'Hear', 'Heaven', 'Heber', 'Hebrew', 'Hebrews', 'Hebron', 'Hemam', 'Hemdan', 'Here', 'Hereby', 'Heth', 'Hezron', 'Hiddekel', 'Hinder', 'Hirah', 'His', 'Hitti', 'Hittite', 'Hittites', 'Hivite', 'Hobah', 'Hori', 'Horite', 'Horites', 'How', 'Hul', 'Huppim', 'Husham', 'Hushim', 'Huz', 'I', 'If', 'In', 'Irad', 'Iram', 'Is', 'Isa', 'Isaac', 'Iscah', 'Ishbak', 'Ishmael', 'Ishmeelites', 'Ishuah', 'Isra', 'Israel', 'Issachar', 'Isui', 'It', 'Ithran', 'Jaalam', 'Jabal', 'Jabbok', 'Jac', 'Jachin', 'Jacob', 'Jahleel', 'Jahzeel', 'Jamin', 'Japhe', 'Japheth', 'Jared', 'Javan', 'Jebusite', 'Jebusites', 'Jegarsahadutha', 'Jehovahjireh', 'Jemuel', 'Jerah', 'Jetheth', 'Jetur', 'Jeush', 'Jezer', 'Jidlaph', 'Jimnah', 'Job', 'Jobab', 'Jokshan', 'Joktan', 'Jordan', 'Joseph', 'Jubal', 'Judah', 'Judge', 'Judith', 'Kadesh', 'Kadmonites', 'Karnaim', 'Kedar', 'Kedemah', 'Kemuel', 'Kenaz', 'Kenites', 'Kenizzites', 'Keturah', 'Kiriathaim', 'Kirjatharba', 'Kittim', 'Know', 'Kohath', 'Kor', 'Korah', 'LO', 'LORD', 'Laban', 'Lahairoi', 'Lamech', 'Lasha', 'Lay', 'Leah', 'Lehabim', 'Lest', 'Let', 'Letushim', 'Leummim', 'Levi', 'Lie', 'Lift', 'Lo', 'Look', 'Lot', 'Lotan', 'Lud', 'Ludim', 'Luz', 'Maachah', 'Machir', 'Machpelah', 'Madai', 'Magdiel', 'Magog', 'Mahalaleel', 'Mahalath', 'Mahanaim', 'Make', 'Malchiel', 'Male', 'Mam', 'Mamre', 'Man', 'Manahath', 'Manass', 'Manasseh', 'Mash', 'Masrekah', 'Massa', 'Matred', 'Me', 'Medan', 'Mehetabel', 'Mehujael', 'Melchizedek', 'Merari', 'Mesha', 'Meshech', 'Mesopotamia', 'Methusa', 'Methusael', 'Methuselah', 'Mezahab', 'Mibsam', 'Mibzar', 'Midian', 'Midianites', 'Milcah', 'Mishma', 'Mizpah', 'Mizraim', 'Mizz', 'Moab', 'Moabites', 'Moreh', 'Moreover', 'Moriah', 'Muppim', 'My', 'Naamah', 'Naaman', 'Nahath', 'Nahor', 'Naphish', 'Naphtali', 'Naphtuhim', 'Nay', 'Nebajoth', 'Neither', 'Night', 'Nimrod', 'Nineveh', 'Noah', 'Nod', 'Not', 'Now', 'O', 'Obal', 'Of', 'Oh', 'Ohad', 'Omar', 'On', 'Onam', 'Onan', 'Only', 'Ophir', 'Our', 'Out', 'Padan', 'Padanaram', 'Paran', 'Pass', 'Pathrusim', 'Pau', 'Peace', 'Peleg', 'Peniel', 'Penuel', 'Peradventure', 'Perizzit', 'Perizzite', 'Perizzites', 'Phallu', 'Phara', 'Pharaoh', 'Pharez', 'Phichol', 'Philistim', 'Philistines', 'Phut', 'Phuvah', 'Pildash', 'Pinon', 'Pison', 'Potiphar', 'Potipherah', 'Put', 'Raamah', 'Rachel', 'Rameses', 'Rebek', 'Rebekah', 'Rehoboth', 'Remain', 'Rephaims', 'Resen', 'Return', 'Reu', 'Reub', 'Reuben', 'Reuel', 'Reumah', 'Riphath', 'Rosh', 'Sabtah', 'Sabtech', 'Said', 'Salah', 'Salem', 'Samlah', 'Sarah', 'Sarai', 'Saul', 'Save', 'Say', 'Se', 'Seba', 'See', 'Seeing', 'Seir', 'Sell', 'Send', 'Sephar', 'Serah', 'Sered', 'Serug', 'Set', 'Seth', 'Shalem', 'Shall', 'Shalt', 'Shammah', 'Shaul', 'Shaveh', 'She', 'Sheba', 'Shebah', 'Shechem', 'Shed', 'Shel', 'Shelah', 'Sheleph', 'Shem', 'Shemeber', 'Shepho', 'Shillem', 'Shiloh', 'Shimron', 'Shinab', 'Shinar', 'Shobal', 'Should', 'Shuah', 'Shuni', 'Shur', 'Sichem', 'Siddim', 'Sidon', 'Simeon', 'Sinite', 'Sitnah', 'Slay', 'So', 'Sod', 'Sodom', 'Sojourn', 'Some', 'Spake', 'Speak', 'Spirit', 'Stand', 'Succoth', 'Surely', 'Swear', 'Syrian', 'Take', 'Tamar', 'Tarshish', 'Tebah', 'Tell', 'Tema', 'Teman', 'Temani', 'Terah', 'Thahash', 'That', 'The', 'Then', 'There', 'Therefore', 'These', 'They', 'Thirty', 'This', 'Thorns', 'Thou', 'Thus', 'Thy', 'Tidal', 'Timna', 'Timnah', 'Timnath', 'Tiras', 'To', 'Togarmah', 'Tola', 'Tubal', 'Tubalcain', 'Twelve', 'Two', 'Unstable', 'Until', 'Unto', 'Up', 'Upon', 'Ur', 'Uz', 'Uzal', 'We', 'What', 'When', 'Whence', 'Where', 'Whereas', 'Wherefore', 'Which', 'While', 'Who', 'Whose', 'Whoso', 'Why', 'Wilt', 'With', 'Woman', 'Ye', 'Yea', 'Yet', 'Zaavan', 'Zaphnathpaaneah', 'Zar', 'Zarah', 'Zeboiim', 'Zeboim', 'Zebul', 'Zebulun', 'Zemarite', 'Zepho', 'Zerah', 'Zibeon', 'Zidon', 'Zillah', 'Zilpah', 'Zimran', 'Ziphion', 'Zo', 'Zoar', 'Zohar', 'Zuzims', 'a', 'abated', 'abide', 'able', 'abode', 'abomination', 'about', 'above', 'abroad', 'absent', 'abundantly', 'accept', 'accepted', 'according', 'acknowledged', 'activity', 'add', 'adder', 'afar', 'afflict', 'affliction', 'afraid', 'after', 'afterward', 'afterwards', 'aga', 'again', 'against', 'age', 'aileth', 'air', 'al', 'alive', 'all', 'almon', 'alo', 'alone', 'aloud', 'also', 'altar', 'altogether', 'always', 'am', 'among', 'amongst', 'an', 'and', 'angel', 'angels', 'anger', 'angry', 'anguish', 'anointedst', 'anoth', 'another', 'answer', 'answered', 'any', 'anything', 'appe', 'appear', 'appeared', 'appease', 'appoint', 'appointed', 'aprons', 'archer', 'archers', 'are', 'arise', 'ark', 'armed', 'arms', 'army', 'arose', 'arrayed', 'art', 'artificer', 'as', 'ascending', 'ash', 'ashamed', 'ask', 'asked', 'asketh', 'ass', 'assembly', 'asses', 'assigned', 'asswaged', 'at', 'attained', 'audience', 'avenged', 'aw', 'awaked', 'away', 'awoke', 'back', 'backward', 'bad', 'bade', 'badest', 'badne', 'bak', 'bake', 'bakemeats', 'baker', 'bakers', 'balm', 'bands', 'bank', 'bare', 'barr', 'barren', 'basket', 'baskets', 'battle', 'bdellium', 'be', 'bear', 'beari', 'bearing', 'beast', 'beasts', 'beautiful', 'became', 'because', 'become', 'bed', 'been', 'befall', 'befell', 'before', 'began', 'begat', 'beget', 'begettest', 'begin', 'beginning', 'begotten', 'beguiled', 'beheld', 'behind', 'behold', 'being', 'believed', 'belly', 'belong', 'beneath', 'bereaved', 'beside', 'besides', 'besought', 'best', 'betimes', 'better', 'between', 'betwixt', 'beyond', 'binding', 'bird', 'birds', 'birthday', 'birthright', 'biteth', 'bitter', 'blame', 'blameless', 'blasted', 'bless', 'blessed', 'blesseth', 'blessi', 'blessing', 'blessings', 'blindness', 'blood', 'blossoms', 'bodies', 'boldly', 'bondman', 'bondmen', 'bondwoman', 'bone', 'bones', 'book', 'booths', 'border', 'borders', 'born', 'bosom', 'both', 'bottle', 'bou', 'boug', 'bough', 'bought', 'bound', 'bow', 'bowed', 'bowels', 'bowing', 'boys', 'bracelets', 'branches', 'brass', 'bre', 'breach', 'bread', 'breadth', 'break', 'breaketh', 'breaking', 'breasts', 'breath', 'breathed', 'breed', 'brethren', 'brick', 'brimstone', 'bring', 'brink', 'broken', 'brook', 'broth', 'brother', 'brought', 'brown', 'bruise', 'budded', 'build', 'builded', 'built', 'bulls', 'bundle', 'bundles', 'burdens', 'buried', 'burn', 'burning', 'burnt', 'bury', 'buryingplace', 'business', 'but', 'butler', 'butlers', 'butlership', 'butter', 'buy', 'by', 'cakes', 'calf', 'call', 'called', 'came', 'camel', 'camels', 'camest', 'can', 'cannot', 'canst', 'captain', 'captive', 'captives', 'carcases', 'carried', 'carry', 'cast', 'castles', 'catt', 'cattle', 'caught', 'cause', 'caused', 'cave', 'cease', 'ceased', 'certain', 'certainly', 'chain', 'chamber', 'change', 'changed', 'changes', 'charge', 'charged', 'chariot', 'chariots', 'chesnut', 'chi', 'chief', 'child', 'childless', 'childr', 'children', 'chode', 'choice', 'chose', 'circumcis', 'circumcise', 'circumcised', 'citi', 'cities', 'city', 'clave', 'clean', 'clear', 'cleave', 'clo', 'closed', 'clothed', 'clothes', 'cloud', 'clusters', 'co', 'coat', 'coats', 'coffin', 'cold', 'colours', 'colt', 'colts', 'come', 'comest', 'cometh', 'comfort', 'comforted', 'comi', 'coming', 'command', 'commanded', 'commanding', 'commandment', 'commandments', 'commended', 'committed', 'commune', 'communed', 'communing', 'company', 'compassed', 'compasseth', 'conceal', 'conceive', 'conceived', 'conception', 'concerning', 'concubi', 'concubine', 'concubines', 'confederate', 'confound', 'consent', 'conspired', 'consume', 'consumed', 'content', 'continually', 'continued', 'cool', 'corn', 'corrupt', 'corrupted', 'couch', 'couched', 'couching', 'could', 'counted', 'countenance', 'countries', 'country', 'covenant', 'covered', 'covering', 'created', 'creature', 'creepeth', 'creeping', 'cried', 'crieth', 'crown', 'cru', 'cruelty', 'cry', 'cubit', 'cubits', 'cunning', 'cup', 'current', 'curse', 'cursed', 'curseth', 'custom', 'cut', 'd', 'da', 'dainties', 'dale', 'damsel', 'damsels', 'dark', 'darkne', 'darkness', 'daughers', 'daught', 'daughte', 'daughter', 'daughters', 'day', 'days', 'dea', 'dead', 'deal', 'dealt', 'dearth', 'death', 'deceitfully', 'deceived', 'deceiver', 'declare', 'decreased', 'deed', 'deeds', 'deep', 'deferred', 'defiled', 'defiledst', 'delight', 'deliver', 'deliverance', 'delivered', 'denied', 'depart', 'departed', 'departing', 'deprived', 'descending', 'desire', 'desired', 'desolate', 'despised', 'destitute', 'destroy', 'destroyed', 'devour', 'devoured', 'dew', 'did', 'didst', 'die', 'died', 'digged', 'dignity', 'dim', 'dine', 'dipped', 'direct', 'discern', 'discerned', 'discreet', 'displease', 'displeased', 'distress', 'distressed', 'divide', 'divided', 'divine', 'divineth', 'do', 'doe', 'doer', 'doest', 'doeth', 'doing', 'dominion', 'done', 'door', 'dost', 'doth', 'double', 'doubled', 'doubt', 'dove', 'down', 'dowry', 'drank', 'draw', 'dread', 'dreadful', 'dream', 'dreamed', 'dreamer', 'dreams', 'dress', 'dressed', 'drew', 'dried', 'drink', 'drinketh', 'drinking', 'driven', 'drought', 'drove', 'droves', 'drunken', 'dry', 'duke', 'dukes', 'dunge', 'dungeon', 'dust', 'dwe', 'dwell', 'dwelled', 'dwelling', 'dwelt', 'e', 'ea', 'each', 'ear', 'earing', 'early', 'earring', 'earrings', 'ears', 'earth', 'east', 'eastward', 'eat', 'eaten', 'eatest', 'edge', 'eight', 'eighteen', 'eighty', 'either', 'elder', 'elders', 'eldest', 'eleven', 'else', 'embalm', 'embalmed', 'embraced', 'emptied', 'empty', 'end', 'ended', 'endued', 'endure', 'enemies', 'enlarge', 'enmity', 'enough', 'enquire', 'enter', 'entered', 'entreated', 'envied', 'erected', 'errand', 'escape', 'escaped', 'espied', 'establish', 'established', 'ev', 'even', 'evening', 'eventide', 'ever', 'everlasting', 'every', 'evil', 'ewe', 'ewes', 'exceeding', 'exceedingly', 'excel', 'excellency', 'except', 'exchange', 'experience', 'ey', 'eyed', 'eyes', 'fa', 'face', 'faces', 'fai', 'fail', 'failed', 'faileth', 'fainted', 'fair', 'fall', 'fallen', 'falsely', 'fame', 'families', 'famine', 'famished', 'far', 'fashion', 'fast', 'fat', 'fatfleshed', 'fath', 'fathe', 'father', 'fathers', 'fatness', 'faults', 'favour', 'favoured', 'fear', 'feared', 'fearest', 'feast', 'fed', 'feeble', 'feebler', 'feed', 'feeding', 'feel', 'feet', 'fell', 'fellow', 'felt', 'fema', 'female', 'fetch', 'fetched', 'fetcht', 'few', 'fie', 'field', 'fierce', 'fifteen', 'fifth', 'fifty', 'fig', 'fill', 'filled', 'find', 'findest', 'findeth', 'finding', 'fine', 'finish', 'finished', 'fir', 'fire', 'firmame', 'firmament', 'first', 'firstborn', 'firstlings', 'fish', 'fishes', 'five', 'flaming', 'fle', 'fled', 'fleddest', 'flee', 'flesh', 'flo', 'floc', 'flock', 'flocks', 'flood', 'floor', 'fly', 'fo', 'foal', 'foals', 'folk', 'follow', 'followed', 'following', 'folly', 'food', 'foolishly', 'foot', 'for', 'forbid', 'force', 'ford', 'foremost', 'foreskin', 'forgat', 'forget', 'forgive', 'forgotten', 'form', 'formed', 'former', 'forth', 'forty', 'forward', 'fou', 'found', 'fountain', 'fountains', 'four', 'fourscore', 'fourteen', 'fourteenth', 'fourth', 'fowl', 'fowls', 'freely', 'friend', 'friends', 'fro', 'from', 'frost', 'fruit', 'fruitful', 'fruits', 'fugitive', 'fulfilled', 'full', 'furnace', 'furniture', 'fury', 'gard', 'garden', 'garmen', 'garment', 'garments', 'gat', 'gate', 'gather', 'gathered', 'gathering', 'gave', 'gavest', 'generatio', 'generation', 'generations', 'get', 'getting', 'ghost', 'giants', 'gift', 'gifts', 'give', 'given', 'giveth', 'giving', 'glory', 'go', 'goa', 'goat', 'goats', 'gods', 'goest', 'goeth', 'going', 'gold', 'golden', 'gone', 'good', 'goodly', 'goods', 'gopher', 'got', 'gotten', 'governor', 'gr', 'grace', 'gracious', 'graciously', 'grap', 'grapes', 'grass', 'grave', 'gray', 'gre', 'great', 'greater', 'greatly', 'green', 'grew', 'grief', 'grieved', 'grievous', 'grisl', 'grisled', 'gro', 'ground', 'grove', 'grow', 'grown', 'guard', 'guiding', 'guiltiness', 'guilty', 'gutters', 'h', 'ha', 'habitations', 'had', 'hadst', 'hairs', 'hairy', 'half', 'halted', 'han', 'hand', 'handfuls', 'handle', 'handmaid', 'handmaidens', 'handmaids', 'hands', 'hang', 'hanged', 'hard', 'hardly', 'harlot', 'harm', 'harp', 'harvest', 'hast', 'haste', 'hasted', 'hastened', 'hastily', 'hate', 'hated', 'hath', 'have', 'haven', 'having', 'hazel', 'he', 'head', 'heads', 'healed', 'health', 'heap', 'hear', 'heard', 'hearken', 'hearkened', 'heart', 'hearth', 'hearts', 'heat', 'heav', 'heaven', 'heavens', 'heed', 'heel', 'heels', 'heifer', 'height', 'heir', 'held', 'help', 'hence', 'henceforth', 'her', 'herb', 'herd', 'herdmen', 'herds', 'here', 'herein', 'herself', 'hid', 'hide', 'high', 'hil', 'hills', 'him', 'himself', 'hind', 'hindermost', 'hire', 'hired', 'his', 'hith', 'hither', 'hold', 'hollow', 'home', 'honey', 'honour', 'honourable', 'hor', 'horror', 'horse', 'horsemen', 'horses', 'host', 'hotly', 'hou', 'hous', 'house', 'household', 'households', 'how', 'hundred', 'hundredfo', 'hundredth', 'hunt', 'hunter', 'hunting', 'hurt', 'husba', 'husband', 'husbandman', 'if', 'ill', 'image', 'images', 'imagination', 'imagined', 'in', 'increase', 'increased', 'indeed', 'inhabitants', 'inhabited', 'inherit', 'inheritance', 'iniquity', 'inn', 'innocency', 'instead', 'instructor', 'instruments', 'integrity', 'interpret', 'interpretation', 'interpretations', 'interpreted', 'interpreter', 'into', 'intreat', 'intreated', 'ir', 'is', 'isles', 'issue', 'it', 'itself', 'jewels', 'joined', 'joint', 'journey', 'journeyed', 'journeys', 'jud', 'judge', 'judged', 'judgment', 'just', 'justice', 'keep', 'keeper', 'kept', 'ki', 'kid', 'kids', 'kill', 'killed', 'kind', 'kindled', 'kindly', 'kindness', 'kindred', 'kinds', 'kine', 'king', 'kingdom', 'kings', 'kiss', 'kissed', 'kn', 'knead', 'kneel', 'knees', 'knew', 'knife', 'know', 'knowest', 'knoweth', 'knowing', 'knowledge', 'known', 'la', 'labour', 'lack', 'lad', 'ladder', 'lade', 'laded', 'laden', 'lads', 'laid', 'lamb', 'lambs', 'lamentati', 'lamp', 'lan', 'land', 'lands', 'language', 'large', 'last', 'laugh', 'laughed', 'law', 'lawgiver', 'laws', 'lay', 'lead', 'leaf', 'lean', 'leanfleshed', 'leap', 'leaped', 'learned', 'least', 'leave', 'leaves', 'led', 'left', 'length', 'lentiles', 'lesser', 'lest', 'let', 'li', 'lie', 'lien', 'liest', 'lieth', 'life', 'lift', 'lifted', 'light', 'lighted', 'lightly', 'lights', 'like', 'likene', 'likeness', 'linen', 'lingered', 'lion', 'little', 'live', 'lived', 'lives', 'liveth', 'living', 'lo', 'lodge', 'lodged', 'loins', 'long', 'longedst', 'longeth', 'look', 'looked', 'loose', 'lord', 'lords', 'loss', 'loud', 'love', 'loved', 'lovest', 'loveth', 'lower', 'lying', 'm', 'ma', 'made', 'magicians', 'magnified', 'maid', 'maiden', 'maidservants', 'make', 'male', 'males', 'man', 'mandrakes', 'manner', 'many', 'mark', 'marriages', 'married', 'marry', 'marvelled', 'mast', 'master', 'matter', 'may', 'mayest', 'me', 'mead', 'meadow', 'meal', 'mean', 'meanest', 'meant', 'measures', 'meat', 'meditate', 'meet', 'meeteth', 'men', 'menservants', 'mention', 'merchant', 'merchantmen', 'mercies', 'merciful', 'mercy', 'merry', 'mess', 'messenger', 'messengers', 'messes', 'met', 'mi', 'midst', 'midwife', 'might', 'mightier', 'mighty', 'milch', 'milk', 'millions', 'mind', 'mine', 'mirth', 'mischief', 'mist', 'mistress', 'mock', 'mocked', 'mocking', 'money', 'month', 'months', 'moon', 'more', 'moreover', 'morever', 'morning', 'morrow', 'morsel', 'morter', 'most', 'mother', 'mou', 'mount', 'mountain', 'mountains', 'mourn', 'mourned', 'mourning', 'mouth', 'mouths', 'moved', 'moveth', 'moving', 'much', 'mules', 'multiplied', 'multiply', 'multiplying', 'multitude', 'must', 'my', 'myrrh', 'myself', 'n', 'na', 'naked', 'nakedness', 'name', 'named', 'names', 'nati', 'natio', 'nation', 'nations', 'nativity', 'ne', 'near', 'neck', 'needeth', 'needs', 'neither', 'never', 'next', 'nig', 'nigh', 'night', 'nights', 'nine', 'nineteen', 'ninety', 'no', 'none', 'noon', 'nor', 'north', 'northward', 'nostrils', 'not', 'nothing', 'nought', 'nourish', 'nourished', 'now', 'number', 'numbered', 'numbering', 'nurse', 'nuts', 'o', 'oa', 'oak', 'oath', 'obeisance', 'obey', 'obeyed', 'observed', 'obtain', 'occasion', 'occupation', 'of', 'off', 'offended', 'offer', 'offered', 'offeri', 'offering', 'offerings', 'office', 'officer', 'officers', 'oil', 'old', 'olive', 'on', 'one', 'ones', 'only', 'onyx', 'open', 'opened', 'openly', 'or', 'order', 'organ', 'oth', 'other', 'ou', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'overcome', 'overdrive', 'overseer', 'oversig', 'overspread', 'overtake', 'overthrew', 'overthrow', 'overtook', 'own', 'oxen', 'parcel', 'part', 'parted', 'parts', 'pass', 'passed', 'past', 'pasture', 'path', 'pea', 'peace', 'peaceable', 'peaceably', 'peop', 'people', 'peradventure', 'perceived', 'perfect', 'perform', 'perish', 'perpetual', 'person', 'persons', 'physicians', 'piece', 'pieces', 'pigeon', 'pilgrimage', 'pillar', 'pilled', 'pillows', 'pit', 'pitch', 'pitched', 'pitcher', 'pla', 'place', 'placed', 'places', 'plagued', 'plagues', 'plain', 'plains', 'plant', 'planted', 'played', 'pleasant', 'pleased', 'pleaseth', 'pleasure', 'pledge', 'plenteous', 'plenteousness', 'plenty', 'pluckt', 'point', 'poor', 'poplar', 'portion', 'possess', 'possessi', 'possession', 'possessions', 'possessor', 'posterity', 'pottage', 'poured', 'poverty', 'pow', 'power', 'praise', 'pray', 'prayed', 'precious', 'prepared', 'presence', 'present', 'presented', 'preserve', 'preserved', 'pressed', 'prevail', 'prevailed', 'prey', 'priest', 'priests', 'prince', 'princes', 'pris', 'prison', 'prisoners', 'proceedeth', 'process', 'profit', 'progenitors', 'prophet', 'prosper', 'prospered', 'prosperous', 'protest', 'proved', 'provender', 'provide', 'provision', 'pulled', 'punishment', 'purchase', 'purchased', 'purposing', 'pursue', 'pursued', 'put', 'putting', 'quart', 'quickly', 'quite', 'quiver', 'raiment', 'rain', 'rained', 'raise', 'ram', 'rams', 'ran', 'rank', 'raven', 'ravin', 'reach', 'reached', 'ready', 'reason', 'rebelled', 'rebuked', 'receive', 'received', 'red', 'redeemed', 'refrain', 'refrained', 'refused', 'regard', 'reign', 'reigned', 'remained', 'remaineth', 'remember', 'remembered', 'remove', 'removed', 'removing', 'renown', 'rent', 'repented', 'repenteth', 'replenish', 'report', 'reproa', 'reproach', 'reproved', 'require', 'required', 'requite', 'reserved', 'respect', 'rest', 'rested', 'restore', 'restored', 'restrained', 'return', 'returned', 'reviv', 'reward', 'rewarded', 'ri', 'rib', 'ribs', 'rich', 'riches', 'rid', 'ride', 'rider', 'right', 'righteous', 'righteousness', 'rightly', 'ring', 'ringstraked', 'ripe', 'rise', 'risen', 'riv', 'river', 'rode', 'rods', 'roll', 'rolled', 'roof', 'room', 'rooms', 'rose', 'roughly', 'round', 'rouse', 'royal', 'rul', 'rule', 'ruled', 'ruler', 'rulers', 'run', 's', 'sa', 'sac', 'sack', 'sackcloth', 'sacks', 'sacrifice', 'sacrifices', 'sad', 'saddled', 'sadly', 'said', 'saidst', 'saith', 'sake', 'sakes', 'salt', 'salvation', 'same', 'sanctified', 'sand', 'sat', 'save', 'saved', 'saving', 'savour', 'savoury', 'saw', 'sawest', 'say', 'saying', 'scarce', 'scarlet', 'scatter', 'scattered', 'sceptre', 'sea', 'searched', 'seas', 'season', 'seasons', 'second', 'secret', 'secretly', 'see', 'seed', 'seedtime', 'seeing', 'seek', 'seekest', 'seem', 'seemed', 'seen', 'seest', 'seeth', 'selfsame', 'selfwill', 'sell', 'send', 'sent', 'separate', 'separated', 'sepulchre', 'sepulchres', 'serpent', 'serva', 'servan', 'servant', 'servants', 'serve', 'served', 'service', 'set', 'seven', 'sevenfold', 'sevens', 'seventeen', 'seventeenth', 'seventh', 'seventy', 'sewed', 'sh', 'shadow', 'shall', 'shalt', 'shamed', 'shaved', 'she', 'sheaf', 'shear', 'sheaves', 'shed', 'sheddeth', 'sheep', 'sheepshearers', 'shekel', 'shekels', 'shepherd', 'shepherds', 'shew', 'shewed', 'sheweth', 'shield', 'ships', 'shoelatchet', 'shore', 'shortly', 'shot', 'should', 'shoulder', 'shoulders', 'shouldest', 'shrank', 'shrubs', 'shut', 'si', 'side', 'sight', 'signet', 'signs', 'silv', 'silver', 'sin', 'since', 'sinew', 'sinners', 'sinning', 'sir', 'sist', 'sister', 'sit', 'six', 'sixteen', 'sixth', 'sixty', 'skins', 'slain', 'slaughter', 'slay', 'slayeth', 'sle', 'sleep', 'slept', 'slew', 'slime', 'slimepits', 'small', 'smell', 'smelled', 'smite', 'smoke', 'smoking', 'smooth', 'smote', 'so', 'sod', 'softly', 'sojourn', 'sojourned', 'sojourner', 'sold', 'sole', 'solemnly', 'some', 'son', 'songs', 'sons', 'soon', 'sore', 'sorely', 'sorrow', 'sort', 'sou', 'sought', 'soul', 'souls', 'south', 'southward', 'sow', 'sowed', 'space', 'spake', 'spare', 'spe', 'speak', 'speaketh', 'speaking', 'speckl', 'speckled', 'spee', 'speech', 'speed', 'speedily', 'spent', 'spi', 'spicery', 'spices', 'spies', 'spilled', 'spirit', 'spoil', 'spoiled', 'spoken', 'sporting', 'spotted', 'spread', 'springing', 'sprung', 'staff', 'stalk', 'stand', 'standest', 'stars', 'state', 'statutes', 'stay', 'stayed', 'ste', 'stead', 'steal', 'steward', 'still', 'stink', 'sto', 'stole', 'stolen', 'stone', 'stones', 'stood', 'stooped', 'stopped', 'store', 'storehouses', 'stories', 'straitly', 'strakes', 'strange', 'stranger', 'strangers', 'straw', 'street', 'strength', 'strengthened', 'stretched', 'stricken', 'strife', 'stript', 'strive', 'strong', 'stronger', 'strove', 'struggled', 'stuff', 'subdue', 'submit', 'substance', 'subtil', 'subtilty', 'such', 'suck', 'suffered', 'summer', 'sun', 'supplanted', 'sure', 'surely', 'surety', 'sustained', 'sware', 'swear', 'sweat', 'sweet', 'sword', 'sworn', 'tabret', 'tak', 'take', 'taken', 'talked', 'talking', 'tar', 'tarried', 'tarry', 'teeth', 'tell', 'tempt', 'ten', 'tender', 'tenor', 'tent', 'tenth', 'tents', 'terror', 'th', 'than', 'that', 'the', 'thee', 'their', 'them', 'themselv', 'themselves', 'then', 'thence', 'there', 'thereby', 'therefore', 'therein', 'thereof', 'thereon', 'these', 'they', 'thi', 'thicket', 'thigh', 'thin', 'thine', 'thing', 'things', 'think', 'third', 'thirteen', 'thirteenth', 'thirty', 'this', 'thistles', 'thither', 'thoroughly', 'those', 'thou', 'though', 'thought', 'thoughts', 'thousand', 'thousands', 'thread', 'three', 'threescore', 'threshingfloor', 'throne', 'through', 'throughout', 'thus', 'thy', 'thyself', 'tidings', 'till', 'tiller', 'tillest', 'tim', 'time', 'times', 'tithes', 'to', 'togeth', 'together', 'toil', 'token', 'told', 'tongue', 'tongues', 'too', 'took', 'top', 'tops', 'torn', 'touch', 'touched', 'toucheth', 'touching', 'toward', 'tower', 'towns', 'tr', 'trade', 'traffick', 'trained', 'travail', 'travailed', 'treasure', 'tree', 'trees', 'trembled', 'trespass', 'tribes', 'tribute', 'troop', 'troubled', 'trough', 'troughs', 'tru', 'true', 'truly', 'truth', 'turn', 'turned', 'turtledove', 'twel', 'twelve', 'twentieth', 'twenty', 'twice', 'twins', 'two', 'unawares', 'uncircumcised', 'uncovered', 'under', 'understand', 'understood', 'ungirded', 'unit', 'unleavened', 'until', 'unto', 'up', 'upon', 'uppermost', 'upright', 'upward', 'urged', 'us', 'utmost', 'vagabond', 'vail', 'vale', 'valley', 'vengeance', 'venison', 'verified', 'verily', 'very', 'vessels', 'vestures', 'victuals', 'vine', 'vineyard', 'violence', 'violently', 'virgin', 'vision', 'visions', 'visit', 'visited', 'voi', 'voice', 'void', 'vow', 'vowed', 'vowedst', 'w', 'wa', 'wages', 'wagons', 'waited', 'walk', 'walked', 'walketh', 'walking', 'wall', 'wander', 'wandered', 'wandering', 'war', 'ward', 'was', 'wash', 'washed', 'wast', 'wat', 'watch', 'water', 'watered', 'watering', 'waters', 'waxed', 'waxen', 'way', 'ways', 'we', 'wealth', 'weaned', 'weapons', 'wearied', 'weary', 'week', 'weep', 'weig', 'weighed', 'weight', 'welfare', 'well', 'wells', 'went', 'wentest', 'wept', 'were', 'west', 'westwa', 'whales', 'what', 'whatsoever', 'wheat', 'whelp', 'when', 'whence', 'whensoever', 'where', 'whereby', 'wherefore', 'wherein', 'whereof', 'whereon', 'wherewith', 'whether', 'which', 'while', 'white', 'whither', 'who', 'whole', 'whom', 'whomsoever', 'whoredom', 'whose', 'whosoever', 'why', 'wi', 'wick', 'wicked', 'wickedly', 'wickedness', 'widow', 'widowhood', 'wife', 'wild', 'wilderness', 'will', 'willing', 'wilt', 'wind', 'window', 'windows', 'wine', 'winged', 'winter', 'wise', 'wit', 'with', 'withered', 'withheld', 'withhold', 'within', 'without', 'witness', 'wittingly', 'wiv', 'wives', 'wo', 'wolf', 'woman', 'womb', 'wombs', 'women', 'womenservan', 'womenservants', 'wondering', 'wood', 'wor', 'word', 'words', 'work', 'worse', 'worship', 'worshipped', 'worth', 'worthy', 'wot', 'wotteth', 'would', 'wouldest', 'wounding', 'wrapped', 'wrath', 'wrestled', 'wrestlings', 'wrong', 'wroth', 'wrought', 'y', 'ye', 'yea', 'year', 'yearn', 'years', 'yesternight', 'yet', 'yield', 'yielded', 'yielding', 'yoke', 'yonder', 'you', 'young', 'younge', 'younger', 'youngest', 'your', 'yourselves', 'youth']
len(text3)/len(set(text3))
16.050197203298673
for i in set(text3):
    print(100 * text3.count(i) / len(text3))

0.008935751943526048
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.004467875971763024
0.02010544187293361
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.07818782950585292
0.006701813957644536
0.02233937985881512
0.01116968992940756
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.008935751943526048
0.10276114735054954
0.002233937985881512
0.02010544187293361
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.002233937985881512
1.4475918148512197
0.002233937985881512
0.2546689303904924
0.03574300777410419
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.008935751943526048
0.017871503887052095
0.017871503887052095
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.18318291484228397
0.002233937985881512
0.6299705120185863
0.002233937985881512
0.024573317844696633
0.006701813957644536
0.004467875971763024
0.017871503887052095
0.004467875971763024
0.006701813957644536
0.02233937985881512
0.026807255830578143
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.008935751943526048
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.053614511661156286
0.004467875971763024
0.008935751943526048
0.008935751943526048
0.02010544187293361
0.03350906978822268
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
1.4542936288088644
0.004467875971763024
0.026807255830578143
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.1295684031811277
0.567420248413904
0.02010544187293361
0.013403627915289072
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.03127513180234117
0.008935751943526048
0.002233937985881512
0.008935751943526048
0.013403627915289072
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.31051738003753016
0.002233937985881512
0.024573317844696633
0.05138057367527477
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.18094897685640246
0.049146635689393266
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.037976945759985704
0.017871503887052095
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.008935751943526048
0.04021088374586722
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.5741220623715486
0.002233937985881512
0.18318291484228397
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.23679742650344027
0.008935751943526048
0.02010544187293361
0.008935751943526048
0.23903136448932177
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.04691269770351175
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.013403627915289072
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.04021088374586722
0.049146635689393266
0.004467875971763024
0.004467875971763024
0.18094897685640246
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.12063265123760164
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.16531141095523189
0.03574300777410419
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.015637565901170585
0.02010544187293361
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.02010544187293361
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.08042176749173444
0.06925207756232687
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.02010544187293361
0.03574300777410419
0.017871503887052095
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.015637565901170585
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.31051738003753016
0.002233937985881512
0.002233937985881512
0.049146635689393266
0.07148601554820838
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.33062282191046377
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.1318023411670092
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.002233937985881512
0.1697792869269949
0.01116968992940756
0.008935751943526048
0.004467875971763024
0.1273344651952462
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.02233937985881512
0.017871503887052095
0.07818782950585292
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.06478420159056385
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.10946296130819408
0.013403627915289072
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.004467875971763024
0.02233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03350906978822268
0.049146635689393266
0.02010544187293361
0.03350906978822268
0.004467875971763024
0.07818782950585292
0.0558484496470378
0.002233937985881512
0.06925207756232687
0.006701813957644536
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.008935751943526048
0.015637565901170585
0.006701813957644536
0.09829327137878653
0.002233937985881512
0.004467875971763024
1.0812259851666517
0.12063265123760164
0.01116968992940756
0.002233937985881512
0.002233937985881512
8.223125726029846
0.1295684031811277
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.12510052720936468
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.06255026360468234
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.10722902332231257
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.037976945759985704
0.05808238763291931
0.002233937985881512
0.002233937985881512
0.12510052720936468
0.002233937985881512
0.053614511661156286
0.02010544187293361
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.04691269770351175
0.024573317844696633
0.024573317844696633
0.002233937985881512
0.013403627915289072
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.08935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.14297203109641676
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.015637565901170585
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.09605933339290501
0.002233937985881512
0.39540702350102763
0.002233937985881512
0.07148601554820838
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.5316772406397998
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.5562505584844964
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.03574300777410419
0.07371995353408989
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.017871503887052095
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.18094897685640246
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.015637565901170585
0.004467875971763024
0.008935751943526048
0.01116968992940756
0.01116968992940756
0.04021088374586722
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.013403627915289072
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.015637565901170585
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.07371995353408989
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.037976945759985704
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.03350906978822268
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.20105441872933608
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.13850415512465375
0.026807255830578143
0.015637565901170585
0.1496738450540613
0.04021088374586722
0.024573317844696633
0.14520596908229827
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.05138057367527477
0.002233937985881512
0.006701813957644536
0.03574300777410419
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.015637565901170585
0.013403627915289072
0.004467875971763024
0.10052720936466804
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.17871503887052095
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.037976945759985704
0.002233937985881512
0.05808238763291931
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.29487981413635955
0.004467875971763024
0.002233937985881512
0.03574300777410419
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.04467875971763024
0.006701813957644536
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.18318291484228397
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.049146635689393266
0.037976945759985704
0.002233937985881512
0.008935751943526048
0.024573317844696633
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.25020105441872936
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.10276114735054954
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.08265570547761594
0.03350906978822268
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.037976945759985704
0.002233937985881512
0.004467875971763024
0.06925207756232687
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.02233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.017871503887052095
0.06701813957644535
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.3507282637833974
0.013403627915289072
0.002233937985881512
0.02233937985881512
0.01116968992940756
0.049146635689393266
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.370833705656331
0.004467875971763024
0.01116968992940756
0.15860959699758734
0.024573317844696633
0.037976945759985704
0.08712358144937897
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.042444821731748725
0.004467875971763024
0.002233937985881512
0.04691269770351175
0.026807255830578143
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.042444821731748725
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.03350906978822268
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.25020105441872936
0.002233937985881512
0.002233937985881512
0.14743990706817978
0.013403627915289072
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.037976945759985704
0.002233937985881512
0.04691269770351175
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.029041193816459657
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.2658386203198999
0.02010544187293361
0.013403627915289072
0.002233937985881512
0.024573317844696633
0.013403627915289072
0.04691269770351175
0.002233937985881512
0.01116968992940756
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.015637565901170585
0.029041193816459657
0.01116968992940756
0.006701813957644536
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.024573317844696633
0.008935751943526048
0.013403627915289072
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.06478420159056385
0.02010544187293361
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.024573317844696633
0.002233937985881512
0.08488964346349745
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.029041193816459657
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.24796711643284783
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.0558484496470378
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.024573317844696633
0.008935751943526048
0.008935751943526048
0.02233937985881512
0.04467875971763024
0.002233937985881512
0.0558484496470378
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.015637565901170585
0.026807255830578143
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.11616477526583863
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.004467875971763024
0.008935751943526048
0.06031632561880082
0.017871503887052095
0.004467875971763024
0.03127513180234117
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.037976945759985704
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.05808238763291931
0.004467875971763024
0.002233937985881512
0.013403627915289072
0.017871503887052095
0.04691269770351175
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.008935751943526048
0.006701813957644536
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.03127513180234117
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.274774372263426
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.05138057367527477
0.03127513180234117
0.004467875971763024
0.14297203109641676
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.10276114735054954
0.006701813957644536
0.03350906978822268
0.002233937985881512
0.39987489947279065
0.002233937985881512
0.6456080779197569
0.002233937985881512
0.14073809311053526
0.002233937985881512
0.004467875971763024
0.03127513180234117
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.4110445894021982
0.002233937985881512
0.05138057367527477
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.08488964346349745
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.09605933339290501
0.002233937985881512
0.002233937985881512
0.04021088374586722
0.1318023411670092
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.02010544187293361
0.006701813957644536
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.06031632561880082
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.16084353498346887
0.024573317844696633
0.02010544187293361
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.026807255830578143
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.015637565901170585
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.0558484496470378
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.026807255830578143
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.02233937985881512
0.02010544187293361
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.09829327137878653
0.006701813957644536
0.002233937985881512
1.1370744348136896
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.16531141095523189
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.024573317844696633
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.09159145742114198
0.5964614422303637
0.01116968992940756
0.006701813957644536
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.006701813957644536
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.5160396747386292
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08265570547761594
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.02010544187293361
0.002233937985881512
0.024573317844696633
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.11616477526583863
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.09605933339290501
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.02233937985881512
0.008935751943526048
0.015637565901170585
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.18094897685640246
0.03127513180234117
0.008935751943526048
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.1116968992940756
0.037976945759985704
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.013403627915289072
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.14520596908229827
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.02010544187293361
0.09829327137878653
0.002233937985881512
0.01116968992940756
0.026807255830578143
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.02010544187293361
0.002233937985881512
0.013403627915289072
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.042444821731748725
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.12063265123760164
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.013403627915289072
0.02010544187293361
0.053614511661156286
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.004467875971763024
0.002233937985881512
1.313555535698329
0.002233937985881512
0.3417925118398713
0.049146635689393266
0.006701813957644536
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.015637565901170585
0.004467875971763024
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.004467875971763024
0.024573317844696633
0.029041193816459657
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.037976945759985704
3.033687784827093
0.017871503887052095
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.06031632561880082
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.004467875971763024
0.5651863104280225
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.09829327137878653
0.008935751943526048
0.04467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.037976945759985704
0.2278616745599142
0.002233937985881512
0.008935751943526048
0.01116968992940756
0.03574300777410419
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.02010544187293361
0.006701813957644536
0.015637565901170585
0.002233937985881512
0.013403627915289072
0.0558484496470378
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.013403627915289072
0.006701813957644536
0.008935751943526048
0.017871503887052095
0.002233937985881512
0.04691269770351175
0.02010544187293361
0.06925207756232687
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.013403627915289072
0.002233937985881512
0.013403627915289072
0.17871503887052095
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.004467875971763024
0.04467875971763024
0.015637565901170585
0.002233937985881512
0.04021088374586722
0.1273344651952462
0.02233937985881512
0.015637565901170585
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.06701813957644535
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.13627021713877221
0.013403627915289072
1.3649361093736039
0.04691269770351175
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.015637565901170585
0.006701813957644536
0.004467875971763024
0.09605933339290501
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.5875256902868377
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.09159145742114198
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.008935751943526048
0.1496738450540613
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.5138057367527478
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.04021088374586722
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.27254043427754443
0.006701813957644536
0.10499508533643107
0.02233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.3395585738539898
0.04691269770351175
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.3596640157269234
0.004467875971763024
0.006701813957644536
5.386024483960325
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.004467875971763024
0.004467875971763024
0.4356179072468948
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.3172191939951747
0.015637565901170585
0.029041193816459657
0.02010544187293361
0.008935751943526048
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.008935751943526048
0.04021088374586722
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.02010544187293361
0.008935751943526048
0.01116968992940756
0.024573317844696633
0.004467875971763024
0.024573317844696633
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.04021088374586722
0.024573317844696633
0.017871503887052095
0.07148601554820838
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.10722902332231257
0.10499508533643107
0.002233937985881512
0.013403627915289072
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.017871503887052095
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.08265570547761594
0.7640067911714771
0.002233937985881512
0.017871503887052095
0.15637565901170583
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.08935751943526048
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.07818782950585292
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.16307747296935038
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.04467875971763024
0.006701813957644536
0.002233937985881512
0.017871503887052095
0.015637565901170585
0.002233937985881512
0.042444821731748725
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08935751943526048
0.008935751943526048
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.1340362791528907
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.09829327137878653
0.006701813957644536
0.02233937985881512
0.002233937985881512
0.006701813957644536
0.20328835671521758
0.02010544187293361
0.015637565901170585
0.002233937985881512
0.013403627915289072
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.006701813957644536
0.026807255830578143
0.004467875971763024
0.015637565901170585
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.06255026360468234
0.024573317844696633
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.013403627915289072
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.19435260477169153
0.015637565901170585
0.002233937985881512
0.5964614422303637
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.663479581806809
0.05138057367527477
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.01116968992940756
0.049146635689393266
0.01116968992940756
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.053614511661156286
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.17648110088463945
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.08265570547761594
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.07371995353408989
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.02233937985881512
0.01116968992940756
0.004467875971763024
0.004467875971763024
0.024573317844696633
0.004467875971763024
0.20328835671521758
0.004467875971763024
0.6478420159056385
0.01116968992940756
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.013403627915289072
0.013403627915289072
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.01116968992940756
0.024573317844696633
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.28817800017871503
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.008935751943526048
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.6076311321597713
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.03350906978822268
0.01116968992940756
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.05808238763291931
0.006701813957644536
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08265570547761594
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.004467875971763024
0.01116968992940756
0.017871503887052095
0.002233937985881512
2.9376284514341884
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
1.318023411670092
0.18318291484228397
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.008935751943526048
0.008935751943526048
0.1720132249128764
0.006701813957644536
0.037976945759985704
0.01116968992940756
0.05808238763291931
0.008935751943526048
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.037976945759985704
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.004467875971763024
0.002233937985881512
0.049146635689393266
0.02233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.037976945759985704
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.10946296130819408
0.01116968992940756
0.049146635689393266
0.06925207756232687
0.008935751943526048
0.002233937985881512
0.049146635689393266
0.24573317844696632
0.004467875971763024
0.5473148065409704
0.002233937985881512
0.04467875971763024
0.004467875971763024
0.013403627915289072
0.13627021713877221
0.5004021088374587
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.06478420159056385
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.008935751943526048
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.5986953802162452
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.02010544187293361
0.006701813957644536
0.06255026360468234
0.10052720936466804
0.004467875971763024
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.3507282637833974
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.024573317844696633
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.002233937985881512
0.026807255830578143
0.2591368063622554
0.002233937985881512
0.026807255830578143
0.06478420159056385
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.026807255830578143
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.07595389151997141
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08265570547761594
2.7924224823518897
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.11616477526583863
0.024573317844696633
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.23232955053167725
0.006701813957644536
0.017871503887052095
0.02233937985881512
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.38647127155750155
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.7081583415244392
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.06031632561880082
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.07595389151997141
0.037976945759985704
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
1.0633544812795996
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.09159145742114198
0.017871503887052095
0.002233937985881512
5.424001429720311
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.04467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.4423197212045394
0.017871503887052095
0.002233937985881512
0.19211866678581002
0.09159145742114198
0.006701813957644536
0.01116968992940756
0.01116968992940756
0.20105441872933608
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.042444821731748725
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.05138057367527477
0.002233937985881512
0.04021088374586722
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.017871503887052095
0.04021088374586722
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.037976945759985704
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.2077562326869806
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.002233937985881512
1.3515324814583147
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.06478420159056385
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.008935751943526048
0.015637565901170585
0.11839871325172013
0.008935751943526048
0.2233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.017871503887052095
0.09605933339290501
0.008935751943526048
0.1295684031811277
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.026807255830578143
0.7260298454114914
0.015637565901170585
0.02010544187293361
0.008935751943526048
0.002233937985881512
0.008935751943526048
0.07371995353408989
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.04691269770351175
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.02233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.024573317844696633
0.11839871325172013
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.3641318916986864
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.19658654275757306
0.01116968992940756
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.01116968992940756
0.024573317844696633
0.006701813957644536
0.01116968992940756
0.017871503887052095
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.024573317844696633
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.21892592261638816
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.049146635689393266
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.06255026360468234
0.01116968992940756
0.008935751943526048
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.037976945759985704
0.017871503887052095
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.004467875971763024
0.006701813957644536
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.04021088374586722
0.4423197212045394
0.8645340005361452
0.02010544187293361
0.11839871325172013
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.07148601554820838
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.006701813957644536
0.006701813957644536
0.02233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.026807255830578143
0.01116968992940756
0.006701813957644536
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.017871503887052095
0.03574300777410419
0.015637565901170585
0.07148601554820838
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.0558484496470378
0.04021088374586722
0.013403627915289072
0.006701813957644536
0.008935751943526048
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.008935751943526048
0.01116968992940756
0.1116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.026807255830578143
0.015637565901170585
0.01116968992940756
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.049146635689393266
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.06701813957644535
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.026807255830578143
0.004467875971763024
0.08712358144937897
0.004467875971763024
0.01116968992940756
0.017871503887052095
0.01116968992940756
0.004467875971763024
0.008935751943526048
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.17871503887052095
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.026807255830578143
0.002233937985881512
0.013403627915289072
0.006701813957644536
0.002233937985881512
0.03574300777410419
0.02233937985881512
0.10499508533643107
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
def lexical_diversity(text):
    return len(text) / len(set(text))

lexical_diveristy(text3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    lexical_diveristy(text3)
NameError: name 'lexical_diveristy' is not defined. Did you mean: 'lexical_diversity'?
lexical_diversity(text4)
15.251970074812968
lexical_diversity(text3)
16.050197203298673
def percentage_each(text,count,total):
    for i in set(text):
        return 100 * count/total

    
percentage_each(text3,text3.cou
def percentage_each(text,total):
    for i in set(text):
        return 100 * text.count(i)/total
    
SyntaxError: '(' was never closed
def percentage_each(text,total):
    for i in set(text):
        return 100 * text.count(i)/total

    
percentage_each(text3,len(text3))
0.008935751943526048
def percentage_each(text,total):
    for i in set(text):
         print(100 * text.count(i)/total)

         
percentage_each(text3,len(text3))
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.004467875971763024
0.02010544187293361
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.07818782950585292
0.006701813957644536
0.02233937985881512
0.01116968992940756
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.008935751943526048
0.10276114735054954
0.002233937985881512
0.02010544187293361
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.002233937985881512
1.4475918148512197
0.002233937985881512
0.2546689303904924
0.03574300777410419
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.008935751943526048
0.017871503887052095
0.017871503887052095
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.18318291484228397
0.002233937985881512
0.6299705120185863
0.002233937985881512
0.024573317844696633
0.006701813957644536
0.004467875971763024
0.017871503887052095
0.004467875971763024
0.006701813957644536
0.02233937985881512
0.026807255830578143
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.008935751943526048
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.053614511661156286
0.004467875971763024
0.008935751943526048
0.008935751943526048
0.02010544187293361
0.03350906978822268
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
1.4542936288088644
0.004467875971763024
0.026807255830578143
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.1295684031811277
0.567420248413904
0.02010544187293361
0.013403627915289072
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.03127513180234117
0.008935751943526048
0.002233937985881512
0.008935751943526048
0.013403627915289072
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.31051738003753016
0.002233937985881512
0.024573317844696633
0.05138057367527477
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.18094897685640246
0.049146635689393266
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.037976945759985704
0.017871503887052095
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.008935751943526048
0.04021088374586722
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.5741220623715486
0.002233937985881512
0.18318291484228397
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.23679742650344027
0.008935751943526048
0.02010544187293361
0.008935751943526048
0.23903136448932177
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.04691269770351175
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.013403627915289072
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.04021088374586722
0.049146635689393266
0.004467875971763024
0.004467875971763024
0.18094897685640246
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.12063265123760164
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.16531141095523189
0.03574300777410419
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.015637565901170585
0.02010544187293361
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.02010544187293361
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.08042176749173444
0.06925207756232687
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.02010544187293361
0.03574300777410419
0.017871503887052095
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.015637565901170585
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.31051738003753016
0.002233937985881512
0.002233937985881512
0.049146635689393266
0.07148601554820838
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.33062282191046377
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.1318023411670092
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.002233937985881512
0.1697792869269949
0.01116968992940756
0.008935751943526048
0.004467875971763024
0.1273344651952462
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.02233937985881512
0.017871503887052095
0.07818782950585292
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.06478420159056385
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.10946296130819408
0.013403627915289072
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.004467875971763024
0.02233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03350906978822268
0.049146635689393266
0.02010544187293361
0.03350906978822268
0.004467875971763024
0.07818782950585292
0.0558484496470378
0.002233937985881512
0.06925207756232687
0.006701813957644536
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.008935751943526048
0.015637565901170585
0.006701813957644536
0.09829327137878653
0.002233937985881512
0.004467875971763024
1.0812259851666517
0.12063265123760164
0.01116968992940756
0.002233937985881512
0.002233937985881512
8.223125726029846
0.1295684031811277
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.12510052720936468
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.06255026360468234
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.10722902332231257
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.037976945759985704
0.05808238763291931
0.002233937985881512
0.002233937985881512
0.12510052720936468
0.002233937985881512
0.053614511661156286
0.02010544187293361
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.04691269770351175
0.024573317844696633
0.024573317844696633
0.002233937985881512
0.013403627915289072
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.08935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.14297203109641676
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.015637565901170585
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.09605933339290501
0.002233937985881512
0.39540702350102763
0.002233937985881512
0.07148601554820838
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.5316772406397998
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.5562505584844964
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.03574300777410419
0.07371995353408989
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.017871503887052095
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.18094897685640246
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.015637565901170585
0.004467875971763024
0.008935751943526048
0.01116968992940756
0.01116968992940756
0.04021088374586722
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.013403627915289072
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.015637565901170585
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.07371995353408989
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.037976945759985704
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.03350906978822268
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.20105441872933608
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.13850415512465375
0.026807255830578143
0.015637565901170585
0.1496738450540613
0.04021088374586722
0.024573317844696633
0.14520596908229827
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.05138057367527477
0.002233937985881512
0.006701813957644536
0.03574300777410419
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.015637565901170585
0.013403627915289072
0.004467875971763024
0.10052720936466804
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.17871503887052095
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.037976945759985704
0.002233937985881512
0.05808238763291931
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.29487981413635955
0.004467875971763024
0.002233937985881512
0.03574300777410419
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.04467875971763024
0.006701813957644536
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.18318291484228397
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.049146635689393266
0.037976945759985704
0.002233937985881512
0.008935751943526048
0.024573317844696633
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.25020105441872936
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.10276114735054954
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.08265570547761594
0.03350906978822268
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.037976945759985704
0.002233937985881512
0.004467875971763024
0.06925207756232687
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.02233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.017871503887052095
0.06701813957644535
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.3507282637833974
0.013403627915289072
0.002233937985881512
0.02233937985881512
0.01116968992940756
0.049146635689393266
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.370833705656331
0.004467875971763024
0.01116968992940756
0.15860959699758734
0.024573317844696633
0.037976945759985704
0.08712358144937897
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.042444821731748725
0.004467875971763024
0.002233937985881512
0.04691269770351175
0.026807255830578143
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.042444821731748725
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.03350906978822268
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.25020105441872936
0.002233937985881512
0.002233937985881512
0.14743990706817978
0.013403627915289072
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.037976945759985704
0.002233937985881512
0.04691269770351175
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.029041193816459657
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.2658386203198999
0.02010544187293361
0.013403627915289072
0.002233937985881512
0.024573317844696633
0.013403627915289072
0.04691269770351175
0.002233937985881512
0.01116968992940756
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.015637565901170585
0.029041193816459657
0.01116968992940756
0.006701813957644536
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.024573317844696633
0.008935751943526048
0.013403627915289072
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.06478420159056385
0.02010544187293361
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.024573317844696633
0.002233937985881512
0.08488964346349745
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.029041193816459657
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.24796711643284783
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.0558484496470378
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.024573317844696633
0.008935751943526048
0.008935751943526048
0.02233937985881512
0.04467875971763024
0.002233937985881512
0.0558484496470378
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.015637565901170585
0.026807255830578143
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.11616477526583863
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.004467875971763024
0.008935751943526048
0.06031632561880082
0.017871503887052095
0.004467875971763024
0.03127513180234117
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.037976945759985704
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.05808238763291931
0.004467875971763024
0.002233937985881512
0.013403627915289072
0.017871503887052095
0.04691269770351175
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.008935751943526048
0.006701813957644536
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.03127513180234117
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.274774372263426
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.05138057367527477
0.03127513180234117
0.004467875971763024
0.14297203109641676
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.10276114735054954
0.006701813957644536
0.03350906978822268
0.002233937985881512
0.39987489947279065
0.002233937985881512
0.6456080779197569
0.002233937985881512
0.14073809311053526
0.002233937985881512
0.004467875971763024
0.03127513180234117
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.4110445894021982
0.002233937985881512
0.05138057367527477
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.08488964346349745
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.09605933339290501
0.002233937985881512
0.002233937985881512
0.04021088374586722
0.1318023411670092
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.02010544187293361
0.006701813957644536
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.06031632561880082
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.16084353498346887
0.024573317844696633
0.02010544187293361
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.026807255830578143
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.015637565901170585
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.0558484496470378
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.026807255830578143
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.02233937985881512
0.02010544187293361
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.09829327137878653
0.006701813957644536
0.002233937985881512
1.1370744348136896
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.16531141095523189
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.024573317844696633
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.09159145742114198
0.5964614422303637
0.01116968992940756
0.006701813957644536
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.006701813957644536
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.5160396747386292
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08265570547761594
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.02010544187293361
0.002233937985881512
0.024573317844696633
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.11616477526583863
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.09605933339290501
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.02233937985881512
0.008935751943526048
0.015637565901170585
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.18094897685640246
0.03127513180234117
0.008935751943526048
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.1116968992940756
0.037976945759985704
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.013403627915289072
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.14520596908229827
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.02010544187293361
0.09829327137878653
0.002233937985881512
0.01116968992940756
0.026807255830578143
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.02010544187293361
0.002233937985881512
0.013403627915289072
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.042444821731748725
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.12063265123760164
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.013403627915289072
0.02010544187293361
0.053614511661156286
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.004467875971763024
0.002233937985881512
1.313555535698329
0.002233937985881512
0.3417925118398713
0.049146635689393266
0.006701813957644536
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.015637565901170585
0.004467875971763024
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.004467875971763024
0.024573317844696633
0.029041193816459657
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.037976945759985704
3.033687784827093
0.017871503887052095
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.06031632561880082
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.004467875971763024
0.5651863104280225
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.09829327137878653
0.008935751943526048
0.04467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.037976945759985704
0.2278616745599142
0.002233937985881512
0.008935751943526048
0.01116968992940756
0.03574300777410419
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.02010544187293361
0.006701813957644536
0.015637565901170585
0.002233937985881512
0.013403627915289072
0.0558484496470378
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.013403627915289072
0.006701813957644536
0.008935751943526048
0.017871503887052095
0.002233937985881512
0.04691269770351175
0.02010544187293361
0.06925207756232687
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.013403627915289072
0.002233937985881512
0.013403627915289072
0.17871503887052095
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.004467875971763024
0.04467875971763024
0.015637565901170585
0.002233937985881512
0.04021088374586722
0.1273344651952462
0.02233937985881512
0.015637565901170585
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.06701813957644535
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.13627021713877221
0.013403627915289072
1.3649361093736039
0.04691269770351175
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.015637565901170585
0.006701813957644536
0.004467875971763024
0.09605933339290501
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.5875256902868377
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.09159145742114198
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.008935751943526048
0.1496738450540613
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.5138057367527478
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.04021088374586722
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.27254043427754443
0.006701813957644536
0.10499508533643107
0.02233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.3395585738539898
0.04691269770351175
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.3596640157269234
0.004467875971763024
0.006701813957644536
5.386024483960325
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.004467875971763024
0.004467875971763024
0.4356179072468948
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.3172191939951747
0.015637565901170585
0.029041193816459657
0.02010544187293361
0.008935751943526048
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.008935751943526048
0.04021088374586722
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.02010544187293361
0.008935751943526048
0.01116968992940756
0.024573317844696633
0.004467875971763024
0.024573317844696633
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.04021088374586722
0.024573317844696633
0.017871503887052095
0.07148601554820838
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.10722902332231257
0.10499508533643107
0.002233937985881512
0.013403627915289072
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.017871503887052095
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.08265570547761594
0.7640067911714771
0.002233937985881512
0.017871503887052095
0.15637565901170583
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.08935751943526048
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.07818782950585292
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.16307747296935038
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.04467875971763024
0.006701813957644536
0.002233937985881512
0.017871503887052095
0.015637565901170585
0.002233937985881512
0.042444821731748725
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08935751943526048
0.008935751943526048
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.1340362791528907
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.09829327137878653
0.006701813957644536
0.02233937985881512
0.002233937985881512
0.006701813957644536
0.20328835671521758
0.02010544187293361
0.015637565901170585
0.002233937985881512
0.013403627915289072
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.02010544187293361
0.006701813957644536
0.026807255830578143
0.004467875971763024
0.015637565901170585
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.06255026360468234
0.024573317844696633
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.013403627915289072
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.004467875971763024
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.19435260477169153
0.015637565901170585
0.002233937985881512
0.5964614422303637
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.03574300777410419
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.663479581806809
0.05138057367527477
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.01116968992940756
0.049146635689393266
0.01116968992940756
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.053614511661156286
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.17648110088463945
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.08265570547761594
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.07371995353408989
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.02233937985881512
0.01116968992940756
0.004467875971763024
0.004467875971763024
0.024573317844696633
0.004467875971763024
0.20328835671521758
0.004467875971763024
0.6478420159056385
0.01116968992940756
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.013403627915289072
0.013403627915289072
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.01116968992940756
0.024573317844696633
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.28817800017871503
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.008935751943526048
0.01116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.6076311321597713
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.03350906978822268
0.01116968992940756
0.004467875971763024
0.004467875971763024
0.006701813957644536
0.05808238763291931
0.006701813957644536
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08265570547761594
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.004467875971763024
0.01116968992940756
0.017871503887052095
0.002233937985881512
2.9376284514341884
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
1.318023411670092
0.18318291484228397
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03127513180234117
0.008935751943526048
0.008935751943526048
0.1720132249128764
0.006701813957644536
0.037976945759985704
0.01116968992940756
0.05808238763291931
0.008935751943526048
0.024573317844696633
0.002233937985881512
0.002233937985881512
0.037976945759985704
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.004467875971763024
0.002233937985881512
0.049146635689393266
0.02233937985881512
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.037976945759985704
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.10946296130819408
0.01116968992940756
0.049146635689393266
0.06925207756232687
0.008935751943526048
0.002233937985881512
0.049146635689393266
0.24573317844696632
0.004467875971763024
0.5473148065409704
0.002233937985881512
0.04467875971763024
0.004467875971763024
0.013403627915289072
0.13627021713877221
0.5004021088374587
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.06478420159056385
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.008935751943526048
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.5986953802162452
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.02010544187293361
0.006701813957644536
0.06255026360468234
0.10052720936466804
0.004467875971763024
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.002233937985881512
0.3507282637833974
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.024573317844696633
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.017871503887052095
0.006701813957644536
0.002233937985881512
0.026807255830578143
0.2591368063622554
0.002233937985881512
0.026807255830578143
0.06478420159056385
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.026807255830578143
0.002233937985881512
0.013403627915289072
0.002233937985881512
0.01116968992940756
0.006701813957644536
0.002233937985881512
0.01116968992940756
0.07595389151997141
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.08265570547761594
2.7924224823518897
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.11616477526583863
0.024573317844696633
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.23232955053167725
0.006701813957644536
0.017871503887052095
0.02233937985881512
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.38647127155750155
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.03127513180234117
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.7081583415244392
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.06031632561880082
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.07595389151997141
0.037976945759985704
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
1.0633544812795996
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.01116968992940756
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.09159145742114198
0.017871503887052095
0.002233937985881512
5.424001429720311
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.04467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.4423197212045394
0.017871503887052095
0.002233937985881512
0.19211866678581002
0.09159145742114198
0.006701813957644536
0.01116968992940756
0.01116968992940756
0.20105441872933608
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.042444821731748725
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.05138057367527477
0.002233937985881512
0.04021088374586722
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.017871503887052095
0.04021088374586722
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.037976945759985704
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.2077562326869806
0.002233937985881512
0.006701813957644536
0.006701813957644536
0.002233937985881512
0.002233937985881512
1.3515324814583147
0.002233937985881512
0.002233937985881512
0.013403627915289072
0.02010544187293361
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.06478420159056385
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.008935751943526048
0.015637565901170585
0.11839871325172013
0.008935751943526048
0.2233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.024573317844696633
0.017871503887052095
0.09605933339290501
0.008935751943526048
0.1295684031811277
0.017871503887052095
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.026807255830578143
0.7260298454114914
0.015637565901170585
0.02010544187293361
0.008935751943526048
0.002233937985881512
0.008935751943526048
0.07371995353408989
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.006701813957644536
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.04691269770351175
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.03574300777410419
0.02233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.024573317844696633
0.11839871325172013
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.3641318916986864
0.002233937985881512
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.017871503887052095
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.01116968992940756
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.006701813957644536
0.004467875971763024
0.19658654275757306
0.01116968992940756
0.026807255830578143
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.029041193816459657
0.002233937985881512
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.01116968992940756
0.024573317844696633
0.006701813957644536
0.01116968992940756
0.017871503887052095
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.024573317844696633
0.004467875971763024
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.21892592261638816
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.017871503887052095
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.049146635689393266
0.006701813957644536
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.06255026360468234
0.01116968992940756
0.008935751943526048
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.037976945759985704
0.017871503887052095
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.029041193816459657
0.004467875971763024
0.006701813957644536
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.026807255830578143
0.004467875971763024
0.002233937985881512
0.006701813957644536
0.04021088374586722
0.4423197212045394
0.8645340005361452
0.02010544187293361
0.11839871325172013
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.07148601554820838
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.006701813957644536
0.006701813957644536
0.02233937985881512
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.008935751943526048
0.004467875971763024
0.026807255830578143
0.01116968992940756
0.006701813957644536
0.015637565901170585
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.008935751943526048
0.002233937985881512
0.006701813957644536
0.002233937985881512
0.004467875971763024
0.013403627915289072
0.002233937985881512
0.017871503887052095
0.03574300777410419
0.015637565901170585
0.07148601554820838
0.002233937985881512
0.002233937985881512
0.006701813957644536
0.0558484496470378
0.04021088374586722
0.013403627915289072
0.006701813957644536
0.008935751943526048
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.013403627915289072
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.02233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.01116968992940756
0.002233937985881512
0.008935751943526048
0.01116968992940756
0.1116968992940756
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.026807255830578143
0.015637565901170585
0.01116968992940756
0.004467875971763024
0.008935751943526048
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.004467875971763024
0.013403627915289072
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.049146635689393266
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.002233937985881512
0.002233937985881512
0.06701813957644535
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.008935751943526048
0.006701813957644536
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.026807255830578143
0.004467875971763024
0.08712358144937897
0.004467875971763024
0.01116968992940756
0.017871503887052095
0.01116968992940756
0.004467875971763024
0.008935751943526048
0.006701813957644536
0.01116968992940756
0.002233937985881512
0.002233937985881512
0.002233937985881512
0.004467875971763024
0.004467875971763024
0.002233937985881512
0.17871503887052095
0.002233937985881512
0.002233937985881512
0.015637565901170585
0.026807255830578143
0.002233937985881512
0.013403627915289072
0.006701813957644536
0.002233937985881512
0.03574300777410419
0.02233937985881512
0.10499508533643107
0.002233937985881512
0.004467875971763024
0.006701813957644536
0.006701813957644536
0.004467875971763024
0.002233937985881512
0.004467875971763024
0.002233937985881512
def percentage_each(text,total):
    for i in set(text):
        print("i:",i , 100 * text.count(i)/total)

        
percentage_each(text3,len(text3))
i: heir 0.008935751943526048
i: book 0.002233937985881512
i: generatio 0.004467875971763024
i: led 0.004467875971763024
i: strangers 0.004467875971763024
i: washed 0.006701813957644536
i: Have 0.004467875971763024
i: maiden 0.002233937985881512
i: sell 0.002233937985881512
i: Saul 0.004467875971763024
i: shouldest 0.008935751943526048
i: Mizraim 0.004467875971763024
i: Gomorrah 0.02010544187293361
i: dark 0.002233937985881512
i: soul 0.029041193816459657
i: Hittites 0.002233937985881512
i: couching 0.002233937985881512
i: perform 0.002233937985881512
i: rained 0.002233937985881512
i: if 0.07818782950585292
i: strove 0.006701813957644536
i: presence 0.02233937985881512
i: Arise 0.01116968992940756
i: shut 0.006701813957644536
i: dearth 0.004467875971763024
i: weighed 0.002233937985881512
i: dwelling 0.006701813957644536
i: state 0.002233937985881512
i: fame 0.002233937985881512
i: Eldaah 0.002233937985881512
i: Eber 0.015637565901170585
i: Uz 0.004467875971763024
i: mocking 0.002233937985881512
i: ships 0.002233937985881512
i: quickly 0.004467875971763024
i: overtook 0.006701813957644536
i: ha 0.015637565901170585
i: changed 0.006701813957644536
i: harm 0.002233937985881512
i: wroth 0.013403627915289072
i: Phara 0.008935751943526048
i: make 0.10276114735054954
i: awaked 0.002233937985881512
i: prison 0.02010544187293361
i: Ur 0.006701813957644536
i: stand 0.004467875971763024
i: moreover 0.004467875971763024
i: Jetur 0.002233937985881512
i: he 1.4475918148512197
i: whosoever 0.002233937985881512
i: man 0.2546689303904924
i: other 0.03574300777410419
i: shoulders 0.002233937985881512
i: Dothan 0.004467875971763024
i: Yet 0.006701813957644536
i: hired 0.002233937985881512
i: devoured 0.01116968992940756
i: Abr 0.002233937985881512
i: loose 0.002233937985881512
i: shew 0.01116968992940756
i: Edar 0.002233937985881512
i: ,) 0.002233937985881512
i: Thahash 0.002233937985881512
i: ass 0.015637565901170585
i: nought 0.002233937985881512
i: clear 0.008935751943526048
i: Enoch 0.017871503887052095
i: exceedingly 0.017871503887052095
i: content 0.002233937985881512
i: Methuselah 0.01116968992940756
i: Beor 0.002233937985881512
i: uppermost 0.002233937985881512
i: sat 0.02010544187293361
i: Shaul 0.002233937985881512
i: hith 0.002233937985881512
i: sa 0.006701813957644536
i: Jebusite 0.002233937985881512
i: sweat 0.002233937985881512
i: Peleg 0.01116968992940756
i: you 0.18318291484228397
i: northward 0.002233937985881512
i: me 0.6299705120185863
i: understood 0.002233937985881512
i: flood 0.024573317844696633
i: Drink 0.006701813957644536
i: Jac 0.004467875971763024
i: souls 0.017871503887052095
i: Nimrod 0.004467875971763024
i: able 0.006701813957644536
i: appeared 0.02233937985881512
i: lay 0.026807255830578143
i: Ammon 0.002233937985881512
i: fine 0.004467875971763024
i: hearth 0.002233937985881512
i: beheld 0.01116968992940756
i: instead 0.006701813957644536
i: withheld 0.008935751943526048
i: began 0.013403627915289072
i: assigned 0.002233937985881512
i: mercies 0.002233937985881512
i: Kadesh 0.006701813957644536
i: poplar 0.002233937985881512
i: Abimelech 0.053614511661156286
i: vow 0.004467875971763024
i: follow 0.008935751943526048
i: ought 0.008935751943526048
i: present 0.02010544187293361
i: another 0.03350906978822268
i: ri 0.002233937985881512
i: Lehabim 0.002233937985881512
i: Padanaram 0.02233937985881512
i: m 0.01116968992940756
i: proved 0.004467875971763024
i: Erech 0.002233937985881512
i: dost 0.004467875971763024
i: wounding 0.002233937985881512
i: his 1.4542936288088644
i: dim 0.004467875971763024
i: maid 0.026807255830578143
i: entered 0.01116968992940756
i: guiltiness 0.002233937985881512
i: almon 0.002233937985881512
i: basket 0.004467875971763024
i: seed 0.1295684031811277
i: be 0.567420248413904
i: Anah 0.02010544187293361
i: draw 0.013403627915289072
i: camest 0.006701813957644536
i: fish 0.004467875971763024
i: arms 0.002233937985881512
i: distressed 0.002233937985881512
i: rebelled 0.002233937985881512
i: subtil 0.002233937985881512
i: feel 0.004467875971763024
i: asses 0.03127513180234117
i: Shelah 0.008935751943526048
i: sceptre 0.002233937985881512
i: trade 0.008935751943526048
i: behind 0.013403627915289072
i: Cursed 0.004467875971763024
i: arose 0.017871503887052095
i: clothed 0.002233937985881512
i: upon 0.31051738003753016
i: force 0.002233937985881512
i: blood 0.024573317844696633
i: say 0.05138057367527477
i: beari 0.002233937985881512
i: pledge 0.006701813957644536
i: commanding 0.002233937985881512
i: dreams 0.008935751943526048
i: vine 0.008935751943526048
i: Muppim 0.002233937985881512
i: possessi 0.002233937985881512
i: pillar 0.026807255830578143
i: bosom 0.002233937985881512
i: yonder 0.002233937985881512
i: ewes 0.004467875971763024
i: jud 0.002233937985881512
i: Peradventure 0.02010544187293361
i: large 0.002233937985881512
i: took 0.18094897685640246
i: tent 0.049146635689393266
i: Sojourn 0.002233937985881512
i: magnified 0.002233937985881512
i: continued 0.002233937985881512
i: hanged 0.004467875971763024
i: healed 0.002233937985881512
i: stood 0.037976945759985704
i: gold 0.017871503887052095
i: Abide 0.002233937985881512
i: Reu 0.008935751943526048
i: Tubalcain 0.004467875971763024
i: abide 0.008935751943526048
i: lad 0.04021088374586722
i: reproved 0.004467875971763024
i: sod 0.002233937985881512
i: clusters 0.002233937985881512
i: angel 0.02233937985881512
i: quite 0.002233937985881512
i: deceitfully 0.002233937985881512
i: thee 0.5741220623715486
i: punishment 0.002233937985881512
i: your 0.18318291484228397
i: sojourned 0.01116968992940756
i: precious 0.002233937985881512
i: planted 0.006701813957644536
i: Phut 0.002233937985881512
i: seedtime 0.002233937985881512
i: smote 0.01116968992940756
i: out 0.23679742650344027
i: angels 0.008935751943526048
i: It 0.02010544187293361
i: offered 0.008935751943526048
i: after 0.23903136448932177
i: Happy 0.002233937985881512
i: tim 0.002233937985881512
i: fig 0.002233937985881512
i: afar 0.004467875971763024
i: asswaged 0.002233937985881512
i: enlarge 0.002233937985881512
i: ruler 0.006701813957644536
i: royal 0.002233937985881512
i: sand 0.006701813957644536
i: Tebah 0.002233937985881512
i: Ask 0.002233937985881512
i: adder 0.002233937985881512
i: space 0.004467875971763024
i: numbering 0.002233937985881512
i: Hiddekel 0.002233937985881512
i: ill 0.015637565901170585
i: path 0.002233937985881512
i: wherefore 0.015637565901170585
i: report 0.002233937985881512
i: drink 0.04691269770351175
i: prepared 0.004467875971763024
i: lodged 0.004467875971763024
i: crown 0.002233937985881512
i: Chaldees 0.006701813957644536
i: Hebron 0.01116968992940756
i: Abelmizraim 0.002233937985881512
i: journey 0.013403627915289072
i: comforted 0.008935751943526048
i: troubled 0.006701813957644536
i: Cheran 0.002233937985881512
i: yearn 0.002233937985881512
i: My 0.04021088374586722
i: wives 0.049146635689393266
i: windows 0.004467875971763024
i: doest 0.004467875971763024
i: pass 0.18094897685640246
i: signs 0.002233937985881512
i: sou 0.004467875971763024
i: spices 0.002233937985881512
i: wrapped 0.002233937985881512
i: lands 0.01116968992940756
i: Beerlahairoi 0.002233937985881512
i: hear 0.015637565901170585
i: ste 0.004467875971763024
i: escaped 0.002233937985881512
i: armed 0.002233937985881512
i: chief 0.03127513180234117
i: knead 0.002233937985881512
i: seven 0.12063265123760164
i: Husham 0.004467875971763024
i: Eshcol 0.004467875971763024
i: yoke 0.002233937985881512
i: fetcht 0.002233937985881512
i: anger 0.01116968992940756
i: Elam 0.006701813957644536
i: cakes 0.002233937985881512
i: Gather 0.006701813957644536
i: Egypt 0.16531141095523189
i: living 0.03574300777410419
i: upward 0.002233937985881512
i: interpretations 0.002233937985881512
i: lights 0.006701813957644536
i: drinking 0.004467875971763024
i: Sell 0.002233937985881512
i: messenger 0.002233937985881512
i: chode 0.002233937985881512
i: cometh 0.013403627915289072
i: moon 0.002233937985881512
i: deliver 0.008935751943526048
i: prayed 0.002233937985881512
i: within 0.02010544187293361
i: onyx 0.002233937985881512
i: communed 0.01116968992940756
i: justice 0.002233937985881512
i: Jabal 0.002233937985881512
i: Mash 0.002233937985881512
i: sheepshearers 0.002233937985881512
i: natio 0.002233937985881512
i: alive 0.026807255830578143
i: Zarah 0.002233937985881512
i: faileth 0.002233937985881512
i: wot 0.004467875971763024
i: seasons 0.002233937985881512
i: coats 0.002233937985881512
i: See 0.01116968992940756
i: Milcah 0.015637565901170585
i: gate 0.02010544187293361
i: ?) 0.002233937985881512
i: talked 0.01116968992940756
i: proceedeth 0.002233937985881512
i: wickedness 0.004467875971763024
i: oath 0.01116968992940756
i: How 0.008935751943526048
i: ours 0.002233937985881512
i: Jaalam 0.006701813957644536
i: burning 0.002233937985881512
i: intreat 0.002233937985881512
i: interpreted 0.006701813957644536
i: eighteen 0.002233937985881512
i: Omar 0.004467875971763024
i: loud 0.002233937985881512
i: Ezbon 0.002233937985881512
i: sepulchres 0.002233937985881512
i: bre 0.006701813957644536
i: fifty 0.02010544187293361
i: kingdom 0.004467875971763024
i: heels 0.002233937985881512
i: rolled 0.004467875971763024
i: roughly 0.004467875971763024
i: done 0.08042176749173444
i: life 0.06925207756232687
i: Here 0.013403627915289072
i: couch 0.002233937985881512
i: bones 0.004467875971763024
i: heel 0.004467875971763024
i: da 0.004467875971763024
i: wombs 0.002233937985881512
i: togeth 0.004467875971763024
i: excel 0.002233937985881512
i: sheaves 0.004467875971763024
i: become 0.02010544187293361
i: bowed 0.03574300777410419
i: Adah 0.017871503887052095
i: overcome 0.004467875971763024
i: scarce 0.002233937985881512
i: lives 0.006701813957644536
i: watch 0.002233937985881512
i: neck 0.017871503887052095
i: Fifteen 0.002233937985881512
i: Lie 0.004467875971763024
i: driven 0.002233937985881512
i: Philistines 0.015637565901170585
i: delivered 0.01116968992940756
i: Siddim 0.006701813957644536
i: frost 0.002233937985881512
i: stooped 0.002233937985881512
i: merchantmen 0.002233937985881512
i: had 0.31051738003753016
i: Kemuel 0.002233937985881512
i: Mesopotamia 0.002233937985881512
i: himself 0.049146635689393266
i: great 0.07148601554820838
i: breach 0.002233937985881512
i: lower 0.002233937985881512
i: goodly 0.006701813957644536
i: Magdiel 0.002233937985881512
i: lesser 0.002233937985881512
i: dead 0.026807255830578143
i: parted 0.002233937985881512
i: ? 0.33062282191046377
i: sh 0.002233937985881512
i: En 0.002233937985881512
i: month 0.026807255830578143
i: birthday 0.002233937985881512
i: Pathrusim 0.002233937985881512
i: give 0.1318023411670092
i: Heber 0.002233937985881512
i: never 0.004467875971763024
i: only 0.029041193816459657
i: anointedst 0.002233937985881512
i: an 0.1697792869269949
i: Abrah 0.01116968992940756
i: wind 0.008935751943526048
i: troop 0.004467875971763024
i: saw 0.1273344651952462
i: crieth 0.002233937985881512
i: Return 0.006701813957644536
i: Which 0.002233937985881512
i: families 0.02010544187293361
i: Riphath 0.002233937985881512
i: law 0.02233937985881512
i: firmament 0.017871503887052095
i: people 0.07818782950585292
i: harvest 0.006701813957644536
i: droves 0.002233937985881512
i: imagined 0.002233937985881512
i: Buz 0.002233937985881512
i: Male 0.002233937985881512
i: Cush 0.006701813957644536
i: ey 0.004467875971763024
i: Hazo 0.002233937985881512
i: findeth 0.002233937985881512
i: Jehovahjireh 0.002233937985881512
i: pulled 0.004467875971763024
i: Let 0.06478420159056385
i: sole 0.002233937985881512
i: mocked 0.002233937985881512
i: caught 0.004467875971763024
i: over 0.10946296130819408
i: grew 0.013403627915289072
i: bearing 0.008935751943526048
i: standest 0.002233937985881512
i: knowing 0.002233937985881512
i: goats 0.02010544187293361
i: dew 0.004467875971763024
i: names 0.02233937985881512
i: Ellasar 0.004467875971763024
i: image 0.01116968992940756
i: gopher 0.002233937985881512
i: wandered 0.002233937985881512
i: mistress 0.006701813957644536
i: following 0.002233937985881512
i: feeding 0.002233937985881512
i: gods 0.01116968992940756
i: sworn 0.002233937985881512
i: shoelatchet 0.002233937985881512
i: spirit 0.006701813957644536
i: ready 0.008935751943526048
i: Naaman 0.002233937985881512
i: discern 0.002233937985881512
i: offeri 0.004467875971763024
i: except 0.015637565901170585
i: magicians 0.004467875971763024
i: dread 0.002233937985881512
i: Sichem 0.002233937985881512
i: barr 0.002233937985881512
i: cause 0.002233937985881512
i: destroy 0.03350906978822268
i: five 0.049146635689393266
i: sack 0.02010544187293361
i: forty 0.03350906978822268
i: knife 0.004467875971763024
i: yet 0.07818782950585292
i: see 0.0558484496470378
i: Alvan 0.002233937985881512
i: Now 0.06925207756232687
i: knowest 0.006701813957644536
i: deliverance 0.002233937985881512
i: raiment 0.015637565901170585
i: battle 0.002233937985881512
i: Hadar 0.004467875971763024
i: prosperous 0.004467875971763024
i: Hadad 0.004467875971763024
i: raise 0.002233937985881512
i: dried 0.006701813957644536
i: innocency 0.002233937985881512
i: fruits 0.002233937985881512
i: kind 0.029041193816459657
i: wrestlings 0.002233937985881512
i: hou 0.008935751943526048
i: ones 0.015637565901170585
i: Whose 0.006701813957644536
i: Rachel 0.09829327137878653
i: vision 0.002233937985881512
i: Javan 0.004467875971763024
i: I 1.0812259851666517
i: because 0.12063265123760164
i: fair 0.01116968992940756
i: ring 0.002233937985881512
i: direct 0.002233937985881512
i: , 8.223125726029846
i: Abram 0.1295684031811277
i: Serug 0.008935751943526048
i: Pharez 0.006701813957644536
i: supplanted 0.002233937985881512
i: han 0.002233937985881512
i: distress 0.004467875971763024
i: Jachin 0.002233937985881512
i: now 0.12510052720936468
i: Togarmah 0.002233937985881512
i: brass 0.002233937985881512
i: leanfleshed 0.006701813957644536
i: Unstable 0.002233937985881512
i: find 0.026807255830578143
i: giving 0.002233937985881512
i: Lasha 0.002233937985881512
i: iniquity 0.006701813957644536
i: prosper 0.008935751943526048
i: even 0.06255026360468234
i: seek 0.004467875971763024
i: confederate 0.002233937985881512
i: dea 0.002233937985881512
i: friends 0.002233937985881512
i: lien 0.002233937985881512
i: Salem 0.002233937985881512
i: speech 0.004467875971763024
i: waxen 0.002233937985881512
i: winter 0.002233937985881512
i: Of 0.013403627915289072
i: regard 0.002233937985881512
i: discreet 0.004467875971763024
i: pray 0.10722902332231257
i: slept 0.002233937985881512
i: save 0.008935751943526048
i: persons 0.004467875971763024
i: Ebal 0.002233937985881512
i: window 0.006701813957644536
i: hunting 0.002233937985881512
i: tell 0.037976945759985704
i: left 0.05808238763291931
i: judgment 0.002233937985881512
i: rid 0.002233937985881512
i: bare 0.12510052720936468
i: nativity 0.002233937985881512
i: ground 0.053614511661156286
i: look 0.02010544187293361
i: open 0.004467875971763024
i: grove 0.002233937985881512
i: protest 0.002233937985881512
i: weapons 0.002233937985881512
i: Shillem 0.002233937985881512
i: war 0.002233937985881512
i: sister 0.04691269770351175
i: twenty 0.024573317844696633
i: bought 0.024573317844696633
i: rulers 0.002233937985881512
i: Who 0.013403627915289072
i: d 0.01116968992940756
i: run 0.002233937985881512
i: laughed 0.006701813957644536
i: strife 0.004467875971763024
i: Israel 0.08935751943526048
i: belly 0.002233937985881512
i: too 0.002233937985881512
i: withered 0.002233937985881512
i: fir 0.002233937985881512
i: mouth 0.03127513180234117
i: abroad 0.015637565901170585
i: poured 0.006701813957644536
i: bou 0.002233937985881512
i: troughs 0.002233937985881512
i: Ishbak 0.002233937985881512
i: Perizzites 0.002233937985881512
i: let 0.14297203109641676
i: longeth 0.002233937985881512
i: pleasant 0.006701813957644536
i: raven 0.002233937985881512
i: till 0.015637565901170585
i: clothes 0.008935751943526048
i: finding 0.002233937985881512
i: begotten 0.002233937985881512
i: gro 0.002233937985881512
i: damsel 0.02010544187293361
i: Phallu 0.002233937985881512
i: Can 0.002233937985881512
i: flock 0.03127513180234117
i: Beersheba 0.024573317844696633
i: tabret 0.002233937985881512
i: knoweth 0.002233937985881512
i: riv 0.002233937985881512
i: ride 0.002233937985881512
i: gather 0.006701813957644536
i: smoking 0.002233937985881512
i: break 0.004467875971763024
i: doeth 0.002233937985881512
i: judged 0.002233937985881512
i: seventy 0.01116968992940756
i: marry 0.002233937985881512
i: mirth 0.002233937985881512
i: Canaan 0.09605933339290501
i: mules 0.002233937985881512
i: came 0.39540702350102763
i: espied 0.002233937985881512
i: king 0.07148601554820838
i: Eri 0.002233937985881512
i: Samlah 0.004467875971763024
i: trembled 0.002233937985881512
i: Reumah 0.002233937985881512
i: inherit 0.006701813957644536
i: friend 0.004467875971763024
i: Asenath 0.006701813957644536
i: teeth 0.002233937985881512
i: Dan 0.013403627915289072
i: Cause 0.002233937985881512
i: fourth 0.006701813957644536
i: observed 0.002233937985881512
i: meeteth 0.002233937985881512
i: gone 0.013403627915289072
i: multiplied 0.002233937985881512
i: Abel 0.017871503887052095
i: walked 0.006701813957644536
i: seventeen 0.004467875971763024
i: far 0.006701813957644536
i: : 0.5316772406397998
i: custom 0.002233937985881512
i: Es 0.004467875971763024
i: floor 0.002233937985881512
i: Sephar 0.002233937985881512
i: they 0.5562505584844964
i: As 0.006701813957644536
i: unawares 0.004467875971763024
i: nourished 0.002233937985881512
i: tongues 0.004467875971763024
i: together 0.03574300777410419
i: Leah 0.07371995353408989
i: dreamer 0.002233937985881512
i: increase 0.002233937985881512
i: Should 0.002233937985881512
i: handfuls 0.002233937985881512
i: kept 0.008935751943526048
i: Come 0.017871503887052095
i: rightly 0.002233937985881512
i: answer 0.006701813957644536
i: Job 0.002233937985881512
i: Zeboim 0.002233937985881512
i: overdrive 0.002233937985881512
i: defiledst 0.002233937985881512
i: been 0.024573317844696633
i: stead 0.015637565901170585
i: womenservan 0.002233937985881512
i: Feed 0.002233937985881512
i: breaketh 0.002233937985881512
i: embalmed 0.004467875971763024
i: also 0.18094897685640246
i: Pison 0.002233937985881512
i: bracelets 0.01116968992940756
i: Upon 0.002233937985881512
i: inn 0.004467875971763024
i: giveth 0.002233937985881512
i: beneath 0.002233937985881512
i: Gera 0.002233937985881512
i: Seth 0.01116968992940756
i: hated 0.015637565901170585
i: embalm 0.004467875971763024
i: hither 0.008935751943526048
i: kindness 0.01116968992940756
i: while 0.01116968992940756
i: commanded 0.04021088374586722
i: dry 0.008935751943526048
i: Whereas 0.002233937985881512
i: linen 0.002233937985881512
i: tenth 0.006701813957644536
i: womb 0.013403627915289072
i: Bashemath 0.013403627915289072
i: refrained 0.002233937985881512
i: bakers 0.002233937985881512
i: springing 0.002233937985881512
i: thus 0.015637565901170585
i: Bera 0.002233937985881512
i: Amalekites 0.002233937985881512
i: pow 0.002233937985881512
i: fugitive 0.004467875971763024
i: require 0.01116968992940756
i: pit 0.015637565901170585
i: feet 0.015637565901170585
i: Isra 0.004467875971763024
i: boys 0.002233937985881512
i: thin 0.01116968992940756
i: Wilt 0.006701813957644536
i: sort 0.006701813957644536
i: afflict 0.004467875971763024
i: born 0.07371995353408989
i: firmame 0.002233937985881512
i: Neither 0.002233937985881512
i: Zillah 0.006701813957644536
i: Sarai 0.037976945759985704
i: speed 0.002233937985881512
i: flee 0.008935751943526048
i: aileth 0.002233937985881512
i: wandering 0.002233937985881512
i: bury 0.03350906978822268
i: dowry 0.004467875971763024
i: shield 0.002233937985881512
i: Jobab 0.006701813957644536
i: perceived 0.004467875971763024
i: Becher 0.002233937985881512
i: Amorites 0.006701813957644536
i: saving 0.002233937985881512
i: Pharaoh 0.20105441872933608
i: increased 0.008935751943526048
i: thoughts 0.002233937985881512
i: nourish 0.004467875971763024
i: Shalem 0.002233937985881512
i: bowels 0.006701813957644536
i: current 0.002233937985881512
i: parcel 0.002233937985881512
i: Alvah 0.002233937985881512
i: Thorns 0.002233937985881512
i: itself 0.004467875971763024
i: Terah 0.02010544187293361
i: Esek 0.002233937985881512
i: commandments 0.002233937985881512
i: host 0.008935751943526048
i: sowed 0.002233937985881512
i: mead 0.002233937985881512
i: desire 0.004467875971763024
i: Oh 0.01116968992940756
i: Tell 0.002233937985881512
i: excellency 0.004467875971763024
i: Se 0.008935751943526048
i: children 0.13850415512465375
i: young 0.026807255830578143
i: Eliphaz 0.015637565901170585
i: come 0.1496738450540613
i: thence 0.04021088374586722
i: slay 0.024573317844696633
i: men 0.14520596908229827
i: cloud 0.006701813957644536
i: Deborah 0.002233937985881512
i: endued 0.002233937985881512
i: last 0.004467875971763024
i: yielding 0.01116968992940756
i: sanctified 0.002233937985881512
i: floc 0.002233937985881512
i: Heaven 0.002233937985881512
i: signet 0.004467875971763024
i: bless 0.05138057367527477
i: spi 0.002233937985881512
i: Be 0.006701813957644536
i: things 0.03574300777410419
i: bade 0.002233937985881512
i: female 0.015637565901170585
i: perish 0.002233937985881512
i: Euphrat 0.002233937985881512
i: Zilpah 0.015637565901170585
i: interpreter 0.004467875971763024
i: He 0.015637565901170585
i: spies 0.013403627915289072
i: captive 0.004467875971763024
i: do 0.10052720936466804
i: dealt 0.006701813957644536
i: Moreover 0.004467875971763024
i: Jemuel 0.002233937985881512
i: sinners 0.002233937985881512
i: openly 0.002233937985881512
i: Pau 0.002233937985881512
i: Said 0.002233937985881512
i: thousands 0.002233937985881512
i: pottage 0.006701813957644536
i: Spake 0.002233937985881512
i: wo 0.004467875971763024
i: brethren 0.17871503887052095
i: clave 0.004467875971763024
i: suffered 0.006701813957644536
i: spare 0.004467875971763024
i: sheaf 0.004467875971763024
i: renown 0.002233937985881512
i: respect 0.004467875971763024
i: Twelve 0.002233937985881512
i: sight 0.037976945759985704
i: gat 0.002233937985881512
i: dwelt 0.05808238763291931
i: bowing 0.002233937985881512
i: Hinder 0.002233937985881512
i: Shinab 0.002233937985881512
i: purposing 0.002233937985881512
i: fle 0.004467875971763024
i: have 0.29487981413635955
i: Tidal 0.004467875971763024
i: artificer 0.002233937985881512
i: head 0.03574300777410419
i: ninety 0.013403627915289072
i: commune 0.002233937985881512
i: husbandman 0.002233937985881512
i: Haste 0.004467875971763024
i: journeyed 0.017871503887052095
i: beast 0.04467875971763024
i: Rehoboth 0.006701813957644536
i: Jamin 0.002233937985881512
i: four 0.026807255830578143
i: dressed 0.002233937985881512
i: Mizpah 0.002233937985881512
i: urged 0.002233937985881512
i: hand 0.18318291484228397
i: Japhe 0.004467875971763024
i: pitch 0.004467875971763024
i: wherewith 0.002233937985881512
i: business 0.002233937985881512
i: laded 0.004467875971763024
i: Save 0.002233937985881512
i: thousand 0.002233937985881512
i: fruitful 0.03127513180234117
i: lead 0.002233937985881512
i: held 0.006701813957644536
i: Abimael 0.002233937985881512
i: secret 0.002233937985881512
i: perfect 0.004467875971763024
i: or 0.049146635689393266
i: Ishmael 0.037976945759985704
i: younge 0.002233937985881512
i: Hast 0.008935751943526048
i: about 0.024573317844696633
i: smoke 0.004467875971763024
i: Discern 0.002233937985881512
i: think 0.002233937985881512
i: back 0.01116968992940756
i: summer 0.002233937985881512
i: Midian 0.006701813957644536
i: pluckt 0.002233937985881512
i: hastily 0.002233937985881512
i: nineteen 0.002233937985881512
i: Zoar 0.013403627915289072
i: as 0.25020105441872936
i: comi 0.002233937985881512
i: laugh 0.008935751943526048
i: possessions 0.004467875971763024
i: poverty 0.002233937985881512
i: findest 0.002233937985881512
i: daughter 0.10276114735054954
i: captives 0.002233937985881512
i: stuff 0.006701813957644536
i: booths 0.002233937985881512
i: kinds 0.002233937985881512
i: birds 0.006701813957644536
i: merchant 0.002233937985881512
i: Jahzeel 0.002233937985881512
i: lads 0.002233937985881512
i: chose 0.004467875971763024
i: speaking 0.004467875971763024
i: hil 0.002233937985881512
i: hurt 0.008935751943526048
i: found 0.08265570547761594
i: gathered 0.03350906978822268
i: voi 0.002233937985881512
i: Tiras 0.002233937985881512
i: reign 0.002233937985881512
i: fallen 0.002233937985881512
i: treasure 0.002233937985881512
i: wittingly 0.002233937985881512
i: enquire 0.004467875971763024
i: loins 0.006701813957644536
i: sevenfold 0.006701813957644536
i: mi 0.002233937985881512
i: fifteen 0.004467875971763024
i: rain 0.008935751943526048
i: lion 0.006701813957644536
i: milk 0.004467875971763024
i: coming 0.002233937985881512
i: exchange 0.002233937985881512
i: spent 0.004467875971763024
i: divine 0.002233937985881512
i: Rosh 0.002233937985881512
i: until 0.037976945759985704
i: vessels 0.002233937985881512
i: failed 0.004467875971763024
i: set 0.06925207756232687
i: forbid 0.004467875971763024
i: Kedemah 0.002233937985881512
i: stricken 0.004467875971763024
i: possessor 0.004467875971763024
i: sojourner 0.002233937985881512
i: Edomites 0.004467875971763024
i: desired 0.002233937985881512
i: stronger 0.006701813957644536
i: reigned 0.02233937985881512
i: activity 0.002233937985881512
i: pressed 0.006701813957644536
i: pleasure 0.002233937985881512
i: fulfilled 0.01116968992940756
i: vestures 0.002233937985881512
i: touch 0.004467875971763024
i: hundredfo 0.002233937985881512
i: Nebajoth 0.006701813957644536
i: whereon 0.002233937985881512
i: everlasting 0.017871503887052095
i: Lot 0.06701813957644535
i: tak 0.002233937985881512
i: Shepho 0.002233937985881512
i: trough 0.002233937985881512
i: from 0.3507282637833974
i: sword 0.013403627915289072
i: deceiver 0.002233937985881512
i: right 0.02233937985881512
i: watered 0.01116968992940756
i: know 0.049146635689393266
i: wit 0.002233937985881512
i: provision 0.004467875971763024
i: biteth 0.002233937985881512
i: rider 0.002233937985881512
i: LORD 0.370833705656331
i: womenservants 0.004467875971763024
i: Where 0.01116968992940756
i: day 0.15860959699758734
i: Thy 0.024573317844696633
i: under 0.037976945759985704
i: thing 0.08712358144937897
i: shed 0.002233937985881512
i: males 0.002233937985881512
i: Yea 0.004467875971763024
i: soon 0.006701813957644536
i: bundles 0.002233937985881512
i: Shall 0.013403627915289072
i: dipped 0.002233937985881512
i: built 0.008935751943526048
i: ungirded 0.002233937985881512
i: Sodom 0.042444821731748725
i: Gatam 0.004467875971763024
i: Pinon 0.002233937985881512
i: tree 0.04691269770351175
i: In 0.026807255830578143
i: anything 0.002233937985881512
i: own 0.017871503887052095
i: sad 0.002233937985881512
i: honour 0.002233937985881512
i: visited 0.002233937985881512
i: Sered 0.002233937985881512
i: strakes 0.002233937985881512
i: salvation 0.002233937985881512
i: tithes 0.002233937985881512
i: Eden 0.013403627915289072
i: Avith 0.002233937985881512
i: profit 0.004467875971763024
i: th 0.042444821731748725
i: emptied 0.004467875971763024
i: rested 0.006701813957644536
i: Bedad 0.002233937985881512
i: surely 0.03350906978822268
i: westwa 0.002233937985881512
i: sought 0.002233937985881512
i: fill 0.004467875971763024
i: Uzal 0.002233937985881512
i: ir 0.002233937985881512
i: Forasmuch 0.002233937985881512
i: when 0.25020105441872936
i: vowed 0.002233937985881512
i: bodies 0.002233937985881512
i: but 0.14743990706817978
i: harlot 0.013403627915289072
i: pla 0.004467875971763024
i: Zaavan 0.002233937985881512
i: hairy 0.006701813957644536
i: Naamah 0.002233937985881512
i: whelp 0.002233937985881512
i: purchased 0.002233937985881512
i: G 0.004467875971763024
i: Dishan 0.006701813957644536
i: butler 0.017871503887052095
i: liveth 0.002233937985881512
i: walking 0.002233937985881512
i: Fill 0.002233937985881512
i: counted 0.006701813957644536
i: Shechem 0.037976945759985704
i: Jimnah 0.002233937985881512
i: should 0.04691269770351175
i: command 0.006701813957644536
i: Our 0.002233937985881512
i: breed 0.002233937985881512
i: breath 0.008935751943526048
i: keep 0.029041193816459657
i: Lift 0.004467875971763024
i: Beriah 0.004467875971763024
i: inhabitants 0.006701813957644536
i: ewe 0.006701813957644536
i: upright 0.002233937985881512
i: surety 0.01116968992940756
i: selfwill 0.002233937985881512
i: are 0.2658386203198999
i: loved 0.02010544187293361
i: leave 0.013403627915289072
i: solemnly 0.002233937985881512
i: possession 0.024573317844696633
i: establish 0.013403627915289072
i: taken 0.04691269770351175
i: sawest 0.002233937985881512
i: true 0.01116968992940756
i: Arphaxad 0.013403627915289072
i: bitter 0.002233937985881512
i: sustained 0.002233937985881512
i: person 0.002233937985881512
i: Man 0.002233937985881512
i: carried 0.008935751943526048
i: Eno 0.002233937985881512
i: get 0.015637565901170585
i: yea 0.029041193816459657
i: south 0.01116968992940756
i: After 0.006701813957644536
i: hastened 0.004467875971763024
i: Gad 0.008935751943526048
i: doer 0.002233937985881512
i: haven 0.004467875971763024
i: requite 0.002233937985881512
i: mess 0.002233937985881512
i: hold 0.006701813957644536
i: messengers 0.004467875971763024
i: bow 0.024573317844696633
i: bed 0.008935751943526048
i: Machpelah 0.013403627915289072
i: amongst 0.004467875971763024
i: Surely 0.01116968992940756
i: bake 0.002233937985881512
i: sake 0.024573317844696633
i: Hitti 0.002233937985881512
i: For 0.06478420159056385
i: manner 0.02010544187293361
i: Phichol 0.006701813957644536
i: Hebrew 0.008935751943526048
i: bank 0.002233937985881512
i: walketh 0.002233937985881512
i: Kadmonites 0.002233937985881512
i: towns 0.002233937985881512
i: strengthened 0.002233937985881512
i: peop 0.002233937985881512
i: blessings 0.01116968992940756
i: tarried 0.006701813957644536
i: dukes 0.024573317844696633
i: commandment 0.002233937985881512
i: lived 0.08488964346349745
i: Syrian 0.01116968992940756
i: burdens 0.002233937985881512
i: widow 0.004467875971763024
i: canst 0.002233937985881512
i: assembly 0.002233937985881512
i: worship 0.002233937985881512
i: sir 0.002233937985881512
i: Pildash 0.002233937985881512
i: Magog 0.002233937985881512
i: Kenizzites 0.002233937985881512
i: dwelled 0.008935751943526048
i: Medan 0.002233937985881512
i: Mehetabel 0.002233937985881512
i: fie 0.004467875971763024
i: bird 0.002233937985881512
i: Obal 0.002233937985881512
i: lovest 0.002233937985881512
i: badest 0.002233937985881512
i: age 0.02010544187293361
i: departing 0.002233937985881512
i: ears 0.029041193816459657
i: Sheba 0.006701813957644536
i: unleavened 0.002233937985881512
i: smelled 0.004467875971763024
i: seas 0.002233937985881512
i: grace 0.024573317844696633
i: sweet 0.002233937985881512
i: touching 0.002233937985881512
i: fatfleshed 0.004467875971763024
i: tender 0.006701813957644536
i: truly 0.008935751943526048
i: While 0.002233937985881512
i: gift 0.002233937985881512
i: earth 0.24796711643284783
i: heap 0.013403627915289072
i: Serah 0.002233937985881512
i: quart 0.002233937985881512
i: Kedar 0.002233937985881512
i: ear 0.02010544187293361
i: clo 0.002233937985881512
i: Amal 0.002233937985881512
i: ark 0.0558484496470378
i: forgotten 0.002233937985881512
i: sakes 0.002233937985881512
i: concerning 0.013403627915289072
i: Epher 0.002233937985881512
i: rods 0.013403627915289072
i: Hamathite 0.002233937985881512
i: knowledge 0.004467875971763024
i: cannot 0.024573317844696633
i: lambs 0.008935751943526048
i: On 0.008935751943526048
i: therein 0.02233937985881512
i: where 0.04467875971763024
i: Look 0.002233937985881512
i: between 0.0558484496470378
i: Jidlaph 0.002233937985881512
i: beside 0.004467875971763024
i: remained 0.004467875971763024
i: six 0.015637565901170585
i: Reuben 0.026807255830578143
i: storehouses 0.002233937985881512
i: elders 0.004467875971763024
i: Jabbok 0.002233937985881512
i: arrayed 0.002233937985881512
i: two 0.11616477526583863
i: sixteen 0.002233937985881512
i: Hirah 0.004467875971763024
i: tidings 0.002233937985881512
i: restrained 0.006701813957644536
i: Bela 0.008935751943526048
i: silv 0.004467875971763024
i: rent 0.008935751943526048
i: What 0.06031632561880082
i: thither 0.017871503887052095
i: Potiphar 0.004467875971763024
i: younger 0.03127513180234117
i: white 0.01116968992940756
i: deceived 0.002233937985881512
i: befell 0.002233937985881512
i: learned 0.002233937985881512
i: vineyard 0.002233937985881512
i: firstborn 0.037976945759985704
i: buryingplace 0.013403627915289072
i: citi 0.002233937985881512
i: getting 0.002233937985881512
i: hairs 0.006701813957644536
i: shot 0.004467875971763024
i: no 0.05808238763291931
i: scattered 0.004467875971763024
i: communing 0.002233937985881512
i: must 0.013403627915289072
i: kissed 0.017871503887052095
i: These 0.04691269770351175
i: dungeon 0.002233937985881512
i: flo 0.002233937985881512
i: whose 0.03574300777410419
i: curse 0.008935751943526048
i: formed 0.006701813957644536
i: hide 0.004467875971763024
i: saith 0.01116968992940756
i: Diklah 0.002233937985881512
i: liest 0.002233937985881512
i: sorrow 0.013403627915289072
i: Shem 0.03127513180234117
i: having 0.002233937985881512
i: Meshech 0.002233937985881512
i: grown 0.002233937985881512
i: long 0.004467875971763024
i: piece 0.002233937985881512
i: kids 0.004467875971763024
i: this 0.274774372263426
i: reason 0.004467875971763024
i: roll 0.002233937985881512
i: declare 0.002233937985881512
i: attained 0.002233937985881512
i: obeisance 0.006701813957644536
i: beginning 0.01116968992940756
i: gotten 0.013403627915289072
i: verily 0.002233937985881512
i: nig 0.002233937985881512
i: thoroughly 0.002233937985881512
i: finish 0.002233937985881512
i: many 0.015637565901170585
i: ruled 0.002233937985881512
i: Hear 0.006701813957644536
i: shewed 0.015637565901170585
i: thine 0.05138057367527477
i: wept 0.03127513180234117
i: weep 0.004467875971763024
i: go 0.14297203109641676
i: stars 0.01116968992940756
i: gutters 0.004467875971763024
i: secretly 0.002233937985881512
i: Zar 0.002233937985881512
i: subdue 0.002233937985881512
i: willing 0.004467875971763024
i: place 0.10276114735054954
i: smell 0.006701813957644536
i: looked 0.03350906978822268
i: Lay 0.002233937985881512
i: Jacob 0.39987489947279065
i: .) 0.002233937985881512
i: with 0.6456080779197569
i: hotly 0.002233937985881512
i: our 0.14073809311053526
i: marvelled 0.002233937985881512
i: Irad 0.004467875971763024
i: river 0.03127513180234117
i: comest 0.006701813957644536
i: labour 0.006701813957644536
i: jewels 0.004467875971763024
i: cold 0.002233937985881512
i: order 0.002233937985881512
i: A 0.004467875971763024
i: strive 0.004467875971763024
i: married 0.002233937985881512
i: travailed 0.004467875971763024
i: land 0.4110445894021982
i: Zebul 0.002233937985881512
i: flocks 0.05138057367527477
i: oxen 0.01116968992940756
i: bakemeats 0.002233937985881512
i: roof 0.002233937985881512
i: Horites 0.006701813957644536
i: Mishma 0.002233937985881512
i: Then 0.08488964346349745
i: Jegarsahadutha 0.002233937985881512
i: prevail 0.004467875971763024
i: noon 0.004467875971763024
i: Hemdan 0.002233937985881512
i: instruments 0.002233937985881512
i: am 0.09605933339290501
i: Lud 0.002233937985881512
i: mean 0.002233937985881512
i: multiply 0.04021088374586722
i: down 0.1318023411670092
i: anguish 0.002233937985881512
i: fast 0.002233937985881512
i: Asshurim 0.002233937985881512
i: Enos 0.01116968992940756
i: Bilhah 0.02010544187293361
i: garments 0.006701813957644536
i: Lest 0.006701813957644536
i: Tamar 0.01116968992940756
i: Huz 0.002233937985881512
i: Isui 0.002233937985881512
i: charge 0.004467875971763024
i: Up 0.004467875971763024
i: overthrew 0.004467875971763024
i: strange 0.006701813957644536
i: former 0.002233937985881512
i: Shuah 0.006701813957644536
i: mark 0.002233937985881512
i: Zeboiim 0.004467875971763024
i: waxed 0.006701813957644536
i: interpret 0.008935751943526048
i: Iram 0.002233937985881512
i: Zemarite 0.002233937985881512
i: killed 0.002233937985881512
i: Jeush 0.006701813957644536
i: water 0.06031632561880082
i: brook 0.002233937985881512
i: Nahath 0.004467875971763024
i: feeble 0.002233937985881512
i: Haggi 0.002233937985881512
i: made 0.16084353498346887
i: fear 0.024573317844696633
i: asked 0.02010544187293361
i: sixth 0.004467875971763024
i: played 0.002233937985881512
i: horse 0.002233937985881512
i: second 0.03127513180234117
i: opened 0.026807255830578143
i: childless 0.002233937985881512
i: Shobal 0.006701813957644536
i: hire 0.008935751943526048
i: bak 0.002233937985881512
i: priests 0.006701813957644536
i: wander 0.002233937985881512
i: vagabond 0.004467875971763024
i: Jetheth 0.002233937985881512
i: sevens 0.004467875971763024
i: seeing 0.015637565901170585
i: help 0.006701813957644536
i: Elah 0.002233937985881512
i: Egyptian 0.015637565901170585
i: appointed 0.008935751943526048
i: removing 0.002233937985881512
i: thicket 0.002233937985881512
i: Hereby 0.004467875971763024
i: time 0.0558484496470378
i: blossoms 0.002233937985881512
i: fatness 0.004467875971763024
i: Unto 0.017871503887052095
i: laden 0.004467875971763024
i: lingered 0.004467875971763024
i: ourselves 0.004467875971763024
i: Babel 0.004467875971763024
i: Enmishpat 0.002233937985881512
i: weig 0.002233937985881512
i: Aner 0.002233937985881512
i: nati 0.002233937985881512
i: didst 0.015637565901170585
i: broth 0.004467875971763024
i: lan 0.002233937985881512
i: inheritance 0.004467875971763024
i: devour 0.002233937985881512
i: sorely 0.002233937985881512
i: rebuked 0.004467875971763024
i: forget 0.004467875971763024
i: nine 0.026807255830578143
i: wick 0.002233937985881512
i: bruise 0.004467875971763024
i: rank 0.004467875971763024
i: meat 0.02233937985881512
i: Bethuel 0.02010544187293361
i: decreased 0.002233937985881512
i: fo 0.004467875971763024
i: His 0.004467875971763024
i: sent 0.09829327137878653
i: continually 0.006701813957644536
i: deprived 0.002233937985881512
i: that 1.1370744348136896
i: Manass 0.002233937985881512
i: beget 0.002233937985881512
i: matter 0.004467875971763024
i: couched 0.002233937985881512
i: moveth 0.006701813957644536
i: Methusa 0.002233937985881512
i: Esau 0.16531141095523189
i: Earth 0.002233937985881512
i: ea 0.006701813957644536
i: Eve 0.004467875971763024
i: earing 0.002233937985881512
i: Naphish 0.002233937985881512
i: wild 0.002233937985881512
i: heads 0.004467875971763024
i: Ephraim 0.024573317844696633
i: Zuzims 0.002233937985881512
i: daught 0.006701813957644536
i: Eshban 0.002233937985881512
i: Set 0.002233937985881512
i: without 0.02010544187293361
i: skins 0.004467875971763024
i: Hivite 0.006701813957644536
i: ne 0.002233937985881512
i: fourteenth 0.002233937985881512
i: strong 0.004467875971763024
i: Er 0.01116968992940756
i: wi 0.002233937985881512
i: prospered 0.002233937985881512
i: loss 0.002233937985881512
i: nigh 0.002233937985881512
i: Forgive 0.002233937985881512
i: none 0.017871503887052095
i: exceeding 0.006701813957644536
i: hazel 0.002233937985881512
i: Speak 0.002233937985881512
i: carcases 0.002233937985881512
i: Dinah 0.015637565901170585
i: reproa 0.002233937985881512
i: co 0.002233937985881512
i: searched 0.008935751943526048
i: Ludim 0.002233937985881512
i: thread 0.006701813957644536
i: Timna 0.004467875971763024
i: abode 0.004467875971763024
i: despised 0.006701813957644536
i: servant 0.09159145742114198
i: thy 0.5964614422303637
i: fetch 0.01116968992940756
i: Potipherah 0.006701813957644536
i: buy 0.026807255830578143
i: descending 0.002233937985881512
i: plant 0.002233937985881512
i: first 0.03574300777410419
i: hunter 0.006701813957644536
i: still 0.004467875971763024
i: tar 0.002233937985881512
i: provide 0.004467875971763024
i: spee 0.002233937985881512
i: al 0.006701813957644536
i: Lahairoi 0.004467875971763024
i: sojourn 0.006701813957644536
i: uncovered 0.002233937985881512
i: Peniel 0.002233937985881512
i: sackcloth 0.002233937985881512
i: haste 0.006701813957644536
i: fa 0.004467875971763024
i: part 0.006701813957644536
i: colours 0.006701813957644536
i: Joktan 0.006701813957644536
i: beasts 0.013403627915289072
i: guilty 0.002233937985881512
i: loveth 0.002233937985881512
i: God 0.5160396747386292
i: anoth 0.004467875971763024
i: daughte 0.017871503887052095
i: seekest 0.002233937985881512
i: dunge 0.002233937985881512
i: Sabtech 0.002233937985881512
i: occasion 0.002233937985881512
i: Sarah 0.08265570547761594
i: just 0.002233937985881512
i: Ararat 0.002233937985881512
i: Penuel 0.002233937985881512
i: entreated 0.002233937985881512
i: laws 0.002233937985881512
i: affliction 0.008935751943526048
i: year 0.02010544187293361
i: utmost 0.002233937985881512
i: fled 0.024573317844696633
i: oil 0.004467875971763024
i: Onan 0.01116968992940756
i: likene 0.002233937985881512
i: quiver 0.002233937985881512
i: instructor 0.002233937985881512
i: Nod 0.002233937985881512
i: youth 0.004467875971763024
i: An 0.002233937985881512
i: Mahalaleel 0.01116968992940756
i: goa 0.002233937985881512
i: hast 0.11616477526583863
i: ash 0.002233937985881512
i: blameless 0.002233937985881512
i: north 0.002233937985881512
i: process 0.004467875971763024
i: wrong 0.002233937985881512
i: scarlet 0.004467875971763024
i: goat 0.002233937985881512
i: Egy 0.006701813957644536
i: physicians 0.004467875971763024
i: altogether 0.002233937985881512
i: blessed 0.09605933339290501
i: Euphrates 0.002233937985881512
i: Ephah 0.002233937985881512
i: overseer 0.004467875971763024
i: childr 0.002233937985881512
i: Elbethel 0.002233937985881512
i: greatly 0.01116968992940756
i: kiss 0.004467875971763024
i: Shuni 0.002233937985881512
i: afraid 0.02010544187293361
i: Anamim 0.002233937985881512
i: child 0.03574300777410419
i: Emins 0.002233937985881512
i: Spirit 0.004467875971763024
i: kneel 0.002233937985881512
i: weight 0.004467875971763024
i: slayeth 0.002233937985881512
i: Asher 0.008935751943526048
i: Baalhanan 0.004467875971763024
i: evening 0.02233937985881512
i: mountains 0.008935751943526048
i: Aholibamah 0.015637565901170585
i: plagues 0.002233937985881512
i: here 0.026807255830578143
i: hardly 0.002233937985881512
i: Until 0.002233937985881512
i: preserved 0.002233937985881512
i: these 0.18094897685640246
i: mine 0.03127513180234117
i: drank 0.008935751943526048
i: elder 0.008935751943526048
i: handmaids 0.004467875971763024
i: peaceable 0.002233937985881512
i: saved 0.002233937985881512
i: pigeon 0.002233937985881512
i: why 0.01116968992940756
i: breadth 0.004467875971763024
i: pursued 0.008935751943526048
i: grief 0.002233937985881512
i: brick 0.004467875971763024
i: cattle 0.1116968992940756
i: We 0.037976945759985704
i: travail 0.002233937985881512
i: Zimran 0.002233937985881512
i: Gershon 0.002233937985881512
i: Eliezer 0.002233937985881512
i: Tubal 0.002233937985881512
i: stalk 0.004467875971763024
i: They 0.013403627915289072
i: door 0.026807255830578143
i: Angel 0.002233937985881512
i: tongue 0.002233937985881512
i: meal 0.002233937985881512
i: behold 0.14520596908229827
i: dreadful 0.002233937985881512
i: issue 0.002233937985881512
i: vale 0.008935751943526048
i: reward 0.002233937985881512
i: creeping 0.02010544187293361
i: field 0.09829327137878653
i: rib 0.002233937985881512
i: Duke 0.01116968992940756
i: dreamed 0.026807255830578143
i: wherein 0.017871503887052095
i: shaved 0.002233937985881512
i: Karnaim 0.002233937985881512
i: forgive 0.002233937985881512
i: isles 0.002233937985881512
i: forward 0.002233937985881512
i: sheddeth 0.002233937985881512
i: delight 0.002233937985881512
i: Beware 0.002233937985881512
i: eastward 0.006701813957644536
i: Out 0.004467875971763024
i: spoken 0.02010544187293361
i: foals 0.002233937985881512
i: removed 0.013403627915289072
i: nights 0.004467875971763024
i: displease 0.002233937985881512
i: halted 0.002233937985881512
i: wheat 0.002233937985881512
i: food 0.042444821731748725
i: circumcis 0.002233937985881512
i: blessi 0.002233937985881512
i: reached 0.002233937985881512
i: watering 0.002233937985881512
i: throne 0.002233937985881512
i: plagued 0.002233937985881512
i: overtake 0.002233937985881512
i: Whoso 0.002233937985881512
i: worth 0.004467875971763024
i: Birsha 0.002233937985881512
i: sacrifice 0.002233937985881512
i: spotted 0.013403627915289072
i: Laban 0.12063265123760164
i: nothing 0.008935751943526048
i: Judge 0.002233937985881512
i: ways 0.002233937985881512
i: hence 0.006701813957644536
i: herb 0.015637565901170585
i: waited 0.002233937985881512
i: By 0.008935751943526048
i: eventide 0.002233937985881512
i: void 0.002233937985881512
i: youngest 0.02233937985881512
i: Dumah 0.002233937985881512
i: grieved 0.008935751943526048
i: Midianites 0.004467875971763024
i: savoury 0.013403627915289072
i: silver 0.02010544187293361
i: near 0.053614511661156286
i: Dodanim 0.002233937985881512
i: Moab 0.004467875971763024
i: butlers 0.002233937985881512
i: enmity 0.002233937985881512
i: Arbah 0.002233937985881512
i: Shaveh 0.004467875971763024
i: thyself 0.008935751943526048
i: stript 0.002233937985881512
i: doth 0.006701813957644536
i: Sitnah 0.002233937985881512
i: worthy 0.002233937985881512
i: served 0.02010544187293361
i: length 0.004467875971763024
i: Tola 0.002233937985881512
i: in 1.313555535698329
i: Ohad 0.002233937985881512
i: their 0.3417925118398713
i: voice 0.049146635689393266
i: trees 0.006701813957644536
i: east 0.026807255830578143
i: torn 0.004467875971763024
i: accept 0.002233937985881512
i: concubine 0.004467875971763024
i: Get 0.004467875971763024
i: substance 0.015637565901170585
i: truth 0.004467875971763024
i: pitched 0.015637565901170585
i: perpetual 0.002233937985881512
i: Elishah 0.002233937985881512
i: lawgiver 0.002233937985881512
i: conspired 0.002233937985881512
i: Deliver 0.002233937985881512
i: whether 0.017871503887052095
i: rise 0.004467875971763024
i: wine 0.024573317844696633
i: buried 0.029041193816459657
i: add 0.002233937985881512
i: thigh 0.015637565901170585
i: foolishly 0.002233937985881512
i: Canaanite 0.006701813957644536
i: n 0.008935751943526048
i: thirty 0.037976945759985704
i: of 3.033687784827093
i: goods 0.017871503887052095
i: least 0.004467875971763024
i: followed 0.004467875971763024
i: Temani 0.002233937985881512
i: Gaham 0.002233937985881512
i: women 0.01116968992940756
i: inhabited 0.002233937985881512
i: army 0.002233937985881512
i: fou 0.002233937985881512
i: sold 0.02233937985881512
i: At 0.002233937985881512
i: wearied 0.002233937985881512
i: Damascus 0.004467875971763024
i: mouths 0.002233937985881512
i: Machir 0.002233937985881512
i: duke 0.06031632561880082
i: always 0.002233937985881512
i: Every 0.006701813957644536
i: winged 0.002233937985881512
i: blindness 0.002233937985881512
i: above 0.024573317844696633
i: like 0.004467875971763024
i: shall 0.5651863104280225
i: coffin 0.002233937985881512
i: prophet 0.002233937985881512
i: Lo 0.004467875971763024
i: gray 0.006701813957644536
i: Melchizedek 0.002233937985881512
i: presented 0.004467875971763024
i: fountain 0.004467875971763024
i: Woman 0.002233937985881512
i: ripe 0.002233937985881512
i: restore 0.008935751943526048
i: trained 0.002233937985881512
i: morter 0.002233937985881512
i: again 0.09829327137878653
i: abundantly 0.008935751943526048
i: little 0.04467875971763024
i: reviv 0.002233937985881512
i: conceal 0.002233937985881512
i: curseth 0.004467875971763024
i: grass 0.004467875971763024
i: afterward 0.008935751943526048
i: wrought 0.002233937985881512
i: herein 0.002233937985881512
i: favour 0.006701813957644536
i: mourned 0.006701813957644536
i: h 0.037976945759985704
i: years 0.2278616745599142
i: Hazezontamar 0.002233937985881512
i: number 0.008935751943526048
i: known 0.01116968992940756
i: Nahor 0.03574300777410419
i: selfsame 0.006701813957644536
i: besought 0.002233937985881512
i: firstlings 0.002233937985881512
i: plain 0.026807255830578143
i: west 0.004467875971763024
i: bough 0.004467875971763024
i: fed 0.013403627915289072
i: repenteth 0.002233937985881512
i: certainly 0.01116968992940756
i: pitcher 0.02010544187293361
i: Dedan 0.006701813957644536
i: hearkened 0.015637565901170585
i: bondman 0.002233937985881512
i: Zibeon 0.013403627915289072
i: whom 0.0558484496470378
i: depart 0.004467875971763024
i: belong 0.002233937985881512
i: poor 0.002233937985881512
i: Judith 0.002233937985881512
i: stolen 0.017871503887052095
i: twelve 0.013403627915289072
i: Zerah 0.006701813957644536
i: Send 0.008935751943526048
i: She 0.017871503887052095
i: denied 0.002233937985881512
i: So 0.04691269770351175
i: eaten 0.02010544187293361
i: art 0.06925207756232687
i: fierce 0.002233937985881512
i: spoil 0.002233937985881512
i: kine 0.024573317844696633
i: Nay 0.013403627915289072
i: aga 0.002233937985881512
i: high 0.013403627915289072
i: hath 0.17871503887052095
i: birthright 0.013403627915289072
i: nuts 0.002233937985881512
i: spilled 0.002233937985881512
i: kid 0.008935751943526048
i: enemies 0.006701813957644536
i: prey 0.004467875971763024
i: woman 0.04467875971763024
i: wilderness 0.015637565901170585
i: Shel 0.002233937985881512
i: hands 0.04021088374586722
i: on 0.1273344651952462
i: whole 0.02233937985881512
i: Japheth 0.015637565901170585
i: mandrakes 0.01116968992940756
i: chariot 0.004467875971763024
i: cleave 0.002233937985881512
i: heard 0.06701813957644535
i: w 0.004467875971763024
i: saddled 0.002233937985881512
i: committed 0.004467875971763024
i: Atad 0.004467875971763024
i: ! 0.004467875971763024
i: kn 0.002233937985881512
i: health 0.002233937985881512
i: hundred 0.13627021713877221
i: grievous 0.013403627915289072
i: to 1.3649361093736039
i: more 0.04691269770351175
i: sewed 0.002233937985881512
i: purchase 0.002233937985881512
i: la 0.006701813957644536
i: remove 0.002233937985881512
i: Matred 0.002233937985881512
i: whence 0.008935751943526048
i: intreated 0.004467875971763024
i: appoint 0.002233937985881512
i: mighty 0.015637565901170585
i: named 0.006701813957644536
i: visit 0.004467875971763024
i: may 0.09605933339290501
i: errand 0.002233937985881512
i: straitly 0.002233937985881512
i: Massa 0.002233937985881512
i: captain 0.02010544187293361
i: hous 0.002233937985881512
i: themselves 0.03127513180234117
i: stink 0.002233937985881512
i: li 0.004467875971763024
i: Amalek 0.002233937985881512
i: hearken 0.01116968992940756
i: valley 0.006701813957644536
i: darkne 0.002233937985881512
i: enough 0.01116968992940756
i: vowedst 0.002233937985881512
i: slimepits 0.002233937985881512
i: Edom 0.024573317844696633
i: sin 0.017871503887052095
i: wiv 0.002233937985881512
i: aloud 0.002233937985881512
i: drought 0.002233937985881512
i: s 0.5875256902868377
i: Calneh 0.002233937985881512
i: violently 0.002233937985881512
i: Seeing 0.002233937985881512
i: Resen 0.002233937985881512
i: stopped 0.006701813957644536
i: each 0.015637565901170585
i: home 0.006701813957644536
i: Ehi 0.002233937985881512
i: filled 0.01116968992940756
i: hunt 0.002233937985881512
i: got 0.006701813957644536
i: doubled 0.002233937985881512
i: sepulchre 0.002233937985881512
i: sadly 0.002233937985881512
i: Slay 0.002233937985881512
i: fetched 0.004467875971763024
i: city 0.09159145742114198
i: Arkite 0.002233937985881512
i: mention 0.002233937985881512
i: ;) 0.002233937985881512
i: imagination 0.004467875971763024
i: na 0.002233937985881512
i: drunken 0.002233937985881512
i: company 0.013403627915289072
i: darkness 0.008935751943526048
i: begat 0.1496738450540613
i: store 0.004467875971763024
i: blesseth 0.002233937985881512
i: form 0.002233937985881512
i: Almodad 0.002233937985881512
i: drew 0.013403627915289072
i: cru 0.002233937985881512
i: slain 0.004467875971763024
i: cursed 0.01116968992940756
i: them 0.5138057367527478
i: Akan 0.002233937985881512
i: gr 0.002233937985881512
i: Goshen 0.02233937985881512
i: kings 0.017871503887052095
i: Appoint 0.002233937985881512
i: Manahath 0.002233937985881512
i: heav 0.002233937985881512
i: begettest 0.002233937985881512
i: henceforth 0.002233937985881512
i: ask 0.002233937985881512
i: very 0.04021088374586722
i: likeness 0.004467875971763024
i: height 0.002233937985881512
i: putting 0.002233937985881512
i: up 0.27254043427754443
i: blasted 0.006701813957644536
i: face 0.10499508533643107
i: kindred 0.02233937985881512
i: daughers 0.004467875971763024
i: messes 0.002233937985881512
i: fellow 0.002233937985881512
i: angry 0.006701813957644536
i: son 0.3395585738539898
i: given 0.04691269770351175
i: places 0.004467875971763024
i: heavens 0.006701813957644536
i: Accad 0.002233937985881512
i: dove 0.01116968992940756
i: Adullamite 0.006701813957644536
i: Shebah 0.002233937985881512
i: she 0.3596640157269234
i: mind 0.004467875971763024
i: knees 0.006701813957644536
i: the 5.386024483960325
i: foot 0.004467875971763024
i: Elon 0.006701813957644536
i: Hori 0.004467875971763024
i: Moriah 0.002233937985881512
i: vail 0.006701813957644536
i: bulls 0.002233937985881512
i: mercy 0.008935751943526048
i: Mehujael 0.004467875971763024
i: Philistim 0.002233937985881512
i: Kiriathaim 0.002233937985881512
i: Raamah 0.004467875971763024
i: Timnah 0.002233937985881512
i: Lamech 0.02233937985881512
i: reproach 0.002233937985881512
i: most 0.008935751943526048
i: Bow 0.002233937985881512
i: lamentati 0.002233937985881512
i: Moabites 0.002233937985881512
i: Shammah 0.004467875971763024
i: wealth 0.002233937985881512
i: creature 0.017871503887052095
i: Mizz 0.004467875971763024
i: salt 0.004467875971763024
i: will 0.4356179072468948
i: blessing 0.026807255830578143
i: Dinhabah 0.002233937985881512
i: reserved 0.002233937985881512
i: household 0.01116968992940756
i: cunning 0.002233937985881512
i: uncircumcised 0.004467875971763024
i: merry 0.002233937985881512
i: sons 0.3172191939951747
i: can 0.015637565901170585
i: Haran 0.029041193816459657
i: end 0.02010544187293361
i: cry 0.008935751943526048
i: eldest 0.008935751943526048
i: Succoth 0.004467875971763024
i: Jahleel 0.002233937985881512
i: lighted 0.004467875971763024
i: sprung 0.004467875971763024
i: traffick 0.002233937985881512
i: steal 0.004467875971763024
i: Swear 0.004467875971763024
i: Fulfil 0.002233937985881512
i: Shimron 0.002233937985881512
i: restored 0.008935751943526048
i: closed 0.004467875971763024
i: Kittim 0.002233937985881512
i: Zo 0.002233937985881512
i: dust 0.017871503887052095
i: worshipped 0.006701813957644536
i: gifts 0.002233937985881512
i: Almighty 0.013403627915289072
i: thereby 0.002233937985881512
i: cubits 0.008935751943526048
i: If 0.04021088374586722
i: ceased 0.002233937985881512
i: LO 0.008935751943526048
i: Sidon 0.004467875971763024
i: fruit 0.02010544187293361
i: seventh 0.008935751943526048
i: fifth 0.01116968992940756
i: heart 0.024573317844696633
i: balm 0.004467875971763024
i: could 0.024573317844696633
i: serva 0.004467875971763024
i: eleven 0.004467875971763024
i: deep 0.013403627915289072
i: fishes 0.002233937985881512
i: fowls 0.01116968992940756
i: returned 0.04021088374586722
i: Because 0.024573317844696633
i: speckled 0.017871503887052095
i: waters 0.07148601554820838
i: Beno 0.002233937985881512
i: themselv 0.004467875971763024
i: fat 0.01116968992940756
i: replenish 0.004467875971763024
i: dainties 0.002233937985881512
i: Put 0.004467875971763024
i: garden 0.029041193816459657
i: cut 0.004467875971763024
i: pea 0.002233937985881512
i: hollow 0.008935751943526048
i: room 0.008935751943526048
i: Know 0.004467875971763024
i: past 0.002233937985881512
i: Girgasite 0.002233937985881512
i: gave 0.10722902332231257
i: take 0.10499508533643107
i: olive 0.002233937985881512
i: sun 0.013403627915289072
i: Therefore 0.026807255830578143
i: service 0.004467875971763024
i: grapes 0.002233937985881512
i: sacks 0.017871503887052095
i: Gerar 0.017871503887052095
i: Havilah 0.008935751943526048
i: Stand 0.002233937985881512
i: brink 0.002233937985881512
i: yield 0.004467875971763024
i: away 0.08265570547761594
i: a 0.7640067911714771
i: stories 0.002233937985881512
i: nation 0.017871503887052095
i: one 0.15637565901170583
i: fly 0.002233937985881512
i: pleased 0.008935751943526048
i: concubi 0.002233937985881512
i: Beeri 0.002233937985881512
i: shekels 0.006701813957644536
i: put 0.08935751943526048
i: Bring 0.017871503887052095
i: Hamul 0.002233937985881512
i: needeth 0.002233937985881512
i: therefore 0.07818782950585292
i: side 0.004467875971763024
i: integrity 0.004467875971763024
i: thi 0.006701813957644536
i: Mibsam 0.002233937985881512
i: shalt 0.16307747296935038
i: favoured 0.024573317844696633
i: Tema 0.002233937985881512
i: mou 0.002233937985881512
i: commended 0.002233937985881512
i: When 0.017871503887052095
i: Hobah 0.002233937985881512
i: morning 0.04467875971763024
i: backward 0.006701813957644536
i: Reub 0.002233937985881512
i: creepeth 0.017871503887052095
i: ringstraked 0.015637565901170585
i: welfare 0.002233937985881512
i: toward 0.042444821731748725
i: faults 0.002233937985881512
i: lightly 0.002233937985881512
i: Except 0.004467875971763024
i: naked 0.008935751943526048
i: avenged 0.002233937985881512
i: feebler 0.002233937985881512
i: stole 0.002233937985881512
i: bring 0.08935751943526048
i: goeth 0.008935751943526048
i: feed 0.013403627915289072
i: Bered 0.002233937985881512
i: Me 0.002233937985881512
i: Cast 0.002233937985881512
i: lentiles 0.002233937985881512
i: brought 0.1340362791528907
i: stretched 0.004467875971763024
i: redeemed 0.002233937985881512
i: horses 0.002233937985881512
i: portion 0.013403627915289072
i: flaming 0.002233937985881512
i: Zepho 0.004467875971763024
i: good 0.09829327137878653
i: Timnath 0.006701813957644536
i: righteous 0.02233937985881512
i: struggled 0.002233937985881512
i: Amorite 0.006701813957644536
i: brother 0.20328835671521758
i: Ye 0.02010544187293361
i: builded 0.015637565901170585
i: ladder 0.002233937985881512
i: serpent 0.013403627915289072
i: Take 0.013403627915289072
i: chi 0.002233937985881512
i: tents 0.01116968992940756
i: lade 0.002233937985881512
i: Zaphnathpaaneah 0.002233937985881512
i: fathers 0.02010544187293361
i: fire 0.006701813957644536
i: send 0.026807255830578143
i: changes 0.004467875971763024
i: Canaanites 0.015637565901170585
i: meadow 0.002233937985881512
i: keeper 0.01116968992940756
i: Ophir 0.002233937985881512
i: countenance 0.008935751943526048
i: fashion 0.002233937985881512
i: Keturah 0.004467875971763024
i: chesnut 0.002233937985881512
i: Asshur 0.004467875971763024
i: Cherubims 0.002233937985881512
i: needs 0.008935751943526048
i: Rameses 0.002233937985881512
i: mother 0.06255026360468234
i: herds 0.024573317844696633
i: Rebek 0.002233937985881512
i: deal 0.013403627915289072
i: morsel 0.002233937985881512
i: catt 0.006701813957644536
i: Egyptia 0.002233937985881512
i: garmen 0.002233937985881512
i: bundle 0.002233937985881512
i: Naphtuhim 0.002233937985881512
i: sinew 0.004467875971763024
i: beyond 0.006701813957644536
i: terror 0.002233937985881512
i: concubines 0.002233937985881512
i: speak 0.029041193816459657
i: Arvadite 0.002233937985881512
i: foal 0.002233937985881512
i: breathed 0.002233937985881512
i: Cain 0.03574300777410419
i: handle 0.002233937985881512
i: some 0.013403627915289072
i: compasseth 0.004467875971763024
i: endure 0.002233937985881512
i: Tarshish 0.002233937985881512
i: Isa 0.006701813957644536
i: accepted 0.004467875971763024
i: else 0.004467875971763024
i: Hittite 0.015637565901170585
i: cease 0.002233937985881512
i: songs 0.002233937985881512
i: ye 0.19435260477169153
i: grave 0.015637565901170585
i: tribute 0.002233937985881512
i: is 0.5964614422303637
i: oth 0.002233937985881512
i: occupation 0.004467875971763024
i: Why 0.006701813957644536
i: eatest 0.002233937985881512
i: unit 0.002233937985881512
i: Gilead 0.008935751943526048
i: Teman 0.006701813957644536
i: spread 0.008935751943526048
i: ribs 0.002233937985881512
i: lifted 0.03574300777410419
i: speckl 0.002233937985881512
i: smite 0.006701813957644536
i: wentest 0.002233937985881512
i: stay 0.002233937985881512
i: light 0.024573317844696633
i: sacrifices 0.002233937985881512
i: country 0.03574300777410419
i: hearts 0.002233937985881512
i: princes 0.006701813957644536
i: Paran 0.002233937985881512
i: begin 0.002233937985881512
i: doing 0.004467875971763024
i: rewarded 0.002233937985881512
i: Leummim 0.002233937985881512
i: since 0.004467875971763024
i: dine 0.002233937985881512
i: rest 0.008935751943526048
i: Sheleph 0.002233937985881512
i: for 0.663479581806809
i: against 0.05138057367527477
i: Rephaims 0.004467875971763024
i: rode 0.002233937985881512
i: Do 0.006701813957644536
i: wells 0.004467875971763024
i: ward 0.01116968992940756
i: bread 0.049146635689393266
i: Reuel 0.01116968992940756
i: fleddest 0.002233937985881512
i: garment 0.017871503887052095
i: ravin 0.002233937985881512
i: Gentiles 0.002233937985881512
i: edge 0.002233937985881512
i: bone 0.004467875971763024
i: change 0.002233937985881512
i: obtain 0.002233937985881512
i: famine 0.053614511661156286
i: doubt 0.002233937985881512
i: milch 0.002233937985881512
i: trespass 0.006701813957644536
i: strength 0.006701813957644536
i: Canaanitish 0.002233937985881512
i: officers 0.006701813957644536
i: branches 0.006701813957644536
i: saying 0.17648110088463945
i: nostrils 0.004467875971763024
i: Maachah 0.002233937985881512
i: oa 0.002233937985881512
i: burn 0.004467875971763024
i: thought 0.008935751943526048
i: eyes 0.08265570547761594
i: offering 0.017871503887052095
i: Assyria 0.002233937985881512
i: grisl 0.002233937985881512
i: tenor 0.002233937985881512
i: died 0.07371995353408989
i: chariots 0.002233937985881512
i: millions 0.002233937985881512
i: shear 0.004467875971763024
i: Simeon 0.02233937985881512
i: feast 0.01116968992940756
i: weaned 0.004467875971763024
i: Ephra 0.004467875971763024
i: live 0.024573317844696633
i: choice 0.004467875971763024
i: before 0.20328835671521758
i: either 0.004467875971763024
i: it 0.6478420159056385
i: whither 0.01116968992940756
i: multitude 0.015637565901170585
i: forgat 0.002233937985881512
i: gavest 0.002233937985881512
i: ) 0.004467875971763024
i: Ishmeelites 0.008935751943526048
i: midst 0.013403627915289072
i: sixty 0.013403627915289072
i: tower 0.006701813957644536
i: threescore 0.01116968992940756
i: Bilhan 0.002233937985881512
i: wa 0.002233937985881512
i: heat 0.004467875971763024
i: ev 0.008935751943526048
i: wages 0.01116968992940756
i: Hamor 0.024573317844696633
i: experience 0.002233937985881512
i: Also 0.004467875971763024
i: withhold 0.002233937985881512
i: Abraham 0.28817800017871503
i: shrank 0.004467875971763024
i: merciful 0.002233937985881512
i: dwe 0.006701813957644536
i: early 0.015637565901170585
i: Chesed 0.002233937985881512
i: office 0.002233937985881512
i: Zebulun 0.006701813957644536
i: hills 0.002233937985881512
i: Mesha 0.002233937985881512
i: destitute 0.002233937985881512
i: Shiloh 0.002233937985881512
i: earring 0.006701813957644536
i: That 0.024573317844696633
i: Allonbachuth 0.002233937985881512
i: Perizzit 0.002233937985881512
i: might 0.024573317844696633
i: aprons 0.002233937985881512
i: befall 0.008935751943526048
i: round 0.01116968992940756
i: Calah 0.004467875971763024
i: afterwards 0.002233937985881512
i: shepherds 0.004467875971763024
i: From 0.002233937985881512
i: meanest 0.002233937985881512
i: Hebrews 0.004467875971763024
i: thou 0.6076311321597713
i: peaceably 0.002233937985881512
i: Am 0.004467875971763024
i: envied 0.006701813957644536
i: bad 0.006701813957644536
i: than 0.03350906978822268
i: maidservants 0.01116968992940756
i: pilled 0.004467875971763024
i: Hanoch 0.004467875971763024
i: sist 0.006701813957644536
i: flesh 0.05808238763291931
i: servan 0.006701813957644536
i: thereof 0.026807255830578143
i: heifer 0.002233937985881512
i: Kohath 0.002233937985881512
i: brimstone 0.002233937985881512
i: Areli 0.002233937985881512
i: Some 0.002233937985881512
i: But 0.08265570547761594
i: progenitors 0.002233937985881512
i: leaves 0.002233937985881512
i: covered 0.013403627915289072
i: Say 0.004467875971763024
i: Jared 0.01116968992940756
i: arise 0.017871503887052095
i: Masrekah 0.002233937985881512
i: . 2.9376284514341884
i: Letushim 0.002233937985881512
i: Ham 0.02233937985881512
i: submit 0.002233937985881512
i: months 0.002233937985881512
i: Is 0.024573317844696633
i: meant 0.002233937985881512
i: cool 0.002233937985881512
i: generation 0.006701813957644536
i: Ashkenaz 0.002233937985881512
i: unto 1.318023411670092
i: house 0.18318291484228397
i: token 0.008935751943526048
i: Elparan 0.002233937985881512
i: consume 0.002233937985881512
i: felt 0.002233937985881512
i: lest 0.03127513180234117
i: wise 0.008935751943526048
i: brown 0.008935751943526048
i: Isaac 0.1720132249128764
i: bereaved 0.006701813957644536
i: sheep 0.037976945759985704
i: o 0.01116968992940756
i: covenant 0.05808238763291931
i: love 0.008935751943526048
i: stone 0.024573317844696633
i: tiller 0.002233937985881512
i: golden 0.002233937985881512
i: corn 0.037976945759985704
i: Zidon 0.002233937985881512
i: Go 0.03127513180234117
i: Chezib 0.002233937985881512
i: believed 0.004467875971763024
i: overspread 0.002233937985881512
i: sea 0.017871503887052095
i: furnace 0.004467875971763024
i: badne 0.002233937985881512
i: conceived 0.049146635689393266
i: sore 0.02233937985881512
i: stranger 0.015637565901170585
i: borders 0.004467875971763024
i: si 0.002233937985881512
i: wicked 0.008935751943526048
i: Hemam 0.002233937985881512
i: slaughter 0.002233937985881512
i: Levi 0.013403627915289072
i: Girgashites 0.002233937985881512
i: answered 0.037976945759985704
i: virgin 0.004467875971763024
i: Methusael 0.002233937985881512
i: seeth 0.004467875971763024
i: hor 0.002233937985881512
i: Luz 0.006701813957644536
i: overthrow 0.004467875971763024
i: erected 0.002233937985881512
i: prisoners 0.004467875971763024
i: divineth 0.002233937985881512
i: week 0.004467875971763024
i: air 0.017871503887052095
i: oak 0.002233937985881512
i: lean 0.002233937985881512
i: southward 0.002233937985881512
i: well 0.10946296130819408
i: All 0.01116968992940756
i: camels 0.049146635689393266
i: dream 0.06925207756232687
i: faces 0.008935751943526048
i: Padan 0.002233937985881512
i: This 0.049146635689393266
i: went 0.24573317844696632
i: straw 0.004467875971763024
i: all 0.5473148065409704
i: Mezahab 0.002233937985881512
i: among 0.04467875971763024
i: tribes 0.004467875971763024
i: drove 0.013403627915289072
i: days 0.13627021713877221
i: not 0.5004021088374587
i: furniture 0.002233937985881512
i: build 0.004467875971763024
i: laid 0.029041193816459657
i: leaf 0.002233937985881512
i: mist 0.002233937985881512
i: Not 0.002233937985881512
i: Are 0.002233937985881512
i: Ajah 0.002233937985881512
i: going 0.006701813957644536
i: Sinite 0.002233937985881512
i: Rebekah 0.06478420159056385
i: shepherd 0.004467875971763024
i: dale 0.002233937985881512
i: lying 0.004467875971763024
i: meditate 0.002233937985881512
i: bondmen 0.004467875971763024
i: thereon 0.004467875971763024
i: mountain 0.01116968992940756
i: finished 0.002233937985881512
i: reach 0.002233937985881512
i: separated 0.006701813957644536
i: through 0.01116968992940756
i: bondwoman 0.008935751943526048
i: serve 0.02010544187293361
i: chain 0.002233937985881512
i: sit 0.002233937985881512
i: Night 0.002233937985881512
i: myself 0.004467875971763024
i: Seba 0.002233937985881512
i: provender 0.008935751943526048
i: lords 0.002233937985881512
i: touched 0.006701813957644536
i: ' 0.5986953802162452
i: ou 0.002233937985881512
i: mount 0.02233937985881512
i: shadow 0.002233937985881512
i: Sabtah 0.002233937985881512
i: Aram 0.006701813957644536
i: carry 0.02010544187293361
i: consumed 0.006701813957644536
i: Judah 0.06255026360468234
i: old 0.10052720936466804
i: Nineveh 0.004467875971763024
i: nor 0.015637565901170585
i: audience 0.006701813957644536
i: hind 0.002233937985881512
i: spe 0.002233937985881512
i: drinketh 0.002233937985881512
i: would 0.015637565901170585
i: yesternight 0.006701813957644536
i: appease 0.002233937985881512
i: work 0.008935751943526048
i: spoiled 0.004467875971763024
i: horsemen 0.002233937985881512
i: Joseph 0.3507282637833974
i: Shinar 0.008935751943526048
i: numbered 0.006701813957644536
i: visions 0.002233937985881512
i: Jokshan 0.004467875971763024
i: empty 0.006701813957644536
i: tr 0.002233937985881512
i: grap 0.004467875971763024
i: beguiled 0.004467875971763024
i: sure 0.004467875971763024
i: created 0.024573317844696633
i: beautiful 0.002233937985881512
i: covering 0.004467875971763024
i: victuals 0.002233937985881512
i: whensoever 0.002233937985881512
i: much 0.017871503887052095
i: stones 0.006701813957644536
i: point 0.002233937985881512
i: Heth 0.026807255830578143
i: there 0.2591368063622554
i: cruelty 0.002233937985881512
i: departed 0.026807255830578143
i: both 0.06478420159056385
i: hate 0.006701813957644536
i: To 0.002233937985881512
i: righteousness 0.004467875971763024
i: Thou 0.026807255830578143
i: camel 0.004467875971763024
i: enter 0.002233937985881512
i: ascending 0.002233937985881512
i: Bless 0.002233937985881512
i: power 0.006701813957644536
i: images 0.006701813957644536
i: fell 0.026807255830578143
i: Arodi 0.002233937985881512
i: witness 0.013403627915289072
i: binding 0.002233937985881512
i: divide 0.01116968992940756
i: staff 0.006701813957644536
i: Ashbel 0.002233937985881512
i: escape 0.01116968992940756
i: told 0.07595389151997141
i: mock 0.004467875971763024
i: tempt 0.002233937985881512
i: Madai 0.002233937985881512
i: next 0.002233937985881512
i: servants 0.08265570547761594
i: And 2.7924224823518897
i: mayest 0.01116968992940756
i: Ithran 0.002233937985881512
i: habitations 0.004467875971763024
i: circumcise 0.002233937985881512
i: calf 0.004467875971763024
i: Art 0.002233937985881512
i: asketh 0.002233937985881512
i: Bethlehem 0.004467875971763024
i: so 0.11616477526583863
i: male 0.024573317844696633
i: ( 0.013403627915289072
i: threshingfloor 0.002233937985881512
i: Ephrath 0.004467875971763024
i: wife 0.23232955053167725
i: mischief 0.006701813957644536
i: burnt 0.017871503887052095
i: betwixt 0.02233937985881512
i: separate 0.006701813957644536
i: green 0.006701813957644536
i: sto 0.002233937985881512
i: pasture 0.002233937985881512
i: Only 0.004467875971763024
i: her 0.38647127155750155
i: plains 0.002233937985881512
i: walk 0.008935751943526048
i: grisled 0.002233937985881512
i: circumcised 0.03127513180234117
i: hang 0.002233937985881512
i: lodge 0.004467875971763024
i: offended 0.004467875971763024
i: twins 0.004467875971763024
i: plenty 0.008935751943526048
i: Whence 0.002233937985881512
i: feared 0.004467875971763024
i: rooms 0.002233937985881512
i: was 0.7081583415244392
i: fury 0.002233937985881512
i: butlership 0.002233937985881512
i: digged 0.024573317844696633
i: night 0.06031632561880082
i: pursue 0.002233937985881512
i: boldly 0.002233937985881512
i: wast 0.008935751943526048
i: way 0.07595389151997141
i: words 0.037976945759985704
i: fainted 0.004467875971763024
i: ghost 0.008935751943526048
i: Horite 0.002233937985881512
i: ashamed 0.002233937985881512
i: Binding 0.002233937985881512
i: subtilty 0.002233937985881512
i: hard 0.006701813957644536
i: wolf 0.002233937985881512
i: longedst 0.002233937985881512
i: yourselves 0.008935751943526048
i: Jezer 0.002233937985881512
i: Mahalath 0.002233937985881512
i: fema 0.002233937985881512
i: Gihon 0.002233937985881512
i: received 0.002233937985881512
i: wotteth 0.002233937985881512
i: said 1.0633544812795996
i: guiding 0.002233937985881512
i: Hai 0.004467875971763024
i: displeased 0.004467875971763024
i: With 0.008935751943526048
i: fro 0.002233937985881512
i: Blessed 0.006701813957644536
i: sware 0.02010544187293361
i: shekel 0.002233937985881512
i: season 0.002233937985881512
i: parts 0.002233937985881512
i: leaped 0.002233937985881512
i: rule 0.01116968992940756
i: few 0.01116968992940756
i: whoredom 0.002233937985881512
i: toil 0.004467875971763024
i: Shemeber 0.002233937985881512
i: shrubs 0.002233937985881512
i: pilgrimage 0.004467875971763024
i: lord 0.09159145742114198
i: indeed 0.017871503887052095
i: Mahanaim 0.002233937985881512
i: and 5.424001429720311
i: Thirty 0.002233937985881512
i: Aran 0.002233937985881512
i: established 0.004467875971763024
i: though 0.006701813957644536
i: gracious 0.002233937985881512
i: Ezer 0.006701813957644536
i: Kor 0.002233937985881512
i: sinning 0.002233937985881512
i: whereby 0.004467875971763024
i: off 0.04467875971763024
i: besides 0.004467875971763024
i: Phuvah 0.002233937985881512
i: butter 0.002233937985881512
i: which 0.4423197212045394
i: venison 0.017871503887052095
i: journeys 0.002233937985881512
i: into 0.19211866678581002
i: Noah 0.09159145742114198
i: obey 0.006701813957644536
i: Cainan 0.01116968992940756
i: destroyed 0.01116968992940756
i: we 0.20105441872933608
i: pleaseth 0.004467875971763024
i: statutes 0.002233937985881512
i: offer 0.002233937985881512
i: what 0.042444821731748725
i: ever 0.004467875971763024
i: EleloheIsrael 0.002233937985881512
i: yielded 0.002233937985881512
i: Zohar 0.006701813957644536
i: wood 0.01116968992940756
i: honourable 0.002233937985881512
i: twice 0.002233937985881512
i: moved 0.004467875971763024
i: sheweth 0.002233937985881512
i: spicery 0.002233937985881512
i: wrath 0.004467875971763024
i: defiled 0.008935751943526048
i: Carmi 0.002233937985881512
i: compassed 0.002233937985881512
i: Amraphel 0.004467875971763024
i: desolate 0.002233937985881512
i: any 0.05138057367527477
i: seem 0.002233937985881512
i: ten 0.04021088374586722
i: charged 0.008935751943526048
i: Hul 0.002233937985881512
i: Casluhim 0.002233937985881512
i: best 0.006701813957644536
i: call 0.017871503887052095
i: who 0.04021088374586722
i: appe 0.002233937985881512
i: Arioch 0.004467875971763024
i: ram 0.006701813957644536
i: marriages 0.002233937985881512
i: conceive 0.006701813957644536
i: Benjamin 0.037976945759985704
i: dress 0.004467875971763024
i: coat 0.017871503887052095
i: Belah 0.002233937985881512
i: Huppim 0.002233937985881512
i: measures 0.002233937985881512
i: Thus 0.026807255830578143
i: Kirjatharba 0.002233937985881512
i: Bozrah 0.002233937985881512
i: Jubal 0.002233937985881512
i: us 0.2077562326869806
i: colt 0.002233937985881512
i: abated 0.006701813957644536
i: consent 0.006701813957644536
i: verified 0.002233937985881512
i: breasts 0.002233937985881512
i: ; 1.3515324814583147
i: twel 0.002233937985881512
i: husba 0.002233937985881512
i: guard 0.013403627915289072
i: O 0.02010544187293361
i: speaketh 0.002233937985881512
i: street 0.002233937985881512
i: archers 0.002233937985881512
i: breaking 0.002233937985881512
i: language 0.008935751943526048
i: master 0.06478420159056385
i: speedily 0.002233937985881512
i: fall 0.008935751943526048
i: ma 0.002233937985881512
i: understand 0.004467875971763024
i: lift 0.017871503887052095
i: preserve 0.008935751943526048
i: death 0.015637565901170585
i: at 0.11839871325172013
i: priest 0.008935751943526048
i: name 0.2233937985881512
i: Iscah 0.002233937985881512
i: tillest 0.002233937985881512
i: joined 0.006701813957644536
i: archer 0.002233937985881512
i: morever 0.002233937985881512
i: shamed 0.002233937985881512
i: altar 0.029041193816459657
i: half 0.002233937985881512
i: lieth 0.004467875971763024
i: Gomer 0.004467875971763024
i: corrupted 0.002233937985881512
i: Peace 0.002233937985881512
i: lamp 0.002233937985881512
i: Ard 0.002233937985881512
i: lo 0.024573317844696633
i: Give 0.017871503887052095
i: forth 0.09605933339290501
i: hid 0.008935751943526048
i: did 0.1295684031811277
i: cities 0.017871503887052095
i: Jebusites 0.002233937985881512
i: Ziphion 0.002233937985881512
i: seemed 0.004467875971763024
i: became 0.026807255830578143
i: my 0.7260298454114914
i: word 0.015637565901170585
i: Mamre 0.02010544187293361
i: comfort 0.008935751943526048
i: falsely 0.002233937985881512
i: wagons 0.008935751943526048
i: then 0.07371995353408989
i: discerned 0.002233937985881512
i: lack 0.004467875971763024
i: worse 0.002233937985881512
i: cast 0.015637565901170585
i: better 0.002233937985881512
i: alone 0.006701813957644536
i: Naphtali 0.008935751943526048
i: chamber 0.002233937985881512
i: bands 0.004467875971763024
i: hadst 0.004467875971763024
i: sow 0.002233937985881512
i: lamb 0.004467875971763024
i: abomination 0.004467875971763024
i: passed 0.017871503887052095
i: handmaidens 0.002233937985881512
i: rose 0.04691269770351175
i: whatsoever 0.01116968992940756
i: wickedly 0.002233937985881512
i: oversig 0.002233937985881512
i: Day 0.002233937985881512
i: generations 0.03574300777410419
i: cup 0.02233937985881512
i: whales 0.002233937985881512
i: Jordan 0.01116968992940756
i: Assyr 0.002233937985881512
i: alo 0.002233937985881512
i: cried 0.015637565901170585
i: cave 0.024573317844696633
i: daughters 0.11839871325172013
i: lie 0.013403627915289072
i: Perizzite 0.002233937985881512
i: officer 0.004467875971763024
i: mourning 0.013403627915289072
i: deed 0.002233937985881512
i: conception 0.002233937985881512
i: aw 0.004467875971763024
i: Admah 0.006701813957644536
i: were 0.3641318916986864
i: Escape 0.002233937985881512
i: Hagar 0.026807255830578143
i: fail 0.002233937985881512
i: rul 0.002233937985881512
i: placed 0.004467875971763024
i: Seir 0.017871503887052095
i: remaineth 0.002233937985881512
i: throughout 0.006701813957644536
i: sle 0.002233937985881512
i: fai 0.004467875971763024
i: shoulder 0.01116968992940756
i: wash 0.006701813957644536
i: Kenaz 0.006701813957644536
i: double 0.004467875971763024
i: ended 0.006701813957644536
i: midwife 0.004467875971763024
i: every 0.19658654275757306
i: ki 0.01116968992940756
i: neither 0.026807255830578143
i: slime 0.002233937985881512
i: Abidah 0.002233937985881512
i: fearest 0.002233937985881512
i: peace 0.015637565901170585
i: fourscore 0.004467875971763024
i: kindled 0.004467875971763024
i: Salah 0.013403627915289072
i: joint 0.002233937985881512
i: scatter 0.004467875971763024
i: wouldest 0.006701813957644536
i: pris 0.002233937985881512
i: bear 0.029041193816459657
i: mast 0.002233937985881512
i: colts 0.002233937985881512
i: sleep 0.01116968992940756
i: absent 0.002233937985881512
i: goest 0.01116968992940756
i: seen 0.024573317844696633
i: households 0.006701813957644536
i: foreskin 0.01116968992940756
i: bound 0.017871503887052095
i: bottle 0.006701813957644536
i: menservants 0.01116968992940756
i: Both 0.002233937985881512
i: such 0.024573317844696633
i: pillows 0.004467875971763024
i: stayed 0.006701813957644536
i: offerings 0.002233937985881512
i: possess 0.004467875971763024
i: tops 0.002233937985881512
i: Gaza 0.002233937985881512
i: baskets 0.004467875971763024
i: met 0.004467875971763024
i: multiplying 0.002233937985881512
i: Make 0.004467875971763024
i: myrrh 0.004467875971763024
i: remember 0.008935751943526048
i: Ashteroth 0.002233937985881512
i: Guni 0.002233937985881512
i: whereof 0.002233937985881512
i: called 0.21892592261638816
i: damsels 0.002233937985881512
i: blame 0.004467875971763024
i: rich 0.002233937985881512
i: those 0.017871503887052095
i: thirteenth 0.002233937985881512
i: Sod 0.004467875971763024
i: hindermost 0.002233937985881512
i: Malchiel 0.002233937985881512
i: tru 0.002233937985881512
i: fath 0.006701813957644536
i: dwell 0.049146635689393266
i: Fear 0.006701813957644536
i: posterity 0.002233937985881512
i: receive 0.006701813957644536
i: risen 0.002233937985881512
i: heaven 0.06255026360468234
i: greater 0.01116968992940756
i: herself 0.008935751943526048
i: rams 0.008935751943526048
i: Merari 0.002233937985881512
i: whomsoever 0.004467875971763024
i: vengeance 0.002233937985881512
i: knew 0.037976945759985704
i: being 0.017871503887052095
i: Hadoram 0.002233937985881512
i: glory 0.004467875971763024
i: Hazarmaveth 0.002233937985881512
i: Moreh 0.002233937985881512
i: refrain 0.002233937985881512
i: nurse 0.004467875971763024
i: wilt 0.029041193816459657
i: praise 0.004467875971763024
i: Korah 0.006701813957644536
i: pieces 0.015637565901170585
i: Two 0.004467875971763024
i: Mam 0.002233937985881512
i: budded 0.002233937985881512
i: savour 0.002233937985881512
i: Bethel 0.026807255830578143
i: foremost 0.004467875971763024
i: bdellium 0.002233937985881512
i: wrestled 0.006701813957644536
i: nations 0.04021088374586722
i: father 0.4423197212045394
i: him 0.8645340005361452
i: ran 0.02010544187293361
i: Behold 0.11839871325172013
i: Benam 0.002233937985881512
i: Shalt 0.002233937985881512
i: deferred 0.002233937985881512
i: Gether 0.002233937985881512
i: remembered 0.008935751943526048
i: according 0.07148601554820838
i: appear 0.002233937985881512
i: ford 0.002233937985881512
i: harp 0.004467875971763024
i: twentieth 0.002233937985881512
i: shortly 0.002233937985881512
i: turn 0.008935751943526048
i: leap 0.002233937985881512
i: governor 0.004467875971763024
i: castles 0.002233937985881512
i: rouse 0.002233937985881512
i: divided 0.02233937985881512
i: eighty 0.006701813957644536
i: tarry 0.006701813957644536
i: third 0.02233937985881512
i: graciously 0.004467875971763024
i: certain 0.008935751943526048
i: famished 0.002233937985881512
i: Issachar 0.008935751943526048
i: confound 0.004467875971763024
i: Ephron 0.026807255830578143
i: judge 0.01116968992940756
i: embraced 0.006701813957644536
i: clean 0.015637565901170585
i: heed 0.004467875971763024
i: honey 0.002233937985881512
i: Din 0.002233937985881512
i: prince 0.006701813957644536
i: Remain 0.002233937985881512
i: times 0.008935751943526048
i: Kenites 0.002233937985881512
i: deeds 0.002233937985881512
i: slew 0.015637565901170585
i: mightier 0.002233937985881512
i: Lotan 0.008935751943526048
i: plenteousness 0.002233937985881512
i: red 0.006701813957644536
i: sac 0.002233937985881512
i: Even 0.004467875971763024
i: swear 0.013403627915289072
i: folly 0.002233937985881512
i: how 0.017871503887052095
i: evil 0.03574300777410419
i: handmaid 0.015637565901170585
i: money 0.07148601554820838
i: Hushim 0.002233937985881512
i: wor 0.002233937985881512
i: top 0.006701813957644536
i: die 0.0558484496470378
i: Adam 0.04021088374586722
i: herdmen 0.013403627915289072
i: obeyed 0.006701813957644536
i: kindly 0.008935751943526048
i: fourteen 0.004467875971763024
i: Achbor 0.004467875971763024
i: Pass 0.002233937985881512
i: toucheth 0.002233937985881512
i: caused 0.008935751943526048
i: turned 0.013403627915289072
i: horror 0.002233937985881512
i: gard 0.002233937985881512
i: prevailed 0.015637565901170585
i: sporting 0.002233937985881512
i: wondering 0.002233937985881512
i: weary 0.002233937985881512
i: shore 0.002233937985881512
i: Manasseh 0.02233937985881512
i: required 0.002233937985881512
i: Jerah 0.002233937985881512
i: countries 0.008935751943526048
i: gre 0.006701813957644536
i: fathe 0.002233937985881512
i: boug 0.002233937985881512
i: corrupt 0.004467875971763024
i: mourn 0.002233937985881512
i: earrings 0.002233937985881512
i: moving 0.004467875971763024
i: Caphtorim 0.002233937985881512
i: interpretation 0.01116968992940756
i: giants 0.002233937985881512
i: dominion 0.008935751943526048
i: Chedorlaomer 0.01116968992940756
i: The 0.1116968992940756
i: hundredth 0.004467875971763024
i: Shed 0.002233937985881512
i: seventeenth 0.004467875971763024
i: herd 0.002233937985881512
i: meet 0.026807255830578143
i: husband 0.015637565901170585
i: baker 0.01116968992940756
i: plenteous 0.004467875971763024
i: steward 0.008935751943526048
i: Adbeel 0.002233937985881512
i: wall 0.002233937985881512
i: doe 0.002233937985881512
i: gathering 0.004467875971763024
i: grow 0.004467875971763024
i: barren 0.004467875971763024
i: return 0.013403627915289072
i: seest 0.006701813957644536
i: betimes 0.002233937985881512
i: softly 0.002233937985881512
i: same 0.049146635689393266
i: y 0.002233937985881512
i: freely 0.002233937985881512
i: fountains 0.004467875971763024
i: Onam 0.002233937985881512
i: Ishuah 0.002233937985881512
i: three 0.06701813957644535
i: turtledove 0.002233937985881512
i: talking 0.002233937985881512
i: morrow 0.002233937985881512
i: Dishon 0.008935751943526048
i: broken 0.006701813957644536
i: Ahuzzath 0.002233937985881512
i: Ethiopia 0.002233937985881512
i: thistles 0.002233937985881512
i: riches 0.004467875971763024
i: Egyptians 0.026807255830578143
i: small 0.004467875971763024
i: spake 0.08712358144937897
i: Hezron 0.004467875971763024
i: kill 0.01116968992940756
i: full 0.017871503887052095
i: There 0.01116968992940756
i: Galeed 0.004467875971763024
i: awoke 0.008935751943526048
i: Cana 0.006701813957644536
i: nakedness 0.01116968992940756
i: dignity 0.002233937985881512
i: repented 0.002233937985881512
i: acknowledged 0.002233937985881512
i: wat 0.004467875971763024
i: border 0.004467875971763024
i: folk 0.002233937985881512
i: by 0.17871503887052095
i: widowhood 0.002233937985881512
i: eyed 0.002233937985881512
i: peradventure 0.015637565901170585
i: Wherefore 0.026807255830578143
i: organ 0.002233937985881512
i: saidst 0.013403627915289072
i: hasted 0.006701813957644536
i: suck 0.002233937985881512
i: fowl 0.03574300777410419
i: eight 0.02233937985881512
i: eat 0.10499508533643107
i: Mibzar 0.002233937985881512
i: e 0.004467875971763024
i: refused 0.006701813957644536
i: Shur 0.006701813957644536
i: violence 0.004467875971763024
i: thirteen 0.002233937985881512
i: smooth 0.004467875971763024
i: cubit 0.002233937985881512
def percentage_each(text,total):
    for i in set(text):
        print(i,100 * text.count(i)/total)

        
percentage_each(text3,len(text3))
heir 0.008935751943526048
book 0.002233937985881512
generatio 0.004467875971763024
led 0.004467875971763024
strangers 0.004467875971763024
washed 0.006701813957644536
Have 0.004467875971763024
maiden 0.002233937985881512
sell 0.002233937985881512
Saul 0.004467875971763024
shouldest 0.008935751943526048
Mizraim 0.004467875971763024
Gomorrah 0.02010544187293361
dark 0.002233937985881512
soul 0.029041193816459657
Hittites 0.002233937985881512
couching 0.002233937985881512
perform 0.002233937985881512
rained 0.002233937985881512
if 0.07818782950585292
strove 0.006701813957644536
presence 0.02233937985881512
Arise 0.01116968992940756
shut 0.006701813957644536
dearth 0.004467875971763024
weighed 0.002233937985881512
dwelling 0.006701813957644536
state 0.002233937985881512
fame 0.002233937985881512
Eldaah 0.002233937985881512
Eber 0.015637565901170585
Uz 0.004467875971763024
mocking 0.002233937985881512
ships 0.002233937985881512
quickly 0.004467875971763024
overtook 0.006701813957644536
ha 0.015637565901170585
changed 0.006701813957644536
harm 0.002233937985881512
wroth 0.013403627915289072
Phara 0.008935751943526048
make 0.10276114735054954
awaked 0.002233937985881512
prison 0.02010544187293361
Ur 0.006701813957644536
stand 0.004467875971763024
moreover 0.004467875971763024
Jetur 0.002233937985881512
he 1.4475918148512197
whosoever 0.002233937985881512
man 0.2546689303904924
other 0.03574300777410419
shoulders 0.002233937985881512
Dothan 0.004467875971763024
Yet 0.006701813957644536
hired 0.002233937985881512
devoured 0.01116968992940756
Abr 0.002233937985881512
loose 0.002233937985881512
shew 0.01116968992940756
Edar 0.002233937985881512
,) 0.002233937985881512
Thahash 0.002233937985881512
ass 0.015637565901170585
nought 0.002233937985881512
clear 0.008935751943526048
Enoch 0.017871503887052095
exceedingly 0.017871503887052095
content 0.002233937985881512
Methuselah 0.01116968992940756
Beor 0.002233937985881512
uppermost 0.002233937985881512
sat 0.02010544187293361
Shaul 0.002233937985881512
hith 0.002233937985881512
sa 0.006701813957644536
Jebusite 0.002233937985881512
sweat 0.002233937985881512
Peleg 0.01116968992940756
you 0.18318291484228397
northward 0.002233937985881512
me 0.6299705120185863
understood 0.002233937985881512
flood 0.024573317844696633
Drink 0.006701813957644536
Jac 0.004467875971763024
souls 0.017871503887052095
Nimrod 0.004467875971763024
able 0.006701813957644536
appeared 0.02233937985881512
lay 0.026807255830578143
Ammon 0.002233937985881512
fine 0.004467875971763024
hearth 0.002233937985881512
beheld 0.01116968992940756
instead 0.006701813957644536
withheld 0.008935751943526048
began 0.013403627915289072
assigned 0.002233937985881512
mercies 0.002233937985881512
Kadesh 0.006701813957644536
poplar 0.002233937985881512
Abimelech 0.053614511661156286
vow 0.004467875971763024
follow 0.008935751943526048
ought 0.008935751943526048
present 0.02010544187293361
another 0.03350906978822268
ri 0.002233937985881512
Lehabim 0.002233937985881512
Padanaram 0.02233937985881512
m 0.01116968992940756
proved 0.004467875971763024
Erech 0.002233937985881512
dost 0.004467875971763024
wounding 0.002233937985881512
his 1.4542936288088644
dim 0.004467875971763024
maid 0.026807255830578143
entered 0.01116968992940756
guiltiness 0.002233937985881512
almon 0.002233937985881512
basket 0.004467875971763024
seed 0.1295684031811277
be 0.567420248413904
Anah 0.02010544187293361
draw 0.013403627915289072
camest 0.006701813957644536
fish 0.004467875971763024
arms 0.002233937985881512
distressed 0.002233937985881512
rebelled 0.002233937985881512
subtil 0.002233937985881512
feel 0.004467875971763024
asses 0.03127513180234117
Shelah 0.008935751943526048
sceptre 0.002233937985881512
trade 0.008935751943526048
behind 0.013403627915289072
Cursed 0.004467875971763024
arose 0.017871503887052095
clothed 0.002233937985881512
upon 0.31051738003753016
force 0.002233937985881512
blood 0.024573317844696633
say 0.05138057367527477
beari 0.002233937985881512
pledge 0.006701813957644536
commanding 0.002233937985881512
dreams 0.008935751943526048
vine 0.008935751943526048
Muppim 0.002233937985881512
possessi 0.002233937985881512
pillar 0.026807255830578143
bosom 0.002233937985881512
yonder 0.002233937985881512
ewes 0.004467875971763024
jud 0.002233937985881512
Peradventure 0.02010544187293361
large 0.002233937985881512
took 0.18094897685640246
tent 0.049146635689393266
Sojourn 0.002233937985881512
magnified 0.002233937985881512
continued 0.002233937985881512
hanged 0.004467875971763024
healed 0.002233937985881512
stood 0.037976945759985704
gold 0.017871503887052095
Abide 0.002233937985881512
Reu 0.008935751943526048
Tubalcain 0.004467875971763024
abide 0.008935751943526048
lad 0.04021088374586722
reproved 0.004467875971763024
sod 0.002233937985881512
clusters 0.002233937985881512
angel 0.02233937985881512
quite 0.002233937985881512
deceitfully 0.002233937985881512
thee 0.5741220623715486
punishment 0.002233937985881512
your 0.18318291484228397
sojourned 0.01116968992940756
precious 0.002233937985881512
planted 0.006701813957644536
Phut 0.002233937985881512
seedtime 0.002233937985881512
smote 0.01116968992940756
out 0.23679742650344027
angels 0.008935751943526048
It 0.02010544187293361
offered 0.008935751943526048
after 0.23903136448932177
Happy 0.002233937985881512
tim 0.002233937985881512
fig 0.002233937985881512
afar 0.004467875971763024
asswaged 0.002233937985881512
enlarge 0.002233937985881512
ruler 0.006701813957644536
royal 0.002233937985881512
sand 0.006701813957644536
Tebah 0.002233937985881512
Ask 0.002233937985881512
adder 0.002233937985881512
space 0.004467875971763024
numbering 0.002233937985881512
Hiddekel 0.002233937985881512
ill 0.015637565901170585
path 0.002233937985881512
wherefore 0.015637565901170585
report 0.002233937985881512
drink 0.04691269770351175
prepared 0.004467875971763024
lodged 0.004467875971763024
crown 0.002233937985881512
Chaldees 0.006701813957644536
Hebron 0.01116968992940756
Abelmizraim 0.002233937985881512
journey 0.013403627915289072
comforted 0.008935751943526048
troubled 0.006701813957644536
Cheran 0.002233937985881512
yearn 0.002233937985881512
My 0.04021088374586722
wives 0.049146635689393266
windows 0.004467875971763024
doest 0.004467875971763024
pass 0.18094897685640246
signs 0.002233937985881512
sou 0.004467875971763024
spices 0.002233937985881512
wrapped 0.002233937985881512
lands 0.01116968992940756
Beerlahairoi 0.002233937985881512
hear 0.015637565901170585
ste 0.004467875971763024
escaped 0.002233937985881512
armed 0.002233937985881512
chief 0.03127513180234117
knead 0.002233937985881512
seven 0.12063265123760164
Husham 0.004467875971763024
Eshcol 0.004467875971763024
yoke 0.002233937985881512
fetcht 0.002233937985881512
anger 0.01116968992940756
Elam 0.006701813957644536
cakes 0.002233937985881512
Gather 0.006701813957644536
Egypt 0.16531141095523189
living 0.03574300777410419
upward 0.002233937985881512
interpretations 0.002233937985881512
lights 0.006701813957644536
drinking 0.004467875971763024
Sell 0.002233937985881512
messenger 0.002233937985881512
chode 0.002233937985881512
cometh 0.013403627915289072
moon 0.002233937985881512
deliver 0.008935751943526048
prayed 0.002233937985881512
within 0.02010544187293361
onyx 0.002233937985881512
communed 0.01116968992940756
justice 0.002233937985881512
Jabal 0.002233937985881512
Mash 0.002233937985881512
sheepshearers 0.002233937985881512
natio 0.002233937985881512
alive 0.026807255830578143
Zarah 0.002233937985881512
faileth 0.002233937985881512
wot 0.004467875971763024
seasons 0.002233937985881512
coats 0.002233937985881512
See 0.01116968992940756
Milcah 0.015637565901170585
gate 0.02010544187293361
?) 0.002233937985881512
talked 0.01116968992940756
proceedeth 0.002233937985881512
wickedness 0.004467875971763024
oath 0.01116968992940756
How 0.008935751943526048
ours 0.002233937985881512
Jaalam 0.006701813957644536
burning 0.002233937985881512
intreat 0.002233937985881512
interpreted 0.006701813957644536
eighteen 0.002233937985881512
Omar 0.004467875971763024
loud 0.002233937985881512
Ezbon 0.002233937985881512
sepulchres 0.002233937985881512
bre 0.006701813957644536
fifty 0.02010544187293361
kingdom 0.004467875971763024
heels 0.002233937985881512
rolled 0.004467875971763024
roughly 0.004467875971763024
done 0.08042176749173444
life 0.06925207756232687
Here 0.013403627915289072
couch 0.002233937985881512
bones 0.004467875971763024
heel 0.004467875971763024
da 0.004467875971763024
wombs 0.002233937985881512
togeth 0.004467875971763024
excel 0.002233937985881512
sheaves 0.004467875971763024
become 0.02010544187293361
bowed 0.03574300777410419
Adah 0.017871503887052095
overcome 0.004467875971763024
scarce 0.002233937985881512
lives 0.006701813957644536
watch 0.002233937985881512
neck 0.017871503887052095
Fifteen 0.002233937985881512
Lie 0.004467875971763024
driven 0.002233937985881512
Philistines 0.015637565901170585
delivered 0.01116968992940756
Siddim 0.006701813957644536
frost 0.002233937985881512
stooped 0.002233937985881512
merchantmen 0.002233937985881512
had 0.31051738003753016
Kemuel 0.002233937985881512
Mesopotamia 0.002233937985881512
himself 0.049146635689393266
great 0.07148601554820838
breach 0.002233937985881512
lower 0.002233937985881512
goodly 0.006701813957644536
Magdiel 0.002233937985881512
lesser 0.002233937985881512
dead 0.026807255830578143
parted 0.002233937985881512
? 0.33062282191046377
sh 0.002233937985881512
En 0.002233937985881512
month 0.026807255830578143
birthday 0.002233937985881512
Pathrusim 0.002233937985881512
give 0.1318023411670092
Heber 0.002233937985881512
never 0.004467875971763024
only 0.029041193816459657
anointedst 0.002233937985881512
an 0.1697792869269949
Abrah 0.01116968992940756
wind 0.008935751943526048
troop 0.004467875971763024
saw 0.1273344651952462
crieth 0.002233937985881512
Return 0.006701813957644536
Which 0.002233937985881512
families 0.02010544187293361
Riphath 0.002233937985881512
law 0.02233937985881512
firmament 0.017871503887052095
people 0.07818782950585292
harvest 0.006701813957644536
droves 0.002233937985881512
imagined 0.002233937985881512
Buz 0.002233937985881512
Male 0.002233937985881512
Cush 0.006701813957644536
ey 0.004467875971763024
Hazo 0.002233937985881512
findeth 0.002233937985881512
Jehovahjireh 0.002233937985881512
pulled 0.004467875971763024
Let 0.06478420159056385
sole 0.002233937985881512
mocked 0.002233937985881512
caught 0.004467875971763024
over 0.10946296130819408
grew 0.013403627915289072
bearing 0.008935751943526048
standest 0.002233937985881512
knowing 0.002233937985881512
goats 0.02010544187293361
dew 0.004467875971763024
names 0.02233937985881512
Ellasar 0.004467875971763024
image 0.01116968992940756
gopher 0.002233937985881512
wandered 0.002233937985881512
mistress 0.006701813957644536
following 0.002233937985881512
feeding 0.002233937985881512
gods 0.01116968992940756
sworn 0.002233937985881512
shoelatchet 0.002233937985881512
spirit 0.006701813957644536
ready 0.008935751943526048
Naaman 0.002233937985881512
discern 0.002233937985881512
offeri 0.004467875971763024
except 0.015637565901170585
magicians 0.004467875971763024
dread 0.002233937985881512
Sichem 0.002233937985881512
barr 0.002233937985881512
cause 0.002233937985881512
destroy 0.03350906978822268
five 0.049146635689393266
sack 0.02010544187293361
forty 0.03350906978822268
knife 0.004467875971763024
yet 0.07818782950585292
see 0.0558484496470378
Alvan 0.002233937985881512
Now 0.06925207756232687
knowest 0.006701813957644536
deliverance 0.002233937985881512
raiment 0.015637565901170585
battle 0.002233937985881512
Hadar 0.004467875971763024
prosperous 0.004467875971763024
Hadad 0.004467875971763024
raise 0.002233937985881512
dried 0.006701813957644536
innocency 0.002233937985881512
fruits 0.002233937985881512
kind 0.029041193816459657
wrestlings 0.002233937985881512
hou 0.008935751943526048
ones 0.015637565901170585
Whose 0.006701813957644536
Rachel 0.09829327137878653
vision 0.002233937985881512
Javan 0.004467875971763024
I 1.0812259851666517
because 0.12063265123760164
fair 0.01116968992940756
ring 0.002233937985881512
direct 0.002233937985881512
, 8.223125726029846
Abram 0.1295684031811277
Serug 0.008935751943526048
Pharez 0.006701813957644536
supplanted 0.002233937985881512
han 0.002233937985881512
distress 0.004467875971763024
Jachin 0.002233937985881512
now 0.12510052720936468
Togarmah 0.002233937985881512
brass 0.002233937985881512
leanfleshed 0.006701813957644536
Unstable 0.002233937985881512
find 0.026807255830578143
giving 0.002233937985881512
Lasha 0.002233937985881512
iniquity 0.006701813957644536
prosper 0.008935751943526048
even 0.06255026360468234
seek 0.004467875971763024
confederate 0.002233937985881512
dea 0.002233937985881512
friends 0.002233937985881512
lien 0.002233937985881512
Salem 0.002233937985881512
speech 0.004467875971763024
waxen 0.002233937985881512
winter 0.002233937985881512
Of 0.013403627915289072
regard 0.002233937985881512
discreet 0.004467875971763024
pray 0.10722902332231257
slept 0.002233937985881512
save 0.008935751943526048
persons 0.004467875971763024
Ebal 0.002233937985881512
window 0.006701813957644536
hunting 0.002233937985881512
tell 0.037976945759985704
left 0.05808238763291931
judgment 0.002233937985881512
rid 0.002233937985881512
bare 0.12510052720936468
nativity 0.002233937985881512
ground 0.053614511661156286
look 0.02010544187293361
open 0.004467875971763024
grove 0.002233937985881512
protest 0.002233937985881512
weapons 0.002233937985881512
Shillem 0.002233937985881512
war 0.002233937985881512
sister 0.04691269770351175
twenty 0.024573317844696633
bought 0.024573317844696633
rulers 0.002233937985881512
Who 0.013403627915289072
d 0.01116968992940756
run 0.002233937985881512
laughed 0.006701813957644536
strife 0.004467875971763024
Israel 0.08935751943526048
belly 0.002233937985881512
too 0.002233937985881512
withered 0.002233937985881512
fir 0.002233937985881512
mouth 0.03127513180234117
abroad 0.015637565901170585
poured 0.006701813957644536
bou 0.002233937985881512
troughs 0.002233937985881512
Ishbak 0.002233937985881512
Perizzites 0.002233937985881512
let 0.14297203109641676
longeth 0.002233937985881512
pleasant 0.006701813957644536
raven 0.002233937985881512
till 0.015637565901170585
clothes 0.008935751943526048
finding 0.002233937985881512
begotten 0.002233937985881512
gro 0.002233937985881512
damsel 0.02010544187293361
Phallu 0.002233937985881512
Can 0.002233937985881512
flock 0.03127513180234117
Beersheba 0.024573317844696633
tabret 0.002233937985881512
knoweth 0.002233937985881512
riv 0.002233937985881512
ride 0.002233937985881512
gather 0.006701813957644536
smoking 0.002233937985881512
break 0.004467875971763024
doeth 0.002233937985881512
judged 0.002233937985881512
seventy 0.01116968992940756
marry 0.002233937985881512
mirth 0.002233937985881512
Canaan 0.09605933339290501
mules 0.002233937985881512
came 0.39540702350102763
espied 0.002233937985881512
king 0.07148601554820838
Eri 0.002233937985881512
Samlah 0.004467875971763024
trembled 0.002233937985881512
Reumah 0.002233937985881512
inherit 0.006701813957644536
friend 0.004467875971763024
Asenath 0.006701813957644536
teeth 0.002233937985881512
Dan 0.013403627915289072
Cause 0.002233937985881512
fourth 0.006701813957644536
observed 0.002233937985881512
meeteth 0.002233937985881512
gone 0.013403627915289072
multiplied 0.002233937985881512
Abel 0.017871503887052095
walked 0.006701813957644536
seventeen 0.004467875971763024
far 0.006701813957644536
: 0.5316772406397998
custom 0.002233937985881512
Es 0.004467875971763024
floor 0.002233937985881512
Sephar 0.002233937985881512
they 0.5562505584844964
As 0.006701813957644536
unawares 0.004467875971763024
nourished 0.002233937985881512
tongues 0.004467875971763024
together 0.03574300777410419
Leah 0.07371995353408989
dreamer 0.002233937985881512
increase 0.002233937985881512
Should 0.002233937985881512
handfuls 0.002233937985881512
kept 0.008935751943526048
Come 0.017871503887052095
rightly 0.002233937985881512
answer 0.006701813957644536
Job 0.002233937985881512
Zeboim 0.002233937985881512
overdrive 0.002233937985881512
defiledst 0.002233937985881512
been 0.024573317844696633
stead 0.015637565901170585
womenservan 0.002233937985881512
Feed 0.002233937985881512
breaketh 0.002233937985881512
embalmed 0.004467875971763024
also 0.18094897685640246
Pison 0.002233937985881512
bracelets 0.01116968992940756
Upon 0.002233937985881512
inn 0.004467875971763024
giveth 0.002233937985881512
beneath 0.002233937985881512
Gera 0.002233937985881512
Seth 0.01116968992940756
hated 0.015637565901170585
embalm 0.004467875971763024
hither 0.008935751943526048
kindness 0.01116968992940756
while 0.01116968992940756
commanded 0.04021088374586722
dry 0.008935751943526048
Whereas 0.002233937985881512
linen 0.002233937985881512
tenth 0.006701813957644536
womb 0.013403627915289072
Bashemath 0.013403627915289072
refrained 0.002233937985881512
bakers 0.002233937985881512
springing 0.002233937985881512
thus 0.015637565901170585
Bera 0.002233937985881512
Amalekites 0.002233937985881512
pow 0.002233937985881512
fugitive 0.004467875971763024
require 0.01116968992940756
pit 0.015637565901170585
feet 0.015637565901170585
Isra 0.004467875971763024
boys 0.002233937985881512
thin 0.01116968992940756
Wilt 0.006701813957644536
sort 0.006701813957644536
afflict 0.004467875971763024
born 0.07371995353408989
firmame 0.002233937985881512
Neither 0.002233937985881512
Zillah 0.006701813957644536
Sarai 0.037976945759985704
speed 0.002233937985881512
flee 0.008935751943526048
aileth 0.002233937985881512
wandering 0.002233937985881512
bury 0.03350906978822268
dowry 0.004467875971763024
shield 0.002233937985881512
Jobab 0.006701813957644536
perceived 0.004467875971763024
Becher 0.002233937985881512
Amorites 0.006701813957644536
saving 0.002233937985881512
Pharaoh 0.20105441872933608
increased 0.008935751943526048
thoughts 0.002233937985881512
nourish 0.004467875971763024
Shalem 0.002233937985881512
bowels 0.006701813957644536
current 0.002233937985881512
parcel 0.002233937985881512
Alvah 0.002233937985881512
Thorns 0.002233937985881512
itself 0.004467875971763024
Terah 0.02010544187293361
Esek 0.002233937985881512
commandments 0.002233937985881512
host 0.008935751943526048
sowed 0.002233937985881512
mead 0.002233937985881512
desire 0.004467875971763024
Oh 0.01116968992940756
Tell 0.002233937985881512
excellency 0.004467875971763024
Se 0.008935751943526048
children 0.13850415512465375
young 0.026807255830578143
Eliphaz 0.015637565901170585
come 0.1496738450540613
thence 0.04021088374586722
slay 0.024573317844696633
men 0.14520596908229827
cloud 0.006701813957644536
Deborah 0.002233937985881512
endued 0.002233937985881512
last 0.004467875971763024
yielding 0.01116968992940756
sanctified 0.002233937985881512
floc 0.002233937985881512
Heaven 0.002233937985881512
signet 0.004467875971763024
bless 0.05138057367527477
spi 0.002233937985881512
Be 0.006701813957644536
things 0.03574300777410419
bade 0.002233937985881512
female 0.015637565901170585
perish 0.002233937985881512
Euphrat 0.002233937985881512
Zilpah 0.015637565901170585
interpreter 0.004467875971763024
He 0.015637565901170585
spies 0.013403627915289072
captive 0.004467875971763024
do 0.10052720936466804
dealt 0.006701813957644536
Moreover 0.004467875971763024
Jemuel 0.002233937985881512
sinners 0.002233937985881512
openly 0.002233937985881512
Pau 0.002233937985881512
Said 0.002233937985881512
thousands 0.002233937985881512
pottage 0.006701813957644536
Spake 0.002233937985881512
wo 0.004467875971763024
brethren 0.17871503887052095
clave 0.004467875971763024
suffered 0.006701813957644536
spare 0.004467875971763024
sheaf 0.004467875971763024
renown 0.002233937985881512
respect 0.004467875971763024
Twelve 0.002233937985881512
sight 0.037976945759985704
gat 0.002233937985881512
dwelt 0.05808238763291931
bowing 0.002233937985881512
Hinder 0.002233937985881512
Shinab 0.002233937985881512
purposing 0.002233937985881512
fle 0.004467875971763024
have 0.29487981413635955
Tidal 0.004467875971763024
artificer 0.002233937985881512
head 0.03574300777410419
ninety 0.013403627915289072
commune 0.002233937985881512
husbandman 0.002233937985881512
Haste 0.004467875971763024
journeyed 0.017871503887052095
beast 0.04467875971763024
Rehoboth 0.006701813957644536
Jamin 0.002233937985881512
four 0.026807255830578143
dressed 0.002233937985881512
Mizpah 0.002233937985881512
urged 0.002233937985881512
hand 0.18318291484228397
Japhe 0.004467875971763024
pitch 0.004467875971763024
wherewith 0.002233937985881512
business 0.002233937985881512
laded 0.004467875971763024
Save 0.002233937985881512
thousand 0.002233937985881512
fruitful 0.03127513180234117
lead 0.002233937985881512
held 0.006701813957644536
Abimael 0.002233937985881512
secret 0.002233937985881512
perfect 0.004467875971763024
or 0.049146635689393266
Ishmael 0.037976945759985704
younge 0.002233937985881512
Hast 0.008935751943526048
about 0.024573317844696633
smoke 0.004467875971763024
Discern 0.002233937985881512
think 0.002233937985881512
back 0.01116968992940756
summer 0.002233937985881512
Midian 0.006701813957644536
pluckt 0.002233937985881512
hastily 0.002233937985881512
nineteen 0.002233937985881512
Zoar 0.013403627915289072
as 0.25020105441872936
comi 0.002233937985881512
laugh 0.008935751943526048
possessions 0.004467875971763024
poverty 0.002233937985881512
findest 0.002233937985881512
daughter 0.10276114735054954
captives 0.002233937985881512
stuff 0.006701813957644536
booths 0.002233937985881512
kinds 0.002233937985881512
birds 0.006701813957644536
merchant 0.002233937985881512
Jahzeel 0.002233937985881512
lads 0.002233937985881512
chose 0.004467875971763024
speaking 0.004467875971763024
hil 0.002233937985881512
hurt 0.008935751943526048
found 0.08265570547761594
gathered 0.03350906978822268
voi 0.002233937985881512
Tiras 0.002233937985881512
reign 0.002233937985881512
fallen 0.002233937985881512
treasure 0.002233937985881512
wittingly 0.002233937985881512
enquire 0.004467875971763024
loins 0.006701813957644536
sevenfold 0.006701813957644536
mi 0.002233937985881512
fifteen 0.004467875971763024
rain 0.008935751943526048
lion 0.006701813957644536
milk 0.004467875971763024
coming 0.002233937985881512
exchange 0.002233937985881512
spent 0.004467875971763024
divine 0.002233937985881512
Rosh 0.002233937985881512
until 0.037976945759985704
vessels 0.002233937985881512
failed 0.004467875971763024
set 0.06925207756232687
forbid 0.004467875971763024
Kedemah 0.002233937985881512
stricken 0.004467875971763024
possessor 0.004467875971763024
sojourner 0.002233937985881512
Edomites 0.004467875971763024
desired 0.002233937985881512
stronger 0.006701813957644536
reigned 0.02233937985881512
activity 0.002233937985881512
pressed 0.006701813957644536
pleasure 0.002233937985881512
fulfilled 0.01116968992940756
vestures 0.002233937985881512
touch 0.004467875971763024
hundredfo 0.002233937985881512
Nebajoth 0.006701813957644536
whereon 0.002233937985881512
everlasting 0.017871503887052095
Lot 0.06701813957644535
tak 0.002233937985881512
Shepho 0.002233937985881512
trough 0.002233937985881512
from 0.3507282637833974
sword 0.013403627915289072
deceiver 0.002233937985881512
right 0.02233937985881512
watered 0.01116968992940756
know 0.049146635689393266
wit 0.002233937985881512
provision 0.004467875971763024
biteth 0.002233937985881512
rider 0.002233937985881512
LORD 0.370833705656331
womenservants 0.004467875971763024
Where 0.01116968992940756
day 0.15860959699758734
Thy 0.024573317844696633
under 0.037976945759985704
thing 0.08712358144937897
shed 0.002233937985881512
males 0.002233937985881512
Yea 0.004467875971763024
soon 0.006701813957644536
bundles 0.002233937985881512
Shall 0.013403627915289072
dipped 0.002233937985881512
built 0.008935751943526048
ungirded 0.002233937985881512
Sodom 0.042444821731748725
Gatam 0.004467875971763024
Pinon 0.002233937985881512
tree 0.04691269770351175
In 0.026807255830578143
anything 0.002233937985881512
own 0.017871503887052095
sad 0.002233937985881512
honour 0.002233937985881512
visited 0.002233937985881512
Sered 0.002233937985881512
strakes 0.002233937985881512
salvation 0.002233937985881512
tithes 0.002233937985881512
Eden 0.013403627915289072
Avith 0.002233937985881512
profit 0.004467875971763024
th 0.042444821731748725
emptied 0.004467875971763024
rested 0.006701813957644536
Bedad 0.002233937985881512
surely 0.03350906978822268
westwa 0.002233937985881512
sought 0.002233937985881512
fill 0.004467875971763024
Uzal 0.002233937985881512
ir 0.002233937985881512
Forasmuch 0.002233937985881512
when 0.25020105441872936
vowed 0.002233937985881512
bodies 0.002233937985881512
but 0.14743990706817978
harlot 0.013403627915289072
pla 0.004467875971763024
Zaavan 0.002233937985881512
hairy 0.006701813957644536
Naamah 0.002233937985881512
whelp 0.002233937985881512
purchased 0.002233937985881512
G 0.004467875971763024
Dishan 0.006701813957644536
butler 0.017871503887052095
liveth 0.002233937985881512
walking 0.002233937985881512
Fill 0.002233937985881512
counted 0.006701813957644536
Shechem 0.037976945759985704
Jimnah 0.002233937985881512
should 0.04691269770351175
command 0.006701813957644536
Our 0.002233937985881512
breed 0.002233937985881512
breath 0.008935751943526048
keep 0.029041193816459657
Lift 0.004467875971763024
Beriah 0.004467875971763024
inhabitants 0.006701813957644536
ewe 0.006701813957644536
upright 0.002233937985881512
surety 0.01116968992940756
selfwill 0.002233937985881512
are 0.2658386203198999
loved 0.02010544187293361
leave 0.013403627915289072
solemnly 0.002233937985881512
possession 0.024573317844696633
establish 0.013403627915289072
taken 0.04691269770351175
sawest 0.002233937985881512
true 0.01116968992940756
Arphaxad 0.013403627915289072
bitter 0.002233937985881512
sustained 0.002233937985881512
person 0.002233937985881512
Man 0.002233937985881512
carried 0.008935751943526048
Eno 0.002233937985881512
get 0.015637565901170585
yea 0.029041193816459657
south 0.01116968992940756
After 0.006701813957644536
hastened 0.004467875971763024
Gad 0.008935751943526048
doer 0.002233937985881512
haven 0.004467875971763024
requite 0.002233937985881512
mess 0.002233937985881512
hold 0.006701813957644536
messengers 0.004467875971763024
bow 0.024573317844696633
bed 0.008935751943526048
Machpelah 0.013403627915289072
amongst 0.004467875971763024
Surely 0.01116968992940756
bake 0.002233937985881512
sake 0.024573317844696633
Hitti 0.002233937985881512
For 0.06478420159056385
manner 0.02010544187293361
Phichol 0.006701813957644536
Hebrew 0.008935751943526048
bank 0.002233937985881512
walketh 0.002233937985881512
Kadmonites 0.002233937985881512
towns 0.002233937985881512
strengthened 0.002233937985881512
peop 0.002233937985881512
blessings 0.01116968992940756
tarried 0.006701813957644536
dukes 0.024573317844696633
commandment 0.002233937985881512
lived 0.08488964346349745
Syrian 0.01116968992940756
burdens 0.002233937985881512
widow 0.004467875971763024
canst 0.002233937985881512
assembly 0.002233937985881512
worship 0.002233937985881512
sir 0.002233937985881512
Pildash 0.002233937985881512
Magog 0.002233937985881512
Kenizzites 0.002233937985881512
dwelled 0.008935751943526048
Medan 0.002233937985881512
Mehetabel 0.002233937985881512
fie 0.004467875971763024
bird 0.002233937985881512
Obal 0.002233937985881512
lovest 0.002233937985881512
badest 0.002233937985881512
age 0.02010544187293361
departing 0.002233937985881512
ears 0.029041193816459657
Sheba 0.006701813957644536
unleavened 0.002233937985881512
smelled 0.004467875971763024
seas 0.002233937985881512
grace 0.024573317844696633
sweet 0.002233937985881512
touching 0.002233937985881512
fatfleshed 0.004467875971763024
tender 0.006701813957644536
truly 0.008935751943526048
While 0.002233937985881512
gift 0.002233937985881512
earth 0.24796711643284783
heap 0.013403627915289072
Serah 0.002233937985881512
quart 0.002233937985881512
Kedar 0.002233937985881512
ear 0.02010544187293361
clo 0.002233937985881512
Amal 0.002233937985881512
ark 0.0558484496470378
forgotten 0.002233937985881512
sakes 0.002233937985881512
concerning 0.013403627915289072
Epher 0.002233937985881512
rods 0.013403627915289072
Hamathite 0.002233937985881512
knowledge 0.004467875971763024
cannot 0.024573317844696633
lambs 0.008935751943526048
On 0.008935751943526048
therein 0.02233937985881512
where 0.04467875971763024
Look 0.002233937985881512
between 0.0558484496470378
Jidlaph 0.002233937985881512
beside 0.004467875971763024
remained 0.004467875971763024
six 0.015637565901170585
Reuben 0.026807255830578143
storehouses 0.002233937985881512
elders 0.004467875971763024
Jabbok 0.002233937985881512
arrayed 0.002233937985881512
two 0.11616477526583863
sixteen 0.002233937985881512
Hirah 0.004467875971763024
tidings 0.002233937985881512
restrained 0.006701813957644536
Bela 0.008935751943526048
silv 0.004467875971763024
rent 0.008935751943526048
What 0.06031632561880082
thither 0.017871503887052095
Potiphar 0.004467875971763024
younger 0.03127513180234117
white 0.01116968992940756
deceived 0.002233937985881512
befell 0.002233937985881512
learned 0.002233937985881512
vineyard 0.002233937985881512
firstborn 0.037976945759985704
buryingplace 0.013403627915289072
citi 0.002233937985881512
getting 0.002233937985881512
hairs 0.006701813957644536
shot 0.004467875971763024
no 0.05808238763291931
scattered 0.004467875971763024
communing 0.002233937985881512
must 0.013403627915289072
kissed 0.017871503887052095
These 0.04691269770351175
dungeon 0.002233937985881512
flo 0.002233937985881512
whose 0.03574300777410419
curse 0.008935751943526048
formed 0.006701813957644536
hide 0.004467875971763024
saith 0.01116968992940756
Diklah 0.002233937985881512
liest 0.002233937985881512
sorrow 0.013403627915289072
Shem 0.03127513180234117
having 0.002233937985881512
Meshech 0.002233937985881512
grown 0.002233937985881512
long 0.004467875971763024
piece 0.002233937985881512
kids 0.004467875971763024
this 0.274774372263426
reason 0.004467875971763024
roll 0.002233937985881512
declare 0.002233937985881512
attained 0.002233937985881512
obeisance 0.006701813957644536
beginning 0.01116968992940756
gotten 0.013403627915289072
verily 0.002233937985881512
nig 0.002233937985881512
thoroughly 0.002233937985881512
finish 0.002233937985881512
many 0.015637565901170585
ruled 0.002233937985881512
Hear 0.006701813957644536
shewed 0.015637565901170585
thine 0.05138057367527477
wept 0.03127513180234117
weep 0.004467875971763024
go 0.14297203109641676
stars 0.01116968992940756
gutters 0.004467875971763024
secretly 0.002233937985881512
Zar 0.002233937985881512
subdue 0.002233937985881512
willing 0.004467875971763024
place 0.10276114735054954
smell 0.006701813957644536
looked 0.03350906978822268
Lay 0.002233937985881512
Jacob 0.39987489947279065
.) 0.002233937985881512
with 0.6456080779197569
hotly 0.002233937985881512
our 0.14073809311053526
marvelled 0.002233937985881512
Irad 0.004467875971763024
river 0.03127513180234117
comest 0.006701813957644536
labour 0.006701813957644536
jewels 0.004467875971763024
cold 0.002233937985881512
order 0.002233937985881512
A 0.004467875971763024
strive 0.004467875971763024
married 0.002233937985881512
travailed 0.004467875971763024
land 0.4110445894021982
Zebul 0.002233937985881512
flocks 0.05138057367527477
oxen 0.01116968992940756
bakemeats 0.002233937985881512
roof 0.002233937985881512
Horites 0.006701813957644536
Mishma 0.002233937985881512
Then 0.08488964346349745
Jegarsahadutha 0.002233937985881512
prevail 0.004467875971763024
noon 0.004467875971763024
Hemdan 0.002233937985881512
instruments 0.002233937985881512
am 0.09605933339290501
Lud 0.002233937985881512
mean 0.002233937985881512
multiply 0.04021088374586722
down 0.1318023411670092
anguish 0.002233937985881512
fast 0.002233937985881512
Asshurim 0.002233937985881512
Enos 0.01116968992940756
Bilhah 0.02010544187293361
garments 0.006701813957644536
Lest 0.006701813957644536
Tamar 0.01116968992940756
Huz 0.002233937985881512
Isui 0.002233937985881512
charge 0.004467875971763024
Up 0.004467875971763024
overthrew 0.004467875971763024
strange 0.006701813957644536
former 0.002233937985881512
Shuah 0.006701813957644536
mark 0.002233937985881512
Zeboiim 0.004467875971763024
waxed 0.006701813957644536
interpret 0.008935751943526048
Iram 0.002233937985881512
Zemarite 0.002233937985881512
killed 0.002233937985881512
Jeush 0.006701813957644536
water 0.06031632561880082
brook 0.002233937985881512
Nahath 0.004467875971763024
feeble 0.002233937985881512
Haggi 0.002233937985881512
made 0.16084353498346887
fear 0.024573317844696633
asked 0.02010544187293361
sixth 0.004467875971763024
played 0.002233937985881512
horse 0.002233937985881512
second 0.03127513180234117
opened 0.026807255830578143
childless 0.002233937985881512
Shobal 0.006701813957644536
hire 0.008935751943526048
bak 0.002233937985881512
priests 0.006701813957644536
wander 0.002233937985881512
vagabond 0.004467875971763024
Jetheth 0.002233937985881512
sevens 0.004467875971763024
seeing 0.015637565901170585
help 0.006701813957644536
Elah 0.002233937985881512
Egyptian 0.015637565901170585
appointed 0.008935751943526048
removing 0.002233937985881512
thicket 0.002233937985881512
Hereby 0.004467875971763024
time 0.0558484496470378
blossoms 0.002233937985881512
fatness 0.004467875971763024
Unto 0.017871503887052095
laden 0.004467875971763024
lingered 0.004467875971763024
ourselves 0.004467875971763024
Babel 0.004467875971763024
Enmishpat 0.002233937985881512
weig 0.002233937985881512
Aner 0.002233937985881512
nati 0.002233937985881512
didst 0.015637565901170585
broth 0.004467875971763024
lan 0.002233937985881512
inheritance 0.004467875971763024
devour 0.002233937985881512
sorely 0.002233937985881512
rebuked 0.004467875971763024
forget 0.004467875971763024
nine 0.026807255830578143
wick 0.002233937985881512
bruise 0.004467875971763024
rank 0.004467875971763024
meat 0.02233937985881512
Bethuel 0.02010544187293361
decreased 0.002233937985881512
fo 0.004467875971763024
His 0.004467875971763024
sent 0.09829327137878653
continually 0.006701813957644536
deprived 0.002233937985881512
that 1.1370744348136896
Manass 0.002233937985881512
beget 0.002233937985881512
matter 0.004467875971763024
couched 0.002233937985881512
moveth 0.006701813957644536
Methusa 0.002233937985881512
Esau 0.16531141095523189
Earth 0.002233937985881512
ea 0.006701813957644536
Eve 0.004467875971763024
earing 0.002233937985881512
Naphish 0.002233937985881512
wild 0.002233937985881512
heads 0.004467875971763024
Ephraim 0.024573317844696633
Zuzims 0.002233937985881512
daught 0.006701813957644536
Eshban 0.002233937985881512
Set 0.002233937985881512
without 0.02010544187293361
skins 0.004467875971763024
Hivite 0.006701813957644536
ne 0.002233937985881512
fourteenth 0.002233937985881512
strong 0.004467875971763024
Er 0.01116968992940756
wi 0.002233937985881512
prospered 0.002233937985881512
loss 0.002233937985881512
nigh 0.002233937985881512
Forgive 0.002233937985881512
none 0.017871503887052095
exceeding 0.006701813957644536
hazel 0.002233937985881512
Speak 0.002233937985881512
carcases 0.002233937985881512
Dinah 0.015637565901170585
reproa 0.002233937985881512
co 0.002233937985881512
searched 0.008935751943526048
Ludim 0.002233937985881512
thread 0.006701813957644536
Timna 0.004467875971763024
abode 0.004467875971763024
despised 0.006701813957644536
servant 0.09159145742114198
thy 0.5964614422303637
fetch 0.01116968992940756
Potipherah 0.006701813957644536
buy 0.026807255830578143
descending 0.002233937985881512
plant 0.002233937985881512
first 0.03574300777410419
hunter 0.006701813957644536
still 0.004467875971763024
tar 0.002233937985881512
provide 0.004467875971763024
spee 0.002233937985881512
al 0.006701813957644536
Lahairoi 0.004467875971763024
sojourn 0.006701813957644536
uncovered 0.002233937985881512
Peniel 0.002233937985881512
sackcloth 0.002233937985881512
haste 0.006701813957644536
fa 0.004467875971763024
part 0.006701813957644536
colours 0.006701813957644536
Joktan 0.006701813957644536
beasts 0.013403627915289072
guilty 0.002233937985881512
loveth 0.002233937985881512
God 0.5160396747386292
anoth 0.004467875971763024
daughte 0.017871503887052095
seekest 0.002233937985881512
dunge 0.002233937985881512
Sabtech 0.002233937985881512
occasion 0.002233937985881512
Sarah 0.08265570547761594
just 0.002233937985881512
Ararat 0.002233937985881512
Penuel 0.002233937985881512
entreated 0.002233937985881512
laws 0.002233937985881512
affliction 0.008935751943526048
year 0.02010544187293361
utmost 0.002233937985881512
fled 0.024573317844696633
oil 0.004467875971763024
Onan 0.01116968992940756
likene 0.002233937985881512
quiver 0.002233937985881512
instructor 0.002233937985881512
Nod 0.002233937985881512
youth 0.004467875971763024
An 0.002233937985881512
Mahalaleel 0.01116968992940756
goa 0.002233937985881512
hast 0.11616477526583863
ash 0.002233937985881512
blameless 0.002233937985881512
north 0.002233937985881512
process 0.004467875971763024
wrong 0.002233937985881512
scarlet 0.004467875971763024
goat 0.002233937985881512
Egy 0.006701813957644536
physicians 0.004467875971763024
altogether 0.002233937985881512
blessed 0.09605933339290501
Euphrates 0.002233937985881512
Ephah 0.002233937985881512
overseer 0.004467875971763024
childr 0.002233937985881512
Elbethel 0.002233937985881512
greatly 0.01116968992940756
kiss 0.004467875971763024
Shuni 0.002233937985881512
afraid 0.02010544187293361
Anamim 0.002233937985881512
child 0.03574300777410419
Emins 0.002233937985881512
Spirit 0.004467875971763024
kneel 0.002233937985881512
weight 0.004467875971763024
slayeth 0.002233937985881512
Asher 0.008935751943526048
Baalhanan 0.004467875971763024
evening 0.02233937985881512
mountains 0.008935751943526048
Aholibamah 0.015637565901170585
plagues 0.002233937985881512
here 0.026807255830578143
hardly 0.002233937985881512
Until 0.002233937985881512
preserved 0.002233937985881512
these 0.18094897685640246
mine 0.03127513180234117
drank 0.008935751943526048
elder 0.008935751943526048
handmaids 0.004467875971763024
peaceable 0.002233937985881512
saved 0.002233937985881512
pigeon 0.002233937985881512
why 0.01116968992940756
breadth 0.004467875971763024
pursued 0.008935751943526048
grief 0.002233937985881512
brick 0.004467875971763024
cattle 0.1116968992940756
We 0.037976945759985704
travail 0.002233937985881512
Zimran 0.002233937985881512
Gershon 0.002233937985881512
Eliezer 0.002233937985881512
Tubal 0.002233937985881512
stalk 0.004467875971763024
They 0.013403627915289072
door 0.026807255830578143
Angel 0.002233937985881512
tongue 0.002233937985881512
meal 0.002233937985881512
behold 0.14520596908229827
dreadful 0.002233937985881512
issue 0.002233937985881512
vale 0.008935751943526048
reward 0.002233937985881512
creeping 0.02010544187293361
field 0.09829327137878653
rib 0.002233937985881512
Duke 0.01116968992940756
dreamed 0.026807255830578143
wherein 0.017871503887052095
shaved 0.002233937985881512
Karnaim 0.002233937985881512
forgive 0.002233937985881512
isles 0.002233937985881512
forward 0.002233937985881512
sheddeth 0.002233937985881512
delight 0.002233937985881512
Beware 0.002233937985881512
eastward 0.006701813957644536
Out 0.004467875971763024
spoken 0.02010544187293361
foals 0.002233937985881512
removed 0.013403627915289072
nights 0.004467875971763024
displease 0.002233937985881512
halted 0.002233937985881512
wheat 0.002233937985881512
food 0.042444821731748725
circumcis 0.002233937985881512
blessi 0.002233937985881512
reached 0.002233937985881512
watering 0.002233937985881512
throne 0.002233937985881512
plagued 0.002233937985881512
overtake 0.002233937985881512
Whoso 0.002233937985881512
worth 0.004467875971763024
Birsha 0.002233937985881512
sacrifice 0.002233937985881512
spotted 0.013403627915289072
Laban 0.12063265123760164
nothing 0.008935751943526048
Judge 0.002233937985881512
ways 0.002233937985881512
hence 0.006701813957644536
herb 0.015637565901170585
waited 0.002233937985881512
By 0.008935751943526048
eventide 0.002233937985881512
void 0.002233937985881512
youngest 0.02233937985881512
Dumah 0.002233937985881512
grieved 0.008935751943526048
Midianites 0.004467875971763024
savoury 0.013403627915289072
silver 0.02010544187293361
near 0.053614511661156286
Dodanim 0.002233937985881512
Moab 0.004467875971763024
butlers 0.002233937985881512
enmity 0.002233937985881512
Arbah 0.002233937985881512
Shaveh 0.004467875971763024
thyself 0.008935751943526048
stript 0.002233937985881512
doth 0.006701813957644536
Sitnah 0.002233937985881512
worthy 0.002233937985881512
served 0.02010544187293361
length 0.004467875971763024
Tola 0.002233937985881512
in 1.313555535698329
Ohad 0.002233937985881512
their 0.3417925118398713
voice 0.049146635689393266
trees 0.006701813957644536
east 0.026807255830578143
torn 0.004467875971763024
accept 0.002233937985881512
concubine 0.004467875971763024
Get 0.004467875971763024
substance 0.015637565901170585
truth 0.004467875971763024
pitched 0.015637565901170585
perpetual 0.002233937985881512
Elishah 0.002233937985881512
lawgiver 0.002233937985881512
conspired 0.002233937985881512
Deliver 0.002233937985881512
whether 0.017871503887052095
rise 0.004467875971763024
wine 0.024573317844696633
buried 0.029041193816459657
add 0.002233937985881512
thigh 0.015637565901170585
foolishly 0.002233937985881512
Canaanite 0.006701813957644536
n 0.008935751943526048
thirty 0.037976945759985704
of 3.033687784827093
goods 0.017871503887052095
least 0.004467875971763024
followed 0.004467875971763024
Temani 0.002233937985881512
Gaham 0.002233937985881512
women 0.01116968992940756
inhabited 0.002233937985881512
army 0.002233937985881512
fou 0.002233937985881512
sold 0.02233937985881512
At 0.002233937985881512
wearied 0.002233937985881512
Damascus 0.004467875971763024
mouths 0.002233937985881512
Machir 0.002233937985881512
duke 0.06031632561880082
always 0.002233937985881512
Every 0.006701813957644536
winged 0.002233937985881512
blindness 0.002233937985881512
above 0.024573317844696633
like 0.004467875971763024
shall 0.5651863104280225
coffin 0.002233937985881512
prophet 0.002233937985881512
Lo 0.004467875971763024
gray 0.006701813957644536
Melchizedek 0.002233937985881512
presented 0.004467875971763024
fountain 0.004467875971763024
Woman 0.002233937985881512
ripe 0.002233937985881512
restore 0.008935751943526048
trained 0.002233937985881512
morter 0.002233937985881512
again 0.09829327137878653
abundantly 0.008935751943526048
little 0.04467875971763024
reviv 0.002233937985881512
conceal 0.002233937985881512
curseth 0.004467875971763024
grass 0.004467875971763024
afterward 0.008935751943526048
wrought 0.002233937985881512
herein 0.002233937985881512
favour 0.006701813957644536
mourned 0.006701813957644536
h 0.037976945759985704
years 0.2278616745599142
Hazezontamar 0.002233937985881512
number 0.008935751943526048
known 0.01116968992940756
Nahor 0.03574300777410419
selfsame 0.006701813957644536
besought 0.002233937985881512
firstlings 0.002233937985881512
plain 0.026807255830578143
west 0.004467875971763024
bough 0.004467875971763024
fed 0.013403627915289072
repenteth 0.002233937985881512
certainly 0.01116968992940756
pitcher 0.02010544187293361
Dedan 0.006701813957644536
hearkened 0.015637565901170585
bondman 0.002233937985881512
Zibeon 0.013403627915289072
whom 0.0558484496470378
depart 0.004467875971763024
belong 0.002233937985881512
poor 0.002233937985881512
Judith 0.002233937985881512
stolen 0.017871503887052095
twelve 0.013403627915289072
Zerah 0.006701813957644536
Send 0.008935751943526048
She 0.017871503887052095
denied 0.002233937985881512
So 0.04691269770351175
eaten 0.02010544187293361
art 0.06925207756232687
fierce 0.002233937985881512
spoil 0.002233937985881512
kine 0.024573317844696633
Nay 0.013403627915289072
aga 0.002233937985881512
high 0.013403627915289072
hath 0.17871503887052095
birthright 0.013403627915289072
nuts 0.002233937985881512
spilled 0.002233937985881512
kid 0.008935751943526048
enemies 0.006701813957644536
prey 0.004467875971763024
woman 0.04467875971763024
wilderness 0.015637565901170585
Shel 0.002233937985881512
hands 0.04021088374586722
on 0.1273344651952462
whole 0.02233937985881512
Japheth 0.015637565901170585
mandrakes 0.01116968992940756
chariot 0.004467875971763024
cleave 0.002233937985881512
heard 0.06701813957644535
w 0.004467875971763024
saddled 0.002233937985881512
committed 0.004467875971763024
Atad 0.004467875971763024
! 0.004467875971763024
kn 0.002233937985881512
health 0.002233937985881512
hundred 0.13627021713877221
grievous 0.013403627915289072
to 1.3649361093736039
more 0.04691269770351175
sewed 0.002233937985881512
purchase 0.002233937985881512
la 0.006701813957644536
remove 0.002233937985881512
Matred 0.002233937985881512
whence 0.008935751943526048
intreated 0.004467875971763024
appoint 0.002233937985881512
mighty 0.015637565901170585
named 0.006701813957644536
visit 0.004467875971763024
may 0.09605933339290501
errand 0.002233937985881512
straitly 0.002233937985881512
Massa 0.002233937985881512
captain 0.02010544187293361
hous 0.002233937985881512
themselves 0.03127513180234117
stink 0.002233937985881512
li 0.004467875971763024
Amalek 0.002233937985881512
hearken 0.01116968992940756
valley 0.006701813957644536
darkne 0.002233937985881512
enough 0.01116968992940756
vowedst 0.002233937985881512
slimepits 0.002233937985881512
Edom 0.024573317844696633
sin 0.017871503887052095
wiv 0.002233937985881512
aloud 0.002233937985881512
drought 0.002233937985881512
s 0.5875256902868377
Calneh 0.002233937985881512
violently 0.002233937985881512
Seeing 0.002233937985881512
Resen 0.002233937985881512
stopped 0.006701813957644536
each 0.015637565901170585
home 0.006701813957644536
Ehi 0.002233937985881512
filled 0.01116968992940756
hunt 0.002233937985881512
got 0.006701813957644536
doubled 0.002233937985881512
sepulchre 0.002233937985881512
sadly 0.002233937985881512
Slay 0.002233937985881512
fetched 0.004467875971763024
city 0.09159145742114198
Arkite 0.002233937985881512
mention 0.002233937985881512
;) 0.002233937985881512
imagination 0.004467875971763024
na 0.002233937985881512
drunken 0.002233937985881512
company 0.013403627915289072
darkness 0.008935751943526048
begat 0.1496738450540613
store 0.004467875971763024
blesseth 0.002233937985881512
form 0.002233937985881512
Almodad 0.002233937985881512
drew 0.013403627915289072
cru 0.002233937985881512
slain 0.004467875971763024
cursed 0.01116968992940756
them 0.5138057367527478
Akan 0.002233937985881512
gr 0.002233937985881512
Goshen 0.02233937985881512
kings 0.017871503887052095
Appoint 0.002233937985881512
Manahath 0.002233937985881512
heav 0.002233937985881512
begettest 0.002233937985881512
henceforth 0.002233937985881512
ask 0.002233937985881512
very 0.04021088374586722
likeness 0.004467875971763024
height 0.002233937985881512
putting 0.002233937985881512
up 0.27254043427754443
blasted 0.006701813957644536
face 0.10499508533643107
kindred 0.02233937985881512
daughers 0.004467875971763024
messes 0.002233937985881512
fellow 0.002233937985881512
angry 0.006701813957644536
son 0.3395585738539898
given 0.04691269770351175
places 0.004467875971763024
heavens 0.006701813957644536
Accad 0.002233937985881512
dove 0.01116968992940756
Adullamite 0.006701813957644536
Shebah 0.002233937985881512
she 0.3596640157269234
mind 0.004467875971763024
knees 0.006701813957644536
the 5.386024483960325
foot 0.004467875971763024
Elon 0.006701813957644536
Hori 0.004467875971763024
Moriah 0.002233937985881512
vail 0.006701813957644536
bulls 0.002233937985881512
mercy 0.008935751943526048
Mehujael 0.004467875971763024
Philistim 0.002233937985881512
Kiriathaim 0.002233937985881512
Raamah 0.004467875971763024
Timnah 0.002233937985881512
Lamech 0.02233937985881512
reproach 0.002233937985881512
most 0.008935751943526048
Bow 0.002233937985881512
lamentati 0.002233937985881512
Moabites 0.002233937985881512
Shammah 0.004467875971763024
wealth 0.002233937985881512
creature 0.017871503887052095
Mizz 0.004467875971763024
salt 0.004467875971763024
will 0.4356179072468948
blessing 0.026807255830578143
Dinhabah 0.002233937985881512
reserved 0.002233937985881512
household 0.01116968992940756
cunning 0.002233937985881512
uncircumcised 0.004467875971763024
merry 0.002233937985881512
sons 0.3172191939951747
can 0.015637565901170585
Haran 0.029041193816459657
end 0.02010544187293361
cry 0.008935751943526048
eldest 0.008935751943526048
Succoth 0.004467875971763024
Jahleel 0.002233937985881512
lighted 0.004467875971763024
sprung 0.004467875971763024
traffick 0.002233937985881512
steal 0.004467875971763024
Swear 0.004467875971763024
Fulfil 0.002233937985881512
Shimron 0.002233937985881512
restored 0.008935751943526048
closed 0.004467875971763024
Kittim 0.002233937985881512
Zo 0.002233937985881512
dust 0.017871503887052095
worshipped 0.006701813957644536
gifts 0.002233937985881512
Almighty 0.013403627915289072
thereby 0.002233937985881512
cubits 0.008935751943526048
If 0.04021088374586722
ceased 0.002233937985881512
LO 0.008935751943526048
Sidon 0.004467875971763024
fruit 0.02010544187293361
seventh 0.008935751943526048
fifth 0.01116968992940756
heart 0.024573317844696633
balm 0.004467875971763024
could 0.024573317844696633
serva 0.004467875971763024
eleven 0.004467875971763024
deep 0.013403627915289072
fishes 0.002233937985881512
fowls 0.01116968992940756
returned 0.04021088374586722
Because 0.024573317844696633
speckled 0.017871503887052095
waters 0.07148601554820838
Beno 0.002233937985881512
themselv 0.004467875971763024
fat 0.01116968992940756
replenish 0.004467875971763024
dainties 0.002233937985881512
Put 0.004467875971763024
garden 0.029041193816459657
cut 0.004467875971763024
pea 0.002233937985881512
hollow 0.008935751943526048
room 0.008935751943526048
Know 0.004467875971763024
past 0.002233937985881512
Girgasite 0.002233937985881512
gave 0.10722902332231257
take 0.10499508533643107
olive 0.002233937985881512
sun 0.013403627915289072
Therefore 0.026807255830578143
service 0.004467875971763024
grapes 0.002233937985881512
sacks 0.017871503887052095
Gerar 0.017871503887052095
Havilah 0.008935751943526048
Stand 0.002233937985881512
brink 0.002233937985881512
yield 0.004467875971763024
away 0.08265570547761594
a 0.7640067911714771
stories 0.002233937985881512
nation 0.017871503887052095
one 0.15637565901170583
fly 0.002233937985881512
pleased 0.008935751943526048
concubi 0.002233937985881512
Beeri 0.002233937985881512
shekels 0.006701813957644536
put 0.08935751943526048
Bring 0.017871503887052095
Hamul 0.002233937985881512
needeth 0.002233937985881512
therefore 0.07818782950585292
side 0.004467875971763024
integrity 0.004467875971763024
thi 0.006701813957644536
Mibsam 0.002233937985881512
shalt 0.16307747296935038
favoured 0.024573317844696633
Tema 0.002233937985881512
mou 0.002233937985881512
commended 0.002233937985881512
When 0.017871503887052095
Hobah 0.002233937985881512
morning 0.04467875971763024
backward 0.006701813957644536
Reub 0.002233937985881512
creepeth 0.017871503887052095
ringstraked 0.015637565901170585
welfare 0.002233937985881512
toward 0.042444821731748725
faults 0.002233937985881512
lightly 0.002233937985881512
Except 0.004467875971763024
naked 0.008935751943526048
avenged 0.002233937985881512
feebler 0.002233937985881512
stole 0.002233937985881512
bring 0.08935751943526048
goeth 0.008935751943526048
feed 0.013403627915289072
Bered 0.002233937985881512
Me 0.002233937985881512
Cast 0.002233937985881512
lentiles 0.002233937985881512
brought 0.1340362791528907
stretched 0.004467875971763024
redeemed 0.002233937985881512
horses 0.002233937985881512
portion 0.013403627915289072
flaming 0.002233937985881512
Zepho 0.004467875971763024
good 0.09829327137878653
Timnath 0.006701813957644536
righteous 0.02233937985881512
struggled 0.002233937985881512
Amorite 0.006701813957644536
brother 0.20328835671521758
Ye 0.02010544187293361
builded 0.015637565901170585
ladder 0.002233937985881512
serpent 0.013403627915289072
Take 0.013403627915289072
chi 0.002233937985881512
tents 0.01116968992940756
lade 0.002233937985881512
Zaphnathpaaneah 0.002233937985881512
fathers 0.02010544187293361
fire 0.006701813957644536
send 0.026807255830578143
changes 0.004467875971763024
Canaanites 0.015637565901170585
meadow 0.002233937985881512
keeper 0.01116968992940756
Ophir 0.002233937985881512
countenance 0.008935751943526048
fashion 0.002233937985881512
Keturah 0.004467875971763024
chesnut 0.002233937985881512
Asshur 0.004467875971763024
Cherubims 0.002233937985881512
needs 0.008935751943526048
Rameses 0.002233937985881512
mother 0.06255026360468234
herds 0.024573317844696633
Rebek 0.002233937985881512
deal 0.013403627915289072
morsel 0.002233937985881512
catt 0.006701813957644536
Egyptia 0.002233937985881512
garmen 0.002233937985881512
bundle 0.002233937985881512
Naphtuhim 0.002233937985881512
sinew 0.004467875971763024
beyond 0.006701813957644536
terror 0.002233937985881512
concubines 0.002233937985881512
speak 0.029041193816459657
Arvadite 0.002233937985881512
foal 0.002233937985881512
breathed 0.002233937985881512
Cain 0.03574300777410419
handle 0.002233937985881512
some 0.013403627915289072
compasseth 0.004467875971763024
endure 0.002233937985881512
Tarshish 0.002233937985881512
Isa 0.006701813957644536
accepted 0.004467875971763024
else 0.004467875971763024
Hittite 0.015637565901170585
cease 0.002233937985881512
songs 0.002233937985881512
ye 0.19435260477169153
grave 0.015637565901170585
tribute 0.002233937985881512
is 0.5964614422303637
oth 0.002233937985881512
occupation 0.004467875971763024
Why 0.006701813957644536
eatest 0.002233937985881512
unit 0.002233937985881512
Gilead 0.008935751943526048
Teman 0.006701813957644536
spread 0.008935751943526048
ribs 0.002233937985881512
lifted 0.03574300777410419
speckl 0.002233937985881512
smite 0.006701813957644536
wentest 0.002233937985881512
stay 0.002233937985881512
light 0.024573317844696633
sacrifices 0.002233937985881512
country 0.03574300777410419
hearts 0.002233937985881512
princes 0.006701813957644536
Paran 0.002233937985881512
begin 0.002233937985881512
doing 0.004467875971763024
rewarded 0.002233937985881512
Leummim 0.002233937985881512
since 0.004467875971763024
dine 0.002233937985881512
rest 0.008935751943526048
Sheleph 0.002233937985881512
for 0.663479581806809
against 0.05138057367527477
Rephaims 0.004467875971763024
rode 0.002233937985881512
Do 0.006701813957644536
wells 0.004467875971763024
ward 0.01116968992940756
bread 0.049146635689393266
Reuel 0.01116968992940756
fleddest 0.002233937985881512
garment 0.017871503887052095
ravin 0.002233937985881512
Gentiles 0.002233937985881512
edge 0.002233937985881512
bone 0.004467875971763024
change 0.002233937985881512
obtain 0.002233937985881512
famine 0.053614511661156286
doubt 0.002233937985881512
milch 0.002233937985881512
trespass 0.006701813957644536
strength 0.006701813957644536
Canaanitish 0.002233937985881512
officers 0.006701813957644536
branches 0.006701813957644536
saying 0.17648110088463945
nostrils 0.004467875971763024
Maachah 0.002233937985881512
oa 0.002233937985881512
burn 0.004467875971763024
thought 0.008935751943526048
eyes 0.08265570547761594
offering 0.017871503887052095
Assyria 0.002233937985881512
grisl 0.002233937985881512
tenor 0.002233937985881512
died 0.07371995353408989
chariots 0.002233937985881512
millions 0.002233937985881512
shear 0.004467875971763024
Simeon 0.02233937985881512
feast 0.01116968992940756
weaned 0.004467875971763024
Ephra 0.004467875971763024
live 0.024573317844696633
choice 0.004467875971763024
before 0.20328835671521758
either 0.004467875971763024
it 0.6478420159056385
whither 0.01116968992940756
multitude 0.015637565901170585
forgat 0.002233937985881512
gavest 0.002233937985881512
) 0.004467875971763024
Ishmeelites 0.008935751943526048
midst 0.013403627915289072
sixty 0.013403627915289072
tower 0.006701813957644536
threescore 0.01116968992940756
Bilhan 0.002233937985881512
wa 0.002233937985881512
heat 0.004467875971763024
ev 0.008935751943526048
wages 0.01116968992940756
Hamor 0.024573317844696633
experience 0.002233937985881512
Also 0.004467875971763024
withhold 0.002233937985881512
Abraham 0.28817800017871503
shrank 0.004467875971763024
merciful 0.002233937985881512
dwe 0.006701813957644536
early 0.015637565901170585
Chesed 0.002233937985881512
office 0.002233937985881512
Zebulun 0.006701813957644536
hills 0.002233937985881512
Mesha 0.002233937985881512
destitute 0.002233937985881512
Shiloh 0.002233937985881512
earring 0.006701813957644536
That 0.024573317844696633
Allonbachuth 0.002233937985881512
Perizzit 0.002233937985881512
might 0.024573317844696633
aprons 0.002233937985881512
befall 0.008935751943526048
round 0.01116968992940756
Calah 0.004467875971763024
afterwards 0.002233937985881512
shepherds 0.004467875971763024
From 0.002233937985881512
meanest 0.002233937985881512
Hebrews 0.004467875971763024
thou 0.6076311321597713
peaceably 0.002233937985881512
Am 0.004467875971763024
envied 0.006701813957644536
bad 0.006701813957644536
than 0.03350906978822268
maidservants 0.01116968992940756
pilled 0.004467875971763024
Hanoch 0.004467875971763024
sist 0.006701813957644536
flesh 0.05808238763291931
servan 0.006701813957644536
thereof 0.026807255830578143
heifer 0.002233937985881512
Kohath 0.002233937985881512
brimstone 0.002233937985881512
Areli 0.002233937985881512
Some 0.002233937985881512
But 0.08265570547761594
progenitors 0.002233937985881512
leaves 0.002233937985881512
covered 0.013403627915289072
Say 0.004467875971763024
Jared 0.01116968992940756
arise 0.017871503887052095
Masrekah 0.002233937985881512
. 2.9376284514341884
Letushim 0.002233937985881512
Ham 0.02233937985881512
submit 0.002233937985881512
months 0.002233937985881512
Is 0.024573317844696633
meant 0.002233937985881512
cool 0.002233937985881512
generation 0.006701813957644536
Ashkenaz 0.002233937985881512
unto 1.318023411670092
house 0.18318291484228397
token 0.008935751943526048
Elparan 0.002233937985881512
consume 0.002233937985881512
felt 0.002233937985881512
lest 0.03127513180234117
wise 0.008935751943526048
brown 0.008935751943526048
Isaac 0.1720132249128764
bereaved 0.006701813957644536
sheep 0.037976945759985704
o 0.01116968992940756
covenant 0.05808238763291931
love 0.008935751943526048
stone 0.024573317844696633
tiller 0.002233937985881512
golden 0.002233937985881512
corn 0.037976945759985704
Zidon 0.002233937985881512
Go 0.03127513180234117
Chezib 0.002233937985881512
believed 0.004467875971763024
overspread 0.002233937985881512
sea 0.017871503887052095
furnace 0.004467875971763024
badne 0.002233937985881512
conceived 0.049146635689393266
sore 0.02233937985881512
stranger 0.015637565901170585
borders 0.004467875971763024
si 0.002233937985881512
wicked 0.008935751943526048
Hemam 0.002233937985881512
slaughter 0.002233937985881512
Levi 0.013403627915289072
Girgashites 0.002233937985881512
answered 0.037976945759985704
virgin 0.004467875971763024
Methusael 0.002233937985881512
seeth 0.004467875971763024
hor 0.002233937985881512
Luz 0.006701813957644536
overthrow 0.004467875971763024
erected 0.002233937985881512
prisoners 0.004467875971763024
divineth 0.002233937985881512
week 0.004467875971763024
air 0.017871503887052095
oak 0.002233937985881512
lean 0.002233937985881512
southward 0.002233937985881512
well 0.10946296130819408
All 0.01116968992940756
camels 0.049146635689393266
dream 0.06925207756232687
faces 0.008935751943526048
Padan 0.002233937985881512
This 0.049146635689393266
went 0.24573317844696632
straw 0.004467875971763024
all 0.5473148065409704
Mezahab 0.002233937985881512
among 0.04467875971763024
tribes 0.004467875971763024
drove 0.013403627915289072
days 0.13627021713877221
not 0.5004021088374587
furniture 0.002233937985881512
build 0.004467875971763024
laid 0.029041193816459657
leaf 0.002233937985881512
mist 0.002233937985881512
Not 0.002233937985881512
Are 0.002233937985881512
Ajah 0.002233937985881512
going 0.006701813957644536
Sinite 0.002233937985881512
Rebekah 0.06478420159056385
shepherd 0.004467875971763024
dale 0.002233937985881512
lying 0.004467875971763024
meditate 0.002233937985881512
bondmen 0.004467875971763024
thereon 0.004467875971763024
mountain 0.01116968992940756
finished 0.002233937985881512
reach 0.002233937985881512
separated 0.006701813957644536
through 0.01116968992940756
bondwoman 0.008935751943526048
serve 0.02010544187293361
chain 0.002233937985881512
sit 0.002233937985881512
Night 0.002233937985881512
myself 0.004467875971763024
Seba 0.002233937985881512
provender 0.008935751943526048
lords 0.002233937985881512
touched 0.006701813957644536
' 0.5986953802162452
ou 0.002233937985881512
mount 0.02233937985881512
shadow 0.002233937985881512
Sabtah 0.002233937985881512
Aram 0.006701813957644536
carry 0.02010544187293361
consumed 0.006701813957644536
Judah 0.06255026360468234
old 0.10052720936466804
Nineveh 0.004467875971763024
nor 0.015637565901170585
audience 0.006701813957644536
hind 0.002233937985881512
spe 0.002233937985881512
drinketh 0.002233937985881512
would 0.015637565901170585
yesternight 0.006701813957644536
appease 0.002233937985881512
work 0.008935751943526048
spoiled 0.004467875971763024
horsemen 0.002233937985881512
Joseph 0.3507282637833974
Shinar 0.008935751943526048
numbered 0.006701813957644536
visions 0.002233937985881512
Jokshan 0.004467875971763024
empty 0.006701813957644536
tr 0.002233937985881512
grap 0.004467875971763024
beguiled 0.004467875971763024
sure 0.004467875971763024
created 0.024573317844696633
beautiful 0.002233937985881512
covering 0.004467875971763024
victuals 0.002233937985881512
whensoever 0.002233937985881512
much 0.017871503887052095
stones 0.006701813957644536
point 0.002233937985881512
Heth 0.026807255830578143
there 0.2591368063622554
cruelty 0.002233937985881512
departed 0.026807255830578143
both 0.06478420159056385
hate 0.006701813957644536
To 0.002233937985881512
righteousness 0.004467875971763024
Thou 0.026807255830578143
camel 0.004467875971763024
enter 0.002233937985881512
ascending 0.002233937985881512
Bless 0.002233937985881512
power 0.006701813957644536
images 0.006701813957644536
fell 0.026807255830578143
Arodi 0.002233937985881512
witness 0.013403627915289072
binding 0.002233937985881512
divide 0.01116968992940756
staff 0.006701813957644536
Ashbel 0.002233937985881512
escape 0.01116968992940756
told 0.07595389151997141
mock 0.004467875971763024
tempt 0.002233937985881512
Madai 0.002233937985881512
next 0.002233937985881512
servants 0.08265570547761594
And 2.7924224823518897
mayest 0.01116968992940756
Ithran 0.002233937985881512
habitations 0.004467875971763024
circumcise 0.002233937985881512
calf 0.004467875971763024
Art 0.002233937985881512
asketh 0.002233937985881512
Bethlehem 0.004467875971763024
so 0.11616477526583863
male 0.024573317844696633
( 0.013403627915289072
threshingfloor 0.002233937985881512
Ephrath 0.004467875971763024
wife 0.23232955053167725
mischief 0.006701813957644536
burnt 0.017871503887052095
betwixt 0.02233937985881512
separate 0.006701813957644536
green 0.006701813957644536
sto 0.002233937985881512
pasture 0.002233937985881512
Only 0.004467875971763024
her 0.38647127155750155
plains 0.002233937985881512
walk 0.008935751943526048
grisled 0.002233937985881512
circumcised 0.03127513180234117
hang 0.002233937985881512
lodge 0.004467875971763024
offended 0.004467875971763024
twins 0.004467875971763024
plenty 0.008935751943526048
Whence 0.002233937985881512
feared 0.004467875971763024
rooms 0.002233937985881512
was 0.7081583415244392
fury 0.002233937985881512
butlership 0.002233937985881512
digged 0.024573317844696633
night 0.06031632561880082
pursue 0.002233937985881512
boldly 0.002233937985881512
wast 0.008935751943526048
way 0.07595389151997141
words 0.037976945759985704
fainted 0.004467875971763024
ghost 0.008935751943526048
Horite 0.002233937985881512
ashamed 0.002233937985881512
Binding 0.002233937985881512
subtilty 0.002233937985881512
hard 0.006701813957644536
wolf 0.002233937985881512
longedst 0.002233937985881512
yourselves 0.008935751943526048
Jezer 0.002233937985881512
Mahalath 0.002233937985881512
fema 0.002233937985881512
Gihon 0.002233937985881512
received 0.002233937985881512
wotteth 0.002233937985881512
said 1.0633544812795996
guiding 0.002233937985881512
Hai 0.004467875971763024
displeased 0.004467875971763024
With 0.008935751943526048
fro 0.002233937985881512
Blessed 0.006701813957644536
sware 0.02010544187293361
shekel 0.002233937985881512
season 0.002233937985881512
parts 0.002233937985881512
leaped 0.002233937985881512
rule 0.01116968992940756
few 0.01116968992940756
whoredom 0.002233937985881512
toil 0.004467875971763024
Shemeber 0.002233937985881512
shrubs 0.002233937985881512
pilgrimage 0.004467875971763024
lord 0.09159145742114198
indeed 0.017871503887052095
Mahanaim 0.002233937985881512
and 5.424001429720311
Thirty 0.002233937985881512
Aran 0.002233937985881512
established 0.004467875971763024
though 0.006701813957644536
gracious 0.002233937985881512
Ezer 0.006701813957644536
Kor 0.002233937985881512
sinning 0.002233937985881512
whereby 0.004467875971763024
off 0.04467875971763024
besides 0.004467875971763024
Phuvah 0.002233937985881512
butter 0.002233937985881512
which 0.4423197212045394
venison 0.017871503887052095
journeys 0.002233937985881512
into 0.19211866678581002
Noah 0.09159145742114198
obey 0.006701813957644536
Cainan 0.01116968992940756
destroyed 0.01116968992940756
we 0.20105441872933608
pleaseth 0.004467875971763024
statutes 0.002233937985881512
offer 0.002233937985881512
what 0.042444821731748725
ever 0.004467875971763024
EleloheIsrael 0.002233937985881512
yielded 0.002233937985881512
Zohar 0.006701813957644536
wood 0.01116968992940756
honourable 0.002233937985881512
twice 0.002233937985881512
moved 0.004467875971763024
sheweth 0.002233937985881512
spicery 0.002233937985881512
wrath 0.004467875971763024
defiled 0.008935751943526048
Carmi 0.002233937985881512
compassed 0.002233937985881512
Amraphel 0.004467875971763024
desolate 0.002233937985881512
any 0.05138057367527477
seem 0.002233937985881512
ten 0.04021088374586722
charged 0.008935751943526048
Hul 0.002233937985881512
Casluhim 0.002233937985881512
best 0.006701813957644536
call 0.017871503887052095
who 0.04021088374586722
appe 0.002233937985881512
Arioch 0.004467875971763024
ram 0.006701813957644536
marriages 0.002233937985881512
conceive 0.006701813957644536
Benjamin 0.037976945759985704
dress 0.004467875971763024
coat 0.017871503887052095
Belah 0.002233937985881512
Huppim 0.002233937985881512
measures 0.002233937985881512
Thus 0.026807255830578143
Kirjatharba 0.002233937985881512
Bozrah 0.002233937985881512
Jubal 0.002233937985881512
us 0.2077562326869806
colt 0.002233937985881512
abated 0.006701813957644536
consent 0.006701813957644536
verified 0.002233937985881512
breasts 0.002233937985881512
; 1.3515324814583147
twel 0.002233937985881512
husba 0.002233937985881512
guard 0.013403627915289072
O 0.02010544187293361
speaketh 0.002233937985881512
street 0.002233937985881512
archers 0.002233937985881512
breaking 0.002233937985881512
language 0.008935751943526048
master 0.06478420159056385
speedily 0.002233937985881512
fall 0.008935751943526048
ma 0.002233937985881512
understand 0.004467875971763024
lift 0.017871503887052095
preserve 0.008935751943526048
death 0.015637565901170585
at 0.11839871325172013
priest 0.008935751943526048
name 0.2233937985881512
Iscah 0.002233937985881512
tillest 0.002233937985881512
joined 0.006701813957644536
archer 0.002233937985881512
morever 0.002233937985881512
shamed 0.002233937985881512
altar 0.029041193816459657
half 0.002233937985881512
lieth 0.004467875971763024
Gomer 0.004467875971763024
corrupted 0.002233937985881512
Peace 0.002233937985881512
lamp 0.002233937985881512
Ard 0.002233937985881512
lo 0.024573317844696633
Give 0.017871503887052095
forth 0.09605933339290501
hid 0.008935751943526048
did 0.1295684031811277
cities 0.017871503887052095
Jebusites 0.002233937985881512
Ziphion 0.002233937985881512
seemed 0.004467875971763024
became 0.026807255830578143
my 0.7260298454114914
word 0.015637565901170585
Mamre 0.02010544187293361
comfort 0.008935751943526048
falsely 0.002233937985881512
wagons 0.008935751943526048
then 0.07371995353408989
discerned 0.002233937985881512
lack 0.004467875971763024
worse 0.002233937985881512
cast 0.015637565901170585
better 0.002233937985881512
alone 0.006701813957644536
Naphtali 0.008935751943526048
chamber 0.002233937985881512
bands 0.004467875971763024
hadst 0.004467875971763024
sow 0.002233937985881512
lamb 0.004467875971763024
abomination 0.004467875971763024
passed 0.017871503887052095
handmaidens 0.002233937985881512
rose 0.04691269770351175
whatsoever 0.01116968992940756
wickedly 0.002233937985881512
oversig 0.002233937985881512
Day 0.002233937985881512
generations 0.03574300777410419
cup 0.02233937985881512
whales 0.002233937985881512
Jordan 0.01116968992940756
Assyr 0.002233937985881512
alo 0.002233937985881512
cried 0.015637565901170585
cave 0.024573317844696633
daughters 0.11839871325172013
lie 0.013403627915289072
Perizzite 0.002233937985881512
officer 0.004467875971763024
mourning 0.013403627915289072
deed 0.002233937985881512
conception 0.002233937985881512
aw 0.004467875971763024
Admah 0.006701813957644536
were 0.3641318916986864
Escape 0.002233937985881512
Hagar 0.026807255830578143
fail 0.002233937985881512
rul 0.002233937985881512
placed 0.004467875971763024
Seir 0.017871503887052095
remaineth 0.002233937985881512
throughout 0.006701813957644536
sle 0.002233937985881512
fai 0.004467875971763024
shoulder 0.01116968992940756
wash 0.006701813957644536
Kenaz 0.006701813957644536
double 0.004467875971763024
ended 0.006701813957644536
midwife 0.004467875971763024
every 0.19658654275757306
ki 0.01116968992940756
neither 0.026807255830578143
slime 0.002233937985881512
Abidah 0.002233937985881512
fearest 0.002233937985881512
peace 0.015637565901170585
fourscore 0.004467875971763024
kindled 0.004467875971763024
Salah 0.013403627915289072
joint 0.002233937985881512
scatter 0.004467875971763024
wouldest 0.006701813957644536
pris 0.002233937985881512
bear 0.029041193816459657
mast 0.002233937985881512
colts 0.002233937985881512
sleep 0.01116968992940756
absent 0.002233937985881512
goest 0.01116968992940756
seen 0.024573317844696633
households 0.006701813957644536
foreskin 0.01116968992940756
bound 0.017871503887052095
bottle 0.006701813957644536
menservants 0.01116968992940756
Both 0.002233937985881512
such 0.024573317844696633
pillows 0.004467875971763024
stayed 0.006701813957644536
offerings 0.002233937985881512
possess 0.004467875971763024
tops 0.002233937985881512
Gaza 0.002233937985881512
baskets 0.004467875971763024
met 0.004467875971763024
multiplying 0.002233937985881512
Make 0.004467875971763024
myrrh 0.004467875971763024
remember 0.008935751943526048
Ashteroth 0.002233937985881512
Guni 0.002233937985881512
whereof 0.002233937985881512
called 0.21892592261638816
damsels 0.002233937985881512
blame 0.004467875971763024
rich 0.002233937985881512
those 0.017871503887052095
thirteenth 0.002233937985881512
Sod 0.004467875971763024
hindermost 0.002233937985881512
Malchiel 0.002233937985881512
tru 0.002233937985881512
fath 0.006701813957644536
dwell 0.049146635689393266
Fear 0.006701813957644536
posterity 0.002233937985881512
receive 0.006701813957644536
risen 0.002233937985881512
heaven 0.06255026360468234
greater 0.01116968992940756
herself 0.008935751943526048
rams 0.008935751943526048
Merari 0.002233937985881512
whomsoever 0.004467875971763024
vengeance 0.002233937985881512
knew 0.037976945759985704
being 0.017871503887052095
Hadoram 0.002233937985881512
glory 0.004467875971763024
Hazarmaveth 0.002233937985881512
Moreh 0.002233937985881512
refrain 0.002233937985881512
nurse 0.004467875971763024
wilt 0.029041193816459657
praise 0.004467875971763024
Korah 0.006701813957644536
pieces 0.015637565901170585
Two 0.004467875971763024
Mam 0.002233937985881512
budded 0.002233937985881512
savour 0.002233937985881512
Bethel 0.026807255830578143
foremost 0.004467875971763024
bdellium 0.002233937985881512
wrestled 0.006701813957644536
nations 0.04021088374586722
father 0.4423197212045394
him 0.8645340005361452
ran 0.02010544187293361
Behold 0.11839871325172013
Benam 0.002233937985881512
Shalt 0.002233937985881512
deferred 0.002233937985881512
Gether 0.002233937985881512
remembered 0.008935751943526048
according 0.07148601554820838
appear 0.002233937985881512
ford 0.002233937985881512
harp 0.004467875971763024
twentieth 0.002233937985881512
shortly 0.002233937985881512
turn 0.008935751943526048
leap 0.002233937985881512
governor 0.004467875971763024
castles 0.002233937985881512
rouse 0.002233937985881512
divided 0.02233937985881512
eighty 0.006701813957644536
tarry 0.006701813957644536
third 0.02233937985881512
graciously 0.004467875971763024
certain 0.008935751943526048
famished 0.002233937985881512
Issachar 0.008935751943526048
confound 0.004467875971763024
Ephron 0.026807255830578143
judge 0.01116968992940756
embraced 0.006701813957644536
clean 0.015637565901170585
heed 0.004467875971763024
honey 0.002233937985881512
Din 0.002233937985881512
prince 0.006701813957644536
Remain 0.002233937985881512
times 0.008935751943526048
Kenites 0.002233937985881512
deeds 0.002233937985881512
slew 0.015637565901170585
mightier 0.002233937985881512
Lotan 0.008935751943526048
plenteousness 0.002233937985881512
red 0.006701813957644536
sac 0.002233937985881512
Even 0.004467875971763024
swear 0.013403627915289072
folly 0.002233937985881512
how 0.017871503887052095
evil 0.03574300777410419
handmaid 0.015637565901170585
money 0.07148601554820838
Hushim 0.002233937985881512
wor 0.002233937985881512
top 0.006701813957644536
die 0.0558484496470378
Adam 0.04021088374586722
herdmen 0.013403627915289072
obeyed 0.006701813957644536
kindly 0.008935751943526048
fourteen 0.004467875971763024
Achbor 0.004467875971763024
Pass 0.002233937985881512
toucheth 0.002233937985881512
caused 0.008935751943526048
turned 0.013403627915289072
horror 0.002233937985881512
gard 0.002233937985881512
prevailed 0.015637565901170585
sporting 0.002233937985881512
wondering 0.002233937985881512
weary 0.002233937985881512
shore 0.002233937985881512
Manasseh 0.02233937985881512
required 0.002233937985881512
Jerah 0.002233937985881512
countries 0.008935751943526048
gre 0.006701813957644536
fathe 0.002233937985881512
boug 0.002233937985881512
corrupt 0.004467875971763024
mourn 0.002233937985881512
earrings 0.002233937985881512
moving 0.004467875971763024
Caphtorim 0.002233937985881512
interpretation 0.01116968992940756
giants 0.002233937985881512
dominion 0.008935751943526048
Chedorlaomer 0.01116968992940756
The 0.1116968992940756
hundredth 0.004467875971763024
Shed 0.002233937985881512
seventeenth 0.004467875971763024
herd 0.002233937985881512
meet 0.026807255830578143
husband 0.015637565901170585
baker 0.01116968992940756
plenteous 0.004467875971763024
steward 0.008935751943526048
Adbeel 0.002233937985881512
wall 0.002233937985881512
doe 0.002233937985881512
gathering 0.004467875971763024
grow 0.004467875971763024
barren 0.004467875971763024
return 0.013403627915289072
seest 0.006701813957644536
betimes 0.002233937985881512
softly 0.002233937985881512
same 0.049146635689393266
y 0.002233937985881512
freely 0.002233937985881512
fountains 0.004467875971763024
Onam 0.002233937985881512
Ishuah 0.002233937985881512
three 0.06701813957644535
turtledove 0.002233937985881512
talking 0.002233937985881512
morrow 0.002233937985881512
Dishon 0.008935751943526048
broken 0.006701813957644536
Ahuzzath 0.002233937985881512
Ethiopia 0.002233937985881512
thistles 0.002233937985881512
riches 0.004467875971763024
Egyptians 0.026807255830578143
small 0.004467875971763024
spake 0.08712358144937897
Hezron 0.004467875971763024
kill 0.01116968992940756
full 0.017871503887052095
There 0.01116968992940756
Galeed 0.004467875971763024
awoke 0.008935751943526048
Cana 0.006701813957644536
nakedness 0.01116968992940756
dignity 0.002233937985881512
repented 0.002233937985881512
acknowledged 0.002233937985881512
wat 0.004467875971763024
border 0.004467875971763024
folk 0.002233937985881512
by 0.17871503887052095
widowhood 0.002233937985881512
eyed 0.002233937985881512
peradventure 0.015637565901170585
Wherefore 0.026807255830578143
organ 0.002233937985881512
saidst 0.013403627915289072
hasted 0.006701813957644536
suck 0.002233937985881512
fowl 0.03574300777410419
eight 0.02233937985881512
eat 0.10499508533643107
Mibzar 0.002233937985881512
e 0.004467875971763024
refused 0.006701813957644536
Shur 0.006701813957644536
violence 0.004467875971763024
thirteen 0.002233937985881512
smooth 0.004467875971763024
cubit 0.002233937985881512
>>> len(text3)
44764
>>> text3.count("cubit")
1
>>> text3.count("cubit")/len(text3) * 100
0.002233937985881512
