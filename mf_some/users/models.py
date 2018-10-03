from django.db import models
from django.urls import reverse
from improved_user.model_mixins import AbstractUser


class FriendRelationship(models.Model):
    STATUS_INVITED = 'invited'
    STATUS_ACCEPTED = 'accepted'

    FRIEND_STATUS = (
        (STATUS_INVITED, 'Invited'),
        (STATUS_ACCEPTED, 'Accepted'),
    )

    from_user = models.ForeignKey('users.User', related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey('users.User', related_name='to_user', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=FRIEND_STATUS, default=STATUS_INVITED)

    def __str__(self):
        return f'{self.from_user} -> {self.to_user} [{self.status}]'

    def accept_invite(self):
        if self.status == self.STATUS_ACCEPTED:
            return

        self.status = self.STATUS_ACCEPTED
        self.save(update_fields=['status'])

        # create reverse relation on accept
        self.to_user.add_friend(self.from_user, status=self.STATUS_ACCEPTED)


class User(AbstractUser):
    friends = models.ManyToManyField('self', through='users.FriendRelationship',
                                     symmetrical=False, related_name='friend_relationships+')

    def get_absolute_url(self):
        return reverse('users:detail', args=[str(self.id)])

    def add_friend(self, user, status=FriendRelationship.STATUS_INVITED):
        friend, created = FriendRelationship.objects.get_or_create(
            from_user=self,
            to_user=user, defaults={'status': status}
        )

    def remove_friend(self, user, symmetrical=True):
        FriendRelationship.objects.filter(
            from_user=self,
            to_user=user
        )

        if symmetrical:
            user.remove_friend(self, False)

    def get_friends(self, status=FriendRelationship.STATUS_ACCEPTED):
        return self.friends.filter(to_user__status=status, to_user__from_user=self)

    def get_pending_invitations(self):
        return FriendRelationship.objects.filter(status=FriendRelationship.STATUS_INVITED, to_user=self)
