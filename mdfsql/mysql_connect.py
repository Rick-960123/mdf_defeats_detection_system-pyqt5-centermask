import mysql.connector
import json
class edit_db():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            port="4306",
            user="root",
            passwd="mvai123456",
            database="mdf_database",
        )
        # self.data={
        #             "image_name":"2.jpg",
        #             "date":"2019-11-15 10:52:59",
        #             "defects_number":"2",
        #             "defects_kind":"soft,glue_spot",
        #             "defects_location":"40,50,100,120",
        #             "confidence":"0.999",
        #             "model_path":"D:/GPW/model",
        #             "image_size":"1024*1024",
        #             "image_path":"D:/GPW/images",
        #             "working_model":"local",
        #             "line_frequency":"1200",
        #             "exposure_time":"100us"
        #             }
        self.mycursor = self.mydb.cursor()
    def createdb(self,val):
        sql = "INSERT INTO mdf_json (image_name,date,working_model,info) VALUES (%s,%s,%s,%s)"
        data=[val["image_name"], val["date"],val["working_model"],json.dumps(val)]
        self.mycursor.execute(sql, data)
        self.mydb.commit()
        self.mycursor.close()
    def finddb(self,val):
        data=[]
        sql = ""
        if val["image_name"]=="" and val["working_model"]=="":
            data = [val["st_date"], val["end_date"]]
            sql = "SELECT * FROM mdf_json WHERE date>%s and date<%s"
        if val["image_name"]=="" and val["working_model"]!="":
            data = [val["working_model"], val["st_date"], val["end_date"]]
            sql = "SELECT * FROM mdf_json WHERE working_model=%s and date>%s and date<%s "
        if val["working_model"]=="" and val["image_name"]!="":
            data = [val["st_date"], val["end_date"], val["image_name"]]
            sql = "SELECT * FROM mdf_json WHERE date>%s and date<%s and image_name=%s"
        if val["image_name"]!="" and val["working_model"]!="":
            data = [val["working_model"], val["st_date"], val["end_date"],val["image_name"]]
            sql = "SELECT * FROM mdf_json WHERE working_model=%s and date>%s and date<%s and image_name=%s"
        self.mycursor.execute(sql, data)
        find_data=self.mycursor.fetchall()  #返回查询结果
        self.mycursor.close()
        return  find_data
    def editdb(self,val):
        sql = "INSERT INTO mdf_json (image_name,image_path, ) VALUES (%s, %s)"
        self.mycursor.execute(sql, val)
        self.mycursor.close()
    def deletedb(self,val):
        sql = "INSERT INTO mdf_json (image_name,image_path, ) VALUES (%s, %s)"
        self.mycursor.execute(sql, val)
        self.mycursor.close()

if __name__ == '__main__':
    abc = {
        "st_date":"2019-11-10 10:52:59",
        "end_date":"2020-12-19 10:56:59",
        "image_name": "",
        "date": "2019-11-15 10:56:59",
        "defects_number": "2",
        "defects_kind": ['胶斑'],
        "defects_location": [ 68, 136, 215, 284],
        "confidence": [0.999],
        "model_path": "D:/GPW/model",
        "image_size": "1024*1024",
        "image_path": "D:/GPW/images",
        "working_model": "",
        "line_frequency": "1200",
        "exposure_time": "100us",
        "defects_area":"100"
    }
    aa=['01DSC03974.jpg', '2019-12-03 18:01:09', '1', "['胶斑']", '[array([ 68, 136, 215, 284])]', '[0.99996936]',
     'D:/GPW/tf+pyqt-faster-r-cnn/maskrcnn/model/mask_rcnn_coco_0027.h5', '(800, 800, 3)',
     'D:/GPW/tf+pyqt-faster-r-cnn/fasterrcnn/data/demo/01DSC03974.jpg', 'local_detection', '1650', '100us', '[0]']
    abcd =edit_db
    # abcd().createdb(abc)
    da=abcd().finddb(abc)
    print(da)


