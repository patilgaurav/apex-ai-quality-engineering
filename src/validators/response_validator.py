
class ResponseValidator:

    @staticmethod
    def validate_balance_schema(data: dict) -> bool:
        required_fields = {
            "customer_id": int,
            "currency": str,
            "balance": int
        }

        for field, expected_type in required_fields.items():

            if field not in data:
                return False

            if type(data[field]) is not expected_type:
                return False

        return True
