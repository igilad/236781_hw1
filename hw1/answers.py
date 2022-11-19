r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**
1)  No, the test set allows us to estimate our loss Ld over the entire distribution.
2)  No, for example there could be a case where there are 10 classes and 9 make up the train set
    and the last makes up the test set. In this case the training is completely irrelevant to the test set 
    and learning will fail.
3)  Yes, validation exists to try to estimate the test accuracy without data leaking from the test set into the
    learning process. Incorporating the test set would go against that goal and make the final test accuracy
    not representative of the generalized loss.
4)  Not exactly. While the performance of each fold can be thought of as a proxy for the generalized error, 
    The point of k-fold cv is to use the average of all the folds as said proxy.

"""

part1_q2 = r"""
**Your answer:**

No, this approach is not justified and would lead to bad generalization.
In general using test data during training is a bad idea since it can lead to the model learning
the test set and as such overfitting to both it and the train set.
Because of that, the test set stops being representative of the generalized distribution and the 
performance on actual unseen data will be bad.
    

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
    - \alpha*\vec{w_{y_i}} \vec{x_i}\right) 
    +
    \frac{\lambda}{2}*\alpha^2 \|{\mathbf{W}}\|^2=\\=
    \frac{1}{N} \sum_{i=1}^{N} 
    \max\left(0, \alpha(\Delta+ \vec{w_j} \vec{x_i} 
    - \vec{w_{y_i}} \vec{x_i}\right)) 
    +
    \frac{\lambda}{2}*\alpha^2 \|{\mathbf{W}}\|^2=\\=
    \frac{1}{N} \sum_{i=1}^{N} 
    \max\left(0, \Delta+ \vec{w_j} \vec{x_i} 
    - \vec{w_{y_i}} \vec{x_i}\right) 
    +
    \frac{\lambda}{2}*\alpha^2 \|{\mathbf{W}}\|^2
    $
    The final formulation is equivalent to the original problem differing in the choice of $\lambda$ and so because for every $\lambda$ that is optimal for the original, $\lambda*\alpha^2$ is optimal for the new problem, we get that the two are equivalent.
"""

part3_q2 = r"""
**Your answer:**


1) What the linear model is actually learning is a "prototype" of each digit,
Meaning an average representation of each digit that is similar to all examples of that digit.
Because of that, the final weights look like the digits and are interpretable.
The samples that we got wrong tend to be rotated or deformed in some way and so because we only learn an 
average digit and we dont try to characterize or define each digit, we get those ones wrong.

2) Both of these interpretations try comparing the sample to other things and seeing what is closest.
the difference is that knn compares the sample to the dataset and does a "vote" to decide the outcome 
while our model learns a representation of each digit and compares the new sample to those representations.

"""

part3_q3 = r"""
**Your answer:**

1) Too high.
In the case of a good learning rate, the graph would be far less steep but would be relatively monotonous, 
decreasing towards the solution at a good rate.
A low learning rate would not even finish converging in the set amount of epochs and as such decrease 
slowly and end on a very high loss.

2) Our model is highly overfitted to the training set.
We can see that because the training loss is quite a bit higher that both the validation loss and the test loss.
This can be fixed by increasing the weight decay value.

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
