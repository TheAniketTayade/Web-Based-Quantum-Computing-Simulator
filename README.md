# Quantum Computing Simulator

## Project Purpose
The Quantum Computing Simulator project aims to provide a user-friendly web-based platform for exploring and experimenting with quantum algorithms. 
Through an interactive interface, users can visualize quantum gates, circuits, and algorithms, gaining hands-on experience in the fascinating field of quantum computing. 
The simulator utilizes web development technologies, including HTML, CSS, and JavaScript for the frontend, while the backend leverages Python with quantum computing libraries such as Qiskit and Cirq. 
Whether you're a quantum enthusiast, student, or researcher, this simulator offers a playground to deepen your understanding of quantum principles and algorithms, fostering exploration and discovery in the world of quantum computing.


## Project Structure

1. **index.html**: The main HTML file serving as the entry point for the web application. It contains the basic structure of the page.

2. **styles.css**: This CSS file provides styles to make the web page visually appealing and user-friendly.

3. **main.js**: The main JavaScript file responsible for handling user interactions, manipulating the DOM, and communicating with the backend.

4. **quantumSimulator.py**: The main Python file for the backend, where the logic is implemented using quantum computing libraries (Qiskit, Cirq) to simulate quantum algorithms.

5. **requirements.txt**: Lists all Python dependencies needed for the project, including the quantum computing libraries.

## Getting Started

To run the Quantum Computing Simulator locally, follow these steps:

### Prerequisites

- Python installed on your machine
- Quantum computing libraries (install using `pip install -r requirements.txt`)

### Running the Simulator

1. Open `index.html` in your preferred web browser.

2. Explore the interactive quantum simulator, visualize quantum gates, and experiment with quantum algorithms.

## QuantumSimulator.py Overview

```python
# quantumSimulator.py

from qiskit import QuantumCircuit, Aer, transpile, assemble

def simulate_quantum_algorithm():
    # Create a quantum circuit
    circuit = QuantumCircuit(2, 2)

    # Apply quantum gates (modify as needed)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])

    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(circuit, simulator)
    result = simulator.run(assemble(compiled_circuit)).result()

    # Display simulation results
    counts = result.get_counts(circuit)
    print("Simulation Result:", counts)

if __name__ == "__main__":
    simulate_quantum_algorithm()
```
## Dependencies
The project relies on the following dependencies:

1. Qiskit
2. Cirq

Install the dependencies using the command:

```
pip install -r requirements.txt
```
## References.

- [`Qiskit Documentation`](https://qiskit.org/documentation/)
- [`Cirq Documentation`](https://quantumai.google/cirq)

These references provide valuable documentation and resources for understanding and working with Qiskit and Cirq, the quantum computing libraries used in this project. Explore these references for in-depth insights into quantum computing concepts and advanced functionalities.





