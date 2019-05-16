from dataclasses import dataclass


@dataclass
class AccessAddress:
    id: int
    personnelId: str
    firstAddress: str
    firstAddressCount: int
    secondAddress: str
    secondAddressCount: int
    totalAddress: str
    totalAddressCount: int
    totalCount: int
    createTime: str
    updateTime: str
    isDeleted: int

    def __init__(self, json):
        if json.get("id") is None:
            pass
        self.id = json.get("id")
        self.personnelId = json.get("personnelId")
        self.firstAddress = json.get("firstAddress")
        self.firstAddressCount = json.get("firstAddressCount")
        self.secondAddress = json.get("secondAddress")
        self.secondAddressCount = json.get("secondAddressCount")
        self.totalAddress = json.get("totalAddress")
        self.totalAddressCount = json.get("totalAddressCount")
        self.totalCount = json.get("totalCount")
        self.createTime = json.get("createTime")
        self.updateTime = json.get("updateTime")
        self.isDeleted = json.get("isDeleted")
