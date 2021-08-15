import imageai
from imageai.Detection import VideoObjectDetection
import os

class ObjectIdentification:
    def __init__(self):
      self.execution_path = os.getcwd()
      # Create an instance of the VideoObjectDetection class.
      self.detector = VideoObjectDetection()
      # The model type to YOLOv3.
      self.detector.setModelTypeAsYOLOv3()
      # The file path of the model file we copied into the folder.
      self.detector.setModelPath( os.path.join(self.execution_path , "yolo.h5"))
      # Upload the model for the VideoObjectDetection class instance.
      self.detector.loadModel()
            
    def introduceyourself(self):
      print(self.detector)
      print(str(self.execution_path))
        

    def forFrame(self,frame_number, output_array, output_count):
      '''
      once every frame in the video is processed and detected, 
      the function will receive and prints out the analytical data for objects detected in the video frame.
      '''
      print("FOR FRAME " , frame_number)
      print("Output for each object : ", output_array)
      print("Output count for unique objects : ", output_count)
      print("------------END OF A FRAME --------------")

    def forSeconds(self, second_number, output_arrays, count_arrays, average_output_count):
      '''
      once every second in the video is processed and detected, 
      the function will receive and prints out the analytical data for objects detected in the video.
      '''
      print("SECOND : ", second_number)
      print("Array for the outputs of each frame ", output_arrays)
      print("Array for output count for unique objects in each frame : ", count_arrays)
      print("Output average count for unique objects in the last second: ", average_output_count)
      print("------------END OF A SECOND --------------")

    
    def forMinute(self,minute_number, output_arrays, count_arrays, average_output_count):
      '''
      For every frame of the video that is detected, the function which was parsed into the parameter will be executed and analytical data
      of the video will be parsed into the function. 
      The data returned has the same nature as the per_second_function.
      The difference is that it covers all the frames in the past 1 minute of the video.
      '''
      print("MINUTE : ", minute_number)
      print("Array for the outputs of each frame ", output_arrays)
      print("Array for output count for unique objects in each frame : ", count_arrays)
      print("Output average count for unique objects in the last minute: ", average_output_count)
      print("------------END OF A MINUTE --------------")

if __name__ == '__main__':
    obj = ObjectIdentification()
    obj.introduceyourself()
    # Call the detectObjectsFromVideo function 
    video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(obj.execution_path, "datatest_vedio/noViolence.mp4"), output_file_path=os.path.join(obj.execution_path, "datatest_vedio/noViolence_detected"), frames_per_second=20, log_progress=True)
    print(video_path)
    # Call functions
    obj.detector.detectObjectsFromVideo(input_file_path=os.path.join(obj.execution_path, "datatest_vedio/noViolence.mp4"), output_file_path=os.path.join(obj.execution_path, "video_frame_analysis") ,  frames_per_second=20, per_frame_function=obj.forFrame,  minimum_percentage_probability=30)
    obj.detector.detectObjectsFromVideo(input_file_path=os.path.join(obj.execution_path, "datatest_vedio/noViolence.mp4"), output_file_path=os.path.join(obj.execution_path, "video_second_analysis") ,  frames_per_second=20, per_second_function=obj.forSeconds,  minimum_percentage_probability=30)
    obj.detector.detectObjectsFromVideo(input_file_path=os.path.join(obj.execution_path, "datatest_vedio/noViolence.mp4"), output_file_path=os.path.join(obj.execution_path, "video_minute_analysis") ,  frames_per_second=20, per_second_function=obj.forMinute,  minimum_percentage_probability=30)
