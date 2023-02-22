from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: gcp_secret
description: This module creates the secret in GCP Secret Manager
author:
    - Prashant Pokhriyal (@https://github.com/Devopcasting)
options:
    project_id:
        description: Project ID in GCP Console
        required: true
        type: str
    service_account_file:
        description: Service Account JSON key file
        required: true
        type: str
    secret_name:
        description: Name of the secret
        required: true
        type: str
    secret_file:
        description: Absoulte path of the secret value file
        required: false
        type: str
    state:
        description: State of the secret
        required: false
        type: str
        default: present
        choices: ['present', 'absent']
'''

from ansible.module_utils.basic import AnsibleModule
from google.cloud import secretmanager

def run_module():

    # define the arguments a user can pass to the module
    module_args = dict(
        project_id=dict(type='str', required=True),
        service_account_file=dict(type='str', required=True),
        secret_name=dict(type='str', required=True),
        secret_file=dict(type='str', required=False),
        state=dict(type='str', required=False, default='present')
    )

    # pass module_args to AnsibleModule
    module = AnsibleModule(argument_spec=module_args)

    # start
    # - check state is present or absent
    # - if present then check secret_file is given
    #


def main():
    run_module()

if __name__ == '__main__':
    main()