import face_recognition

if __name__ == '__main__':
    image = face_recognition.load_image_file('images/zhouwei.jpg')
    # 自动查找图片中的所有面部
    face_locations = face_recognition.face_locations(image)
    print(face_locations)