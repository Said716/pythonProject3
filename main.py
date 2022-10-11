import pandas
import difflib
def lll(a,i):
    normalized1 = a.lower()
    normalized2 = i.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()

df = pandas.read_csv('posts.csv')
a = input()
s = []
for i in df['text']:
    print(lll(i, a))
#     s.append(lll(i, a))
#
# s.sort()
# print(s)


