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
