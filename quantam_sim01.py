import numpy as np

isq2 = 1.0/(2.0**0.5)

class Qstate:
  def __init__(self, n):
    self.n = n
    self.state = np.zeros(2**self.n, dtype=np.complex)
    self.state[0] = 1

  # apply transformation t to bit i 
  # (or i and i+1 in case of binary gates)
  def op(self, t, i):
    # I_{2^i}
    eyeL = np.eye(2**i, dtype=np.complex)

    # I_{2^{n-i-1}}
    # t.shape[0]**0.5 denotes how many bits t applies to
    # in case of NOT, t.shape[0]**0.5 == 1
    eyeR = np.eye(2**(self.n - i - int(t.shape[0]**0.5)), 
        dtype = np.complex)

    # eyeL ⊗ t ⊗ eyeR
    t_all = np.kron(np.kron(eyeL, t), eyeR)

    # apply transformation to state (multiplication)
    self.state = np.matmul(t_all, self.state)

  # Hadamard gate
  def hadamard(self, i):
    h_matrix = isq2 * np.array([
        [1,1],
        [1,-1]
    ])    
    self.op(h_matrix, i)

  # T gate
  def t(self, i):
    t_matrix = np.array([
        [1,0],
        [0,isq2 + isq2 * 1j]
    ])
    self.op(t_matrix, i)

  # S gate
  def s(self, i):
    s_matrix = np.array([
        [1,0],
        [0,0+1j]
    ])    
    self.op(s_matrix,i)

  # CNOT gate
  def cnot(self, i):
    cnot_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    self.op(cnot_matrix, i)
  
  # Swap two qubits
  def swap(self, i):
    swap_matrix = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])
    self.op(swap_matrix, i)