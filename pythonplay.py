import newspaper
import requests
from newspaper import fulltext
fox_paper = newspaper.build('http://cnn.com')
# title_dict = {}
for article in fox_paper.articles:
    print(article.url)
    html = requests.get(article.url).text
    text = fulltext(html)
    print(text)
#     for word in article.text:
#         for i in title_dict.keys():
#             if word == i:
#                 title_dict[i] += 1
#             else:
#                 title_dict.update({i, 0})
# print(title_dict)