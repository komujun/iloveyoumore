from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse,HttpResponse

from django.views.decorators.http import require_GET

import numpy as np
import pandas as pd
import tensorflow as tf
from keras import backend as K
from keras.models import load_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
import face_recognition as fr
import cv2
from firebase_admin import credentials, initialize_app, storage
from keras.preprocessing import image
from PIL import Image
from rest_framework import status
from .models import *
from .serializers import *
import datetime
from django.utils import timezone
import urllib.request

import socket
import sys
import os

cred = credentials.Certificate("./vue-you-279005-64de93f2a211.json")
initialize_app(cred, {'storageBucket': 'vue-you-279005.appspot.com'})

def _load_model_from_path(path):
    global gmodel
    gmodel = load_model(path)  # keras function

_load_model_from_path('./backend/facial_expression_recognition.h5')

@api_view(['POST'])
def get_result(request):
    if request.method== 'POST':

        print(request.data)

        data = request.data

        # p1,p2,relationship,img_path->url 가 들어옴
        url  = data['img_path']
        urllib.request.urlretrieve(url, "test.jpg")

        filename = "test"


        # model load
        # 감정 분석 모델을 import해서 사진을 넣어 결과를 돌려받는다.
        img = fr.load_image_file('test.jpg', mode="L")  # 사진
        face_locations = fr.face_locations(img)



        length = len(face_locations)
        if length != 2:
            return Response({'message': '사진에 찍힌 사람이 두명이 아닙니다'}, status=400)
        p1 = 0.0
        p2 = 0.0
        cnt=1
        for (top, right, bottom, left) in face_locations:


            crop = img[top:bottom, left:right]
            crop = cv2.resize(crop, (48, 48))

            x = image.img_to_array(crop)
            x = np.expand_dims(x, axis=0)

            x /= 255

            custom = gmodel.predict(x)

            if cnt==1 :
                p1 = custom[0][3]
            else :
                p2 = custom[0][3]
            cnt += 1



        # 와중에 파이어베이스에 페이스디텍션뒤 크롭한 얼굴사진을 올린다
        img2 = fr.load_image_file('test.jpg')
        im = Image.open('test.jpg')
        face_locations = fr.face_locations(img2)
        cnt=1
        for (top, right, bottom, left) in face_locations:
            cropImage = im.crop((left, top, right, bottom))
            cropImage.save('test-crop'+str(cnt)+'.jpg')
            cnt += 1
            #crop을 파이어 베이스에 올리기

        # Put your local file path
        fileName = "test-crop1.jpg"
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
        blob.make_public()
        print("your file url", blob.public_url)
        returl1 = blob.public_url
        fileName = "test-crop2.jpg"
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
        blob.make_public()
        print("your file url", blob.public_url)
        returl2 = blob.public_url

        # ('Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral')
        # Lover Friend Family
        # p1 = 처음사람 p2 = 두번째 사람의 퍼센트
        # data['p1'], data['p2'],data['relation']


        p1 *= 100000
        p2 *= 100000
        p1 = round(p1,1)
        p2 = round(p2,1)
        result = ""
        if data['relationship'] == 'Lover' :
            if p1 == p2 :
                result = "서로 더할 나위 없이 좋아하고 있네요~!"
            elif p1 > p2 :
                result = data['p1'] +".. 과연 " +  data['p2'] + "도 너를 좋아할까..?"
            else :
                result = data['p1'] +"! 앞으로의 좋은 관계를 위해서는 노력하자..!"
        elif data['relationship'] == 'Friend' :
            if p1 == p2 :
                result = "당신들의 우정에 치얼스.."
            elif p1 > p2 :
                result = data['p2'] + "는 조금 거리를 둬도 좋을 것 같아.."
            else :
                result = data['p1'] +"! "+data['p2']+"는 너와의 관계를 소중히 여기고 있단다..!"
        elif data['relationship'] == 'Family' :
            if p1 == p2 :
                result = "역시 가족.. 결국 가족.. 화목한 가정입니다..!"
            elif p1 > p2 :
                result = "언젠가는 너에게 애정을 쏟을거야.. 결국 남는건 가족이거든.. 화이팅..!"
            else :
                result = data['p1'] +"! 결국 남는건 가족이란다. 지나서 후회하지 말고 잘하자..!"

        return JsonResponse({'data': result, 'crop_image1' : returl1,'crop_image2':returl2})
















"""
@api_view(['GET','POST','PUT','DELETE'])
def user_detail(request,article_pk):

    if request.method == 'GET':  # 그룹의 사람들 받아오기
        article = get_object_or_404(Usergroup, pk=article_pk)
        serializer = UserDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':  # 그룹의 정보 수정
        article = Usergroup.objects.filter(id=article_pk).first()
        serializers = UserDetailSerializer(article,data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=201)
        else:
            return  JsonResponse(serializers.data,status=400)
    elif request.method == 'DELETE':  # 그룹 내 인원 삭제
        article = Usergroup.objects.filter(id=article_pk)
        article.delete()
        return Response({'message': 'deleted successfully!'}, status=201)



@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'POST': # 그룹 내 직원 추가
        serializers = UserDetailSerializer(data=request.data)#그룹은 한글이름,영어이름,부서,직책,pin번호로 구성됨.
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=201)
        # 에러처리 하기
        else:
            return JsonResponse(serializers.data, status=400)
    elif request.method == 'GET':  # 그룹의 사람들 받아오기
        articles = Usergroup.objects.all()
        serializers = UserDetailSerializer(articles,many=True)
        return Response(serializers.data)


#출결 관리


@api_view(['GET'])#출결 1개
def access_detail_v1(request):
    article = Access.objects.all().order_by('-recent')[:10]
    serializers = AccessListSerializer(article,many=True)
    return Response(serializers.data)

@api_view(['GET','POST','PUT','DELETE'])
def access_detail_v2(request,article_pk):
    if request.method == 'POST':
        data = {'user_pk':article_pk,'enter_at':datetime.datetime.now(),'recent':datetime.datetime.now()}

        serializers = AccessListSerializer(data = data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()

            return Response(serializers.data,status=201)
        #에러처리 하기
        else :
            return JsonResponse(serializers.data,status=400)
    elif request.method == 'GET':# 출결 10개 받아오기
        article = Access.objects.filter(user_pk=article_pk).order_by('-enter_at')
        serializers = AccessListSerializer(article, many=True)
        return Response(serializers.data)
    elif request.method == 'PUT':#out_at 수정하기
        article = Access.objects.filter(user_pk=article_pk).order_by('-enter_at').first()
        #
        temp_enter = article.enter_at
        print(temp_enter)
        nowtime = datetime.datetime.now()
        data ={'enter_at':temp_enter,'out_at':nowtime,'user_pk':article_pk,'recent':nowtime}
        print(nowtime)
        serializers = AccessListSerializer(article,data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=201)
        else :
            return  JsonResponse(serializers.data,status=400)
    elif request.method == 'DELETE':
        article = Access.objects.filter(user_pk=article_pk)
        article.delete()
        return Response({'message': 'deleted successfully!'},status=201)

@api_view(['GET'])
def camera_on(request,article_pk):
    if request.method == 'GET' :
        s = socket.socket()
        num = article_pk
        s.connect(("ssafyteam7.iptime.org", 9999))
        '''192.168.0.29'''
        s.send(bytes(str(num), 'utf8'))

        s.close()
        return Response({'message': 'camera on successfully!'}, status=201)
    
"""
# Create your views here.


#get post create put update delete




