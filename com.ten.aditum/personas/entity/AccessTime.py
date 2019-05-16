from dataclasses import dataclass


@dataclass
class AccessTime:
    id: int
    personnelId: str
    averageEarliestAccessTime: str
    averageEarliestAccessCount: int
    averageLatestAccessTime: str
    averageLatestAccessCount: int
    averageDailyFrequency: int
    averageDailyFrequencyCount: int
    createTime: str
    updateTime: str
    isDeleted: int

    def __init__(self, json):
        if json.get("id") is None:
            pass
        self.id = json.get("id")
        self.personnelId = json.get("personnelId")
        self.averageEarliestAccessTime = json.get("averageEarliestAccessTime")
        self.averageEarliestAccessCount = json.get("averageEarliestAccessCount")
        self.averageLatestAccessTime = json.get("averageLatestAccessTime")
        self.averageLatestAccessCount = json.get("averageLatestAccessCount")
        self.averageDailyFrequency = json.get("averageDailyFrequency")
        self.averageDailyFrequencyCount = json.get("averageDailyFrequencyCount")
        self.createTime = json.get("createTime")
        self.updateTime = json.get("updateTime")
        self.isDeleted = json.get("isDeleted")
