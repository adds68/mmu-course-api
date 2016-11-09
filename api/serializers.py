from rest_framework import serializers
from course.models import Course, Tutor

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('id', 'name', 'room', 'school', 'email')

class CourseSerializer(serializers.ModelSerializer): 
    tutor = TutorSerializer(many=True)

    def create(self, validated_data):
        tutors_data = validated_data.pop("tutor")
        course = Course.objects.create(**validated_data)
        for tutor_data in tutors_data:
            tutor = Tutor.objects.create(**tutor_data)
            course.tutor.add(tutor) 
        return course

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.credits = validated_data.get("credits", instance.credits)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.about = validated_data.get("about", instance.about)
        tutors_data = validated_data.pop("tutor")
        for tutor_data in tutors_data:
            try:
                tutor = Tutor.objects.get(pk=pk)
            except tutor.DoesNotExist:
                tutor = Tutor(**tutor_data)
                instance.tutor.add(tutor)
        return instance

    class Meta:
        model = Course
        fields = ('id', 'name', 'credits', 'duration', 'tutor', 'about')
