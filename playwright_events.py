from playwright.sync_api import sync_playwright, Request, Response


# Это функция-обработчик (callback), которая будет вызываться для каждого сетевого запроса.
# Она принимает в качестве аргумента объект `Request`, содержащий всю информацию о запросе.
# def log_request(request: Request):
#     # Печатаем URL запроса, который страница пытается выполнить.
#     print(f"Request: {request.url}")
log_request = lambda request: print(f"Request: {request.url}")


# Это функция-обработчик (callback), которая будет вызываться для каждого сетевого ответа.
# Она принимает в качестве аргумента объект `Response`, содержащий всю информацию об ответе.
def log_response(response: Response):
    # Печатаем URL, на который пришел ответ от сервера.
    print(f"Response: {response.url} {response.status}")


def log_specific_requests(request: Request):
    if "github.io" in request.url:
        print(f"Filtered request: {request.url}")


def log_response_body(response):
    if response.ok:
        print(f"Response body: {response.body()}")  # Тело ответа


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Здесь мы "подписываемся" на событие 'request'.
    # Метод page.on() регистрирует нашу функцию `log_request` в качестве "слушателя".
    # Теперь каждый раз, когда страница будет инициировать новый сетевой запрос (например, за картинкой или скриптом),
    # Playwright автоматически вызовет функцию `log_request`.
    page.on("request", log_request)
    # Аналогично, мы подписываемся на событие 'response'.
    # Каждый раз, когда страница получит ответ от сервера на один из своих запросов,
    # Playwright вызовет функцию `log_response`.
    page.on("response", log_response)

    #page.on("request", log_specific_requests)

    page.on("response", log_response_body)

    page.remove_listener("response", log_response_body)

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    page.wait_for_timeout(3000)
