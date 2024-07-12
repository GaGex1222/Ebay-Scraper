from flask import Flask, render_template, url_for, request, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from flask_bootstrap import Bootstrap5
from forms import FindProductForm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app=app)



class SeleniumFinder():

    def get_items(self, site, product_name):
        service = Service(executable_path=r"C:\Users\gald1\Desktop\chromedriver-win64\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=service ,options=chrome_options)
        driver.get(site)

        search_bar = driver.find_element(By.CSS_SELECTOR, '.ui-autocomplete-input')
        search_bar.send_keys(product_name)

        search_button = driver.find_element(By.ID, 'gh-btn')
        search_button.click()

        WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.s-item.s-item__pl-on-bottom')))
        all_results = driver.find_elements(By.CSS_SELECTOR, '.s-item.s-item__pl-on-bottom')
        links = []
        product_names = []
        images_url = []
        for item in all_results:
            div1 = item.find_element(By.TAG_NAME, 'div')
            image_section = div1.find_element(By.CSS_SELECTOR, '.s-item__image-section')
            item_image = image_section.find_element(By.TAG_NAME, 'div')
            item_image_div2 = item_image.find_element(By.TAG_NAME, 'div')
            item_image_img_element = item_image_div2.find_element(By.TAG_NAME, "img")
            image_source = item_image_img_element.get_attribute('src')
            images_url.append(image_source)

            div2 = div1.find_element(By.CSS_SELECTOR, '.s-item__info.clearfix')
            a_tag = div2.find_element(By.TAG_NAME, 'a')
            div_item_title = div2.find_element(By.CSS_SELECTOR, '.s-item__title')
            span_item_title = div_item_title.find_element(By.TAG_NAME, 'span')
            link = a_tag.get_attribute('href')
            links.append(link)
            product_names.append(span_item_title.text)
        
        return links[2:], product_names[2:], images_url[2:]
    
    def get_specific_item_info(self, link):
        service = Service(executable_path=r"C:\Users\gald1\Desktop\chromedriver-win64\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=service ,options=chrome_options)
        driver.get(link)
        price = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div[3]/div/div/div[1]/span')
        seller = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div[2]/div/div/div/a/span')

        return price.text, seller.text
                
        

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    form = FindProductForm()
    if form.validate_on_submit():
        driver = SeleniumFinder()
        links, product_names, images_url = driver.get_items(product_name=request.form.get('product'), site=request.form.get('site'))
        search_keyword = request.form.get('product')
        return redirect(url_for('select_product', links=links, images_url=images_url, product_names=product_names, search_keyword=search_keyword))


    return render_template('main.html', form=form)


@app.route('/select-product', methods=['GET', 'POST'])
def select_product():
    links = request.args.getlist('links')
    product_names = request.args.getlist('product_names')
    images_url = request.args.getlist('images_url')
    search_keyword = request.args.get('search_keyword')
    items_and_links = zip(links, product_names, images_url)

    return render_template('selectproducts.html', items_and_links=items_and_links, search_keyword=search_keyword)

@app.route('/specific-item', methods=['POST', 'GET'])
def specific_item():
    link = request.args.get('link')
    product = request.args.get('product')
    image = request.args.get('image')
    driver = SeleniumFinder()
    price, seller = driver.get_specific_item_info(link=link)
    return render_template('specificitem.html', link=link, product=product, image=image, price=price, seller=seller)
if __name__ == '__main__':
    app.run(debug=True)