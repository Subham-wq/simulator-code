#Execute the circuit on a simulator
  simulator = Aer.get_backend('aer_simulator')  # Use aer_simulator backend
  job = execute(circuit1, simulator, shots=1000)
  result1 = job.result()
  counts = result1.get_counts(circuit1)
  shots = sum(counts.values())
  prob_0 = counts.get('0', 0) / shots
  innerproduct=np.sqrt(prob_0)
