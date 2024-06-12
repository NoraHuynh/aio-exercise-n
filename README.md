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
