from prefect_email import EmailServerCredentials, email_send_message
from typing import List
from prefect import flow

@flow
def sample_email_send_message(email_addresses: List[str]):
    email_server_credentials = EmailServerCredentials.load('mailblock')
    for email_address in email_addresses:
        subject = email_send_message.with_options(name=f"email{email_address}").submit(
            email_server_credentials = email_server_credentials,
            subject = "Sample Task Alert",
            msg = "This is to notify you of a successful deployment!!! Check Server UI for details",
            email_to = email_address,
        )
sample_email_send_message(["fogboe@gmail.com"])