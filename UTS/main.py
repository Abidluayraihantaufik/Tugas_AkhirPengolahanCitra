import streamlit as st
import numpy as np
import os
from PIL import Image,ImageEnhance
import cv2 

face_cascade = cv2.CascadeClassifier('./detectors/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./detectors/haarcascade_eye.xml')
eyeglass_cascade = cv2.CascadeClassifier('./detectors/haarcascade_eye_tree_eyeglasses.xml')


def detect_faces(our_image):
    new_img = np.array(our_image.convert("RGB"))
    faces = face_cascade.detectMultiScale(new_img, 1.1, 6)
    for (x, y, w, h) in faces:
        cv2.rectangle(new_img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    return new_img, faces
def detect_eye(our_image):
    new_img = np.array(our_image.convert("RGB"))
    eyes = eye_cascade.detectMultiScale(new_img, 1.1, 16)
    for (x, y, w, h) in eyes:
        cv2.rectangle(new_img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    return new_img, eyes
def detect_glass(our_image):
    new_img = np.array(our_image.convert("RGB"))
    eyesglass = eyeglass_cascade.detectMultiScale(new_img, 1.1, 16)
    for (x, y, w, h) in eyesglass:
        cv2.rectangle(new_img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    return new_img, eyesglass

def main():
    st.title("SELAMAT DATANG FRIENDS")  
    


    activities = {'Detection', 'About'}
    choice = st.sidebar.selectbox('Select Activity', activities)

    if choice == 'Detection':
        st.subheader('Face Detection')
        image_file = st.file_uploader('Upload Image', type=['jpg','png','jpeg','webp'])

        if image_file is not None:
            our_image = Image.open(image_file)
            st.text('Original Image')
            st.image(our_image)

            enhance_type = st.sidebar.radio("Enahance type", ['Original','Gray-scale','Contrast','Brightness','Blurring','Sharpness'])

            if enhance_type == 'Gray-scale':
                img = np.array(our_image.convert('RGB'))
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                st.image(gray)
            elif enhance_type == "Contrast":
                rate = st.sidebar.slider("Contrast",0.5, 6.0)
                enhancer = ImageEnhance.Contrast(our_image)
                enchanced_img = enhancer.enhance(rate)
                st.image(enchanced_img)
            elif enhance_type == "Brightness":
                rate = st.sidebar.slider("Brightness",0.0, 8.0)
                enhancer = ImageEnhance.Brightness(our_image)
                enchanced_img = enhancer.enhance(rate)
                st.image(enchanced_img)
            elif enhance_type == "Blurring":
                rate = st.sidebar.slider("Brightness",0.0, 8.0)
                enhancer = ImageEnhance.Brightness(our_image)
                enchanced_img = enhancer.enhance(rate)
                st.image(enchanced_img)
            elif enhance_type == "Sharpness":
                rate = st.sidebar.slider("Sharpness",0.0, 14.0)
                enhancer = ImageEnhance.Sharpness(our_image)
                enchanced_img = enhancer.enhance(rate)
                st.image(enchanced_img)
            elif enhance_type == "Original":
                st.image(our_image, width = 300)
            else :
                st.image(our_image, width = 300)
        tasks = ["Faces", "Eyes", "Cartoonize", "Cannize","Eyesglass"]
        feature_choice = st.sidebar.selectbox("Find features", tasks)
        if st.button("Process"):
            if feature_choice == "Faces":
                result_img, result_face = detect_faces(our_image)
                st.image(result_img)
                st.success("{} Wajah Terdeteksi".format(len(result_face)))

            if feature_choice == "Eyes":
                result_img, result_eye = detect_eye(our_image)
                st.image(result_img)
                st.success("{} Mata Terdeteksi".format(len(result_eye)))

            if feature_choice == "Eyesglass":
                result_img, result_eye = detect_glass(our_image)
                st.image(result_img)
                st.success("{} Kacamata Terdeteksi".format(len(result_eye)))


    elif choice =='About':
        st.subheader('Tentang gwe')
        st.markdown('Built with streamlit by Abid Luay Raihan Taufik')
        st.text('Im bad')
        
    

if __name__ == "__main__":
    
    main()