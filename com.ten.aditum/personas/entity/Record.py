class Record:

    def __init__(self, id, imei, personel_id, visit_time, visit_status, is_deleted):
        self.is_deleted = is_deleted
        self.visit_status = visit_status
        self.visit_time = visit_time
        self.personel_id = personel_id
        self.imei = imei
        self.id = id

    def createInstance(self, id, imei, personel_id, visit_time, visit_status, is_deleted):
        self.is_deleted = is_deleted
        self.visit_status = visit_status
        self.visit_time = visit_time
        self.personel_id = personel_id
        self.imei = imei
        self.id = id
