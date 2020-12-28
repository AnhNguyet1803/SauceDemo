class CheckOutStepOne:
    def __init__(self, firstname, lastname, postalcode):
        self.firstname = firstname
        self.lastname = lastname
        self.postalcode = postalcode

    def __str__(self):
        # return '{"name" : "%s", "desc" : "%s","price" : "%s"' % (self.name, self.desc, self.price)
        return "firsname is '%s', lastname is '%s', postalcode is '%s'" % (self.firstname, self.lastname,
                                                                           self.postalcode)
