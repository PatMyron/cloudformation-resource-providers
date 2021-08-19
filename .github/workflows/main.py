import os
import re
import requests
for repo in requests.get('https://api.github.com/orgs/aws-cloudformation/repos?type=public&per_page=100&sort=full_name').json():
    if 'aws-cloudformation-resource-providers' in repo['html_url']:
        os.system('git submodule add ' + repo['html_url'] + ' ' + re.sub('.*resource-providers-', '', repo['html_url']))
