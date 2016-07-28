#!/usr/bin/python
DOCUMENTATION = '''
---
module: k8s_service
short_description:
description:
version_added: "2.2"
author: "Jeremiah Stuever, @jstuever"
notes:
requirements:
options:
    name:
        required: true
        description:
            - Name of the service.
    state:
        required: false
        default: "present"
        choices: [ present, absent ]
        description:
            -  Whether the service should exist or not.
    api_version:
        required: false
        default: "v1"
        choices: [ v1 ]
        descriptoin:
            - The API version to use.
    api_endpoint:
        required: false
        default: None
        description:
            - The api endpoint to use.
    username:
        required: false
        default: None
        description:
            - The username to use to authenticate to the api_endpoint.
    password:
        required: false
        default: None
        description:
            - The password to use to authenticate to the api_endpoint.
    client_cert:
        required: false
        default: None
        description:
            - The client certificate to use to authenticate to the api_endpoint.
    client_key:
        required: false
        default: None
        description:
            - The client key to use to authenticate to the api_endpoint.
    token:
        required: false
        default: None
        description:
            - The token to use to authenticate to the api_endpoint.
    certificate_authority:
        required: false
        default: None
        description:
            - The certificate authority for the server certificate.
    insecure_skip_tls_verify:
        required: false
        default: "no"
        choices: [ "yes", "no" ]
            - Whether to skip tls verification.
    labels:
        required: false
        default: None
        description:
            - A dictionary of the labels to apply to this service.
    annotations:
        required: false
        default: None
        description:
            - A dictionary of the annotations to apply to this service.
'''
EXAMPLES = '''
'''
from lib_openshift import Wrapper, WrapperException

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            namespace=dict(required=True, type='str'),
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            api_version=dict(default='v1', choices=['v1'], type='str'),
            api_endpoint=dict(default=None, type='str'),
            username=dict(default=None, type='str'),
            password=dict(default=None, type='str'),
            client_cert=dict(default=None, type='str'),
            client_key=dict(default=None, type='str'),
            token=dict(default=None, type='str'),
            certificate_authority=dict(default=None, type='str'),
            insecure_skip_tls_verify=dict(default='no', type='bool'),
            labels=dict(default=None, type='dict'),
            annotations=dict(default=None, type='dict'),
            ports=dict(default=None, type='list'),
            selector=dict(default=None, type='dict'),
            type=dict(default=None, type='str'),
        )
    )
    wrapper = Wrapper(
        api_endpoint=module.params.get('api_endpoint'),
        username=module.params.get('username'),
        password=module.params.get('password'),
        client_cert=module.params.get('client_cert'),
        client_key=module.params.get('client_key'),
        token=module.params.get('token'),
        certificate_authority=module.params.get('certificate_authority'),
        insecure_skip_tls_verify=module.params.get('insecure_skip_tls_verify'),
    )
    try:
        result = wrapper.service(
            name=module.params.get('name'),
            namespace=module.params.get('namespace'),
            api_version=module.params.get('api_version'),
            labels=module.params.get('labels'),
            annotations=module.params.get('annotations'),
            state=module.params.get('state'),
            ports=module.params.get('ports'),
            selector=module.params.get('selector'),
            type=module.params.get('type')
        )
    except WrapperException as err:
        module.fail_json(msg=err)

    module.exit_json(**result)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
