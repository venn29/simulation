from hashlib import new
import Sketch.BasicSketch
import Common.Packet
class _Switch:
    def __init__(self,switchid):
        # 用来存放sketch
        self.Initiate_Active_Sketch(self,d,w,True)
        self.Initiate_Idle_Sketch(self,d,w,False)
        # 后续用来存放deviation的packet
        self.hash_table = []
        # 放一个map[path_ID：[α，β]],表示本交换机在某个路径上的范围      对应的sketch(只有一个sketch
        self.scope = {}
        self.switch_ID = switchid


    # 返回对应sketch上的sketch_table内容，列表返回，比如d=2，w=3返回[[1,2,3],[1,2,3]]

    def Query(self,path_ID):
        return self.active_sketch.sketch_table
    # 处理正常收到的包,packet为Common.Packet._Packet
    # 根据path_ID找到对应的packet
    # 判断是否正确，如果正确，交给basicsketch，否则交给hashsketch
    def Process_Packet(self,path_ID,packet):
        if(self.Receive(packet)):
            self.active_sketch.Receive_packet(packet,self.scope[path_ID])
        else:
            pass
    # 接收包，判断是否路径正确
    def Receive(self,packet):
        if self.switch_ID in packet.flow.path:
            return True
        else:
            return False

    # 生成一个新的Sketch,d,w为参数
    def Initiate_Active_Sketch(self,d,w,True):
        self.active_sketch = new Sketch.BasicSketch._Basic_Sketch(d,w,True)
    def Initiate_Idle_Sketch(self,d,w,False):
        self.active_sketch = new Sketch.BasicSketch._Basic_Sketch(d,w,True)