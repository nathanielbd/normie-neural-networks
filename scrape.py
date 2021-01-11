from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
import pandas as pd

driver = webdriver.Chrome(executable_path="/mnt/c/Users/nathanielbd/Downloads/chromedriver.exe")

FILENAME = 'data-stats-combs.csv'

columns = [
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
    'Rate your life right now.','Which climate do you live in?','X','Y','result'
]

try:
    data = pd.read_csv(FILENAME, index_col=False)
except:
    data = pd.DataFrame(columns=columns)

def scroll_to(element):
    driver.execute_script("return arguments[0].scrollIntoView();", element)

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

class CaptchaGoneWrongEvent(Exception):
    pass

def scrape_comb(k, comb, data, first=False):
    if first:
        driver.get('http://dulm.blue/normie')
        driver.refresh()
    else:
        driver.back()
    values = []
    for i in range(1, 35):
        to_select = random.choice(driver.find_elements_by_css_selector(f'.question > input[name="q{i}"]'))
        scroll_to(to_select)
        to_select.click()
        values.append(to_select.get_attribute('value'))
    to_select = driver.find_elements_by_css_selector('[name="q35"]')[comb[0]]
    values.append(to_select.get_attribute('value'))
    to_select.click()
    for j in range(36, 42):
        select = Select(driver.find_element_by_id(f'q{j}'))
        to_select = comb[j-35]
        select.select_by_index(to_select)
        values.append(select.options[to_select].get_attribute('value'))
    if first:
        idx = int(input('Index of correct captcha: '))
        captcha = driver.find_elements_by_class_name('robotest')[idx-1]
        captcha.click()
    honest = Select(driver.find_element_by_id('honest'))
    honest.select_by_index(1)
    submit_btn = driver.find_element_by_css_selector('[type="submit"]')
    submit_btn.click()
    driver.implicitly_wait(0.5)
    if driver.find_elements_by_css_selector('.header'):
        raise CaptchaGoneWrongEvent
    xy = driver.find_elements_by_tag_name('b')[1:3]
    result = driver.find_element_by_css_selector('.question > h1')
    values = values + list(map(lambda x: x.text, xy)) + [result.text]
    data = data.append(dict(zip(columns, values)), ignore_index=True)
    print(f'added combination {k}')
    return False, data

all_combs = list(product(*stats_combs))
rows_so_far = data.shape[0]
end_pts = zip(range(rows_so_far, len(all_combs), 600), range(rows_so_far+600, len(all_combs)+600, 600))
for start, end in end_pts:
    first = True
    print(f'Combinations {start} to {end}')
    for k, comb in enumerate(all_combs[start:end]):
        try:
            first, data = scrape_comb(k, comb, data, first)
        except CaptchaGoneWrongEvent:
            print('Failed captcha')
            data.to_csv(FILENAME, index=False)
            driver.close()
            quit()
    data.to_csv(FILENAME, index=False)
driver.close()
