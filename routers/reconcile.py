from fastapi import APIRouter, File, UploadFile
import pandas as pd

router = APIRouter(prefix='/reconcile')

@router.get('/')
def reconcile():
    return {'msg': 'Reconcile'}

@router.post('/uploadfile')
async def uploadfile(file1: UploadFile, file2: UploadFile):
    csv_file1 = pd.read_csv(file1.file)
    csv_file2 = pd.read_csv(file2.file)
    print(csv_file1)
    print(csv_file2)
    # print(file1_content)
    return {'file1': file1.filename, 'file2': file2.filename}
