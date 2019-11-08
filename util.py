
import json

def get_server_info(key: str):
    with open('server.json', 'rt', encoding='utf-8') as f:
        data = json.load(f)
        for k, v in data.items():
            if k == key:
                return v
        raise ValueError('서버 정보 없음')
