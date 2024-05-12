import os
import random
class VerificationResponse:
    def __init__(self, successful, error_message):
        self.successful = successful
        self.error_message = error_message


def send_verification_code(self, phone_number):
    try:
        verification = self.client.verify.services(os.getenv("VERIFY_SERVICE_SID")) \
            .verifications.create(to=phone_number, channel='sms')

        if verification.status == 'pending':
            return VerificationResponse(True, None)
        else:
            return VerificationResponse(False, "Verification failed")

    except Exception as e:
        return VerificationResponse(False, f"An error occurred: {str(e)}")



def generate_verification_code():
    code = ''.join(str(random.randint(0, 9)) for _ in range(6))
    return code

