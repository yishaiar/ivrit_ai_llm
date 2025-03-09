# Name this repo!
[Description goes here]

```python
# some python code for reference..
project run from main.py / main.ipynb



## 💻 Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
    ```shell
    pip install -r requirements.txt
    ```

## 📋 TODOs
- [ ] TODO 1
- [ ] TODO 2
- [ ] TODO 3









# Getting started
the place to store data files and model weights 

find fonetic errors & systematic errors and fix with llm 
steps:
1. preprocess data and remove formatting (for analysis usage)
2. 
    a. find common fonetic mistakes like switching between verbs aleph\hey etc
        use hebrew tokenizer and llm to find
    b. find consistant mistakes which are not good translation (such as japanese)
        fonetic translation  using llm
3. fix to a better fonetic option using llm and whole sentence context
4 metrics: bertscore to find if result is closer to translation


find fonetic errors & systematic errors and fix with llm 
steps:
1. preprocess data and remove formatting (for analysis usage)
2. 
    a. find common fonetic mistakes like switching between verbs aleph\hey etc
        use hebrew tokenizer and llm to find
    b. find consistant mistakes which are not good translation (such as japanese)
        fonetic translation  using llm
3. fix to a better fonetic option using llm and whole sentence context
4 metrics: 
    a. bertscore to find if result is closer to translation
    b. hebrew tokenizer and than word error rate


possible mistakes:
1. model is snot sure what he heard and uses the closest word (low log prob)
2. model did not learn well and had a mistake
    