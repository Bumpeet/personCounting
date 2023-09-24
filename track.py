import supervision as sv
from supervision.geometry.core import Point
from supervision.detection.core import Detections
from supervision.detection.line_counter import LineZone, LineZoneAnnotator

from ultralytics import YOLO
import numpy as np

from argparse import ArgumentParser
import sys

from utils import calculate_execution_time


def filter_person_class(detections:Detections) -> Detections:
    '''
    This function helps in filtering the person class out of all the 
    classes from coco

    detections: This is a output from the yolo model of type Detections
    returns: type Detections with the removed ids related to other class
    '''
    if detections.tracker_id is None:
        return detections
    
    #filtering the person class
    idxs = np.where(detections.class_id==0)
    detections.tracker_id = detections.tracker_id[idxs]
    detections.xyxy = detections.xyxy[idxs]
    detections.confidence = detections.confidence[idxs]
    detections.class_id = detections.class_id[idxs]

    return detections


def main(track_buffer, threshold, point1, point2, src_path, dest_pth):

    model = YOLO("yolov8s.pt") # selecting a model for the detections

    byte_tracker = sv.ByteTrack(match_thresh=threshold,track_buffer=track_buffer)
    track_annotator = sv.BoxAnnotator() # this will annoatate id's on the frame

    line = LineZone(Point(*point1), Point(*point2)) # defining the line for entry and exit
    line_annotator = LineZoneAnnotator() # this will annoatate the etnry and exit on the frames

    @calculate_execution_time
    def callback(frame: np.ndarray, index: int) -> np.ndarray:
        results = model(frame)[0] # inferencing the image
        detections = sv.Detections.from_ultralytics(results)
        detections = byte_tracker.update_with_detections(detections=detections)
        detections = filter_person_class(detections=detections)
        line.trigger(detections= detections) # keeping track of the count for every frame

        labels =  [
            f"{tracker_id}"
            for _, _, _, _, tracker_id
        in detections
    ]
        f = track_annotator.annotate(frame.copy(), detections=detections, labels=labels)
        f = line_annotator.annotate(f,line)
        return f

    sv.process_video(source_path=src_path,
                    target_path=dest_pth,
                    callback=callback)


def arguments():

    parser = ArgumentParser("This program helps in keeping the track of count of \
                            people entering and exiting a location")
    parser.add_argument("--track_buffer",type=int, default=60)
    parser.add_argument("--threshold", type = float, default=0.8)
    parser.add_argument("--point1", type=int, default=[630, 100], nargs="+")
    parser.add_argument("--point2", type=int, default=[0, 500], nargs="+")
    parser.add_argument("--src_path", type=str, default="Main Gate - Luminous.mp4")
    parser.add_argument("--dest_pth", type=str, default="soln.mp4")
    return parser.parse_args()

if __name__=="__main__":
    args = arguments()
    main(**vars(args))