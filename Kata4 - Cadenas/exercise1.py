text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

separte_text = text.split('.')

hint1 = 'average'
hint2 = 'temperature'
hint3 = 'distance'

for item in separte_text:
    if item.lower().count(hint1) or item.lower().count(hint2) or item.lower().count(hint3):
        print(item)

for item in separte_text:
    if item.lower().count(hint1) or item.lower().count(hint2) or item.lower().count(hint3):
        print(item.replace('C', 'Celcius.'))
