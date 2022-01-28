# -*- coding: utf-8 -*-
from  PyQt5.Qt import *
from mdfpyqt5.ui.camera import  Ui_Form
# from camera.linux.ParametrizeCamera_Load import load_camera_parameter
import sys
class Camera(QWidget,Ui_Form):
    cancel_signal = pyqtSignal()
    submit_signal = pyqtSignal()
    def __init__(self,parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setupUi(self)
    def submit_clicked(self,checked):
        flag_camera=load_camera_parameter()
        if flag_camera==False:
            reply = QMessageBox.information(self, "提示", "相机连接错误", QMessageBox.Yes | QMessageBox.No)
        self.submit_signal.emit()
        print("123",checked)
    def cancel_clicked(self,checked):
        self.cancel_signal.emit()
        print("123",checked)
if __name__=='__main__':
    app = QApplication(sys.argv)
    window=Camera()
    window.show()
    sys.exit(app.exec_())

