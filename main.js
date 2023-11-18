// main.js

// Define quantum gates
const quantumGates = ['H', 'X', 'Y', 'Z', 'S', 'T', 'U', 'CNOT', 'SWAP', 'CCNOT', 'CSWAP'];

// Define quantum algorithms
const quantumAlgorithms = ['Deutsch-Jozsa', 'Grover', 'Shor', 'Simon', 'Quantum Fourier Transform'];

// Function to create a list item for each gate
function createGateList() {
    const gateList = document.getElementById('gate-list');
    quantumGates.forEach(gate => {
        const listItem = document.createElement('div');
        listItem.textContent = gate;
        listItem.classList.add('gate');
        gateList.appendChild(listItem);
    });
}

// Function to create a list item for each algorithm
function createAlgorithmList() {
    const algorithmList = document.getElementById('algorithm-list');
    quantumAlgorithms.forEach(algorithm => {
        const listItem = document.createElement('div');
        listItem.textContent = algorithm;
        listItem.classList.add('algorithm');
        algorithmList.appendChild(listItem);
    });
}

// Function to draw the quantum circuit
function drawQuantumCircuit() {
    const canvas = document.getElementById('circuit-canvas');
    const ctx = canvas.getContext('2d');
    // Draw your quantum circuit here
    // This is just a placeholder
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(canvas.width, canvas.height);
    ctx.stroke();
}

// Call the functions when the page loads
window.onload = function() {
    createGateList();
    createAlgorithmList();
    drawQuantumCircuit();
};
