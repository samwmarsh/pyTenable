"""
test for uploading the file and file with encryption
"""
import os
import uuid
import pytest



def test_files_upload(api):
    """
    test to uploads the file object
    """
    api.files.upload(str(uuid.uuid4()))



def test_files_encryption_success(api, datafiles):
    """
    test to upload the file with encryption
    """
    file = 'test.txt'
    with open(os.path.join(str(datafiles), file), 'w+') as fobj:
        fobj.write('test')
        fobj.close()
    with open(os.path.join(str(datafiles), file), 'rb') as fobj:
        api.files.upload(fobj, encrypted=True)