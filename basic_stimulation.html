<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain Explorer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Blockchain Explorer</h1>
        <button id="addBlock">Add Block</button>
        <div class="blockchain" id="blockchain"></div>
    </div>

    <script>
        class Block {
            constructor(index, transactions, previousHash = "0") {
                this.index = index;
                this.timestamp = new Date().toISOString();
                this.transactions = transactions;
                this.previousHash = previousHash;
                this.nonce = 0;
                this.hash = this.calculateHash();
            }

            calculateHash() {
                return btoa(this.index + this.timestamp + JSON.stringify(this.transactions) + this.previousHash + this.nonce);
            }
        }

        class Blockchain {
            constructor() {
                this.chain = [this.createGenesisBlock()];
            }

            createGenesisBlock() {
                return new Block(0, ["Genesis Block"], "0");
            }

            getLatestBlock() {
                return this.chain[this.chain.length - 1];
            }

            addBlock(transactions) {
                const previousBlock = this.getLatestBlock();
                const newBlock = new Block(previousBlock.index + 1, transactions, previousBlock.hash);
                this.chain.push(newBlock);
                this.displayBlockchain();
            }

            displayBlockchain() {
                const blockchainDiv = document.getElementById("blockchain");
                blockchainDiv.innerHTML = "";
                this.chain.forEach(block => {
                    const blockDiv = document.createElement("div");
                    blockDiv.classList.add("block");
                    blockDiv.innerHTML = `
                        <h3>Block #${block.index}</h3>
                        <p><strong>Timestamp:</strong> ${block.timestamp}</p>
                        <p><strong>Transactions:</strong> ${block.transactions.join(", ")}</p>
                        <p><strong>Previous Hash:</strong> ${block.previousHash}</p>
                        <p><strong>Hash:</strong> ${block.hash}</p>
                    `;
                    blockchainDiv.appendChild(blockDiv);
                });
            }
        }

        const myBlockchain = new Blockchain();
        document.getElementById("addBlock").addEventListener("click", () => {
            const transactions = prompt("Enter transactions (comma-separated):").split(",").map(t => t.trim());
            myBlockchain.addBlock(transactions);
        });
        myBlockchain.displayBlockchain();
    </script>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            text-align: center;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333;
        }

        #addBlock {
            background: #007BFF;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            margin: 20px 0;
            border-radius: 5px;
        }

        #addBlock:hover {
            background: #0056b3;
        }

        .blockchain {
            text-align: left;
            margin-top: 20px;
        }

        .block {
            background: #fff;
            padding: 15px;
            margin: 10px 0;
            border-left: 5px solid #007BFF;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }
    </style>
</body>
</html>
