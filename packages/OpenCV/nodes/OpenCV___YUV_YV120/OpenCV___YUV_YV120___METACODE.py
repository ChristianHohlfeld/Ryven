from NIENV import *

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.img_unYUV_YV12 = None
        self.img_YUV_YV12 = None

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unYUV_YV12 = self.input(0)
      
        self.img_YUV_YV12 = cv2.cvtColor(self.img_unYUV_YV12,cv2.COLOR_BGRA2YUV_YV12)
        #self.cnvt=cv2.imshow('gray_image',self.img_YUV_I420)
        self.main_widget.show_image(self.img_YUV_YV12)
        self.set_output_val(0, self.img_YUV_YV12)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
