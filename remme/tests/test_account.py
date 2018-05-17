# Copyright 2018 REMME
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
# ------------------------------------------------------------------------
import logging
import inspect
from remme.protos.account_pb2 import AccountMethod, GenesisStatus, Account
from remme.shared.logging import test
from remme.tests.test_helper import HelperTestCase
from remme.account.client import AccountClient
from remme.account.handler import ZERO_ADDRESS, AccountHandler

LOGGER = logging.getLogger(__name__)


class AccountTestCase(HelperTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AccountHandler)

    @test
    def test_genesis_empty(self):
        TOTAL_SUPPLY = 10000
        zero_address = self.handler.make_address(ZERO_ADDRESS)

        self.send_transaction(AccountMethod.GENESIS, AccountClient.get_genesis_payload(TOTAL_SUPPLY),
                              [zero_address, self.account_address1])

        self.expect_get({self.account_address1: None})
        self.expect_get({zero_address: None})

        genesis_status = GenesisStatus()
        genesis_status.status = True
        account = Account()
        account.balance = TOTAL_SUPPLY

        self.expect_set({
            self.account_address1: account,
            zero_address: genesis_status
        })

        self.expect_ok()

    @test
    def test_genesis_fail(self):
        TOTAL_SUPPLY = 10000
        zero_address = self.handler.make_address(ZERO_ADDRESS)

        self.send_transaction(AccountMethod.GENESIS, AccountClient.get_genesis_payload(TOTAL_SUPPLY),
                              [zero_address, self.account_address1])

        genesis_status = GenesisStatus()
        genesis_status.status = True

        self.expect_get({self.account_address1: None})
        self.expect_get({zero_address: genesis_status})

        self.expect_invalid_transaction()

    @test
    def test_transfer_success(self):
        ACCOUNT_AMOUNT1 = 1000
        ACCOUNT_AMOUNT2 = 500
        TRANSFER_VALUE = ACCOUNT_AMOUNT1
        self.send_transaction(AccountMethod.TRANSFER,
                              AccountClient.get_transfer_payload(self.account_address2, TRANSFER_VALUE),
                              [self.account_address1, self.account_address2])
        self.expect_get({self.account_address1: AccountClient.get_account_model(ACCOUNT_AMOUNT1)})
        self.expect_get({self.account_address2: AccountClient.get_account_model(ACCOUNT_AMOUNT2)})

        self.expect_set({
            self.account_address1: AccountClient.get_account_model(ACCOUNT_AMOUNT1-TRANSFER_VALUE),
            self.account_address2: AccountClient.get_account_model(ACCOUNT_AMOUNT2+TRANSFER_VALUE)
        })

        self.expect_ok()

    @test
    def test_transfer_fail_no_balance(self):
        ACCOUNT_AMOUNT1 = 200
        ACCOUNT_AMOUNT2 = 500
        TRANSFER_VALUE = ACCOUNT_AMOUNT1 + 1
        self.send_transaction(AccountMethod.TRANSFER,
                              AccountClient.get_transfer_payload(self.account_address2, TRANSFER_VALUE),
                              [self.account_address1, self.account_address2])
        self.expect_get({self.account_address1: AccountClient.get_account_model(ACCOUNT_AMOUNT1)})
        self.expect_get({self.account_address2: AccountClient.get_account_model(ACCOUNT_AMOUNT2)})

        self.expect_invalid_transaction()

    @test
    def test_transfer_fail_no_state_address1(self):
        ACCOUNT_AMOUNT2 = 500
        TRANSFER_VALUE = 200
        self.send_transaction(AccountMethod.TRANSFER,
                              AccountClient.get_transfer_payload(self.account_address2, TRANSFER_VALUE),
                              [self.account_address1, self.account_address2])
        self.expect_get({self.account_address1: None})
        self.expect_get({self.account_address2: AccountClient.get_account_model(ACCOUNT_AMOUNT2)})

        self.expect_invalid_transaction()

    @test
    def test_transfer_fail_no_state_address2(self):
        ACCOUNT_AMOUNT1 = 500
        TRANSFER_VALUE = 200
        self.send_transaction(AccountMethod.TRANSFER,
                              AccountClient.get_transfer_payload(self.account_address2, TRANSFER_VALUE),
                              [self.account_address1, self.account_address2])
        self.expect_get({self.account_address1: AccountClient.get_account_model(ACCOUNT_AMOUNT1)})
        self.expect_get({self.account_address2: None})

        self.expect_set({
            self.account_address1: AccountClient.get_account_model(ACCOUNT_AMOUNT1 - TRANSFER_VALUE),
            self.account_address2: AccountClient.get_account_model(0 + TRANSFER_VALUE)
        })

        self.expect_ok()

    @test
    def test_transfer_fail_to_oneself(self):
        ACCOUNT_AMOUNT1 = 500
        TRANSFER_VALUE = 200
        self.send_transaction(AccountMethod.TRANSFER,
                              AccountClient.get_transfer_payload(self.account_address1, TRANSFER_VALUE),
                              [self.account_address1, self.account_address2])
        self.expect_get({self.account_address1: AccountClient.get_account_model(ACCOUNT_AMOUNT1)})

        self.expect_invalid_transaction()

    @test
    def test_transfer_fail_to_zeroaddress(self):
        ACCOUNT_AMOUNT1 = 500
        TRANSFER_VALUE = 200
        self.send_transaction(AccountMethod.TRANSFER,
                              AccountClient.get_transfer_payload(self.handler.make_address(ZERO_ADDRESS), TRANSFER_VALUE),
                              [self.account_address1, self.account_address2])
        self.expect_get({self.account_address1: AccountClient.get_account_model(ACCOUNT_AMOUNT1)})

        self.expect_invalid_transaction()