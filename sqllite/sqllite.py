from peewee import *
database = MYSQLDatabase('mdf',user="root",host="127.0.0.1",port="3306")
class MDF(Model):
        st_date=DateField()
        end_date=DateField(),
        image_name=charField(),
        date=DateField(),
        defects_number=charField(),
        defects_kind=charField()
        defects_location=charField(),
        confidence=charField(),
        model_path=charField(),
        image_size=charField(),
        image_path=charField(),
        working_model=charField(),
        line_frequency=charField(),
        exposure_time=charField(),
        defects_area=charField(),
        class Meta:
                database=database
MDF.create_table()
data = MDF(image_name="abc")
data.save()
