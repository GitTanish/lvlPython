import random

# subjects 
subjects = [
    "Shahrukh Khan",
    'Virat Kohli',
    "A Mumbai cat",
    'A group of monkeys',
    'Auto Rickshaw Driver from Delhi'
]

actions = [
    'launches', 'cancels', 'dances with', 'eats', 'declares war on',
    'orders', 'celebrates', 'challenges to a rap battle', 'adopts',
    'gets emotional about', 'performs a magic trick with'
]

objects = [
    'a packet of Maggi',
    'a UFO shaped like a dosa',
    'an angry parrot',
    'a suspicious golgappa vendor',
    'a haunted pressure cooker',
    'a time-travelling rickshaw'
]

places_of_things = [
    'at Red Fort',
    'in Mumbai local train',
    'inside Parliament',
    'at Ganga Ghat',
    'during IPL Match',
    'at India Gate'
]

prefixes = [
    '🛑 Just In:', '🚨 Exclusive:', '😱 Public Shocked As:',
    '🎤 BREAKING:', '💥 DEVELOPING STORY:'
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places_of_things)
    prefix = random.choice(prefixes)

    headline = f"{prefix} {subject} {action} {obj} {place} 😳"
    print('\n' + headline)

    user_input = input('\nDo you want another headline? (yes/no): ').strip().lower()
    if user_input == 'no':
        break

print('\nThanks for using the Press_X_to_Doubt 🤖🗞️')
