import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# ================= PATHS =================
train_path = r"C:\Users\KIIT\Desktop\rootscan\archive (1)\idata\Image Dataset\ImageDataset\train"
valid_path = r"C:\Users\KIIT\Desktop\rootscan\archive (1)\idata\Image Dataset\ImageDataset\valid"
# ================= DATA PREPROCESSING =================
train_gen = ImageDataGenerator(rescale=1./255)
valid_gen = ImageDataGenerator(rescale=1./255)   
train_data = train_gen.flow_from_directory(
    train_path,
    target_size=(128,128),
    batch_size=32,
    class_mode='categorical'
)

valid_data = valid_gen.flow_from_directory(
    valid_path,
    target_size=(128,128),
    batch_size=32,
    class_mode='categorical'
)

# Print class labels
print("Class Labels:", train_data.class_indices)

model = Sequential()

model.add(Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dense(6, activation='softmax'))  # 6 classes

# ================= COMPILE =================
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ================= TRAIN =================
history = model.fit(
    train_data,
    validation_data=valid_data,
    epochs=10
)

# ================= SAVE =================
model.save("plant_model.h5")

print("Model training complete & saved as plant_model.h5")
