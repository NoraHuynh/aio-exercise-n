# AIO2024 Exercise - From AIVN

## Module 01

### Week 01

#### 1. Evaluation Metrics For Classification Model
$$Precision = \frac{TP}{TP+FP}$$

$$Recall = \frac{TP}{TP+FN}$$

$$F1-score = 2*\frac{Precision*Recall}{Precision+Recall}$$

#### 2. Three activation functions: Sigmoid, ReLU, ELU
$$sigmoid(x) = \frac{1}{1+e^{-x}}$$

$$
relu(x) = max(0, x) = \begin{cases}
              0 & if & x \leq 0 \\
              x & if & x > 0
          \end{cases}
$$

$$
elu(x) = \begin{cases}
              \alpha (e^{x}-1) & if & x \leq 0 \\
              x & if & x > 0
          \end{cases}
$$

#### 3. Regression loss functions
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y_i}|$$

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2$$

$$RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2}$$

#### 4. Trigonometric approximation
$$sin(x) \approx \sum_{n=0}^{\infty}(-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - ...$$

$$cos(x) \approx \sum_{n=0}^{\infty}(-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - ...$$

$$sinh(x) \approx \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!} = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \frac{x^7}{7!} + \frac{x^9}{9!} + ...$$

$$cosh(x) \approx \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!} = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \frac{x^8}{8!} + ...$$

#### 5. Mean Difference of ${n^{th}}$ Root Error
$$MDnRE = \frac{1}{m}\sum_{i=1}^{m}(\sqrt[n]{y_i}-\sqrt[n]{\hat{y_i}})^{p}$$

### Week 02
#### 1. Sliding Window Maximum

* **Input**: num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1], k = 3
* **Output**: [5, 5, 5, 5, 10, 12, 33, 33]
* **Explanation**: 

Window position             |   Max
-|-
**[3 4 5]** 1 -44 5 10 12 33 1  |    5
3 **[4 5 1]** -44 5 10 12 33 1  |    5
3 4 **[5 1 -44]** 5 10 12 33 1  |    5
3 4 5 **[1 -44 5]** 10 12 33 1  |    5
3 4 5 1 **[-44 5 10]** 12 33 1  |    10
3 4 5 1 -44 **[5 10 12]** 33 1  |    12
3 4 5 1 -44 5 **[10 12 33]** 1  |    33
3 4 5 1 -44 5 10 **[12 33 1]**  |    33

#### 2. Occurrences of characters
* **Input**: one word [a-z][A-Z] 
* **Output**: a dictionary that counts the occurrences of characters

#### 3. Occurrences of words

* **Input**: path to the txt file 
* **Output**: dictionary that counts the occurrences of each word

#### 4. Levenshtein distance
$$
lev(a,b) = \begin{cases}
              |a| & if |b| = 0, \\
              |b| & if |a| = 0, \\
              lev(tail(a),tail(b)) & if head(a) = head(b),\\
              1 + min
              \begin{cases}
                lev(tail(a),b) \\
                lev(a,tail(b)) \\
                lev(tail(a),tail(b))
              \end{cases} & otherwise &
          \end{cases}
$$
