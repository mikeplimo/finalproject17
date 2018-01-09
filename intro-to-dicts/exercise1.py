what = {"Spanish": 'qué', "French": 'quelle', "Japanese": 'nani', "Basque": 'zer', "Hawaiian": 'He aha'}
print(what['Spanish'])
print(what.keys())
for language in what.keys():
    print(language)

for language in what.keys():
    print(language, what[language])

for language in what.keys():
    print(f"{language} >^..^< {what[language]}")

for language in what.items():
    print(language)

for k, v in what.items():
    print(f"what in {k} is {v}")

