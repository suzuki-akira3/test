from pathlib2 import Path
import re
import json

class dotdict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

file = Path('./10.1063_1.1774263_jats.txt')
with file.open(encoding='utf-8') as f:
    doc = f.read()

splitLineSpace = re.finditer(r'([^\n]+)(\n)', doc)
textlist = []
for chunk in splitLineSpace:
    dic = {'TX': chunk.group(1), 'LF':chunk.group(2)}
    textlist.append(dic)

d = dotdict(dic)
print(d.TX)
#
# splitspaces = re.finditer(r'([^\s]+?)(\s)', doc)
# token_list = []
# for ss in splitspaces:
#     token_list.append([w for w in ss.groups()])
#
# for token_ in token_list:
#     print(token_)
#     puncts = re.match(r'(.+?)([\.\,\;\:]$)', token_[0])
#     if puncts:
#         print('\t\t', list(puncts.groups()) + [token_[1]])
#     else:
#         print('\t', token_)




