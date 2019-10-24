#!/usr/bin/python3.6

import requests
from termcolor import colored
import pyfiglet
from random import choice

fig = pyfiglet.Figlet(direction='auto', justify='auto', width=100)
word = fig.renderText('Dad Jokes!!')
print(colored(word, 'red', 'on_grey'))


dad_url = 'https://icanhazdadjoke.com/search?'
searchterm = str(input('Let me tell you a Joke! Gimme atopic: '))
res = requests.get(dad_url,
        headers={"Accept" : "Accept: application/json"},
        params={ "term" : searchterm ,
                "limit" : 2}
        )

data = res.json()
totalj = int(data['total_jokes'])
rand_joke = data['results']

if totalj > 1:
      print('There are {0} jokes on {1}, here\'s two'.format(totalj, searchterm))
      print(choice(rand_joke)['joke'])
elif totalj == 1:
      print('I have one joke about {0} and hear is it'.format(searchterm))
      print(data['results'][0]['joke'])
else:
      print('Sorry I donot have any jokes about the topic {0}'.format(searchterm))