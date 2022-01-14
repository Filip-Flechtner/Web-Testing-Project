from infrastructure.browser import driver


def before_all(context):
    context.browser = driver


def after_all(context):
    context.browser.quit()
