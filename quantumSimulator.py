from flask import Flask, request, jsonify
from qiskit import QuantumCircuit, transpile, Aer, execute

app = Flask(__name__)

def run_quantum_simulation(data):
    # Process data and run quantum simulation
    num_qubits = data.get("num_qubits", 2)
    num_classical_bits = data.get("num_classical_bits", 2)

    qc = QuantumCircuit(num_qubits, num_classical_bits)
    qc.h(0)
    qc.cx(0, 1)

    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)

    return {"counts": counts}

@app.route('/run-quantum-simulation', methods=['POST'])
def handle_quantum_simulation():
    data = request.get_json()
    results = run_quantum_simulation(data)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
