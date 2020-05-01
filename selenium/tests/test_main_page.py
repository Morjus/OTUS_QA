def test_main_page(browser):
    link = "http://130.61.126.116/"
    browser.get(link)
    target = browser.find_element_by_css_selector("h1")
    target = target.text
    assert target == "Your Store", "No such element"
