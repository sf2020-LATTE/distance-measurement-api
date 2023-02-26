import pathlib,sys


# インポートさせたいディレクトリパスを取得、sys.pathにインポートさせたいディレクトリを追加する
parent_dir = str(pathlib.Path(__file__).parent.parent.parent)
sys.path.append(parent_dir)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_distance():

    # 緯度経度を全て0でテスト
    response = client.get("/distance/?start_longitude=0&start_latitude=0&end_longitude=0&end_latitude=0")
    assert response.status_code == 200
    assert response.json() == {'distance': 0}

    # 東京タワーとスカリツリーの距離でテスト
    response = client.get("/distance/?start_longitude=139.745433&start_latitude=35.658581&end_longitude=139.8107&end_latitude=35.710063")
    assert response.status_code == 200
    assert response.json() == {'distance': 8.226156}

    # 自由の女神とホワイトハウスの距離でテスト
    response = client.get("/distance/?start_longitude=-74.0445&start_latitude=40.689249&end_longitude=-77.03653&end_latitude=38.897676")
    assert response.status_code == 200
    assert response.json() == {'distance': 324.416908}