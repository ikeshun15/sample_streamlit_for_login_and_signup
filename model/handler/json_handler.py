from typing import Dict
import json

class JsonHandler:
    @staticmethod
    def load_json(json_file_path: str) -> Dict:
        # JSONファイルを読み込み辞書型に格納して返す
        with open(json_file_path, 'r') as f:
            return json.load(f)
        
    
    @staticmethod
    def save_json(json_data: Dict, filename: str) -> None:
        # jsonファイルの書き出し
        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=4)