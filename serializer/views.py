from rest_framework.response import Response
#from rest_framework.decorators import api_view  #function based views
from rest_framework.views import APIView  #class based views
from rest_framework import status #showing proper error form
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializer import WatchListSerializer,StreamPlatformSerializer

class StreamPlatformAV(APIView):
    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Movie Not Found'} , status=status.HTTP_404_NOT_FOUND)

        serializer=StreamPlatformSerializer(platform,context={'request':request})
        return Response(serializer.data)

    def put(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            platform=StreamPlatform.objects.get(pk=pk)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk) 
        platform.delete()                         #delete it 
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class WatchListAV(APIView):
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie Not Found'} , status=status.HTTP_404_NOT_FOUND)

        serializer=WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            movie=WatchList.objects.get(pk=pk)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk) 
        movie.delete()                         #delete it 
        return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET','POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):

#     if request.method == 'GET':              #visualize data
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie Not Found'} , status=status.HTTP_404_NOT_FOUND)

#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie=Movie.objects.get(pk=pk)
        
#         serializer=MovieSerializer(movie,data=request.data)  #add data
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movie=Movie.objects.get(pk=pk) 
        
#         movie.delete()                         #delete it 
#         return Response(status=status.HTTP_204_NO_CONTENT)


