# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 00:02:12 2018
@author: frank
"""
from estimator import Estimator
import cv2
import os
#import sys

image_exts = ['.jpeg','.jpg','.png','.bmp']
video_exts = ['.mpg','.mpeg','.mp4','.avi']

'''
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QFileDialog, QMessageBox, QProgressBar
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QSplitter#, QCheckBox
from PyQt5.QtWidgets import QComboBox,QDialog, QLabel,QLineEdit#, QTableWidget,QStackedWidget
from PyQt5.QtWidgets import QDateTimeEdit,QDialogButtonBox
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtGui import QIcon,QFont,QKeySequence#,QVBoxLayout,QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread
from PyQt5.Qt import QDateTime
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage,QPixmap

import numpy as np

class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.filepath = None
        self.width = 640
        self.height = 480
        self.isfinished = False
        self.estimator = None
        self.image = np.zeros((self.height,self.width,3), dtype=np.uint8)

    def isFinished(self):
        return self.isfinished
 
    def refresh(self):
        rgbImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
        p = convertToQtFormat.scaled(self.width, self.height, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)        
        
    def run(self):
        if not self.filepath or not os.path.exists(self.filepath):
            return
        print(self.filepath)
        filepath,filename=os.path.split(self.filepath)
        fname,ext = os.path.splitext(filename)
        print('ext:%s'%ext)
        if ext in image_exts:
            print('processing image...')
            frame = cv2.imread(self.filepath)
            frame = self.estimator.process_all(frame) if self.estimator else frame
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
            convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
            p = convertToQtFormat.scaled(self.width, self.height, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
            self.isfinished = True
            self.image = frame.copy()
            
        elif ext in video_exts:
            cap = cv2.VideoCapture(os.path.abspath(self.filepath))
            while True:
                ret, frame = cap.read()
                if ret is False:
                    break
                frame = self.estimator.process_all(frame) if self.estimator else frame
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(self.width, self.height, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                self.image = frame.copy()
            self.isfinished = True

    def setestimator(self,estimator):
        self.estimator = estimator
        
    def setpath(self,path):
        self.filepath = os.path.abspath(path)
        self.isfinished = False
        
    def setsize(self,width,height):
        self.width,self.height = width,height
   
class Dialog(QDialog):
    up_camera_signal = QtCore.pyqtSignal(QImage)
    def __init__(self, estimator):
        super(Dialog, self).__init__(None)
        self.isfinished = False
        self.estimator = estimator
        self.initialize()

    def act_fileopen(self):
        filepath,extensions = QFileDialog.getOpenFileName(self, r'File Open','',"Image/Video files (*.jpeg *.jpg *.png *.avi *.mpeg *.mpg *.mp4)")
        self.thread.setpath(filepath)
        self.thread.start()
 
    def closeEvent(self, event):
        
        if self.isfinished:
            self.deleteLater()
            return
        
        reply = QMessageBox.question(self, 'warning',
                                     "Are you sure to quit dialog?", QMessageBox.Yes | 
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.thread.quit()
            self.deleteLater()
            event.accept()
        else:
            event.ignore()
            
    def initialize(self):
        ###
        self.up_camera = None
        ###
        self.label = QLabel(self)
        #label.move(180, 120)
        self.label.resize(350, 350)
        button = QPushButton(self)
        button.setText('open')
        button.released.connect(self.act_fileopen)
        ###
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label)
        vbox.addWidget(button)
        self.setLayout(vbox)
        ###
        self.thread = Thread(self)
        self.thread.setestimator(self.estimator)
        self.thread.changePixmap.connect(self.label.setPixmap)
        ###
        self.setMinimumSize(500,350)
        self.setWindowTitle("Demo")  
        self.show()

    def resizeEvent(self, event):
        #self.resized.emit()
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        self.thread.setsize(width-30,height-30)
        if not self.thread.isFinished():
            self.thread.refresh()
        self.label.setGeometry(QtCore.QRect(0, height-20, width-20, 20))
        self.label.setVisible(True)
        self.update()
        return super(Dialog, self).resizeEvent(event)

    def setestimator(self,estimator):
        self.estimator = estimator
        self.thread.setestimator(estimator)
        
def main():
    #
    est = Estimator('model.h5')
    # Create an PyQT5 application object.
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    ex = Dialog(estimator=est)
    sys.exit(app.exec_())
''' 
import argparse
import time

def test_estimator():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True, help='input image')
    parser.add_argument('--output', type=str, default='result.png', help='output image')
    parser.add_argument('--model', type=str, default='model.h5', help='path to the weights file')

    args = parser.parse_args()
    output = args.output
    keras_weights_file = args.model

    estimator = Estimator(keras_weights_file)

    # generate image with body parts
    if os.path.isdir(args.image):
        for file in os.listdir(args.image):
            fpath,fname = os.path.split(os.path.abspath(file))
            name,ext = os.path.splitext(fname)
            if not os.path.isfile(file) or ext not in image_exts:
                continue
            tic = time.time()
            frame = cv2.imread(os.path.abspath(file))
            canvas = estimator.process_all(frame)
            toc = time.time()
            print ('processing time is %.5f' % (toc - tic))
            # saving
            output = os.path.join(fpath,'%s_processed%s'%(name,ext))
            cv2.imwrite(output, canvas)
    else:
        fpath,fname = os.path.split(os.path.abspath(args.image))
        name,ext = os.path.splitext(fname)
        if not os.path.isfile(args.image) or ext not in image_exts:
            return
        tic = time.time()
        frame = cv2.imread(os.path.abspath(args.image))
        canvas = estimator.process_all(frame)
        toc = time.time()
        print ('processing time is %.5f' % (toc - tic))
        # saving
        output = os.path.join(fpath,'%s_processed%s'%(name,ext))
        cv2.imwrite(output, canvas)        
    
if __name__ == "__main__":
    test_estimator()