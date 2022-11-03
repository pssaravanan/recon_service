from fastapi import APIRouter, File, UploadFile
import pandas as pd
import csv

router = APIRouter(prefix='/reconcile')

@router.get('/')
def reconcile():
    return {'msg': 'Reconcile'}

@router.post('/uploadfile')
async def uploadfile(file1: UploadFile, file2: UploadFile):
    has_header1 = has_header2 = False
    has_header1 = csv.Sniffer().has_header(str(file1.file.read(2048)))
    has_header2 = csv.Sniffer().has_header(str(file2.file.read(2048)))
    file1.file.seek(0)
    file2.file.seek(0)
    csv_file1 = pd.read_csv(file1.file, header= (0 if has_header1 else None))
    csv_file2 = pd.read_csv(file2.file, header=(0 if has_header2 else None ))
    print(csv_file1)
    print(csv_file2)
    return {'file1': {
        'name': file1.filename,
        'headers': list(csv_file1.columns)
    }, 'file2': {
        'name': file2.filename,
        'headers': list(csv_file2.columns)
    }}
