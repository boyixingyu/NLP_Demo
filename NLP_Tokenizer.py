# 逆向最大匹配
class IMM(object):
    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximun = 0
        # 读取词典
        with open(dic_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                self.maximun = max(self.maximun, len(line))

    def cut(self, text):
        result = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maximun, 0, -1):
                if index - size < 0:
                    continue
                piece = text[(index-size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
            if word is None:
                index -= 1
                result.append(text[index])
        return result[::-1]



if __name__=="__main__":
    text = "南京市长江大桥"
    tokenizer = IMM(".\imm_dic.txt")
    print(tokenizer.cut(text))
