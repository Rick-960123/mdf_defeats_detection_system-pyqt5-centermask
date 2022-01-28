# -*- coding: utf-8 -*-
from  PyQt5.Qt import *
from mdfpyqt5.ui.detection import Ui_widget
# ##from centermask.demo.centermask_demo_mdf import Center_mask
### from camera.linux.save_image import hkcamera
from pretreatment.pretreatment import pre_treatment
import sys,cv2,numpy,time,json,os, traceback
import serial,binascii,skimage.io
from  sqllite.mysql_connect import edit_db
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFileDialog

###################################光电开关线程####################################
class MyThread(QThread):
    collect_image=pyqtSignal()
    real_time = pyqtSignal()
    def __init__(self,parent=None):
        super(MyThread,self).__init__(parent)
    def setval(self,val):
        self.val=val
        self.start()
    def run(self):
        s = serial.Serial('COM4', 115200, timeout=0.5)
        print("已连接com4口")
        while True:
            n = s.inWaiting()
            if n:
                data = str(binascii.b2a_hex(s.read(n)))[2:-1]
                if data == "aa" and self.val=="collect_image":
                    self.collect_image.emit()
                if data == "aa" and self.val == "real_time":
                    self.real_time.emit()
###################################缺陷检测线程####################################
class Center_mask(object):
    adc="da"
    def __init__(self):
        pass
    def abc(self):
        pass

class hkcamer():
    adc="da"
    def __init__(self):
        pass
    def abc(self):
        pass
