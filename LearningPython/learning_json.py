# -*- coding: utf-8 -*-
import json

try:
    with open("server.json","r",encoding="utf-8") as f:
        loaded_data=json.load(f)
        print(f"ホスト名: {loaded_data['hostname']}")
        print(f"IPアドレス: {loaded_data['ip']}")
        os_info=loaded_data["os"]
        print(f"OS: {os_info['name']} {os_info['version']}")
        
        print("サービス一覧")
        for service in loaded_data["services"]:
            print(f" - {service}")
except json.JSONDecodeError:
    print("JSONの読み込みに失敗しました。（形式が正しくない可能性があります）")

except Exception as e:
    print(f"ファイル読み込みでエラーが発生しました。\n{e}")
    