
import torch
import cv2
from segment_anything import build_sam, SamPredictor

def load_sam_model(checkpoint_path='sam_vit_h_4b8939.pth', model_type='vit_h'):
    '''Load SAM2 model for segmentation.'''
    sam = build_sam(checkpoint=checkpoint_path, model_type=model_type)
    return SamPredictor(sam)

def segment_object_in_image(image_path, predictor):
    '''Perform segmentation on a given image using SAM2.'''
    image = cv2.imread(image_path)
    predictor.set_image(image)
    masks, _, _ = predictor.predict(point_coords=None, point_labels=None, box=None, multimask_output=False)
    for mask in masks:
        annotated_image = cv2.addWeighted(image, 0.7, mask, 0.3, 0)
        cv2.imshow("Segmented Image", annotated_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