class Detection_Thread(QThread):
    detect_image_1 = pyqtSignal(str,dict)
    def __init__(self, parent=None):
        super(Detection_Thread, self).__init__(parent)
        self.center_mask = Center_mask()
    def setVal(self, im_path,im_datas,model_path,pattern,first):
        self.im_path=im_path
        self.im_datas=im_datas
        self.pattern=pattern
        self.model_path=model_path
        self.first=first
        ##执行线程的run方法
        self.start()  #多线程检测
        #self.run()       #单线程检测
    def run(self):
        if self.first == 1:
            self.load_model()
        if self.pattern=="local":
            path=self.im_path.copy()
            for i in path:
                self.im_path=i
                re_data=self.detect_images()
                self.detect_image_1.emit(self.pattern, re_data)
        else:
            re_data=self.detect_images()
            self.detect_image_1.emit(self.pattern, re_data)

    def load_model(self):
        self.center_mask.load_model(self.model_path)
    def detect_images(self):
        defects_chinese = ["松软", "黑斑", "划痕", "金属杂质", "边缘破损", "油污", ]
        defects = ["soft", "black", "scratch", "metal", "edge", "oil", ]
        confidence, kind, location = [], [], []
        defects_kind = []
        area = []
        defects_kind_chinese = []
        defects_location = []
        number = 0
        detect_data = []
        detect_results1 = []
        im_masks1 = []
        if self.im_datas == "":  #本地检测
            image_1 = skimage.io.imread(os.path.join(self.im_path))
            image = image_1.copy()
            if image_1.shape[0] == 4096:    #本地检测4096大小的图片
                detect_result = {"masks": [], "class_ids": [], "rois": [], "scores": [], "area": []}
                image_2 = cv2.cvtColor(image_1, cv2.COLOR_RGB2BGR)
                pre_image_1 = pre_treatment(image_2)
                pre_image = cv2.cvtColor(pre_image_1, cv2.COLOR_BGR2RGB)
                im_mask = numpy.zeros([4096, 4096, 3], numpy.uint8)
                images_data = []
                zero_ids = []
                for y in range(4):
                    for x in range(4):
                        detect_data.append(pre_image[x * 1024:(x * 1024) + 1024, y * 1024:(y * 1024) + 1024])
                    images_data.append(detect_data)
                    detect_data = numpy.array(detect_data)
                    detect_results2, im_masks2, zero_ids2 = self.center_mask.detect_data(detect_data)
                    detect_results1.append(detect_results2), im_masks1.append(im_masks2), zero_ids.append(zero_ids2)
                    detect_data = []
                for y in range(4):
                    index = 0
                    for x in range(4):
                        if zero_ids[y] != []:
                            if zero_ids[y][index] == x:
                                im_mask[x * 1024:(x + 1) * 1024, y * 1024:(y + 1) * 1024] = images_data[y][x]
                                index += 1
                                continue
                        if len(detect_results1[y][x - index]['class_ids']) == 0:
                            im_mask[x * 1024:(x + 1) * 1024, y * 1024:(y + 1) * 1024] = images_data[y][x]
                            continue
                        im_mask[x * 1024:(x + 1) * 1024, y * 1024:(y + 1) * 1024] = im_masks1[y][x - index][:]
                        for xxx in range(len(detect_results1[y][x - index]['scores'])):
                            detect_result['masks'].append(detect_results1[y][x - index]['masks'][xxx])
                            detect_result['class_ids'].append(detect_results1[y][x - index]['class_ids'][xxx])
                            detect_result['scores'].append(detect_results1[y][x - index]['scores'][xxx])
                            detect_result['area'].append(detect_results1[y][x - index]['area'][xxx])
                            rois = [detect_results1[y][x - index]['rois'][xxx][0] + (y * 1024),
                                    detect_results1[y][x - index]['rois'][xxx][1] + ((x) * 1024),
                                    detect_results1[y][x - index]['rois'][xxx][2] + (y * 1024),
                                    detect_results1[y][x - index]['rois'][xxx][3] + (x) * 1024]
                            detect_result['rois'].append(rois)
            else:                                  #本地检测其他大小的图片
                image_1 = numpy.array([image_1])
                detect_results, im_masks, zero_ids = self.center_mask.detect_data(image_1)
                detect_result, im_mask = detect_results[0], im_masks[0]
        else:     #实时检测
            image = self.im_datas.copy()
            if self.im_datas.shape[0] == 4096:     #实时检测4096大小图片
                image_1 = cv2.cvtColor(self.im_datas, cv2.COLOR_RGB2BGR)
                pre_image_1 = pre_treatment(image_1)
                pre_image = cv2.cvtColor(pre_image_1, cv2.COLOR_BGR2RGB)
                detect_result = {"masks": [], "class_ids": [], "rois": [], "scores": [], "area": []}
                im_mask = numpy.zeros([4096, 4096, 3], numpy.uint8)
                images_data = []
                zero_ids = []
                for y in range(4):
                    for x in range(4):
                        detect_data.append(pre_image[x * 1024:(x * 1024) + 1024, y * 1024:(y * 1024) + 1024])
                    images_data.append(detect_data)
                    detect_data = numpy.array(detect_data)
                    detect_results2, im_masks2, zero_ids2 = self.center_mask.detect_data(detect_data)
                    detect_results1.append(detect_results2), im_masks1.append(im_masks2), zero_ids.append(zero_ids2)
                    detect_data = []
                for y in range(4):
                    index = 0
                    for x in range(4):
                        if zero_ids[y] != []:
                            if zero_ids[y][index] == x:
                                im_mask[x * 1024:(x + 1) * 1024, y * 1024:(y + 1) * 1024] = images_data[y][x]
                                index += 1
                                continue
                        if len(detect_results1[y][x - index]['class_ids']) == 0:
                            im_mask[x * 1024:(x + 1) * 1024, y * 1024:(y + 1) * 1024] = images_data[y][x]
                            continue
                        im_mask[x * 1024:(x + 1) * 1024, y * 1024:(y + 1) * 1024] = im_masks1[y][x - index][:]
                        for xxx in range(len(detect_results1[y][x - index]['scores'])):
                            detect_result['masks'].append(detect_results1[y][x - index]['masks'][xxx])
                            detect_result['class_ids'].append(detect_results1[y][x - index]['class_ids'][xxx])
                            detect_result['scores'].append(detect_results1[y][x - index]['scores'][xxx])
                            detect_result['area'].append(detect_results1[y][x - index]['area'][xxx])
                            rois = [detect_results1[y][x - index]['rois'][xxx][0] + (y * 1024),
                                    detect_results1[y][x - index]['rois'][xxx][1] + ((x) * 1024),
                                    detect_results1[y][x - index]['rois'][xxx][2] + (y * 1024),
                                    detect_results1[y][x - index]['rois'][xxx][3] + (x) * 1024]
                            detect_result['rois'].append(rois)
            else:                                      #实时检测其他大小图片
                detect_results, im_masks, zero_ids = self.center_mask.detect_data(self.im_datas)
                detect_result, im_mask = detect_results[0], im_masks[0]
        defects_number = {"soft": 0, "spot": 0, "scratch": 0, "edge": 0}
        for i in range(len(detect_result['rois'])):
            number += 1
            conf = detect_result['scores'][i]
            confidence.append(conf)
            y = detect_result['class_ids'][i]
            kind_chinese = defects_chinese[y - 1]
            kind = defects[y - 1]
            defects_kind_chinese.append(kind_chinese)
            defects_kind.append(kind)
            abc = int(detect_result['area'][i] / 15)
            location = detect_result['rois'][i]
            location_1 = self.listToJson(location)
            defects_location.append(location_1)
            width = 0
            if kind == "edge":   #表面质量分级
                width = int(min(location[3] - location[1], location[2] - location[0]))
                abc = int(width / 4)
            if (kind == "soft" and abc <= 2000):
                defects_number["soft"] += 1
            elif (kind == "oil"):
                abc = int(abc / 1.1)
                if abc <= 40:
                    defects_number["spot"] += 1
                else:
                    defects_number["soft"] = 10000
            elif (kind == "edge" and width <= 10):
                defects_number["edge"] += 1
            elif (kind == "black"):
                abc = int(abc / 1.2)
                if abc <= 40:
                    defects_number["spot"] += 1
                else:
                    defects_number["soft"] = 10000
            elif (kind == "metal" and abc <= 40):
                defects_number["spot"] += 1
            elif (kind == "scratch"):
                abc = int(abc / 1.4)
                defects_number["scratch"] += 1
            else:
                defects_number["soft"] = 10000
            area.append(abc)
        if defects_number["soft"] == defects_number["spot"] == defects_number["scratch"] == defects_number["edge"] == 0:
            level = "优等品"
        elif (defects_number["soft"] <= 3) and (defects_number["spot"] <= 1):
            level = "合格品"
        else:
            level = "不合格品"
        conf = self.listToJson(confidence)
        kin_c = self.listToJson(defects_kind_chinese)
        kin = self.listToJson(defects_kind)
        are = self.listToJson(area)
        loc = self.listToJson(defects_location)
        shape = numpy.shape(image)
        re_data = {"image_name": self.im_path.split("/")[-1],
                   "defects_count": str(number),
                   "defects_kind": kin,
                   "defects_kind_chinese": kin_c,
                   "defects_location": loc,
                   "confidence": conf,
                   "level": level,
                   "image_size": str(shape),
                   "image_path": self.im_path,
                   "defects_area": are,
                   "image_mask": im_mask.astype(numpy.int8),
                   "image": image,
                   "date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                   }
        return re_data

    def listToJson(self,lst):
        keys = [str(x) for x in numpy.arange(len(lst))]
        list_json = dict(zip(keys, lst))
        try:
            data_json = json.dumps(list_json, skipkeys=True, ensure_ascii=False)
        except Exception:
            traceback.format_exc()
            a = [str(x) for x in lst]
            list_json = dict(zip(keys, a))
            data_json = json.dumps(list_json, skipkeys=True, ensure_ascii=False)
        return data_json

###################################主程序线程####################################
class Detection(QWidget,Ui_widget):
    show_camera_panel = pyqtSignal()
    start_detect=pyqtSignal()
    TableDataSignal_list_1 = pyqtSignal(int, int, str)
    TableDataSignal_detail_1 = pyqtSignal(int, int, str)
    TableDataSignal_clear_1=pyqtSignal(int)
    TableDataSignal_list_2 = pyqtSignal(int, int, str)
    TableDataSignal_detail_2 = pyqtSignal(int, int, str)
    TableDataSignal_clear_2 = pyqtSignal(int)
    TableDataSignal_list_3 = pyqtSignal(int, int, str)
    TableDataSignal_detail_3 = pyqtSignal(int, int, str)
    TableDataSignal_clear_3 = pyqtSignal(int)
    TableDataSignal_list_4 = pyqtSignal(int, int, str)
    TableDataSignal_detail_4 = pyqtSignal(int, int, str)
    TableDataSignal_clear_4 = pyqtSignal(int)
    def __init__(self,parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.TableData_find_list=TableData_list()
        self.TableData_local_list = TableData_local_list()
        self.TableData_collect_list = TableData_collect_list()
        self.TableData_detect_list = TableData_list()
        self._thread = MyThread()
        self._thread1 = Detection_Thread()

        self.Model_Data_list = QStandardItemModel(12, 7)  # 初始化一个模型QStandardItemModel，4行13列
        self.Model_Data_list1 = QStandardItemModel(12, 7)
        self.Model_Data_list2 = QStandardItemModel(12, 5)
        self.Model_Data_list3 = QStandardItemModel(18, 5)

        self.TableData_detect_list.TableViewInit(self.list, self.Model_Data_list1)  # 调用类TableData中初始化表格函数
        self.TableData_local_list.TableViewInit(self.list_2, self.Model_Data_list2)
        self.TableData_collect_list.TableViewInit(self.list_3, self.Model_Data_list3)
        self.TableData_find_list.TableViewInit(self.list_4, self.Model_Data_list)

        self.TableData_collect_detail = TableData_collect_detail()
        self.TableData_local_detail = TableData_detail()
        self.TableData_find_detail = TableData_detail()
        self.TableData_detect_detail = TableData_detail()

        self.Model_Data_detail = QStandardItemModel(5, 4)  # 初始化一个模型QStandardItemModel，4行13列
        self.Model_Data_detail1 = QStandardItemModel(5, 4)  # 初始化一个模型QStandardItemModel，4行13列
        self.Model_Data_detail2 = QStandardItemModel(1, 3)  # 初始化一个模型QStandardItemModel，4行13列
        self.Model_Data_detail3 = QStandardItemModel(5, 4)  # 初始化一个模型QStandardItemModel，4行13列

        self.TableData_detect_detail.TableViewInit(self.detail, self.Model_Data_detail)  # 调用类TableData中初始化表格函数
        self.TableData_local_detail.TableViewInit(self.detail_2, self.Model_Data_detail1)
        self.TableData_collect_detail.TableViewInit(self.detail_3, self.Model_Data_detail2)
        self.TableData_find_detail.TableViewInit(self.detail_4, self.Model_Data_detail3)
        self.edit_db=edit_db
        self.i,self.y=0,0
        self.load_model,self.start=0,0
        self.files,self.model_path,self.save_path=[],[],[]
        self.start_detect_flag,self.start_collect_flag,self.local_start_detect_flag,self.parameter_flag=False,False,False,False

        self._thread1.detect_image_1.connect(self.show_image)  ################缺陷检测线程信号槽######
        self._thread.collect_image.connect(self.collect_image)  ###############图像采集线程信号槽######
        self._thread.real_time.connect(self.real_time)  ###############实时图像采集线程信号槽######

        self.TableDataSignal_list_3.connect(self.TableData_collect_list.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新
        self.TableDataSignal_list_4.connect(self.TableData_find_list.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新
        self.TableDataSignal_list_1.connect(self.TableData_detect_list.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新
        self.TableDataSignal_list_2.connect(self.TableData_local_list.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新

        self.TableDataSignal_detail_1.connect(self.TableData_detect_detail.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新
        self.TableDataSignal_detail_4.connect(self.TableData_find_detail.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新
        self.TableDataSignal_detail_3.connect(self.TableData_collect_detail.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新
        self.TableDataSignal_detail_2.connect(self.TableData_local_detail.Model_setItem)  # 这里采用信号槽来绑定Model_setItem进行数据更新

        self.TableDataSignal_clear_4.connect(self.TableData_find_detail.Model_clear)
        self.TableDataSignal_clear_2.connect(self.TableData_local_detail.Model_clear)
        self.TableDataSignal_clear_1.connect(self.TableData_detect_detail.Model_clear)

    # def closeEvent(self, event): # 重构closeEvent(self, event)函数,防止子线程不退出
    #     result = QMessageBox.question(self, "标题", "确定关闭?",
    #                                             QMessageBox.Yes | QMessageBox.No)
    #     if (result == QMessageBox.Yes):
    #         event.accept()
    #         os._exit(0)
    #     else:
    #         event.ignore()

    def table_show(self, name, row, column, data):
        if name=="list":
            self.list.setItem(row,column,QStandardItem(data))
        if name=="list_2":
            self.list_2.setItem(row,column,QStandardItem(data))
        if name=="list_3":
            self.list_3.setItem(row,column,QStandardItem(data))
        if name=="list_4":
            self.list.setItem(row,column,QStandardItem(data))
        if name=="detail":
            self.detail.setItem(row,column,QStandardItem(data))
        if name=="detail_2":
            self.detail_2.setItem(row,column,QStandardItem(data))
        if name=="detail_3":
            self.detail_3.setItem(row,column,QStandardItem(data))
        if name=="detail_4":
            self.detail_4.setItem(row,column,QStandardItem(data))
    def show_image(self, name, data):
        if name == "real":  #################################################实时检测########################################################
            self.i+=1
            re_data=data
            image_save_path = self.save_path + '/' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".jpg"
            skimage.io.imsave(image_save_path,re_data["image"].astype(numpy.uint8))
            skimage.io.imsave("test_img/"+re_data["image_name"],re_data["image_mask"].astype(numpy.uint8))
            x = re_data["image"].shape[1]
            y = re_data["image"].shape[0]
            frame = QImage(data, x, y, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)
            self.scene = QGraphicsScene()
            self.scene.addItem(self.item)
            self.tuxiang.setScene(self.scene)
            if x==4096:
                self.item.setScale(0.14)
            else:
                self.item.setScale(0.4)
            frame1 = QImage(re_data["image_mask"], x, y, QImage.Format_RGB888)
            pix1 = QPixmap.fromImage(frame1)
            self.item1 = QGraphicsPixmapItem(pix1)
            self.scene1 = QGraphicsScene()
            self.scene1.addItem(self.item1)
            self.tuxiang_5.setScene(self.scene1)
            if x==4096:
                self.item1.setScale(0.14)
            else:
                self.item1.setScale(0.4)
            self.TableDataSignal_list_1.emit(self.i - 1, 0, re_data["image_name"])
            self.TableDataSignal_list_1.emit(self.i - 1, 1, re_data['image_size'])
            self.TableDataSignal_list_1.emit(self.i - 1, 6, '1650')
            self.TableDataSignal_list_1.emit(self.i - 1, 7, "100us")
            self.TableDataSignal_list_1.emit(self.i - 1, 4, re_data["date"])
            self.TableDataSignal_list_1.emit(self.i - 1, 3, re_data["level"])
            self.TableDataSignal_list_1.emit(self.i - 1, 5, re_data["model_name"])
            self.TableDataSignal_list_1.emit(self.i - 1, 2, re_data["defects_count"])
            self.TableDataSignal_clear_1.emit(self.y)
            xxx=0
            for key in json.loads(re_data["defects_kind_chinese"]):
                self.TableDataSignal_detail_1.emit(xxx, 0, str(json.loads(re_data["defects_kind_chinese"])[key]))
                location = json.loads(re_data["defects_location"])
                cc = "(" + str(json.loads(location[key])['0']) + "," + str(
                    json.loads(location[key])['1']) + ")" + " " + "(" + str(json.loads(location[key])['2']) + "," + str(
                    json.loads(location[key])['3']) + ")"
                self.TableDataSignal_detail_1.emit(xxx, 1, cc)
                if json.loads(re_data['defects_kind'])[key]=="edge":
                    unit="mm"
                else:
                    unit="mm2"
                self.TableDataSignal_detail_1.emit(xxx, 2, str(json.loads(re_data["defects_area"])[key])+unit)
                self.TableDataSignal_detail_1.emit(xxx, 3, str(json.loads(re_data["confidence"])[key]))
                self.y += 1
                xxx += 1
            self.textBrowser.clear()
            self.textBrowser.append(re_data["image_name"])
            abc = {
                "image_name": re_data['image_name'],
                "image_size": re_data['image_size'],
                "image_path": re_data["image_path"],
                "date": re_data['date'],
                "defects_number": re_data['defects_count'],
                "defects_kind": re_data['defects_kind'],
                "defects_kind_chinese": re_data['defects_kind_chinese'],
                "defects_location": re_data['defects_location'],
                "confidence": re_data['confidence'],
                "model_path": self.model_path[0],

                "working_model": "real_time_detection",
                "line_frequency": "1650",
                "exposure_time": "100us",
                "defects_area": re_data['defects_area'],
                "level": re_data['level'],
            }
            try:
                create_db = edit_db()
                create_db.createdb(abc)
            except BaseException:
                traceback.format_exc()
                self.show_message("db_error")
        if name == "local":      #################################################本地检测####################################
            re_data=data
            self.i+=1
            skimage.io.imsave("test_img/"+re_data["image_name"],re_data["image_mask"].astype(numpy.uint8))
            model_name=self.model_path[0].split("/")[-1]
            x = re_data["image"].shape[1]
            y = re_data["image"].shape[0]
            frame = QImage(re_data["image"], x, y, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)
            self.scene = QGraphicsScene()
            self.scene.addItem(self.item)
            self.tuxiang_2.setScene(self.scene)
            if x == 4096:
                self.item.setScale(0.14)
            else:
                self.item.setScale(0.4)
            frame1 = QImage(re_data["image_mask"], x, y, QImage.Format_RGB888)
            pix1 = QPixmap.fromImage(frame1)
            self.item1 = QGraphicsPixmapItem(pix1)
            self.scene1 = QGraphicsScene()
            self.scene1.addItem(self.item1)
            self.tuxiang_6.setScene(self.scene1)
            if x==4096:
                self.item1.setScale(0.14)
            else:
                self.item1.setScale(0.4)
            self.TableDataSignal_list_2.emit(self.i - 1, 0, re_data["image_name"])
            self.TableDataSignal_list_2.emit(self.i - 1, 1, re_data['image_size'])
            self.TableDataSignal_list_2.emit(self.i - 1, 4, re_data["date"])
            self.TableDataSignal_list_2.emit(self.i - 1, 3,re_data["level"])
            self.TableDataSignal_list_2.emit(self.i - 1, 5, model_name)
            self.TableDataSignal_list_2.emit(self.i - 1, 2, re_data["defects_count"])
            self.TableDataSignal_clear_2.emit(self.y)

            xxx = 0

            for key in json.loads(re_data["defects_kind_chinese"]):
                self.TableDataSignal_detail_2.emit(xxx, 0, str(json.loads(re_data["defects_kind_chinese"])[key]))
                location=json.loads(re_data["defects_location"])
                cc="("+str(json.loads(location[key])['0'])+","+str(json.loads(location[key])['1'])+")"+" "+"("+str(json.loads(location[key])['2'])+","+str(json.loads(location[key])['3'])+")"
                self.TableDataSignal_detail_2.emit(xxx, 1, cc)
                if json.loads(re_data['defects_kind'])[key]=="edge":
                    unit="mm"
                else:
                    unit="mm2"
                self.TableDataSignal_detail_2.emit(xxx, 2, str(json.loads(re_data["defects_area"])[key])+unit)
                self.TableDataSignal_detail_2.emit(xxx, 3, str(json.loads(re_data["confidence"])[key]))
                self.y+=1
                xxx+=1
            self.textBrowser_2.clear()
            self.textBrowser_2.append(re_data["image_name"])
            data_r = {
                "image_name": re_data['image_name'],
                "date": re_data['date'],
                "defects_number": re_data['defects_count'],
                "defects_kind": re_data['defects_kind'],
                "defects_kind_chinese": re_data['defects_kind_chinese'],
                "defects_location": re_data['defects_location'],
                "confidence": re_data['confidence'],
                "model_path": self.model_path[0],
                "image_size": re_data['image_size'],
                "image_path": re_data["image_path"],
                "working_model": "local_detection",
                "line_frequency": "1650",
                "exposure_time": "100us",
                "defects_area": re_data['defects_area'],
                "level": re_data['level'],
            }
            try:
                create_db = edit_db()
                create_db.createdb(data_r)
            except BaseException:
                traceback.format_exc()
                self.show_message("db_error")
        if name == "collect":   #####################################图像采集#######################################
            self.i+=1
            image_name = time.strftime("%Y%m%d%H%M%S", time.localtime())+'.jpg'
            data1 = data[..., ::-1]  # rgb2bgr
            image_save_path=self.save_path+'/'+image_name
            cv2.imwrite(image_save_path,data1)
            x = data.shape[1]
            y = data.shape[0]
            frame = QImage(data, x, y, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)
            self.scene = QGraphicsScene()
            self.scene.addItem(self.item)
            self.tuxiang_3.setScene(self.scene)
            self.item.setScale(0.6)
            self.TableDataSignal_list_3.emit(self.i - 1, 0,image_name)
            self.TableDataSignal_list_3.emit(self.i - 1, 1, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            self.TableDataSignal_list_3.emit(self.i - 1, 2, self.save_path)
            self.TableDataSignal_list_3.emit(self.i - 1, 3, "1200")
            self.TableDataSignal_list_3.emit(self.i - 1, 4, "100us")
            self.TableDataSignal_detail_3.emit(0, 0, str(x)+"*"+str(y))
            self.TableDataSignal_detail_3.emit(0, 1, "rgb888")
            self.TableDataSignal_detail_3.emit(0, 2, "jpg")
            self.textBrowser_3.clear()
            self.textBrowser_3.append(image_name)
        if name == "find":  #################################历史查询####################################
            length=len(data)
            for i in range(length):
                db_data = json.loads(data[i][3])
                self.TableDataSignal_list_4.emit(i, 0, db_data["image_name"])
                self.TableDataSignal_list_4.emit(i, 1, db_data["image_size"])
                self.TableDataSignal_list_4.emit(i, 2, db_data["defects_number"])
                self.TableDataSignal_list_4.emit(i, 3, db_data["level"])
                self.TableDataSignal_list_4.emit(i, 4, db_data["date"])
                self.TableDataSignal_list_4.emit(i, 5, db_data["model_path"])
                self.TableDataSignal_list_4.emit(i, 6, db_data["line_frequency"])
                self.TableDataSignal_list_4.emit(i, 7, db_data["exposure_time"])
            defects=json.loads(data[length-1][3])
            try:
                image1 = cv2.imread(defects["image_path"])
                b,g,r=cv2.split(image1)  #bgr 2 rgb
                image =cv2.merge([r, g, b])
            except Exception:
                traceback.format_exc()
                image1=cv2.imread("mdfqt5/image/error.jpg")
                b, g, r = cv2.split(image1)
                image = cv2.merge([r, g, b])
            x = image.shape[1]
            y = image.shape[0]
            frame = QImage(image, x, y, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)
            self.scene = QGraphicsScene()
            self.scene.addItem(self.item)
            self.tuxiang_4.setScene(self.scene)
            if x == 4096:
                self.item.setScale(0.14)
            else:
                self.item.setScale(0.4)
            masked_image=[]
            xxx=0
            for key in json.loads(defects['defects_area']):
                location = json.loads(defects["defects_location"])
                x1,y1, x2 , y2= json.loads(location[key])['0'], json.loads(location[key])['1'], json.loads(location[key])['2'], json.loads(location[key])['3']
                cc = "(" + str(y1) + "," + str(x1)+ ")" + " " + "(" + str(y2) + "," + str(x2) + ")"
                self.TableDataSignal_detail_4.emit(xxx, 0, str(json.loads(defects["defects_kind_chinese"])[key]))
                self.TableDataSignal_detail_4.emit(xxx, 1, cc)
                if json.loads(defects['defects_kind'])[key]=="edge":
                    unit="mm"
                else:
                    unit="mm2"
                self.TableDataSignal_detail_4.emit(xxx, 2, str(json.loads(defects["defects_area"])[key])+unit)
                self.TableDataSignal_detail_4.emit(xxx, 3, str(json.loads(defects["confidence"])[key]))
                if xxx==0:
                    masked_image = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 5)
                    masked_image = cv2.putText(masked_image, str(json.loads(defects["defects_kind"])[key])+' '+str(json.loads(defects["confidence"])[key]), (int(x1), int(y1) - 6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2,
                                               (255, 0, 0), 2)
                else:
                    masked_image = cv2.rectangle(masked_image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 5)
                    masked_image = cv2.putText(masked_image, str(json.loads(defects["defects_kind"])[key]) + ' ' + str(json.loads(defects["confidence"])[key]), (int(x1), int(y1) - 6),
                                               cv2.FONT_HERSHEY_COMPLEX_SMALL, 2,
                                               (255, 0, 0), 2)
                    # cv2.imshow("das",masked_image)
                    # cv2.waitKey()
                xxx += 1
                self.y+=1


            frame1 = QImage(masked_image, x, y, QImage.Format_RGB888)
            pix1 = QPixmap.fromImage(frame1)
            self.item1 = QGraphicsPixmapItem(pix1)
            self.scene1 = QGraphicsScene()
            self.scene1.addItem(self.item1)
            self.tuxiang_7.setScene(self.scene1)
            if x == 4096:
                self.item1.setScale(0.14)
            else:
                self.item1.setScale(0.4)

            self.textBrowser_4.clear()
            self.textBrowser_4.append(data[length-1][1])

    def find_clicked(self,checked):  #历史查询 查询按钮
        st=self.dateTimeEdit.dateTime().toString(Qt.ISODate)
        end=self.dateTimeEdit_2.dateTime().toString(Qt.ISODate)
        st1=str.replace(st,"T"," ",1)
        end1 = str.replace(end, "T", " ", 1)
        if self.comboBox_2.currentText()=="实时检测":
            working_model="real_time_detection"
        elif self.comboBox_2.currentText()=="实时检测":
            working_model="local_detection"
        else:
            working_model = ""
        abc={
            "st_date": st1,
            "end_date": end1,
            "image_name": self.lineEdit.text(),
            "working_model":working_model,
        }
        try:
            find_db = edit_db()
            re_data=find_db.finddb(abc)
            if re_data!=[]:
                self.show_image("find",re_data)
            else:
                self.show_message("db_none")
        except Exception:
            traceback.format_exc()
            self.show_message("db_error")
        print("历史查询")
    def save_clicked(self,checked):
        print("路径选择", checked)
        self.save_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "D:/GPW/tf+pyqt-faster-r-cnn/fasterrcnn/data")
        print(self.save_path )  # 打印文件夹路径
    def file_clicked(self,checked): #图片选择函数
        self.files, self.file_type = QFileDialog.getOpenFileNames(self, "多文件选择", "../centermask/datasets/test2020/", "图像文件 (*.jpg);;图像文件 (*.bmp);;所有文件 (*.*)")
        print(self.files, self.file_type)
        print("文件选择", checked)
    def camera_clicked(self,checked):
        print("参数设置", checked)
        try:
            self.show_camera_panel.emit()
            self.parameter_flag=True
        except Exception:
            traceback.format_exc()
            self.show_message("camera_error")
    def suspend_clicked(self,checked):
        if self.start_detect_flag == True:
            print("实时检测暂停", checked)
        else:
            self.show_message("st_error")

    def suspend2_clicked(self, checked):
        if self.local_start_detect_flag==True:
            print("本地检测暂停", checked)
        else:
            self.show_message("st_error")
    def suspend3_clicked(self, checked):
        if self.start_collect_flag == True:
            print("采集暂停", checked)
        else:
            self.show_message("st_error")

    def detect_start_clicked(self,checked):
        if checked:
            if self.model_path != [] and self.save_path != []:
                self.start+=1
                self.hk = hkcamera()
                print("开始检测", checked)
                self.start_detect_flag = True
                self.hk.open_device()
                self._thread.setval("real_time")
            else:
                self.show_message("file_error")
                self.start_detect_flag = False
        else:
            self.hk.close_device()
            self.start_detect_flag = False
    def local_start_clicked(self,checked):
        if checked:

            if self.model_path!=[] and self.files !=[]:
                self.start+=1
                print("本地检测", checked)
                self.local_start_detect_flag = True
                self._thread1.setVal(self.files,"",self.model_path[0],"local",self.start)

            else:
                self.local_start_detect_flag = False
                self.show_message("file_error")
        else:
            self.local_start_detect_flag=False
    def collect_start_clicked(self,checked):
        if checked:
            if self.save_path!=[] and self.parameter_flag==True:
                print("图像采集",checked)
                self.hk = hkcamera()
                self.start_collect_flag = True
                self.hk.open_device()
                self._thread.setval("collect_image")
            else:
                self.show_message("file_error")
                self.start_collect_flag = False

        else:
            self.hk.close_device()
            self.start_collect_flag=False
    def model_clicked(self):
        self.model_path, self.model_type = QFileDialog.getOpenFileNames(self, "多文件选择", "../centermask/tools/",
                                     "模型文件 (*.pth);;所有文件 (*.*)")
        self.load_model+=1
        print("模型选择")
    def collect_image(self):
        print("已开始采集")
        image_data = self.hk.grab_image()
        self.show_image("collect", image_data)
        print("已完成采集")
    def real_time(self):
        image_data = self.hk.grab_image()
        model_name = self.model_path[0].split("/")[-1]
        try:
            self._thread1.setVal("", image_data, model_name, "real",self.start)
        except Exception:
            traceback.format_exc()
            self.show_message("model_error")
    def show_message(self,flag):
        if flag=="db_error":
            reply = QMessageBox.information(self,"提示","数据库错误",QMessageBox.Yes | QMessageBox.No)
        if flag=="model_error":
            reply = QMessageBox.information(self,"提示","模型导入错误",QMessageBox.Yes | QMessageBox.No)
        if flag=="camera_error":
            reply = QMessageBox.information(self,"提示","相机连接错误",QMessageBox.Yes | QMessageBox.No)
        if flag=="st_error":
            reply = QMessageBox.information(self,"提示","请先点击开始",QMessageBox.Yes | QMessageBox.No)
        if flag=="db_none":
            reply = QMessageBox.information(self,"提示","数据为空",QMessageBox.Yes | QMessageBox.No)
        if flag=="file_error":
            reply = QMessageBox.information(self,"提示","请设置相机参数、检测模型、检测图片、储存路径！",QMessageBox.Yes | QMessageBox.No)
        # if flag=="db_error":
        #     reply = QMessageBox.information(self,"提示","请先开始检测",QMessageBox.Yes | QMessageBox.No)
        # if flag=="db_error":
        #     reply = QMessageBox.information(self,"提示","请先开始检测",QMessageBox.Yes | QMessageBox.No)
        # if flag=="db_error":
        #     reply = QMessageBox.information(self,"提示","请先开始检测",QMessageBox.Yes | QMessageBox.No)
class TableData_list():
    def TableViewInit(self, tableView,Model):
        '''表格初始化'''
        try:
            self.HeaderList = ["图片名称","图像大小","缺陷数量","产品等级","检测日期","检测模型","采集行频","曝光时间",]
            '表格初始化'
            self.DataModel = Model
            self.DataModel.setHorizontalHeaderLabels(self.HeaderList)#
            self.tableView = tableView
            self.tableView.setModel(self.DataModel)
            #下面代码让表格100填满窗口
            self.tableView.horizontalHeader().setStretchLastSection(True)
            self.tableView.setColumnWidth(0, 100)
            self.tableView.setColumnWidth(1, 100)
            self.tableView.setColumnWidth(2, 100)
            self.tableView.setColumnWidth(3, 100)
            self.tableView.setColumnWidth(4, 100)
            self.tableView.setColumnWidth(5, 100)
            self.tableView.setColumnWidth(6, 100)
            self.tableView.setColumnWidth(7, 100)

            return True
        except Exception as e:
            traceback.format_exc()
            logging(e)

    def Model_setItem(self, row, column, data):
        '''表格添加数据：第row行，column列数据更改为data'''
        self.DataModel.setItem(row, column, QStandardItem(data))
class TableData_local_list():
    def TableViewInit(self, tableView,Model):
        '''表格初始化'''
        try:
            self.HeaderList = ["图片名称","图像大小","缺陷数量","产品等级","检测日期","检测模型",]
            '表格初始化'
            self.DataModel = Model
            self.DataModel.setHorizontalHeaderLabels(self.HeaderList)#
            self.tableView = tableView
            self.tableView.setModel(self.DataModel)
            #下面代码让表格100填满窗口
            self.tableView.horizontalHeader().setStretchLastSection(True)
            self.tableView.setColumnWidth(0, 100)
            self.tableView.setColumnWidth(1, 100)
            self.tableView.setColumnWidth(2, 100)
            self.tableView.setColumnWidth(3, 100)
            self.tableView.setColumnWidth(4, 100)
            self.tableView.setColumnWidth(5, 100)


            return True
        except Exception as e:
            traceback.format_exc()
            logging(e)

    def Model_setItem(self, row, column, data):
        '''表格添加数据：第row行，column列数据更改为data'''
        self.DataModel.setItem(row, column, QStandardItem(data))
class TableData_detail():
    def TableViewInit(self, tableView,Model):
        '''表格初始化'''
        try:
            self.HeaderList = ["缺陷种类","缺陷位置","缺陷尺寸","置信度"]
            '表格初始化'
            self.DataModel = Model
            self.DataModel.setHorizontalHeaderLabels(self.HeaderList)#
            self.tableView = tableView
            self.tableView.setModel(self.DataModel)
            #下面代码让表格100填满窗口
            self.tableView.horizontalHeader().setStretchLastSection(True)

            self.tableView.setColumnWidth(0, 140)
            self.tableView.setColumnWidth(1, 240)
            self.tableView.setColumnWidth(2, 100)
            self.tableView.setColumnWidth(3, 100)
            return True
        except Exception as e:
            traceback.format_exc()
            logging(e)

    def Model_setItem(self, row, column, data):
        '''表格添加数据：第row行，column列数据更改为data'''
        self.DataModel.setItem(row, column, QStandardItem(data))
    def Model_clear(self,row):
        for i in range(row):
            self.DataModel.removeRow(i)
class TableData_collect_list():
    def TableViewInit(self, tableView,Model):
        '''表格初始化'''
        try:
            self.HeaderList = ["图片名称","采集日期","保存路径","采集行频","曝光时间"]
            '表格初始化'
            self.DataModel = Model
            self.DataModel.setHorizontalHeaderLabels(self.HeaderList)#
            self.tableView = tableView
            self.tableView.setModel(self.DataModel)
            #下面代码让表格100填满窗口
            self.tableView.horizontalHeader().setStretchLastSection(True)
            self.tableView.setColumnWidth(0, 120)
            self.tableView.setColumnWidth(1, 120)
            self.tableView.setColumnWidth(2, 120)
            self.tableView.setColumnWidth(3, 100)
            self.tableView.setColumnWidth(4, 100)
            return True
        except Exception as e:
            traceback.format_exc()
            logging(e)

    def Model_setItem(self, row, column, data):
        '''表格添加数据：第row行，column列数据更改为data'''
        self.DataModel.setItem(row, column, QStandardItem(data))
class TableData_collect_detail():
    def TableViewInit(self, tableView,Model):
        '''表格初始化'''
        try:
            self.HeaderList = ["图像大小","像素种类","图片格式"]
            '表格初始化'
            self.DataModel = Model
            self.DataModel.setHorizontalHeaderLabels(self.HeaderList)#

            self.tableView = tableView
            self.tableView.setModel(self.DataModel)
            self.tableView.setRowHeight(0, 120)
            # 下面代码让表格100填满窗口
            self.tableView.horizontalHeader().setStretchLastSection(True)
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView.verticalHeader().setVisible(False)  #

            return True
        except Exception as e:
            traceback.format_exc()
            logging(e)

    def Model_setItem(self, row, column, data):
        '''表格添加数据：第row行，column列数据更改为data'''
        self.DataModel.setItem(row, column, QStandardItem(data))
    def Model_clear(self,row):
        for i in range(row):
            self.DataModel.removeRow(i)
if __name__=='__main__':
    app = QApplication(sys.argv)
    window=Detection()
    window.show()
    sys.exit(app.exec_())

