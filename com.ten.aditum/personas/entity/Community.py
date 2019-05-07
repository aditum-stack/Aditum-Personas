class Community:

    def __init__(self):
        self.id = None
        self.communityId = None
        self.communityName = None
        self.communityCity = None
        self.communityAddress = None
        self.deviceCount = None
        self.deviceOnlineCount = None
        self.createTime = None
        self.updateTime = None
        self.isDeleted = None

    @property
    def id(self):
        return self.id

    @property
    def communityId(self):
        return self.communityId

    @property
    def communityName(self):
        return self.communityName

    @property
    def communityCity(self):
        return self.communityCity

    @property
    def communityAddress(self):
        return self.communityAddress

    @property
    def deviceCount(self):
        return self.deviceCount

    @property
    def deviceOnlineCount(self):
        return self.deviceOnlineCount

    @property
    def createTime(self):
        return self.createTime

    @property
    def updateTime(self):
        return self.updateTime

    @property
    def isDeleted(self):
        return self.isDeleted

    @id.setter
    def id(self, value):
        self._id = value

    @communityId.setter
    def communityId(self, value):
        self._communityId = value

    @communityName.setter
    def communityName(self, value):
        self._communityName = value

    @communityCity.setter
    def communityCity(self, value):
        self._communityCity = value

    @communityAddress.setter
    def communityAddress(self, value):
        self._communityAddress = value

    @deviceCount.setter
    def deviceCount(self, value):
        self._deviceCount = value

    @deviceOnlineCount.setter
    def deviceOnlineCount(self, value):
        self._deviceOnlineCount = value

    @createTime.setter
    def createTime(self, value):
        self._createTime = value

    @updateTime.setter
    def updateTime(self, value):
        self._updateTime = value

    @isDeleted.setter
    def isDeleted(self, value):
        self._isDeleted = value
