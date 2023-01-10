from appium import webdriver
from time import sleep

dic = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', dic)
sleep(1)
driver.press_keycode(3)
sleep(1)


def sendToRecent():
    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Snapchat"]').click()
    driver.tap([(530, 1918)])
    # driver.tap([(353, 1278)])
    sleep(1)
    driver.find_element_by_id('com.snapchat.android:id/send_btn_hint_label').click()
    sleep(2)
    driver.find_element_by_id('com.snapchat.android:id/send_to_last_snap').click()
    driver.find_element_by_id('com.snapchat.android:id/send_to_send_button').click()

    driver.press_keycode(3)
    sleep(1)


def sendToShortcut():
    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Snapchat"]').click()
    driver.tap([(530, 1918)])
    # driver.tap([(353, 1278)])
    sleep(1)
    driver.find_element_by_id('com.snapchat.android:id/send_btn_hint_label').click()
    sleep(2)
    driver.find_element_by_xpath('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView''').click()
    # driver.find_element_by_id('com.snapchat.android:id/send_to_section_header').click()
    sleep(1)
    driver.tap([(863, 399)])
    driver.find_element_by_id('com.snapchat.android:id/send_to_send_button').click()

    driver.press_keycode(3)
    sleep(1)


if __name__ == '__main__':
    n = 10
    for i in range(n):
        # sendToShortcut()
        print(f"{i + 1}/{n}")
