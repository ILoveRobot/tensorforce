# Copyright 2017 reinforce.io. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
Comment
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from tensorforce.preprocessing import Preprocessor


class Grayscale(Preprocessor):

    default_config = {
        'weights': [0.299, 0.587, 0.114]
    }

    config_args = [
        'weights'
    ]

    def process(self, state):
        """
        Turn 3D color state into grayscale, thereby removing the last dimension.
        :param state: state input
        :return: new_state
        """
        return (self.config.weights * state).sum(-1)

    def shape(self, original_shape):
        return list(original_shape[:-1])
