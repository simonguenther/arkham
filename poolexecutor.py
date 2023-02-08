import asyncio
from concurrent.futures import ProcessPoolExecutor
import aiohttp
import json

def process_page(response):
    resp = json.loads(response)
    _hash = resp.get("result",[])[0]
    print(_hash["transactionhash"])

async def fetch_page(url, session):
    async with asyncio.Semaphore(1):
        print("tick")
        async with session.get(url, timeout=15) as res:
            return await res.text()

async def process(session, pool, hash, sender) -> None:
    url = f"http://116.202.100.54/api/Ethereum/DeconstructEthTransaction?apiKey=2pTDE74oR0zw7h32xZuKf2Rm7taTIl&transactionHash={hash}&address={sender}"
    response = await fetch_page(url, session)
    return await asyncio.wrap_future(pool.submit(process_page, response))

async def run(txs) -> None:
    pool = ProcessPoolExecutor()
    connector = aiohttp.TCPConnector(limit=1)
    async with aiohttp.ClientSession(connector=connector) as session:
        coros = (process(session, pool, hash, txs[hash]) for hash in txs)
        return await asyncio.gather(*coros)

if __name__ == "__main__":
    txs = {}
    txs["0xf10eb797c95a6829c283b77edd4c6db046431ed38d69ddd0850bd377035ba19a"] =  "0x9d96b0561be0440ebe93e79fe06a23bbe8270f90"
    txs["0x3d35b930b9a89868dfa91797592639320a9d01d31f4c9c0ee7a9726ad50f5932"] =  "0x39a9b4866a36dcd7ee6f6154c731950783425c6d"
    txs["0x82420ec0c8550b3d2676621a731a32b777b7baf602afb3ec82b9683b69c62937"] =  "0xe291cc3e5b9e0c9b37c9fbdd549abf3b5c0ad342"
    txs["0xea06241197165023252c4e21f038f034cc86254894bb886b13f05790ada34dd9"] =  "0xc084bede87eb4337e7176578c4e2096797063a67"
    txs["0x44bff27c44f04d474b242d83d4a2a33ee5f001c78d2cd55f0cf95bf6e7f13bb2"] =  "0xa802c006663e30dee700c022adcf18c7a2b99240"
    txs["0xaa93177f70766ed7b19b4cf1f18b07ed03a0c98d38ca1afa1bcdce847125cfdb"] =  "0xf4e4c44d9636cf0727e087ec3a8ea06aa98a8529"
    txs["0xff967860503ece63fb80761a5b4e613f14fa5d721f9db66138a4a5f028dd05ba"] =  "0x1bb22b6e8e93840930bbbc7c1d00490678bde5ba"
    txs["0x2a1ad5adcee18c3db4dcf35dde0b782d931c2db64abecfad872a92d14f58e7be"] =  "0x34f236d64712b8dda2c85e91730d8d628c113db9"
    txs["0x711cf6d442d8bf80f77355040870bc1cc0e1c0eb5a069d8ebd7975258eeff633"] =  "0x83828ace37b5d0ebb0786d49f778df0698e827b7"
    
    asyncio.get_event_loop().run_until_complete(run(txs))