# -*- coding: utf-8 -*-
import sys,os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.Qt import *
from mdfpyqt5.camera_panel import Camera
from mdfpyqt5.detection_panel import Detection

def camera_panel_Fc():
    animation = QPropertyAnimation(camera_panel)
    animation.setTargetObject(camera_panel)
    animation.setPropertyName(b"pos")
    animation.setStartValue(camera_panel.pos())
    animation.setEndValue(QPoint(0, 0))
    animation.setDuration(500)
    animation.setEasingCurve(QEasingCurve.OutBounce)
    animation.start(QAbstractAnimation.DeleteWhenStopped)

def exit_camera_panel_Fc():
    animation = QPropertyAnimation(camera_panel)
    animation.setTargetObject(camera_panel)
    animation.setPropertyName(b"pos")
    animation.setStartValue(QPoint(0, 0))
    animation.setEndValue(QPoint(camera_panel.width(),0))
    animation.setDuration(500)
    animation.setEasingCurve(QEasingCurve.OutBounce)
    animation.start(QAbstractAnimation.DeleteWhenStopped)


if __name__=='__main__':
    app = QApplication(sys.argv)
    detection_panel = Detection()
    camera_panel = Camera(detection_panel)
    detection_panel.show_camera_panel.connect(camera_panel_Fc)
    camera_panel.move(0, camera_panel.height())
    camera_panel.show()
    camera_panel.submit_signal.connect(exit_camera_panel_Fc)
    camera_panel.cancel_signal.connect(exit_camera_panel_Fc)
    detection_panel.show()
    sys.exit(app.exec_())
