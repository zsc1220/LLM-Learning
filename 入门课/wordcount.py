import re

def wordcount(text):
    # 将文本转换为小写
    text = text.lower()
    # 用正则表达式移除标点符号
    text = re.sub(r'[!.,]', ' ', text)
    # 将文本分割成单词列表
    words = text.split()
    # 创建一个字典来存储单词出现的次数
    word_count = {}
    # 遍历单词列表并统计每个单词的出现次数
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def demo():
    # 示例输入
    input_text = "Hello world! This is an example. Word count is fun. Is it fun to count words? Yes, it is fun!"
    # 调用wordcount函数并获取结果
    result = wordcount(input_text)
    # 打印输出结果
    print(result)
    
# 作业运行
def homework():
    text = """
        Got this panda plush toy for my daughter's birthday, 
        who loves it and takes it everywhere. It's soft and 
        super cute, and its face has a friendly look. It's 
        a bit small for what I paid though. I think there 
        might be other options that are bigger for the 
        same price. It arrived a day earlier than expected, 
        so I got to play with it myself before I gave it 
        to her.
        """
    # 调用wordcount函数并获取结果
    result = wordcount(text)
    # 打印输出结果
    print(result)

# 判断是否是作为主程序运行
if __name__ == "__main__":
    # demo()
    homework()