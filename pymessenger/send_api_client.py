from pymessenger.bot import Bot

class SendApiClient(Bot):
    def send(self, recipient_id, message_type, **kwargs):
        if message_type == 'text':
            message_text = kwargs['text']
            response = self.send_text_message(recipient_id, message_text)
        elif message_type == 'button':
            message_text = kwargs['text']
            buttons = kwargs['buttons']
            response = self.send_button_message(recipient_id, message_text, buttons)
        elif message_type == 'image_url':
            image_url = kwargs['image_url']
            response = self.send_image_url(recipient_id, image_url)
        else:
            response = "Message type {0} currently unsupported.".format(message_type)
        return response

    def _send_payload(self, payload):
        request_endpoint = '{0}/me/messages'.format(self.graph_url)
        response = requests.post(
            request_endpoint,
            params=self.auth_args,
            json=payload
        )
        return response
