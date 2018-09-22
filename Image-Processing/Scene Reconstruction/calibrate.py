import cv2
import numpy as np
import wx

from gui import BaseLayout

class CameraCalibration(BaseLayout):
    
    def _init_custom_layout(self):
        #setting of chessboard size
        self.chessboard_size = (9, 6)

        #prepare object points
        self.objp = np.zeros((np.prod(self.chessboard_size), 3),
                            dtype=np.float32)
        self.objp[:, :2] = np.mgrid[0:self.chessboard_size[0],
                                    0:self,chessboard_size[1]].T.reshape(-1, 2)

        #prepare recording
        self.recording = False
        self.record_min_num_frames = 20
        self.__reset_recording()

    def _create_custom_layout(self):
        pnl = wx.Panel(self, -1)
        self.button_calibrate = wx.Button(pnl, label='Calibrate Camera')
        self.bind(wx.EVT_BUTTON, self._on_button_calibrate)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.button_calibrate)
        pnl.SetSizer(hbox)

        self.panels_vertical.Add(pnl, flag=wx.EXPAND | wx.BOTTOM | wx.TOP,
                                border = 1)

    def _process_frame(self, frame):
        if not self.recording:
            return frame
    
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.uint8)

        if self.record_cnt < self.record_min_num_frames:
            ret, corners = cv2.findChessboardCorners(img_gray, self.chessboard_size, None)

            if ret:
                cv2.drawChessboardCorners(frame, self.chessboard_size, corners, ret)

                criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
                                30, 0.01)
                cv2.cornerSubPrix(img_gray, corners, (9, 9), (-1 , -1), criteria)
                self.obj_points.append(self.objp)
                self.img_points.append(corners)            
                self.record_cnt += 1

        else:
            print "Calibrating..."
            ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(self.obj_points,
                                                                self.img_points,
                                                                (self.imgHeight,
                                                                self.imgWidth),
                                                                None, None)
            print "K=", K
            print "dist=", dist

            mean_error = 0
            
            for i in xrange(len(self.obj_points)):
                img_points2, _ = cv2.projectPoints(self.obj_points[i],
                                                    rvecs[i], tvecs[i], K, dist)
                error = cv2.norm(self.img_points[i], img_points2,
                                    cv2.NORM_L2)/len(img_points2)
                mean_error += error
            
            print "mean error=", mean_error

            self.recording = False
            self._reset_recording()
            self.button_calibrate.Enable()
        
        return frame

    def _on_button_calibrate(self, event):
        self.button_calibrate.Disable()
        self.recording = True
        self._reset_recording()

    def _reset_recording(self):
        self.record_cnt = 0
        self.obj_points = []
        self.img_points = []

def main():
    capture = cv2.VideoCapture(0)
    if not(capture.isOpened()):
        capture.open()

    capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    #start gui
    app = wx.App()

    layout = CameraCalibration(None, -1, 'Camera Calibration', capture)
    layout.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()