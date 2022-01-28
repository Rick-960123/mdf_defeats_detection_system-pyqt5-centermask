from peewee import *
connect = SqliteDatabase('sqllite/mdf.db')

class Mdf(Model):
        st_date=DateField()
        end_date=DateField(),
        image_name=CharField(),
        date=DateField(),
        defects_number=CharField(),
        defects_kind=CharField()
        defects_location=CharField(),
        confidence=CharField(),
        model_path=CharField(),
        image_size=CharField(),
        image_path=CharField(),
        working_model=CharField(),
        line_frequency=CharField(),
        exposure_time=CharField(),
        defects_area=CharField(),
        class Meta:
                database=connect
if __name__=="__main__":
        db = Mdf()
        db.image_name="abc.png"
        db.save()
        for data in Mdf.select():
                print(data)