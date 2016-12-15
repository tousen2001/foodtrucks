from mysite import db


class MobileFoodFacilityPermit(db.Model):
    __tablename__ = 'mobile_food_facility_permit'

    locationid = db.Column(db.Integer, nullable=True, primary_key=True)
    applicant = db.Column(db.String(500), nullable=True)
    facilitytype = db.Column(db.String(500), nullable=True)
    cnn = db.Column(db.Integer, nullable=True)
    locationdescription = db.Column(db.String(500), nullable=True)
    address = db.Column(db.String(500), nullable=True)
    blocklot = db.Column(db.String(500), nullable=True)
    block = db.Column(db.Integer, nullable=True)
    lot = db.Column(db.String(500), nullable=True)
    permit = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(500), nullable=True)
    fooditems = db.Column(db.String(500), nullable=True)
    x = db.Column(db.NUMERIC, nullable=True)
    y = db.Column(db.NUMERIC, nullable=True)
    latitude = db.Column(db.NUMERIC, nullable=True)
    longitude = db.Column(db.NUMERIC, nullable=True)
    schedule = db.Column(db.String(500), nullable=True)
    dayshours = db.Column(db.String(500), nullable=True)
    noisent = db.Column(db.String(500), nullable=True)
    approved = db.Column(db.String(500), nullable=True)
    received = db.Column(db.String(500), nullable=True)
    priorpermit = db.Column(db.Boolean(1), nullable=True)
    expirationdate = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(500), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}