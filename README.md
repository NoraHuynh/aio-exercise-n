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

#### 2. Number of characters
* **Input**: one word [a-z][A-Z] 
* **Output**: a dictionary that counts the occurrences of characters

#### 3. Number of words

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

### Week 4 Projects

This section contains small projects developed using [Streamlit](https://streamlit.io/). Each project demonstrates different functionalities and use cases of Streamlit.

#### Project List

##### **1. Chatbot**
This project demonstrates a simple chatbot application built using [Streamlit](https://streamlit.io/) and [HugChat](https://github.com/Soulter/hugging-chat-api). The chatbot allows users to log in with their Hugging Face credentials and interact with the model through a user-friendly interface.
![image](https://github.com/NoraHuynh/factorial-app/assets/138383339/1e262026-5ee4-4e50-a309-4d0b305f5b09)
###### **How to Run**
1. Clone the repository
   ```bash
   git clone https://github.com/NoraHuynh/aio-exercise-nr.git
   ```
1. Create and Activate Conda Environment
    ```bash
    conda create --name chatbot-env python=3.12
    conda activate chatbot-env
    ```
1. Navigate to the project directory
    ```bash
    cd AIO-Exercise-nr/Module1/Week4/chatbot
    ```
1. Install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```
1. Run the Streamlit app
    ```bash
    streamlit run app.py
    ```

##### **2. Word Correction**
Word Correction is a basic NLP application that corrects single-word inputs. It uses the Levenshtein distance algorithm to identify and fix misspelled words, enhancing text accuracy for various text processing tasks.
![image](https://github.com/NoraHuynh/factorial-app/assets/138383339/3cd4bf47-b31c-42c7-b3c0-fe2619afa60a)
###### **How to Run**
1. Clone the repository
   ```bash
   git clone https://github.com/NoraHuynh/aio-exercise-nr.git
   ```
1. Create and Activate Conda Environment
    ```bash
    conda create --name word-correction-env python=3.12
    conda activate word-correction-env
    ```
1. Navigate to the project directory
    ```bash
    cd AIO-Exercise-nr/Module1/Week4/word-correction
    ```
1. Install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```
1. Run the Streamlit app
    ```bash
    streamlit run app.py
    ```

##### **3. Object Detection**
Word Correction is a basic NLP application that corrects single-word inputs. It uses the Levenshtein distance algorithm to identify and fix misspelled words, enhancing text accuracy for various text processing tasks.
![image](https://github.com/NoraHuynh/factorial-app/assets/138383339/8c3f4928-cc3b-4203-a725-7d9db672f9ed)

###### **How to Run**
1. Clone the repository
   ```bash
   git clone https://github.com/NoraHuynh/aio-exercise-nr.git
   ```
1. Create and Activate Conda Environment
    ```bash
    conda create --name obj-detection-env python=3.12
    conda activate obj-detection-env
    ```
1. Navigate to the project directory
    ```bash
    cd AIO-Exercise-nr/Module1/Week4/object-detection
    ```
1. Install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```
1. Run the Streamlit app
    ```bash
    streamlit run app.py
    ```

## Additional Information
For any questions or issues, please open an issue in the repository or contact me at noravnhuynh@gmail.com.

Feel free to customize the project names, descriptions, and any other details specific to your projects. Let me know if there’s anything else you need!

