import allure
from selene import have
from selene.support.shared import browser



class Payment:
    def open_main(self):
        with allure.step('Open main'):
            browser.open('https://shop.spacex.com/')
        return self


    def search_click(self):
        with allure.step('Search things'):
            browser.element('[data-action="toggle-search"]').click()
        return self

    def search(self, things):
        browser.element('#search-input').type(things)
        return self

    def choose_things(self):
        with allure.step('Choose various'):
            browser.element('.ProductItem__Wrapper > a[href^="/products/spacex-back-pack"]').click()
        return self

    def add(self):
        with allure.step('Add things'):
            browser.element('[data-hcid="pdp-ac"]').click()
        return self

    def go_checkout(self):
        browser.element('[type="submit"]').click()
        return self

    def fill_form(self, email, name, last_name, country, code, city, phone):
        with allure.step('Fill form'):
            browser.element('[name="checkout[email]"]').type(email)
            browser.element('.field__input--select').click()
            browser.element('[data-code="TR"]').click()
            browser.element('#checkout_shipping_address_first_name').type(name)
            browser.element('#checkout_shipping_address_last_name').type(last_name)
            browser.element('#checkout_shipping_address_address1').type(country)
            browser.element('#checkout_shipping_address_zip').type(code)
            browser.element('#checkout_shipping_address_city').type(city)
            browser.element('#checkout_shipping_address_phone').type(phone)
        return self

    def switch(self):
        with allure.step('Switch on payment'):
            browser.element('#continue_button').click()
        return self

    def should_have_text(self, text: str):
        browser.config.timeout = 30
        browser.element('.breadcrumb__item.breadcrumb__item--blank').should(have.text(text))
        return self