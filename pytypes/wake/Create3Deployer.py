
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class Create3Deployer(Contract):
    """
    [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#6)
    """
    _abi = {b'S\xdeT\xb9': {'inputs': [], 'name': 'ErrorCreatingContract', 'type': 'error'}, b'\xbb\xd2\xfe\x87': {'inputs': [], 'name': 'ErrorCreatingProxy', 'type': 'error'}, b'\xcdC\xef\xa1': {'inputs': [], 'name': 'TargetAlreadyExists', 'type': 'error'}, b'\x7f\xdeV\xda': {'inputs': [{'internalType': 'bytes32', 'name': '_salt', 'type': 'bytes32'}], 'name': 'computeAddress', 'outputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xcd\xcbv\n': {'inputs': [{'internalType': 'bytes32', 'name': '_salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': '_creationCode', 'type': 'bytes'}], 'name': 'deploy', 'outputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x99\x95BR': {'inputs': [{'internalType': 'bytes32', 'name': '_salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': '_creationCode', 'type': 'bytes'}, {'internalType': 'uint256', 'name': '_value', 'type': 'uint256'}], 'name': 'deployWithValue', 'outputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080604052348015600e575f5ffd5b506108c28061001c5f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c80637fde56da146100435780639995425214610073578063cdcb760a146100a3575b5f5ffd5b61005d600480360381019061005891906103a8565b6100d3565b60405161006a9190610412565b60405180910390f35b61008d6004803603810190610088919061059a565b6100e4565b60405161009a9190610412565b60405180910390f35b6100bd60048036038101906100b89190610606565b6100f9565b6040516100ca9190610412565b60405180910390f35b5f6100dd8261010c565b9050919050565b5f6100f0848484610190565b90509392505050565b5f6101048383610346565b905092915050565b5f5f30837f21c35dbe1b344a2488cf3321d6ce542f8e9f305544ff09e4993a62319a497c1f5f1b60405160200161014593929190610719565b604051602081830303815290604052805190602001205f1c90508060405160200161017091906107f4565b604051602081830303815290604052805190602001205f1c915050919050565b5f5f6040518060400160405280601081526020017f67363d3d37363d34f03d5260086018f30000000000000000000000000000000081525090506101d38561010c565b91505f6101df8361035a565b14610216576040517fcd43efa100000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f858251602084015ff590505f73ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1603610287576040517fbbd2fe8700000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f8173ffffffffffffffffffffffffffffffffffffffff1685876040516102ae9190610876565b5f6040518083038185875af1925050503d805f81146102e8576040519150601f19603f3d011682016040523d82523d5f602084013e6102ed565b606091505b5050905080158061030557505f6103038561035a565b145b1561033c576040517f53de54b900000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5050509392505050565b5f61035283835f610190565b905092915050565b5f813b9050919050565b5f604051905090565b5f5ffd5b5f5ffd5b5f819050919050565b61038781610375565b8114610391575f5ffd5b50565b5f813590506103a28161037e565b92915050565b5f602082840312156103bd576103bc61036d565b5b5f6103ca84828501610394565b91505092915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6103fc826103d3565b9050919050565b61040c816103f2565b82525050565b5f6020820190506104255f830184610403565b92915050565b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b61047982610433565b810181811067ffffffffffffffff8211171561049857610497610443565b5b80604052505050565b5f6104aa610364565b90506104b68282610470565b919050565b5f67ffffffffffffffff8211156104d5576104d4610443565b5b6104de82610433565b9050602081019050919050565b828183375f83830152505050565b5f61050b610506846104bb565b6104a1565b9050828152602081018484840111156105275761052661042f565b5b6105328482856104eb565b509392505050565b5f82601f83011261054e5761054d61042b565b5b813561055e8482602086016104f9565b91505092915050565b5f819050919050565b61057981610567565b8114610583575f5ffd5b50565b5f8135905061059481610570565b92915050565b5f5f5f606084860312156105b1576105b061036d565b5b5f6105be86828701610394565b935050602084013567ffffffffffffffff8111156105df576105de610371565b5b6105eb8682870161053a565b92505060406105fc86828701610586565b9150509250925092565b5f5f6040838503121561061c5761061b61036d565b5b5f61062985828601610394565b925050602083013567ffffffffffffffff81111561064a57610649610371565b5b6106568582860161053a565b9150509250929050565b5f81905092915050565b7fff000000000000000000000000000000000000000000000000000000000000005f82015250565b5f61069e600183610660565b91506106a98261066a565b600182019050919050565b5f8160601b9050919050565b5f6106ca826106b4565b9050919050565b5f6106db826106c0565b9050919050565b6106f36106ee826103f2565b6106d1565b82525050565b5f819050919050565b61071361070e82610375565b6106f9565b82525050565b5f61072382610692565b915061072f82866106e2565b60148201915061073f8285610702565b60208201915061074f8284610702565b602082019150819050949350505050565b7fd6940000000000000000000000000000000000000000000000000000000000005f82015250565b5f610794600283610660565b915061079f82610760565b600282019050919050565b7f01000000000000000000000000000000000000000000000000000000000000005f82015250565b5f6107de600183610660565b91506107e9826107aa565b600182019050919050565b5f6107fe82610788565b915061080a82846106e2565b601482019150610819826107d2565b915081905092915050565b5f81519050919050565b5f81905092915050565b8281835e5f83830152505050565b5f61085082610824565b61085a818561082e565b935061086a818560208601610838565b80840191505092915050565b5f6108818284610846565b91508190509291505056fea2646970667358221220584459b31e25af5213e231e2131ae3e072d9b4c19ef4b3dfe567f3461f44bdc264736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Create3Deployer:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Create3Deployer]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Create3Deployer, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Create3Deployer]]:
        return cls._deploy(request_type, [], return_tx, Create3Deployer, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        return self._execute(self.chain, request_type, "cdcb760a", [_salt, _creationCode], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        return self._execute(self.chain, request_type, "99954252", [_salt, _creationCode, _value], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        return self._execute(self.chain, request_type, "7fde56da", [_salt], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

Create3Deployer.deploy_.selector = bytes4(b'\xcd\xcbv\n')
Create3Deployer.deployWithValue.selector = bytes4(b'\x99\x95BR')
Create3Deployer.computeAddress.selector = bytes4(b'\x7f\xdeV\xda')
