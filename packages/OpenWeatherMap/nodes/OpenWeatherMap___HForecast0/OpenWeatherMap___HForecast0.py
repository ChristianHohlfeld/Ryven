from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import m


# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------


class HForecast_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(HForecast_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        self.initialized()

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        mgr = self.input(0)
        daily_forecast = None
        if self.input(2) != '':
            daily_forecast = mgr.forecast_at_place(self.input(1)+','+self.input(2), '3h')
        else:
            daily_forecast = mgr.forecast_at_place(self.input(1), '3h')
        fcast = daily_forecast.forecast
        self.set_output_val(0, fcast)
        self.set_output_val(1, list(fcast))

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass