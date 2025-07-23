import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
   # log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
   # allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')
    try:
        logs = browser.driver.get_log('browser')
        log_text = "".join(f"{entry['level']}: {entry['message']}\n" for entry in logs)
        allure.attach(log_text, 'browser_logs', AttachmentType.TEXT, '.log')
    except Exception as e:
        allure.attach(str(e), 'log_error', AttachmentType.TEXT)


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')