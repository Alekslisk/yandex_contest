text = 'Мама мыла раму!'

print({i:text.lower().count(i) for i in text.lower() if i.islower()})