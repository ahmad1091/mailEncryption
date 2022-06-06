from operator import ge
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .helpers import AESCipher,sendDestructionEmail
from .serializers import NoteSerializer
from cryptoMail.settings import CRYPTO_KEY
from .models import Note
import datetime

# Create your views here.

@api_view(['GET', 'OPTIONS'])
def home(request):
    return Response({'msg': 'SUCCESS'}, status=status.HTTP_200_OK)


class privateNote(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [ProjectAddPermission]
    def get(self, request, pk):
        obj = Note.objects.get(pk=pk)
        isDestroyed = obj.isDestroyed
        notificationEmail = obj.notificationEmail
        if isDestroyed:
            return Response({'msg':'this message has been destroyed'}, status=status.HTTP_200_OK)
        else:
            destructionOption = obj.destructionOption
            C = AESCipher(CRYPTO_KEY)
            if destructionOption == 1:
                f = C.decrypt(obj.note)
                obj.isDestroyed = True
                obj.save()
                sendDestructionEmail(notificationEmail,'Your Message has successfully been destructed')
                return Response({'msg':f}, status=status.HTTP_200_OK)
            else:
                destructionDate = obj.destructionDate
                current_datetime = datetime.datetime.now()  
                print(current_datetime.isoformat())
                if current_datetime.isoformat()>destructionDate.isoformat():
                    obj.isDestroyed = True
                    obj.save()
                    sendDestructionEmail(notificationEmail,'Your Message has successfully been destructed')
                    return Response({'msg':'this message is out of date'}, status=status.HTTP_200_OK)
                else:
                    f = C.decrypt(obj.note)
                    return Response({'msg':f}, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        rawMessage = data['note']
        C = AESCipher(CRYPTO_KEY)
        encryptedNote = C.encrypt(rawMessage)
        data._mutable = True
        data['note'] = encryptedNote
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            saved = serializer.save()
            pk = saved.id
            genertedUrl = f'http://localhost:8000/note/{pk}'
            return Response({'msg': 'SUCCESS',"URL":genertedUrl}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # key = CRYPTO_KEY
        # print(key)
        # C = AESCipher(CRYPTO_KEY)
        # d = C.encrypt(rawMessage)
        # print(d)
        # pk=159
        # genertedUrl = f'http://localhost:8000/note/{pk}'
        # print(genertedUrl)
        # return Response({'msg': 'SUCCESS',"URL":genertedUrl}, status=status.HTTP_200_OK)
        

