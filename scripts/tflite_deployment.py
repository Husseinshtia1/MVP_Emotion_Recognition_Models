
import tensorflow as tf

def convert_to_tflite(model_path, tflite_path):
    """Convert TensorFlow model to TensorFlow Lite format."""
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    with open(tflite_path, 'wb') as f:
        f.write(tflite_model)

convert_to_tflite('models/vision_model.h5', 'models/vision_model.tflite')
