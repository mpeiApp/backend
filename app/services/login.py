import httpx
from ..services.grades import get_html

async def login_to_bars(username: str, password: str):
    login_data = {
        'username': username,
        'password': password
    }

    async with httpx.AsyncClient() as client:
        try:
            # Отправляем POST запрос на вход
            response = await client.post("https://bars.mpei.ru/bars_web/", data=login_data)

            # Проверка статуса перенаправления
            if response.status_code == 302:
                redirect_url = response.headers.get("Location")

                # Получаем HTML-контент сразу, не закрывая client
                html_content = await get_html(client, redirect_url)

                return {
                    'message': 'OK',
                    'status_code': 302,
                    'html_content': html_content
                }
            else:
                return {
                    'message': 'NOT OK',
                    'status_code': response.status_code
                }
        except Exception as e:
            return {
                'message': 'NOT OK',
                'status_code': None,
                'error': str(e)
            }
