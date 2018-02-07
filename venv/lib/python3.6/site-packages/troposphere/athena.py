# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class NamedQuery(AWSObject):
    resource_type = "AWS::Athena::NamedQuery"

    props = {
        'Database': (str, True),
        'Description': (str, False),
        'Name': (str, False),
        'QueryString': (str, True),
    }
