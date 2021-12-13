import time

from  selenium import webdriver

class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        try:
            cooki_acc = self.driver.find_element_by_xpath('//*[@id="q-274726726"]/div/div[2]/div/div/div[1]/button')
            cooki_acc.click()
        except Exception as msg:
            print(msg)

        login_btn = self.driver.find_element_by_xpath('//*[@id="q-274726726"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')

        login_btn.click()
        time.sleep(5)
        ph_btn = self.driver.find_element_by_xpath('//*[@id="q-53386290"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        ph_btn.click()

        time.sleep(5)
        for i in [0,1,2]:
            try:
                ph_num = self.driver.find_element_by_xpath('//*[@id="q-53386290"]/div/div/div[1]/div[2]/div/input')
                break
            except Exception as msg:
                if i == 2:
                    print(msg)
                    print('%i attempt'%i)
                    exit(999)
                else:
                    print('Ops, something is wrong.')
                    print('%i attempt'%i)
                    time.sleep(5)


    def right(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="q-274726726"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button').click()
        except Exception:
            self.driver.find_element_by_xpath('//*[@id="q-274726726"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[5]/div/div[4]/button').click()
    def left(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="q-274726726"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[2]/button').click()
        except Exception:
            self.driver.find_element_by_xpath('//*[@id="q-274726726"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[5]/div/div[2]/button').click()
    def auto_pilot(self, n_profile, accept_p=0.8):
        import random
        for i in range(n_profile):

            try:
                age = self.driver.find_element_by_xpath('//*[@id="q-274726726"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div[3]')

                #eleminate old women
                profile_text = age.get_attribute("innerText").split('\n')
                if len(profile_text)<2 or (not profile_text[1].isdigit() ):
                    self.right()
                    continue
                else:
                    aged = int(profile_text[1])>42
                    if aged:
                        self.left()
                        continue

                time.sleep(random.randint(3, 15))
                if random.random()>0.8:
                    self.left()
                else:
                    self.right()
            except Exception:
                try:
                    self.driver.find_element_by_xpath('//*[@id="q-53386290"]/div/div/button[2]').click()
                except Exception:
                    self.driver.find_element_by_xpath('//*[@id="q-53386290"]/div/div/div[2]/button[2]').click()





