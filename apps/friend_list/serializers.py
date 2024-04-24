from rest_framework import serializers
from apps.friend_list.models import FriendRequest
from apps.users.models import User
from apps.users.serializers import RegisterResponseSerializer


class FriendRequestBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = [
            "id",
            "status",
            "sent_to",
        ]
    
    def validate_sent_to(self, validated_data):
        if validated_data == self.context.get("request").user:
            raise serializers.ValidationError("can't send request to yourself")
        if FriendRequest.objects.filter(sent_from=self.context.get("request").user, sent_to=validated_data).exists():
            raise serializers.ValidationError("already sent friend-request")
        return validated_data


class FriendRequestSerializer(FriendRequestBaseSerializer):
    sent_from = serializers.SerializerMethodField()
    sent_to = serializers.SerializerMethodField()

    class Meta(FriendRequestBaseSerializer.Meta):
        fields = FriendRequestBaseSerializer.Meta.fields + ["sent_from", "sent_to"]
    

    def get_sent_from(self, obj):
        if obj:
            return RegisterResponseSerializer(obj.sent_from).data

    def get_sent_to(self, obj):
        if obj:
            return RegisterResponseSerializer(obj.sent_to).data


class FriendRequestActionSerializer(serializers.Serializer):
    action = serializers.CharField()

    class Meta:
        fields = ["action"]
    
    def validate_action(self, validated_data):
        if validated_data not in ["accept", "decline"]:
            raise serializers.ValidationError("action must be accept or decline")
        return validated_data