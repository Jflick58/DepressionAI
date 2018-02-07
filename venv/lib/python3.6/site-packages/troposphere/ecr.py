from . import AWSObject, AWSProperty
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class LifecyclePolicy(AWSProperty):
    props = {
        'LifecyclePolicyText': (str, False),
        'RegistryId': (str, False),
    }


class Repository(AWSObject):
    resource_type = "AWS::ECR::Repository"

    props = {
        'LifecyclePolicy': (LifecyclePolicy, False),
        'RepositoryName': (str, False),
        'RepositoryPolicyText': (policytypes, False),
    }
