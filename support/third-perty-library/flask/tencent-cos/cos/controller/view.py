# -*- coding: utf-8 -*-

import json
from flask import request, render_template, flash
from qcloud_cos.cos_client import CosClient
from qcloud_cos.cos_request import UploadFileRequest, ListFolderRequest
from cos import app

bucket = u'masonmou'
cos_client = CosClient(1251123904, u'AKIDkk98ZBnRT4VolE9jL4e3pSVOhSJf8hXC', u'fQxxIXhhoEb4iQYowvli2P0Tm8h8OUQp', region="cd")


@app.route('/list')
def list():
    req = ListFolderRequest(bucket, u'/')
    return render_template('list.html', list_folder_ret=cos_client.list_folder(req)['data']['infos'])


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    path = request.form.get('file', '')
    if request.method == 'POST':
        if '\\' in path:
            filename = path.split('\\')[-1]
        elif '/' in path:
            filename = path.split('/')[-1]
        else:
            filename = path

        req = UploadFileRequest(bucket, u'/%s' % filename, u'%s' % path)
        upload_file_ret = cos_client.upload_file(req)

        if upload_file_ret['code'] == 0:
            flash('Upload Success!')
        else:
            flash('Upload Failed!')

    return render_template('upload.html', req='')
