**2. src/vanik/blockchain/interactor.py (Core Blockchain Component):**
```python
"""
VANIK Blockchain Interactor Module
"""
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

class BlockchainManager:
    def __init__(self, network="testnet"):
        self.network = network
        self.w3 = self._connect_provider()
        self.contract = self._load_contract()
    
    def _connect_provider(self):
        if self.network == "mainnet":
            uri = os.getenv("MAINNET_PROVIDER_URI")
        else:
            uri = os.getenv("TESTNET_PROVIDER_URI")
            
        return Web3(Web3.HTTPProvider(uri))
    
    def _load_contract(self):
        contract_address = os.getenv("CONTRACT_ADDRESS")
        abi = self._get_contract_abi()
        return self.w3.eth.contract(address=contract_address, abi=abi)
    
    def _get_contract_abi(self):
        # Load from compiled contract JSON
        return [...]  # Mock ABI array
    
    def create_task(self, task_hash: str) -> str:
        """Store task hash on-chain"""
        tx_hash = self.contract.functions.createTask(
            task_hash
        ).buildTransaction({
            'chainId': self.w3.eth.chain_id,
            'gas': 200000,
            'nonce': self.w3.eth.getTransactionCount(
                self.w3.eth.defaultAccount
            ),
        })
        return tx_hash.hex()
