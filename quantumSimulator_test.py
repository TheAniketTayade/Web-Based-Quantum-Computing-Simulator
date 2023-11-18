from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram

def deutsch_josza_algorithm(oracle_type):
    n = len(oracle_type)

    # Quantum circuit with n+1 qubits and n classical bits
    qc = QuantumCircuit(n+1, n)

    # Apply Hadamard gate to all qubits
    qc.h(range(n+1))

    # Apply X gate to the last qubit
    qc.x(n)

    # Apply Hadamard gate to the last qubit
    qc.h(n)

    # Apply the oracle based on the type
    if oracle_type == "constant":
        pass  # Do nothing for a constant oracle
    elif oracle_type == "balanced":
        for qubit in range(n):
            qc.cx(qubit, n)

    # Apply Hadamard gate to the first n qubits
    qc.h(range(n))

    # Measure the first n qubits
    qc.measure(range(n), range(n))

    return qc

def run_deutsch_josza_algorithm(oracle_type):
    qc = deutsch_josza_algorithm(oracle_type)

    # Simulate the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def main():
    oracle_types = ["constant", "balanced"]

    for oracle_type in oracle_types:
        counts = run_deutsch_josza_algorithm(oracle_type)
        print(f"Oracle Type: {oracle_type}, Measurement Outcome: {list(counts.keys())[0]}")

if __name__ == "__main__":
    main()
