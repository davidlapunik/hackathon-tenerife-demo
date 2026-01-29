
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class ERC1967Factory(Contract):
    """
    [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#7)
    """
    _abi = {b'0\x11d%': {'inputs': [], 'name': 'DeploymentFailed', 'type': 'error'}, b'/cH6': {'inputs': [], 'name': 'SaltDoesNotStartWithCaller', 'type': 'error'}, b'\x82\xb4)\x00': {'inputs': [], 'name': 'Unauthorized', 'type': 'error'}, b'U)\x9bI': {'inputs': [], 'name': 'UpgradeFailed', 'type': 'error'}, b'~dMyB/\x17\xc0\x1eH\x94\xb5\xf4\xf5\x88\xd31\xeb\xfa(e=B\xae\x83-\xc5\x9e8\xc9y\x8f': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'AdminChanged', 'type': 'event'}, b'\xc9Y5\xa6m\x15\xe0\xda^A*\xca\n\xd2z\xe8\x91\xd2\x0b/\xb9\x1c\xf3\x99Kj;\xf2\xb8\x17\x80\x82': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'Deployed', 'type': 'event'}, b"]a\x1f1\x86\x80\xd0\x05\x98\xbbs]a\xba\xcf\x0cQLkP\xe1\xe5\xad0\x04\nM\xf2\xb1'\x91\xc7": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, b'*\xbb\xef\x15': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'name': 'adminOf', 'outputs': [{'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1a\xcf\xd0*': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'changeAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'T^|a': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'deploy', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'C\x14\xf1 ': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'deployAndCall', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'7)\xf9"': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'deployDeterministic', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'\xa9{\x90\xd5': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'deployDeterministicAndCall', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'\xdbLT^': {'inputs': [], 'name': 'initCodeHash', 'outputs': [{'internalType': 'bytes32', 'name': 'result', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'T\x14\xdf\xf0': {'inputs': [{'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'predictDeterministicAddress', 'outputs': [{'internalType': 'address', 'name': 'predicted', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x99\xa8\x8e\xc4': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'upgrade', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\x96#`\x9d': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'upgradeAndCall', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080604052348015600e575f5ffd5b506109ab8061001c5f395ff3fe608060405260043610610090575f3560e01c8063545e7c6111610058578063545e7c61146101945780639623609d146101c457806399a88ec4146101e0578063a97b90d5146101fc578063db4c545e1461022c57610090565b80631acfd02a146100945780632abbef15146100bc5780633729f922146100f85780634314f120146101285780635414dff014610158575b5f5ffd5b34801561009f575f5ffd5b506100ba60048036038101906100b591906106b8565b610256565b005b3480156100c7575f5ffd5b506100e260048036038101906100dd91906106f6565b61029e565b6040516100ef9190610730565b60405180910390f35b610112600480360381019061010d919061077c565b6102ab565b60405161011f9190610730565b60405180910390f35b610142600480360381019061013d919061082d565b6102c8565b60405161014f9190610730565b60405180910390f35b348015610163575f5ffd5b5061017e6004803603810190610179919061089e565b6102e3565b60405161018b9190610730565b60405180910390f35b6101ae60048036038101906101a991906106b8565b610312565b6040516101bb9190610730565b60405180910390f35b6101de60048036038101906101d9919061082d565b61032d565b005b6101fa60048036038101906101f591906106b8565b6103ce565b005b610216600480360381019061021191906108c9565b6103e4565b6040516102239190610730565b60405180910390f35b348015610237575f5ffd5b5061024061041c565b60405161024d919061095c565b60405180910390f35b338260601b541461026e576382b429005f526004601cfd5b808260601b5580827f7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f5f5fa35050565b5f8160601b549050919050565b5f6102bf8484846102ba610435565b6103e4565b90509392505050565b5f6102d985855f5f1b5f878761043e565b9050949350505050565b5f5f6102ed61041c565b905060ff5f53806035523060601b6001528260155260555f2091505f60355250919050565b5f6103258383610320610435565b6102c8565b905092915050565b338460601b5414610345576382b429005f526004601cfd5b6040518381527f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc6020820152818360408301375f5f836040018334895af16103a1573d610399576355299b495f526004601cfd5b3d5f5f3e3d5ffd5b83857f5d611f318680d00598bb735d61bacf0c514c6b50e1e5ad30040a4df2b12791c75f5fa35050505050565b6103e082826103db610435565b61032d565b5050565b5f8360601c33148460601c151761040257632f6348365f526004601cfd5b6104118686866001878761043e565b905095945050505050565b5f5f610426610511565b90506088601382012091505090565b365f5f90509091565b5f5f610448610511565b9050845f811461046257866088601384015ff5925061046d565b6088601383015ff092505b50816104805763301164255f526004601cfd5b8781527f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc6020820152828460408301375f5f846040018334865af16104d9573d6104d15763301164255f526004601cfd5b3d5f5f3e3d5ffd5b868260601b558688837fc95935a66d15e0da5e412aca0ad27ae891d20b2fb91cf3994b6a3bf2b81780825f5fa4509695505050505050565b5f60405190503060701c5f81146105bc57666052573d6000fd607b8301527f3d356020355560408036111560525736038060403d373d3d355af43d6000803e60748301527f3735a920a3ca505d382bbc545af43d6000803e6052573d6000fd5b3d6000f35b60548301527f14605757363d3d37363d7f360894a13ba1a3210667c828492db98dca3e2076cc60348301523060148301526c607f3d8160093d39f33d3d33738252610652565b66604c573d6000fd60758301527f3d3560203555604080361115604c5736038060403d373d3d355af43d6000803e606e8301527f3735a920a3ca505d382bbc545af43d6000803e604c573d6000fd5b3d6000f35b604e8301527f14605157363d3d37363d7f360894a13ba1a3210667c828492db98dca3e2076cc602e83015230600e8301526c60793d8160093d39f33d3d336d82525b5090565b5f5ffd5b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6106878261065e565b9050919050565b6106978161067d565b81146106a1575f5ffd5b50565b5f813590506106b28161068e565b92915050565b5f5f604083850312156106ce576106cd610656565b5b5f6106db858286016106a4565b92505060206106ec858286016106a4565b9150509250929050565b5f6020828403121561070b5761070a610656565b5b5f610718848285016106a4565b91505092915050565b61072a8161067d565b82525050565b5f6020820190506107435f830184610721565b92915050565b5f819050919050565b61075b81610749565b8114610765575f5ffd5b50565b5f8135905061077681610752565b92915050565b5f5f5f6060848603121561079357610792610656565b5b5f6107a0868287016106a4565b93505060206107b1868287016106a4565b92505060406107c286828701610768565b9150509250925092565b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f8401126107ed576107ec6107cc565b5b8235905067ffffffffffffffff81111561080a576108096107d0565b5b602083019150836001820283011115610826576108256107d4565b5b9250929050565b5f5f5f5f6060858703121561084557610844610656565b5b5f610852878288016106a4565b9450506020610863878288016106a4565b935050604085013567ffffffffffffffff8111156108845761088361065a565b5b610890878288016107d8565b925092505092959194509250565b5f602082840312156108b3576108b2610656565b5b5f6108c084828501610768565b91505092915050565b5f5f5f5f5f608086880312156108e2576108e1610656565b5b5f6108ef888289016106a4565b9550506020610900888289016106a4565b945050604061091188828901610768565b935050606086013567ffffffffffffffff8111156109325761093161065a565b5b61093e888289016107d8565b92509250509295509295909350565b61095681610749565b82525050565b5f60208201905061096f5f83018461094d565b9291505056fea26469706673582212205b692c3f9b7b8fd51920f3e8c1d1824ca7097c09c821bc86290493098825b82e64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC1967Factory:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC1967Factory]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC1967Factory, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC1967Factory]]:
        return cls._deploy(request_type, [], return_tx, ERC1967Factory, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class Unauthorized(TransactionRevertedError):
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#13)
        """
        _abi = {'inputs': [], 'name': 'Unauthorized', 'type': 'error'}
        original_name = 'Unauthorized'
        selector = bytes4(b'\x82\xb4)\x00')



    @dataclasses.dataclass
    class DeploymentFailed(TransactionRevertedError):
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#16)
        """
        _abi = {'inputs': [], 'name': 'DeploymentFailed', 'type': 'error'}
        original_name = 'DeploymentFailed'
        selector = bytes4(b'0\x11d%')



    @dataclasses.dataclass
    class UpgradeFailed(TransactionRevertedError):
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#19)
        """
        _abi = {'inputs': [], 'name': 'UpgradeFailed', 'type': 'error'}
        original_name = 'UpgradeFailed'
        selector = bytes4(b'U)\x9bI')



    @dataclasses.dataclass
    class SaltDoesNotStartWithCaller(TransactionRevertedError):
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#22)
        """
        _abi = {'inputs': [], 'name': 'SaltDoesNotStartWithCaller', 'type': 'error'}
        original_name = 'SaltDoesNotStartWithCaller'
        selector = bytes4(b'/cH6')



    @dataclasses.dataclass
    class AdminChanged:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#41)

        Attributes:
            proxy (Address): indexed address
            admin (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'AdminChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'AdminChanged'
        selector = bytes32(b'~dMyB/\x17\xc0\x1eH\x94\xb5\xf4\xf5\x88\xd31\xeb\xfa(e=B\xae\x83-\xc5\x9e8\xc9y\x8f')

        proxy: Address
        admin: Address


    @dataclasses.dataclass
    class Upgraded:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#44)

        Attributes:
            proxy (Address): indexed address
            implementation (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'Upgraded'
        selector = bytes32(b"]a\x1f1\x86\x80\xd0\x05\x98\xbbs]a\xba\xcf\x0cQLkP\xe1\xe5\xad0\x04\nM\xf2\xb1'\x91\xc7")

        proxy: Address
        implementation: Address


    @dataclasses.dataclass
    class Deployed:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#47)

        Attributes:
            proxy (Address): indexed address
            implementation (Address): indexed address
            admin (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'Deployed', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'Deployed'
        selector = bytes32(b'\xc9Y5\xa6m\x15\xe0\xda^A*\xca\n\xd2z\xe8\x91\xd2\x0b/\xb9\x1c\xf3\x99Kj;\xf2\xb8\x17\x80\x82')

        proxy: Address
        implementation: Address
        admin: Address


    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        return self._execute(self.chain, request_type, "2abbef15", [proxy], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        return self._execute(self.chain, request_type, "1acfd02a", [proxy, admin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        return self._execute(self.chain, request_type, "99a88ec4", [proxy, implementation], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        return self._execute(self.chain, request_type, "9623609d", [proxy, implementation, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "545e7c61", [implementation, admin], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "4314f120", [implementation, admin, data], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "3729f922", [implementation, admin, salt], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "a97b90d5", [implementation, admin, salt, data], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        return self._execute(self.chain, request_type, "5414dff0", [salt], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///home/david/Work/hackathon/wake/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        return self._execute(self.chain, request_type, "db4c545e", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC1967Factory.adminOf.selector = bytes4(b'*\xbb\xef\x15')
ERC1967Factory.changeAdmin.selector = bytes4(b'\x1a\xcf\xd0*')
ERC1967Factory.upgrade.selector = bytes4(b'\x99\xa8\x8e\xc4')
ERC1967Factory.upgradeAndCall.selector = bytes4(b'\x96#`\x9d')
ERC1967Factory.deploy_.selector = bytes4(b'T^|a')
ERC1967Factory.deployAndCall.selector = bytes4(b'C\x14\xf1 ')
ERC1967Factory.deployDeterministic.selector = bytes4(b'7)\xf9"')
ERC1967Factory.deployDeterministicAndCall.selector = bytes4(b'\xa9{\x90\xd5')
ERC1967Factory.predictDeterministicAddress.selector = bytes4(b'T\x14\xdf\xf0')
ERC1967Factory.initCodeHash.selector = bytes4(b'\xdbLT^')
