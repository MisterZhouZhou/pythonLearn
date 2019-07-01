import face_recognition
image = face_recognition.load_image_file("images/zhouwei.jpg")
# 查找面部
face_locations = face_recognition.face_locations(image)
# 查找面部特征
face_landmarks_list = face_recognition.face_landmarks(image)
# 查找面部编码
list_of_face_encodings = face_recognition.face_encodings(image)

# 打印输出
print(face_locations)
print(face_landmarks_list)
print(list_of_face_encodings)
