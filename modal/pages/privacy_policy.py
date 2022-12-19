from selene import command, have
from selene.support.shared import browser


class PrivacyPolicy:
    def open_main(self):
        browser.open('https://shop.spacex.com/')
        return self

    def scroll(self):
        browser.element('.Linklist__Item > a[href="/policies/privacy-policy"]').perform(command.js.scroll_into_view)
        return self

    def switch(self):
        browser.element('.Linklist__Item > a[href="/policies/privacy-policy"]').click()
        return self


    def should_have_text(self):
        browser.element('.shopify-policy__title').should(have.text('Privacy policy'))
        return self