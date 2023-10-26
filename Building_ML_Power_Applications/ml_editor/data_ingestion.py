import pandas as pd 
import xml.etree.ElementTree as ElT
from bs4 import BeautifulSoup

from tqdm import tqdm 

def parse_xml_to_csv(path, save_path=None):
    """ 
    .xml 덤프 파일을 열고 텍스트를 토큰화하여 csv로 변환
    :param path: 포스트가 담긴 xml 문서 경로
    :return: 전처리된 텍스트의 데이터프레임
    """
    
    doc = ElT.parse(path)
    root = doc.getroot()
    
    # 각 행은 하나의 포스트
    all_rows = [row.attrib for row in root.findall('row')]
    
    # tqdm을 사용해 전처리 진행과정 출력
    for item in tqdm(all_rows):
        # HTML에서 텍스트 디코딩
        soup = BeautifulSoup(item["Body"], features="html.parser")
        item["body_text"] = soup.get_text()
        
    # 딕셔너리의 리스트에서 데이터프레임 생성
    df = pd.DataFrame.from_dict(all_rows)
    if save_path:
        df.to_csv(save_path)
    return df