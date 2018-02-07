# Copyright (c) 2016, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty


class Trigger(AWSProperty):
    props = {
        'Branches': ([str], False),
        'CustomData': (str, False),
        'DestinationArn': (str, False),
        'Events': ([str], False),
        'Name': (str, False),
    }

    def validate(self):
        valid = [
            'all',
            'createReference',
            'deleteReference',
            'updateReference',
        ]
        events = self.properties.get('Events')
        if events and not isinstance(events, AWSHelperFn):
            if 'all' in events and len(events) != 1:
                raise ValueError('Trigger events: all must be used alone')
            else:
                for e in events:
                    if e not in valid and not isinstance(e, AWSHelperFn):
                        raise ValueError('Trigger: invalid event %s' % e)


class Repository(AWSObject):
    resource_type = "AWS::CodeCommit::Repository"

    props = {
        'RepositoryDescription': (str, False),
        'RepositoryName': (str, True),
        'Triggers': ([Trigger], False),
    }
