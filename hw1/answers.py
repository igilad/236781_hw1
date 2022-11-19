r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part1_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**
We will show that $\Delta > 0$  is arbitrary by showing that changing it to $\alpha\Delta$ results in an equivalent problem.
Let $\alpha > 0$ and define $\mathbf{W'} = \alpha*\mathbf{W}$ Hence the new loss is now 
    $L(\mathbf{W'}) =
    \frac{1}{N} \sum_{i=1}^{N} 
    \max\left(0, \alpha\Delta+ \vec{w'_j} \vec{x_i} 
    - \vec{w'_{y_i}} \vec{x_i}\right) 
    +
    \frac{\lambda}{2} \|{\mathbf{W'}}\|^2 =\\=
    \frac{1}{N} \sum_{i=1}^{N} 
    \max\left(0, \alpha\Delta+ \vec{w'_j} \vec{x_i} 
    - \vec{w'_{y_i}} \vec{x_i}\right) 
    +
    \frac{\lambda}{2} \|{\mathbf{W'}}\|^2 =\\=
    \frac{1}{N} \sum_{i=1}^{N} 
    \max\left(0, \alpha\Delta+ \alpha*\vec{w_j} \vec{x_i} 
    - \alpha*\vec{w'_{y_i}} \vec{x_i}\right) 
    +
    \frac{\lambda}{2}*\alpha^2 \|{\mathbf{W}}\|^2=\\=
    \frac{1}{N} \sum_{i=1}^{N} 
    \max\left(0, \alpha(\Delta+ \vec{w_j} \vec{x_i} 
    - \vec{w'_{y_i}} \vec{x_i}\right)) 
    +
    \frac{\lambda}{2}*\alpha^2 \|{\mathbf{W}}\|^2=\\=
    \frac{1}{N} \sum_{i=1}^{N} 
    \max\left(0, \Delta+ \vec{w_j} \vec{x_i} 
    - \vec{w'_{y_i}} \vec{x_i}\right) 
    +
    \frac{\lambda}{2}*\alpha^2 \|{\mathbf{W}}\|^2
    $
    The final formulation is equivalent to the original problem differing in the choice of $\lambda$ and so because for every $\lambda$ that is optimal for the original, $\lambda*\alpha^2$ is optimal for the new problem, we get that the two are equivalent.
"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
z
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
