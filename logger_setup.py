import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(),          # 화면에도 보여주고
            logging.FileHandler("app.log")    # 파일에도 저장
        ]
    )
