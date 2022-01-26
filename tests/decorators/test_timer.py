#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.
import unittest

from azure.functions import DataType
from azure.functions.decorators.core import BindingDirection
from azure.functions.decorators.timer import TimerTrigger


class TestTimer(unittest.TestCase):
    def test_timer_trigger_valid_creation(self):
        trigger = TimerTrigger(name="req",
                               schedule="dummy_schedule",
                               data_type=DataType.UNDEFINED)

        self.assertEqual(trigger.get_binding_name(), "timerTrigger")
        self.assertEqual(trigger.get_dict_repr(), {
            "type": "timerTrigger",
            "direction": BindingDirection.IN.value,
            "name": "req",
            "dataType": DataType.UNDEFINED.value,
            "schedule": "dummy_schedule",
            "runOnStartup": None,
            "useMonitor": None
        })