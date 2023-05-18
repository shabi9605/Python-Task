from marshmallow import Schema, fields, validates, ValidationError


# in flask e use marshmallow schema instaed of forms in django
class QuadraticForm(Schema):
    a = fields.Float(required=True)
    b = fields.Float(required=True)
    c = fields.Float(required=True)

    @validates('a')
    def validate_a(self, obj):
        if obj == 0:
            raise ValidationError("The value of a not equal to zero")
        