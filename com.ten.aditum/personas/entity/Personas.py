from dataclasses import dataclass


@dataclass
class Personas:
    personnelId: str
    labelId: str
    labelName: str
    labelType: int
    personasList: []
    createTime: str
    updateTime: str
    isDeleted: int

    def __init__(self, json):
        self.personnelId = json.get("personnelId")
        self.labelId = json.get("labelId")
        self.labelName = json.get("labelName")
        self.labelType = json.get("labelType")
        self.personasList = json.get("personasList")
        self.createTime = json.get("createTime")
        self.updateTime = json.get("updateTime")
        self.isDeleted = json.get("isDeleted")
