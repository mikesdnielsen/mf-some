import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Post


class LikeConsumer(WebsocketConsumer):
    def connect(self):
        if self.scope['user'].is_anonymous:
            self.close()

        else:
            self.post_id = self.scope['url_route']['kwargs']['post_id']

            async_to_sync(self.channel_layer.group_add)(
                self.post_id,
                self.channel_name
            )

            self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.post_id,
            self.channel_name
        )

    def receive(self, text_data):
        print('receive text_data', text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.post_id,
            {
                'type': 'like_post',
                'message': self.post_id
            }
        )

    def like_post(self, event):
        post = Post.objects.get(pk=self.post_id)
        post.likes.create(user=self.scope['user'])
        post.save()

        self.send(text_data=json.dumps({
            'message': post.likes.count()
        }))
