from . import AWSObject, AWSProperty
from .validators import boolean
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class CloudwatchAlarmAction(AWSProperty):
    props = {
        'AlarmName': (str, True),
        'RoleArn': (str, True),
        'StateReason': (str, True),
        'StateValue': (str, True),
    }


class CloudwatchMetricAction(AWSProperty):
    props = {
        'MetricName': (str, True),
        'MetricNamespace': (str, True),
        'MetricTimestamp': (str, False),
        'MetricUnit': (str, True),
        'MetricValue': (str, True),
        'RoleArn': (str, True),
    }


class DynamoDBAction(AWSProperty):
    props = {
        'HashKeyField': (str, True),
        'HashKeyType': (str, False),
        'HashKeyValue': (str, True),
        'PayloadField': (str, False),
        'RangeKeyField': (str, False),
        'RangeKeyType': (str, False),
        'RangeKeyValue': (str, False),
        'RoleArn': (str, True),
        'TableName': (str, True),
    }


class PutItemInput(AWSProperty):
    props = {
        'TableName': (str, True),
    }


class DynamoDBv2Action(AWSProperty):
    props = {
        'PutItem': (PutItemInput, False),
        'RoleArn': (str, False),
    }


class ElasticsearchAction(AWSProperty):
    props = {
        'Endpoint': (str, True),
        'Id': (str, True),
        'Index': (str, True),
        'RoleArn': (str, True),
        'Type': (str, True),
    }


class FirehoseAction(AWSProperty):
    props = {
        'DeliveryStreamName': (str, True),
        'RoleArn': (str, True),
        'Separator': (str, False),
    }


class KinesisAction(AWSProperty):
    props = {
        'PartitionKey': (str, False),
        'RoleArn': (str, True),
        'StreamName': (str, True),
    }


class LambdaAction(AWSProperty):
    props = {
        'FunctionArn': (str, True),
    }


class RepublishAction(AWSProperty):
    props = {
        'RoleArn': (str, True),
        'Topic': (str, True),
    }


class S3Action(AWSProperty):
    props = {
        'BucketName': (str, True),
        'Key': (str, True),
        'RoleArn': (str, True),
    }


class SnsAction(AWSProperty):
    props = {
        'MessageFormat': (str, False),
        'RoleArn': (str, True),
        'TargetArn': (str, True),
    }


class SqsAction(AWSProperty):
    props = {
        'QueueUrl': (str, True),
        'RoleArn': (str, True),
        'UseBase64': (str, False),
    }


class Action(AWSProperty):
    props = {
        'CloudwatchAlarm': (CloudwatchAlarmAction, False),
        'CloudwatchMetric': (CloudwatchMetricAction, False),
        'DynamoDB': (DynamoDBAction, False),
        'DynamoDBv2': (DynamoDBv2Action, False),
        'Elasticsearch': (ElasticsearchAction, False),
        'Firehose': (FirehoseAction, False),
        'Kinesis': (KinesisAction, False),
        'Lambda': (LambdaAction, False),
        'Republish': (RepublishAction, False),
        'S3': (S3Action, False),
        'Sns': (SnsAction, False),
        'Sqs': (SqsAction, False),
    }


class TopicRulePayload(AWSProperty):
    props = {
        'Actions': ([Action], True),
        'AwsIotSqlVersion': (str, False),
        'Description': (str, False),
        'RuleDisabled': (boolean, True),
        'Sql': (str, True),
    }


class TopicRule(AWSObject):
    resource_type = "AWS::IoT::TopicRule"

    props = {
        'RuleName': (str, False),
        'TopicRulePayload': (TopicRulePayload, True),
    }


class ThingPrincipalAttachment(AWSObject):
    resource_type = "AWS::IoT::ThingPrincipalAttachment"

    props = {
        'Principal': (str, True),
        'ThingName': (str, True),
    }


class Thing(AWSObject):
    resource_type = "AWS::IoT::Thing"

    props = {
        'AttributePayload': (dict, False),
        'ThingName': (str, False),
    }


class PolicyPrincipalAttachment(AWSObject):
    resource_type = "AWS::IoT::PolicyPrincipalAttachment"

    props = {
        'PolicyName': (str, True),
        'Principal': (str, True),
    }


class Policy(AWSObject):
    resource_type = "AWS::IoT::Policy"

    props = {
        'PolicyDocument': (policytypes, True),
        'PolicyName': (str, False),
    }


class Certificate(AWSObject):
    resource_type = "AWS::IoT::Certificate"

    props = {
        'CertificateSigningRequest': (str, True),
        'Status': (str, True),
    }
