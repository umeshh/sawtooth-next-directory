# Copyright 2019 Contributors to Hyperledger Sawtooth
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
# -----------------------------------------------------------------------------
"""Test Propose Role Task Helper"""
# pylint: disable=no-member

import logging
import pytest

from rbac.common import protobuf
from rbac.common.crypto.keys import Key
from tests.rbac.common import helper


LOGGER = logging.getLogger(__name__)


@pytest.mark.role
@pytest.mark.library
def test_id():
    """Test get a random proposal id"""
    id1 = helper.role.task.propose.id()
    id2 = helper.role.task.propose.id()
    assert isinstance(id1, str)
    assert isinstance(id2, str)
    assert len(id1) == 24
    assert len(id2) == 24
    assert id1 != id2


@pytest.mark.role
@pytest.mark.library
def test_reason():
    """Test get a random reason"""
    reason1 = helper.role.task.propose.reason()
    reason2 = helper.role.task.propose.reason()
    assert isinstance(reason1, str)
    assert isinstance(reason2, str)
    assert len(reason1) > 4
    assert len(reason2) > 4
    assert reason1 != reason2


@pytest.mark.role
@pytest.mark.integration
def test_create():
    """A role owner creates an add role task proposal
    to add a task to their role"""
    proposal, role, role_owner, role_owner_key, task, task_owner, task_owner_key = (
        helper.role.task.propose.create()
    )
    assert isinstance(proposal, protobuf.proposal_state_pb2.Proposal)
    assert isinstance(role, protobuf.role_state_pb2.RoleAttributes)
    assert isinstance(task, protobuf.task_state_pb2.TaskAttributes)
    assert isinstance(role_owner, protobuf.user_state_pb2.User)
    assert isinstance(task_owner, protobuf.user_state_pb2.User)
    assert isinstance(role_owner_key, Key)
    assert isinstance(task_owner_key, Key)
    assert proposal.object_id == role.role_id
    assert proposal.related_id == task.task_id
