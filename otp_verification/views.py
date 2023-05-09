from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .helper import *
from rest_framework import status
from .serializers import *



# {"phone": "7427089473"}
class OTPsend(APIView):
    def post(self, request):
        serializer = PhoneOTPSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            phone_number = "+91" + data['phone']
            MessageHandler(phone_number).send_otp_via_message()
            return Response({"message": "OTP sent to "+ phone_number}, status = status.HTTP_201_CREATED)
        return Response({"message": "serializer.is_valid() returned False"}, status=status.HTTP_400_BAD_REQUEST)


# {"phone": "7427089473", "otp": "123456"}
class OTPverify(APIView):
    def post(self, request):
        serializer = PhoneOTPSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            phone_number = "+91" + data['phone']
            otp = data['otp']
            verify = MessageHandler(phone_number).verify_message_otp(otp)
            if verify == 'approved':
                return Response({"message": "OTP Verified Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid OTP"})
        return Response({"message": "serializer.is_valid() returned False"}, status=status.HTTP_400_BAD_REQUEST)




# class OTPsend(APIView):
#     def post(self, request):
#         serializer = PhoneOTPSerializer(data=request.data)
#         if serializer.is_valid():
#             # Extract validated data
#             data = serializer.validated_data
#             phone_number = "+91" + data['phone']

#             # Save PhoneOTP to our model


#             # Send OTP message
#             MessageHandler(phone_number).send_otp_via_message()
#             return Response({"message": "OTP sent to "+ phone_number}, status = status.HTTP_201_CREATED)

#         return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# class OTPverify(APIView):
#     def post(self, request):
#         serializer = PhoneOTPSerializer(data=request.data)
#         if serializer.is_valid():
#             data = serializer.validated_data
#             phone_number = "+91" + data['phone']
#             otp = data['otp']
#             verify = MessageHandler(phone_number).verify_message_otp(otp)
#             if verify == 'approved':
#                 PhoneOTP.object.get("")
#                 return Response({"message": "OTP Verified Successfully"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"message": "Invalid OTP"})
#         return Response({"message": "serializer.is_valid() returned False"}, status=status.HTTP_400_BAD_REQUEST)

