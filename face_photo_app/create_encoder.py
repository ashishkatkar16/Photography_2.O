import os
import pickle
import cv2
import face_recognition


def encoder_script(dir_path, enc_path):
    # Define the path to the directory containing test images
    test_images = dir_path

    # Dictionary to store known face encodings
    known_encodings = dict()

    # Dictionary to store full paths of images
    image_full_path = dict()

    # Loop through each image in the test_images directory

    for image in os.listdir(test_images):
        print(image)
        if image.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.PNG')) and image is not None:
            path = f"{test_images}/{image}"

            # Store image path to the dictionary
            image_full_path[image] = path

            # Read and resize the image
            img = cv2.imread(path)
            resized_image = cv2.resize(img, dsize=(round(img.shape[1] * 0.25), round(img.shape[0] * 0.25)))
            rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

            # Load face encodings
            encodes = face_recognition.face_encodings(rgb)

            if encodes:
                print(f"[Info] Encodes loaded: {image}")

                known_encodings[image] = encodes
            else:

                print(f"[Skip] Encodes not present in: {image}.")

        # Store image paths in a pickle file
        with open(os.path.join(enc_path, "full_image_path.pickle"), "wb") as file:
            pickle.dump(image_full_path, file)

        # Store known face encodings in a pickle file
        with open(os.path.join(enc_path, "image_encodings.pickle"), "wb") as file:
            pickle.dump(known_encodings, file)


if __name__ == '__main__':

    encoder_script(dir_path="media/admin/Birthday", enc_path="media/root/Birthday/Encodings")
    path = "media/admin/Birthday/Encodings/image_encodings.pickle"

    encoder_script(dir_path="media/admin/Birthday", enc_path="media/root/Birthday/Encodings")
    path = "media/admin/Birthday/Encodings/full_image_path.pickle"


    with open(path, 'rb') as file:
        enc = pickle.load(file)

    print(enc)
