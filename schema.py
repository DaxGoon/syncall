from app import ma


class RecordsSchema(ma.Schema):
    """Schema for serialization"""

    class Meta:
        fields = ("id", "message", "signed_message")


message_schema = RecordsSchema()
