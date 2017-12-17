import requests

file = open('proj/app/f.xml','r')

# xml = file.read()



xml = '<document><text>новые технологии</text><text>политика россии</text></document>'
print(xml)
print( requests.post('http://127.0.0.1:8000/classifiers/1/api_classify/', 
					data=xml.encode('utf-8')).text )