##############################################################################
# Copyright (c) 2017 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

from __future__ import print_function
from __future__ import absolute_import

import logging

from yardstick.benchmark.scenarios import base
import yardstick.common.openstack_utils as op_utils

LOG = logging.getLogger(__name__)


class FloatingIpAssociate(base.Scenario):
    """Create an OpenStack floating ip associate"""

    __scenario_type__ = "FloatingIpAssociate"

    def __init__(self, scenario_cfg, context_cfg):
        self.scenario_cfg = scenario_cfg
        self.context_cfg = context_cfg
        self.options = self.scenario_cfg['options']

        self.ip_addr = self.options.get("floating_ip_addr", None)
        self.server_id = self.options.get("server_id", None)

        self.nova_client = op_utils.get_nova_client()

        self.setup_done = False

    def setup(self):
        """scenario setup"""

        self.setup_done = True

    def run(self, result):
        """execute the test"""

        if not self.setup_done:
            self.setup()

        status = op_utils.add_floating_ip(self.nova_client,
                                          server_id=self.server_id,
                                          floatingip_addr=self.ip_addr)
        if status:
            result.update({"add_floating_ip": 1})
            LOG.info("Adding floating ip successful!")
        else:
            result.update({"add_floating_ip": 0})
            LOG.error("Adding floating ip failed!")
