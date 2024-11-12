import httpx
from app.utils.schedule import form_schedule, get_schedule


async def get_group_id(group_name: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"http://ts.mpei.ru/api/search?term={group_name}&type=group")
            if response.status_code == 200:
                responseData = response.json()
                if len(responseData) == 1:
                    return {
                        "message": "ok",
                        "data": responseData[0]["id"]
                    }
                else:
                    return {
                        "message": "not ok",
                        "data": "Invalid group number"
                    }

            else:
                return {
                    "message": "not ok",
                    "data": response.status_code
                }

        except Exception as exc:
            return {
                "message": "not ok",
                "data": "Server error"
            }


async def fetch_and_form_schedule(group_id, date_start, date_end):
    response = await get_schedule(group_id, date_start, date_end)
    print(response)
    if response['message'] == "ok":
        data = await form_schedule(response['data'])
        return {
            'message': 'ok',
            'data': data
        }
    return {
        'message': 'not ok',
        'data': response['data']
    }



