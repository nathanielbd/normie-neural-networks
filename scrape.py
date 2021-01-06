from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
import pandas as pd

# driver = webdriver.Firefox(executable_path="/mnt/c/Program Files/Mozilla Firefox/firefox.exe")
# driver = webdriver.Chrome(executable_path='/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe')
driver = webdriver.Chrome(executable_path="/mnt/c/Users/nathanielbd/Downloads/chromedriver.exe")
driver.get('http://dulm.blue/normie')
values = []
for i in range(1, 36):
    to_select = random.choice(driver.find_elements_by_css_selector(f'.question > input[name="q{i}"]'))
    to_select.click()
    values.append(to_select.get_attribute('value'))
for j in range(36, 42):
    select = Select(driver.find_element_by_id(f'q{j}'))
    to_select = random.randrange(len(select.options))
    select.select_by_index(to_select)
    values.append(select.options[to_select].get_attribute('value'))
honest = Select(driver.find_element_by_id('honest'))
honest.select_by_index(1)
# do the captcha
idx = int(input('Index of correct captcha: '))
captcha = driver.find_elements_by_class_name('robotest')[idx-1]
captcha.click()
submit_btn = driver.find_element_by_css_selector('[type="submit"]')
submit_btn.click()
driver.implicitly_wait(0.5)
xy = driver.find_elements_by_tag_name('b')[1:3]
values = values + list(map(lambda x: x.text, xy))

data = pd.DataFrame([values], columns=[
    'Do you want to be in society?','Do you make an attempt to socialise?',
    'Do you consume things to alter your perspective? (Alcohol and stuff)',
    'Are you depressed?','Do you try to improve yourself?',
    'Would you compromise with a friend?',
    'If you and another person were both thirsty and you only had enough water for one person; would you share with the other person?',
    'If a colleague invited you to do something with them; how would you answer? (Date; hang-out; party; etc.)',
    'Are you anxious of social interaction?','Do you think you fit in with other people?',
    'Do you shower more than twice a week?','Do you take care of your appearance? (shaving; hair styling; make up; fashion; etc.)',
    'Do you talk back in equal volume to someone that is talking to you? (Talking as much as they are to you and amplitude of voice)',
    'Which is more difficult?','Does it seem unrealistic to imagine yourself with another person in an intimate context? (Girlfriend; best friends; etc)',
    'Do you have long term goals?','Would you rather work in food service; or be unemployed?',
    "You've lived a life with many moments where you regret doing nothing.",
    'Is it reasonable to think that the majority of people are dumb?',
    'Have you given up?','Are you currently celibate? (No sex for a while)',
    'Do you live your life by your own volition?',
    'Can you look people in the eyes without discomfort?',
    'Has anyone ever described you as awkward; autistic; weird; etc.?',
    'Do you currently have a romantic partner? (Unrequited(crushes); non-exclusive and/or non-monogamous relationships DO NOT count)',
    'Do you currently have a medium for socialization? (Social media; work; etc.)',
    "Do you talk to people on a regular basis? (Internet stuff doesn't count)",
    'Do you have unconventional interests? (Anime; collecting specific items; weird fetishes; etc.)',
    'Are you currently in education; training or employment?','Are you good at speaking?',
    'Is your family proud of you?','Do people usually like being around you?',
    'Can you transport yourself easily?','Are you physically in-shape?',
    'What is your biological sex?','How tall are you?',
    'How attractive are you (from 0 to 10)','What is your BMI?',
    'How many friends and colleagues do you currently have?',
    'Rate your life right now.','Which climate do you live in?','X','Y'
])

from itertools import product
stats_combs = [
    [0, 1, 2],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2],
    [0, 1, 2, 3],
    [0, 1, 2, 3, 4]
]

try:
    for i, comb in enumerate(product(*stats_combs)):
        # driver.get('http://dulm.blue/normie')
        driver.back()
        values = []
        for i in range(1, 35):
            to_select = random.choice(driver.find_elements_by_css_selector(f'.question > input[name="q{i}"]'))
            to_select.click()
            values.append(to_select.get_attribute('value'))
        to_select = driver.find_elements_by_css_selector('[name="q35"]')[comb[0]]
        to_select.click()
        for j in range(36, 42):
            select = Select(driver.find_element_by_id(f'q{j}'))
            to_select = comb[j-35]
            select.select_by_index(to_select)
            values.append(select.options[to_select].get_attribute('value'))
        # idx = int(input('Index of correct captcha: '))
        # captcha = driver.find_elements_by_class_name('robotest')[idx-1]
        # captcha.click()
        honest = Select(driver.find_element_by_id('honest'))
        honest.select_by_index(1)
        submit_btn = driver.find_element_by_css_selector('[type="submit"]')
        submit_btn.click()
        driver.implicitly_wait(0.5)
        xy = driver.find_elements_by_tag_name('b')[1:3]
        values = values + list(map(lambda x: x.text, xy))
        data.append(values)
        print(f'added combination {i}')
finally:
    data.to_csv('data-stats.csv')