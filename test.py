# from flask import Flask, render_template, url_for, request
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from flask_bootstrap import Bootstrap5
# from forms import FindProductForm
# import time


# service = Service(executable_path=r"C:\Users\gald1\Desktop\chromedriver-win64\chromedriver.exe")
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(service=service ,options=chrome_options)

# driver.get('https://www.ebay.com/itm/325820872720?itmmeta=01J2G6S00BN69N14TPTGV76S57&hash=item4bdc6ff810:g:iCMAAOSwYO5lC0wV&itmprp=enc%3AAQAJAAAA4AR7MpxD0ReHG25iTwc1%2BGwAQABjDmd9dmJqmefDv4pDa4Dqo%2BZoo%2BgBs%2FLbBeFutTs3jt5IDp7Yq7mm0uBOfwpOrxKFlWdRBS5Uig5OWwb%2BtGzHQMPFPI48F7goDnOV7jkZQud%2B9n2by%2FYNFi0Lb3%2BzRNlqUTcR8mfnBNJ1V7jOmXvU%2B%2B8DgnFLbxez0mAi6dZ9Llgo7gnQ2ZShUeN9zG8C1ky1KfbrXG8rZjVeIL0%2Bdy5qVGviNS8dXtmom7RJxxVPTbg53bNE%2FaQtXAjk%2FiT0Fh9LR8O8z3RRxv9B8IMx%7Ctkp%3ABFBMoIDkhpRk')


# price = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div[3]/div/div/div[1]/span')
# print(price.text)


link = 'https://www.ebay.com/itm/166810841237?itmmeta=01J2RQQ9V7EWGY49THMR78QVV6&hash=item26d6b37095:g:ATUAAOSwPnpkCTZ2&itmprp=enc%3AAQAJAAAA4EeV8qw458B0IJOQGHOrwb5kvb3%2BW8TSebJ%2B7fdYe9MJlVVHGu1KojoGjfHfRid0BcbXX0%2F6eArumW9Dxl7q7fKQyrDMKFU3uARxiu%2B6lZo0t%2ByUEK%2FL4Gp57R9ICBGZRwIrLjKrL5nXXmH9kcLaVTG2uMiqYny5i%2FH6wIpA7XMXYBsxjX%2Brpgnz8X7j1yN8GuFV6fmEiGWC3IwLo2kiq%2FQks6JR4fHnnDOdelZ%2BnnxAP20mD95OiVhBzk45w5LEGykCMAgf%2BRGTLXBZZEwsWaUs5zocauBozURMfyaFQ7mD%7Ctkp%3ABFBM6p3dl5Zk'
link_splitter = link.split('?')
print(link_splitter)