class Block {
    constructor(index, transactions, previousHash) {
        this.index = index;
        this.timestamp = new Date().toLocaleString();
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
        return new Block(0, "Genesis Block", "0");
    }

    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock(transactions) {
        const prevBlock = this.getLatestBlock();
        const newBlock = new Block(prevBlock.index + 1, transactions, prevBlock.hash);
        this.chain.push(newBlock);
        this.displayBlockchain();
    }

    displayBlockchain() {
        const blockchainDiv = document.getElementById("blockchain");
        blockchainDiv.innerHTML = "";
        this.chain.forEach(block => {
            const blockDiv = document.createElement("div");
            blockDiv.className = "block";
            blockDiv.innerHTML = `
                <p><strong>Index:</strong> ${block.index}</p>
                <p><strong>Timestamp:</strong> ${block.timestamp}</p>
                <p><strong>Transactions:</strong> ${block.transactions}</p>
                <p><strong>Previous Hash:</strong> ${block.previousHash}</p>
                <p><strong>Hash:</strong> ${block.hash}</p>
            `;
            blockchainDiv.appendChild(blockDiv);
        });
    }
}

const myBlockchain = new Blockchain();
document.getElementById("addBlock").addEventListener("click", () => {
    const transactions = prompt("Enter transactions (comma-separated):").split(",");
    myBlockchain.addBlock(transactions);
});
