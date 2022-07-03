from selenium import webdriver
import time
import kullaniciBilgileri as kb


class Browser:
    def __init__(self,link):
        self.link=link
        self.browser=webdriver.Chrome()
        Browser.goInstagram(self)

    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        time.sleep(2)
        Browser.compare(self)

    def getFollowers(self):
        self.browser.get(self.link + "/" + kb.instagram_username + "/"+"followers"+"/")
        time.sleep(10)

        Browser.scrollDown(self)
        temp = []
        takipciler=self.browser.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")
        for takipci in takipciler:
            print(takipci.text)
            temp.append(takipci.text)
        time.sleep(5)
        return temp

    def getFollowing(self):
        self.browser.get(self.link + "/" + kb.instagram_username + "/" + "following" + "/")
        time.sleep(10)

        Browser.scrollDown(self)

        following=self.browser.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")
        temp = []
        for follow in following:
            temp.append(follow.text)
            print(follow.text)
        return temp






    def scrollDown(self):
        js_command="""
        sayfa=document.querySelector("._aano");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu=sayfa.scrollHeight;
        return sayfaSonu;
        """
        sayfaSonu=self.browser.execute_script(js_command)

        while True:
            son=sayfaSonu
            time.sleep(1)
            sayfaSonu=self.browser.execute_script(js_command)
            if son==sayfaSonu:
                break




    def login(self):


         username= self.browser.find_elements_by_name("username")[0]
         username.send_keys(kb.username)

         password=self.browser.find_elements_by_name("password")[0]
         password.send_keys(kb.password)
         time.sleep(2)

         login_button=self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button")
         login_button.click()
         time.sleep(5)


         self.browser.get(self.link+"/"+kb.instagram_username+"/")
         time.sleep(10)

    def compare(self):
        takipciler=Browser.getFollowers(self)
        following=Browser.getFollowing(self)


        for element in following :

            if element not in takipciler:
                print(element, "is not following")

























