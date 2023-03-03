import datetime


class packagesClass:
    def __init__(self,id,address,city,state,zip,deadline,kilo,notes,start,location,status,deliveredAt):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        if self.deadline != 'EOD':
            self.deadline = datetime.timedelta(float(deadline))
        self.kilo = kilo
        self.notes = notes
        self.start = start
        self.location = location
        self.status = status
        self.deliveredAt = deliveredAt

    def stat(self, src):
        # used to assign in route delivered and at hub
        if self.deliveredAt > src and self.start < src:
            # compare delivery time and package start time to search time.
            # if greater than and less than respectively package is in route
            self.status = "in route"
            self.deliveredAt = "On the way"
            # if package start is greater than search the package has been delivered
        elif self.start < src:
            self.status = "Delivered"
            # otherwise the package has not yet left the hub.
        else:
            self.status = "At hub"
            self.deliveredAt = "Package not yet out for delivery"

    def __str__(self):
        return "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s"%("ID:",self.id, "Address:",self.address," City: ", self.city, " State: " , self.state , " Zip: ", self.zip, " Deadline: " , self.deadline , " Weight: " , self.kilo ,  "Deadline:Delivery Status: ",self.status," Delivered At: ",self.deliveredAt,'\n')

