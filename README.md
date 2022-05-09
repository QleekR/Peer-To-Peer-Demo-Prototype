# A P2P architecture to study if its possible to have Liquidity pools as seperate peers for a P2P CEX

# Prerequisites:
- Python3.0+ [I am using Python-3.7.5]
- Basic Networking Knowledge

# How to run?
- Make sure you pip install the packages from **Client.py** & **LP.py** if needed.
- Run the LP.py first, as it presents the peer which will act as a liquidity pool for the exchange.
- Then, run Client.py and do as program prompts.
- **Wallet.json** represents hypothetical wallet assets for client & **LP.json** represents hypothetical assets for LiquidityPool(LP) peer.

# TODO:

- So the existing prototype I have built lacks 2 things:

**1. financial asset handling**
- basically all the btc and usd value in the code are just json objects in a json file since everything is hypothetical in that prototype, which i dont think so applies for real world fintech softwares.

- we need to test transactions with real cryptocurrency wallets and payment gateways rather than using hypothetical json files as wallets and gateways.

**2. Lack of Security**
- lack of security, till now i have hard coded ip and port for client peer to connect to the "liquidity providing"(LP) peer for exchange, we must figure out a way to securely store ip and port of every LP peer on every client peer.
- The benefit of such will be that we wont need a central server for matchmaking every client peer to every LP peer.

**3. LP--Client Match Algorithm**
- An Algorithm on client side code to determine which LP it will connect to perform an exchange.



