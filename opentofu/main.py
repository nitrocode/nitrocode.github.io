#!/usr/bin/env python3
import os
import requests
import json

ACCESS_TOKEN = os.environ.get('GH_ADMIN_TOKEN')

org = 'opentofu'
repo = 'opentofu'
binary = 'tofu'

extensions = [
  '386.apk',
  '386.deb',
  '386.rpm',
  'amd64.apk',
  'amd64.deb',
  'amd64.rpm',
  'arm.apk',
  'arm.deb',
  'arm.rpm',
  'arm64.apk',
  'arm64.deb',
  'arm64.rpm',
  'darwin_amd64.zip',
  'darwin_arm64.zip',
  'freebsd_386.zip',
  'freebsd_amd64.zip',
  'freebsd_arm.zip',
  'linux_386.zip',
  'linux_amd64.zip',
  'linux_arm.zip',
  'linux_arm64.zip',
  'openbsd_386.zip',
  'openbsd_amd64.zip',
  'SHA256SUMS',
  'SHA256SUMS.pem',
  'SHA256SUMS.sig',
  'solaris_amd64.zip',
  'windows_amd64.zip'
]

page = 1
main_str = '<ul>\n<li>\n<a href="../">../</a></li>\n'

while True:
    response = requests.get(
        f"https://api.github.com/repos/{org}/{repo}/releases?per_page=100&page={page}",
        headers={"Authorization": "token " + ACCESS_TOKEN},
    )
    releases = response.json()
    for release in releases:
        version_trimmed = f"{release['name'][1:]}"
        version = f"{release['name']}"
        # child page
        path = f'{version_trimmed}/'
        try:
            os.mkdir(path)
        except:
            pass
        child_str = '<ul>\n<li>\n<a href="../">../</a></li>\n'
        # https://github.com/opentofu/opentofu/releases/download/v1.6.0-rc1/tofu_1.6.0-rc1_386.apk
        for ext in extensions:
            file_name = f"{binary}_{version_trimmed}_{ext}"
            child_str += "<li>\n"
            child_str += f'<a href="https://github.com/{org}/{repo}/releases/download/{version}/{file_name}">{file_name}</a>\n'
            child_str += "</li>\n"
        child_str += "</ul>\n"
        with open(f'{path}/index.html', 'w') as f:
            f.write(child_str)
        # main page
        main_str += "<li>\n"
        main_str += f'<a href="/{repo}/{path}">{binary}_{version_trimmed}</a>\n'
        main_str += "</li>\n"
    if not releases:
        break
    page += 1
main_str += "</ul>\n"

with open(f'index.html', 'w') as f:
    f.write(main_str)
