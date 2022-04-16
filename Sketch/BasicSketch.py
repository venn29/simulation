# sketch基类
import Utility.Hash
class _Basic_Sketch:
    def __init__(self,d,w,active):
        # 哈希表长宽
        self.active = active
        self.d = d
        self.w = w
        # 哈希表    二维数组
        self.sketch_table=[]
        # 工具类
        self.hash = Utility.Hash._Hash()
        # 每行对应的hash方法
        self.hash_function=[]
    # 生成对应的哈希表并初始化，根据d和w初始化hash_table，为每行固定一种hash方法
    def Generate_Hash_Table(self):
        self.hash_function.append(self.hash.md5)
        self.hash_function.append(self.hash.sha256)
        for i in range (0,self.d):
            self.sketch_table.append( [0 for x in range(0, self.w)])
    
    def Receive_packet(packet):
        


