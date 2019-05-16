from dataclasses import dataclass


@dataclass
class Person:
    id: int
    personnelId: str
    personnelName: str
    communityId: str
    personnelAddress: str
    personnelPhone: str
    createTime: str
    updateTime: str
    isDeleted: int

    def __init__(self, json):
        if json.get("id") is None:
            pass
        self.id = json.get("id")
        self.personnelId = json.get("personnelId")
        self.personnelName = json.get("personnelName")
        self.communityId = json.get("communityId")
        self.personnelAddress = json.get("personnelAddress")
        self.personnelPhone = json.get("personnelPhone")
        self.createTime = json.get("createTime")
        self.updateTime = json.get("updateTime")
        self.isDeleted = json.get("isDeleted")
